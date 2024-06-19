from typing import Dict, Optional

import hug
import hug.directives
from pydantic import BaseModel

from apphelpers.rest import endpoint as ep
from apphelpers.rest.hug import user_id
from tests.app.models import globalgroups, sitegroups


def echo(word, user: hug.directives.user = None):
    return "%s:%s" % (user.id, word) if user else word


@ep.login_required
def secure_echo(word, user: hug.directives.user = None):
    return "%s:%s" % (user.id, word) if user else word


@ep.any_group_required(globalgroups.privileged.value)
@ep.groups_forbidden(globalgroups.forbidden.value)
def echo_groups(user: hug.directives.user = None):
    return user.groups


def add(nums: hug.types.multiple):
    return sum(int(x) for x in nums)


@ep.login_required
def get_my_uid(uid: user_id):
    return uid


@ep.not_found_on_none
def get_snake(name=None):
    return name


@ep.login_required
@ep.not_found_on_none
def get_secure_snake(site_id, name=None):
    return name


@ep.login_required
def secure_multisite_echo(word, user: hug.directives.user = None):
    return "%s:%s" % (user.id, word) if user else word


@ep.any_group_required(sitegroups.privileged.value)
@ep.groups_forbidden(globalgroups.forbidden.value)
def echo_multisite_groups(site_id: int, user: hug.directives.user = None):
    return user.groups


@ep.all_groups_required(
    globalgroups.privileged.value,
    sitegroups.privileged.value,
)
def echo_multisite_all_groups(site_id: int, user: hug.directives.user = None):
    return user.groups + user.site_groups[site_id]


def process_request(request, body):
    return {"body": body, "headers": request.headers}


@ep.not_found_on_none
def process_raw_request(request):
    return {"raw_body": request.stream.read().decode(), "headers": request.headers}


def check_authorization(user, *args, **kw):
    return kw["word"] == "authorized"


@ep.authorizer(check_authorization)
def custom_authorization_echo(word):
    return word


def setup_routes(factory):
    factory.get("/echo/{word}")(echo)
    factory.post("/echo")(echo)

    factory.get("/add")(add)

    factory.get("/secure-echo/{word}")(secure_echo)
    factory.get("/custom-authorization-echo/{word}")(custom_authorization_echo)
    factory.get("/echo-groups")(echo_groups)

    factory.post("/me/uid")(get_my_uid)

    factory.get("/snakes/{name}")(get_snake)

    factory.get("/sites/{site_id}/secure-echo/{word}")(secure_multisite_echo)
    factory.get("/sites/{site_id}/echo-groups")(echo_multisite_groups)
    factory.get("/sites/{site_id}/echo-all-groups")(echo_multisite_all_groups)
    factory.get("/sites/{site_id}/snakes/{name}")(get_secure_snake)

    factory.post("/request-and-body")(process_request)
    factory.post("/request-raw-body", parse_body=False)(process_raw_request)

    # ar_handlers = (None, arlib.create, None, arlib.get, arlib.update, None)
    # factory.map_resource('/resttest/', handlers=ar_handlers)
