import inspect
from functools import wraps

from converge import settings
from fastapi import APIRouter, Depends
from fastapi.routing import APIRoute
from starlette.requests import Request

from apphelpers.db import dbtransaction_ctx
from apphelpers.errors.fastapi import (
    HTTP401Unauthorized,
    HTTP403Forbidden,
    HTTP404NotFound,
    InvalidSessionError,
)
from apphelpers.rest import endpoint as ep
from apphelpers.rest.common import User, phony
from apphelpers.sessions import SessionDBHandler

if settings.get("HONEYBADGER_API_KEY"):
    from honeybadger import Honeybadger
    from honeybadger.utils import filter_dict


def raise_not_found_on_none(f):
    if getattr(f, "not_found_on_none", None) is True:
        if inspect.iscoroutinefunction(f):

            @wraps(f)
            async def async_wrapper(*ar, **kw):
                ret = await f(*ar, **kw)
                if ret is None:
                    raise HTTP404NotFound()
                return ret

            return async_wrapper
        else:

            @wraps(f)
            def wrapper(*ar, **kw):
                ret = f(*ar, **kw)
                if ret is None:
                    raise HTTP404NotFound()
                return ret

            return wrapper
    return f


def honeybadger_wrapper(hb):
    """
    wrapper that executes the function in a try/except
    If an exception occurs, it is first reported to Honeybadger
    """

    def wrapper(f):
        @wraps(f)
        def f_wrapped(*args, **kw):
            try:
                ret = f(*args, **kw)
            except Exception as e:
                try:
                    hb.notify(
                        e,
                        context={
                            "func": f.__name__,
                            "args": args,
                            "kwargs": filter_dict(kw, settings.HB_PARAM_FILTERS),
                        },
                    )
                finally:
                    raise e
            return ret

        return f_wrapped

    return wrapper


async def get_current_user(request: Request):
    return request.state.user


async def get_current_user_id(request: Request):
    return request.state.user.id


async def get_current_user_name(request: Request):
    return request.state.user.name


async def get_current_user_email(request: Request):
    return request.state.user.email


async def get_current_user_mobile(request: Request):
    return request.state.user.mobile


async def get_current_domain(request: Request):
    return request.headers["HOST"]


async def get_json_body(request: Request):
    return (
        await request.json()
        if request.headers.get("content-type") == "application/json"
        else {}
    )


async def get_raw_body(request: Request):
    return request.body()


async def get_user_agent(request: Request):
    return request.headers.get("USER-AGENT", "")


user = Depends(get_current_user)
user_id = Depends(get_current_user_id)
user_name = Depends(get_current_user_name)
user_email = Depends(get_current_user_email)
user_mobile = Depends(get_current_user_mobile)
domain = Depends(get_current_domain)
raw_body = Depends(get_raw_body)
json_body = Depends(get_json_body)
user_agent = Depends(get_user_agent)


def dbtransaction(engine, allow_nested=True):
    async def dependency():
        async with dbtransaction_ctx(engine, allow_nested=allow_nested):
            yield

    return Depends(dependency)


class SecureRouter(APIRoute):
    sessions = None

    @classmethod
    def setup_ssessions(cls, sessions: SessionDBHandler):
        cls.sessions = sessions

    def get_route_handler(self):
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(_request: Request):
            uid, groups, name, email, mobile, site_groups, site_ctx = (
                None,
                [],
                "",
                None,
                None,
                {},
                None,
            )

            token = _request.headers.get("Authorization")
            if token:
                session = self.sessions.get(  # type: ignore
                    token,
                    [
                        "uid",
                        "name",
                        "groups",
                        "email",
                        "mobile",
                        "site_groups",
                        "site_ctx",
                    ],
                )
                uid, name, groups, email, mobile, site_groups, site_ctx = (
                    session["uid"],
                    session["name"],
                    session["groups"],
                    session["email"],
                    session["mobile"],
                    session["site_groups"],
                    session["site_ctx"],
                )

            _request.state.user = User(
                sid=token,
                id=uid,
                name=name,
                groups=groups,
                email=email,
                mobile=mobile,
                site_groups=site_groups,
                site_ctx=site_ctx,
            )

            return await original_route_handler(_request)

        original_route_handler.__signature__ = inspect.signature(
            original_route_handler
        ).replace(
            parameters=[
                # Use all parameters from handler
                *inspect.signature(original_route_handler).parameters.values(),
                inspect.Parameter(
                    name="_request",
                    kind=inspect.Parameter.VAR_POSITIONAL,
                    annotation=Request,
                ),
            ],
        )
        return custom_route_handler


