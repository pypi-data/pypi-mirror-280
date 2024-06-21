from typing import List

from pypanther.base import PantherRule, PantherRuleTest, PantherSeverity
from pypanther.helpers.panther_base_helpers import deep_get
from pypanther.helpers.panther_notion_helpers import notion_alert_context
from pypanther.log_types import PantherLogType

notion_page_perms_guest_perms_changed_tests: List[PantherRuleTest] = [
    PantherRuleTest(
        Name="Guest Role Added",
        ExpectedResult=True,
        Log={
            "event": {
                "actor": {
                    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "object": "user",
                    "person": {"email": "aragorn.elessar@lotr.com"},
                    "type": "person",
                },
                "details": {
                    "entity": {
                        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                        "object": "user",
                        "person": {"email": "frodo.baggins@lotr.com"},
                        "type": "person",
                    },
                    "new_permission": "full_access",
                    "old_permission": "none",
                    "page_audience": "shared_internally",
                    "target": {
                        "page_id": "441356b5-557b-4053-8d2f-7932d2607d66",
                        "type": "page_id",
                    },
                },
                "id": "e18690f8-e24b-4b03-ba6f-123eb7ec0f08",
                "timestamp": "2023-08-11 23:02:53.113000000",
                "type": "page.permissions.guest_role_added",
                "workspace_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            }
        },
    ),
    PantherRuleTest(
        Name="Guest Role Changed",
        ExpectedResult=True,
        Log={
            "event": {
                "actor": {
                    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "object": "user",
                    "person": {"email": "aragorn.elessar@lotr.com"},
                    "type": "person",
                },
                "details": {
                    "entity": {
                        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                        "object": "user",
                        "person": {"email": "frodo.baggins@lotr.com"},
                        "type": "person",
                    },
                    "new_permission": "full_access",
                    "old_permission": "read_only",
                    "page_audience": "shared_internally",
                    "target": {
                        "page_id": "441356b5-557b-4053-8d2f-7932d2607d66",
                        "type": "page_id",
                    },
                },
                "id": "e18690f8-e24b-4b03-ba6f-123eb7ec0f08",
                "timestamp": "2023-08-11 23:02:53.113000000",
                "type": "page.permissions.guest_role_updated",
                "workspace_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            }
        },
    ),
]


class NotionPagePermsGuestPermsChanged(PantherRule):
    RuleID = "Notion.PagePerms.GuestPermsChanged-prototype"
    DisplayName = "Notion Page Guest Permissions Changed"
    LogTypes = [PantherLogType.Notion_AuditLogs]
    Tags = ["Notion", "Data Security", "Information Disclosure"]
    Severity = PantherSeverity.Low
    Description = "The external guest permissions for a Notion page have been altered."
    Runbook = "Potential information exposure - review the shared page and rectify if needed."
    Reference = "https://www.notion.so/help/sharing-and-permissions"
    Tests = notion_page_perms_guest_perms_changed_tests
    # These event types correspond to users adding or editing the default role on a public page
    event_types = ("page.permissions.guest_role_added", "page.permissions.guest_role_updated")

    def rule(self, event):
        return event.deep_get("event", "type", default="<NO_EVENT_TYPE_FOUND>") in self.event_types

    def title(self, event):
        user = event.deep_get("event", "actor", "person", "email", default="<NO_USER_FOUND>")
        guest = event.deep_get(
            "event", "details", "entity", "person", "email", default="<NO_USER_FOUND>"
        )
        page_id = event.deep_get(
            "event", "details", "target", "page_id", default="<NO_PAGE_ID_FOUND>"
        )
        event_type = event.deep_get("event", "type", default="<NO_EVENT_TYPE_FOUND>")
        action = {
            "page.permissions.guest_role_added": "added a guest",
            "page.permissions.guest_role_updated": "changed the guest permissions of",
        }.get(event_type, "changed the guest permissions of")
        return f"Notion User [{user}] {action} [{guest}] on page [{page_id}]."

    def alert_context(self, event):
        context = notion_alert_context(event)
        page_id = event.deep_get(
            "event", "details", "target", "page_id", default="<NO_PAGE_ID_FOUND>"
        )
        context["page_id"] = page_id
        details = event.deep_get("event", "details", default={})
        context["guest"] = deep_get(details, "entity", "person", "email", default="<NO_USER_FOUND>")
        context["new_permission"] = deep_get(
            details, "new_permission", default="<UNKNOWN PERMISSION>"
        )
        context["old_permission"] = deep_get(
            details, "old_permission", default="<UNKNOWN PERMISSION>"
        )
        return context
