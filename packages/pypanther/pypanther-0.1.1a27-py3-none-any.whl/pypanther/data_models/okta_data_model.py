from typing import List

import pypanther.helpers.panther_event_type_helpers as event_type
from pypanther.base import PantherDataModel, PantherDataModelMapping
from pypanther.helpers.panther_base_helpers import deep_get
from pypanther.log_types import PantherLogType


def get_event_type(event):
    # pylint: disable=too-many-return-statements
    if (
        event.get("eventType") == "user.session.start"
        and event.get("outcome", {}).get("result") == "FAILURE"
    ):
        return event_type.FAILED_LOGIN
    if (
        event.get("eventType") == "user.session.start"
        and event.get("outcome", {}).get("result") == "SUCCESS"
    ):
        return event_type.SUCCESSFUL_LOGIN
    if event.get("eventType") in ["user.mfa.factor.deactivate", "user.mfa.factor.suspend"]:
        if event.get("outcome", {}).get("reason", "").startswith("User reset"):
            return event_type.MFA_RESET
        return event_type.MFA_DISABLED

    if event.get("eventType") in [
        "user.mfa.factor.activate",
        "user.mfa.factor.unsuspend",
        "user.mfa.factor.update ",
    ]:
        return event_type.MFA_ENABLED

    if event.get("eventType") == "system.mfa.factor.deactivate":
        return event_type.ADMIN_MFA_DISABLED
    return None


def get_actor_user(event):
    actor = deep_get(event, "actor", "displayName", default="unknown")
    if actor == "unknown":
        actor = deep_get(event, "actor", "alternateId", default="Unknown User")
    return actor


class StandardOktaSystemLog(PantherDataModel):
    DataModelID: str = "Standard.Okta.SystemLog"
    DisplayName: str = "Okta System Log"
    Enabled: bool = True
    LogTypes: List[str] = [PantherLogType.Okta_SystemLog]
    Mappings: List[PantherDataModelMapping] = [
        PantherDataModelMapping(Name="actor_user", Method=get_actor_user),
        PantherDataModelMapping(Name="event_type", Method=get_event_type),
        PantherDataModelMapping(Name="source_ip", Path="$.client.ipAddress"),
        PantherDataModelMapping(Name="user_agent", Path="$.client.userAgent.rawUserAgent"),
    ]