class Router(APIRoute):
    sessions = None

    @classmethod
    def setup_ssessions(cls, sessions: SessionDBHandler):
        cls.sessions = sessions

    def get_route_handler(self):
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(_request: Request):
            uid, groups, name, email, mobile, site_groups, site_ctx = (
                None,
                [],
                "",
                None,
                None,
                {},
                None,
            )

            token = _request.headers.get("Authorization")
            if token:
                try:
                    session = self.sessions.get(  # type: ignore
                        token,
                        [
                            "uid",
                            "name",
                            "groups",
                            "email",
                            "mobile",
                            "site_groups",
                            "site_ctx",
                        ],
                    )
                    uid, name, groups, email, mobile, site_groups, site_ctx = (
                        session["uid"],
                        session["name"],
                        session["groups"],
                        session["email"],
                        session["mobile"],
                        session["site_groups"],
                        session["site_ctx"],
                    )
                except InvalidSessionError:
                    pass

            _request.state.user = User(
                sid=token,
                id=uid,
                name=name,
                groups=groups,
                email=email,
                mobile=mobile,
                site_groups=site_groups,
                site_ctx=site_ctx,
            )
            return await original_route_handler(_request)

        original_route_handler.__signature__ = inspect.signature(
            original_route_handler
        ).replace(
            parameters=[
                # Use all parameters from handler
                *inspect.signature(original_route_handler).parameters.values(),
                inspect.Parameter(
                    name="_request",
                    kind=inspect.Parameter.VAR_POSITIONAL,
                    annotation=Request,
                ),
            ],
        )
        return custom_route_handler


class APIFactory:
    def __init__(self, sessiondb_conn=None, urls_prefix="", site_identifier=None):
        self.access_wrapper = phony
        self.multi_site_enabled = False
        self.site_identifier = site_identifier
        self.urls_prefix = urls_prefix
        self.honeybadger_wrapper = phony
        if site_identifier:
            self.enable_multi_site(site_identifier)
        self.setup_session_db(sessiondb_conn)
        self.router = APIRouter(route_class=Router)
        self.secure_router = APIRouter(route_class=SecureRouter)

    def enable_multi_site(self, site_identifier: str):
        self.multi_site_enabled = True
        self.site_identifier = site_identifier

    def setup_db_transaction(self, db):
        self.router.dependencies.append(dbtransaction(db))

    def setup_honeybadger_monitoring(self):
        api_key = settings.HONEYBADGER_API_KEY
        if not api_key:
            print("Info: Honeybadger API KEY not found. Honeybadger not set")
            return

        print("Info: Setting up Honeybadger")
        hb = Honeybadger()
        hb.configure(api_key=api_key)
        self.honeybadger_wrapper = honeybadger_wrapper(hb)

    def setup_session_db(self, sessiondb_conn):
        """
        redis_conn_params: dict() with below keys
                           (host, port, password, db)
        """
        self.sessions = SessionDBHandler(sessiondb_conn)
        Router.setup_ssessions(self.sessions)
        SecureRouter.setup_ssessions(self.sessions)

        def access_wrapper(f):
            """
            This is the authentication + authorization part
            """
            login_required = getattr(f, "login_required", None)
            any_group_required = getattr(f, "any_group_required", None)
            all_groups_required = getattr(f, "all_groups_required", None)
            groups_forbidden = getattr(f, "groups_forbidden", None)
            authorizer = getattr(f, "authorizer", None)

            if (
                login_required
                or any_group_required
                or all_groups_required
                or groups_forbidden
                or authorizer
            ):

                @wraps(f)
                async def wrapper(_request, *args, **kw):
                    user = _request.state.user

                    # this is authentication part
                    if not user.id:
                        raise HTTP401Unauthorized("Invalid or expired session")

                    # this is authorization part
                    groups = set(user.groups)

                    if any_group_required and groups.isdisjoint(any_group_required):
                        raise HTTP403Forbidden("Unauthorized access")

                    if all_groups_required and not groups.issuperset(
                        all_groups_required
                    ):
                        raise HTTP403Forbidden("Unauthorized access")

                    if groups_forbidden and groups.intersection(groups_forbidden):
                        raise HTTP403Forbidden("Unauthorized access")

                    if authorizer and not authorizer(user, *args, **kw):
                        raise HTTP403Forbidden("Unauthorized access")

                    return (
                        await f(*args, **kw)
                        if inspect.iscoroutinefunction(f)
                        else f(*args, **kw)
                    )

                f.__signature__ = inspect.signature(f).replace(
                    parameters=[
                        # Use all parameters from handler
                        *inspect.signature(f).parameters.values(),
                        inspect.Parameter(
                            name="_request",
                            kind=inspect.Parameter.VAR_POSITIONAL,
                            annotation=Request,
                        ),
                    ],
                )
            else:
                wrapper = f

            return wrapper

        def multisite_access_wrapper(f):
            """
            This is the authentication + authorization part
            """

            login_required = getattr(f, "login_required", None)
            any_group_required = getattr(f, "any_group_required", None)
            all_groups_required = getattr(f, "all_groups_required", None)
            groups_forbidden = getattr(f, "groups_forbidden", None)
            authorizer = getattr(f, "authorizer", None)

            if (
                login_required
                or any_group_required
                or all_groups_required
                or groups_forbidden
                or authorizer
            ):

                @wraps(f)
                async def wrapper(_request, *args, **kw):
                    user: User = _request.state.user
                    site_id = (
                        int(kw[self.site_identifier])
                        if self.site_identifier in kw
                        else None
                    )

                    # this is authentication part
                    if not user.id:
                        raise HTTP401Unauthorized("Invalid or expired session")

                    # bound site authorization
                    if (
                        user.site_ctx
                        and site_id != user.site_ctx
                        and getattr(f, "ignore_site_ctx", False) is False
                    ):
                        raise HTTP401Unauthorized("Invalid or expired session")

                    # this is authorization part
                    groups = set(user.groups)
                    if site_id:
                        groups = groups.union(user.site_groups.get(site_id, []))

                    if any_group_required and groups.isdisjoint(any_group_required):
                        raise HTTP403Forbidden("Unauthorized access")

                    if all_groups_required and not groups.issuperset(
                        all_groups_required
                    ):
                        raise HTTP403Forbidden("Unauthorized access")

                    if groups_forbidden and groups.intersection(groups_forbidden):
                        raise HTTP403Forbidden("Unauthorized access")

                    if authorizer and not authorizer(user, *args, **kw):
                        raise HTTP403Forbidden("Unauthorized access")

                    return (
                        await f(*args, **kw)
                        if inspect.iscoroutinefunction(f)
                        else f(*args, **kw)
                    )

                f.__signature__ = inspect.signature(f).replace(
                    parameters=[
                        # Use all parameters from handler
                        *inspect.signature(f).parameters.values(),
                        inspect.Parameter(
                            name="_request",
                            kind=inspect.Parameter.VAR_POSITIONAL,
                            annotation=Request,
                        ),
                    ],
                )
            else:
                wrapper = f

            return wrapper

        self.access_wrapper = (
            multisite_access_wrapper if self.multi_site_enabled else access_wrapper
        )

    def choose_router(self, f):
        login_required = getattr(f, "login_required", None) is True
        return self.secure_router if login_required else self.router

    def build(self, method, method_args, method_kw, f):
        module = f.__module__.split(".")[-1].strip("_")
        name = f.__name__.strip("_")
        response_model = getattr(f, "response_model", None)

        if "operation_id" not in method_kw:
            method_kw["operation_id"] = f"{name}_{module}"
        if "name" not in method_kw:
            method_kw["name"] = method_kw["operation_id"]
        if "tags" not in method_kw:
            method_kw["tags"] = [module]

        if response_model is not None and "response_model" not in method_kw:
            method_kw["response_model"] = response_model

        if (
            "response_model" in method_kw
            and "response_model_exclude_unset" not in method_kw
        ):
            method_kw["response_model_exclude_unset"] = True

        print(
            f"{method_args[0]}",
            f"[{method.__name__.upper()}] => {f.__module__}:{f.__name__}",
        )
        m = method(*method_args, **method_kw)
        f = self.access_wrapper(self.honeybadger_wrapper(raise_not_found_on_none(f)))
        # NOTE: ^ wrapper ordering is important. access_wrapper needs request which
        # others don't. If access_wrapper comes late in the order it won't be passed
        # request parameter.
        return m(f)

    def get(self, path, *a, **k):
        def _wrapper(f):
            router = self.choose_router(f)
            args = (path if path.startswith("/") else (self.urls_prefix + path),) + a
            return self.build(router.get, args, k, f)

        return _wrapper

    def post(self, path, *a, **k):
        def _wrapper(f):
            router = self.choose_router(f)
            args = (path if path.startswith("/") else (self.urls_prefix + path),) + a
            return self.build(router.post, args, k, f)

        return _wrapper

    def put(self, path, *a, **k):
        def _wrapper(f):
            router = self.choose_router(f)
            args = (path if path.startswith("/") else (self.urls_prefix + path),) + a
            return self.build(router.put, args, k, f)

        return _wrapper

    def patch(self, path, *a, **k):
        def _wrapper(f):
            router = self.choose_router(f)
            args = (path if path.startswith("/") else (self.urls_prefix + path),) + a
            return self.build(router.patch, args, k, f)

        return _wrapper

    def delete(self, path, *a, **k):
        def _wrapper(f):
            router = self.choose_router(f)
            args = (path if path.startswith("/") else (self.urls_prefix + path),) + a
            return self.build(router.delete, args, k, f)

        return _wrapper

    def map_resource(self, collection_url, resource=None, handlers=None, id_field="id"):
        if resource:
            raise NotImplementedError("Resource not supported yet")

        resource_url = collection_url + "{" + id_field + "}"
        assert isinstance(handlers, (list, tuple)), "handlers should be list or tuple"
        (
            get_collection,
            add_resource,
            replace_resource,
            get_resource,
            update_resource,
            delete_resource,
        ) = handlers

        if get_collection:
            self.get(collection_url)(get_collection)
        if add_resource:
            self.post(collection_url)(add_resource)
        if replace_resource:
            self.put(resource_url)(replace_resource)
        if get_resource:
            self.get(resource_url)(get_resource)
        if update_resource:
            self.patch(resource_url)(update_resource)
        if delete_resource:
            self.delete(resource_url)(delete_resource)


@ep.login_required
def whoami(user: User = user):
    return user.to_dict()
