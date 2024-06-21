import json
from typing import List
from unittest.mock import MagicMock

from pypanther.base import PantherRule, PantherRuleMock, PantherRuleTest, PantherSeverity
from pypanther.helpers.panther_base_helpers import deep_get
from pypanther.helpers.panther_config import config
from pypanther.log_types import PantherLogType

dropbox_external_share_tests: List[PantherRuleTest] = [
    PantherRuleTest(
        Name="Domain in Allowlist",
        ExpectedResult=False,
        Mocks=[
            PantherRuleMock(
                ObjectName="DROPBOX_ALLOWED_SHARE_DOMAINS", ReturnValue='[\n    "example.com"\n]'
            )
        ],
        Log={
            "actor": {
                "_tag": "user",
                "user": {
                    "_tag": "team_member",
                    "account_id": "dbid:AAACjvKy90uezyOiLRadIuCy66dK5d1vGGw",
                    "display_name": "Alice Bob",
                    "email": "alice.bob@company.com",
                    "team_member_id": "dbmid:AADSERs2cAsByYt8yQEDU4_qdNQiSdxgCl8",
                },
            },
            "assets": [
                {
                    ".tag": "file",
                    "display_name": "paper1.paper",
                    "file_id": "id:lUP4ZxMYmc4AAAAAAAAAaA",
                    "path": {
                        "contextual": "/pathtest/paper1.paper",
                        "namespace_relative": {
                            "is_shared_namespace": True,
                            "ns_id": "3590048721",
                            "relative_path": "/paper1.paper",
                        },
                    },
                }
            ],
            "context": {
                "_tag": "team_member",
                "account_id": "dbid:AAACjvKy90uezyOiLRadIuCy66dK5d1vGGw",
                "display_name": "Alice Bob",
                "email": "alice.bob@company.com",
                "team_member_id": "dbmid:AADSERs2cAsByYt8yQEDU4_qdNQiSdxgCl8",
            },
            "details": {
                ".tag": "shared_content_add_member_details",
                "shared_content_access_level": {".tag": "viewer"},
            },
            "event_category": {"_tag": "sharing"},
            "event_type": {
                "_tag": "shared_content_add_member",
                "description": "Added users and/or groups to shared file/folder",
            },
            "involve_non_team_member": True,
            "origin": {
                "access_method": {
                    ".tag": "end_user",
                    "end_user": {
                        ".tag": "web",
                        "session_id": "dbwsid:237034608707419186011941491025532848312",
                    },
                },
                "geo_location": {
                    "city": "Austin",
                    "country": "US",
                    "ip_address": "1.2.3.4",
                    "region": "Texas",
                },
            },
            "p_any_emails": ["david.davidson@example.com", "alice.bob@company.com"],
            "p_any_ip_addresses": ["1.2.3.4"],
            "p_any_usernames": ["Alice Bob", "david davidson"],
            "p_event_time": "2023-04-18 22:31:03",
            "p_log_type": "Dropbox.TeamEvent",
            "p_parse_time": "2023-04-18 22:32:46.967",
            "p_row_id": "fe2163f14b45f3c1b9a49fd31799a504",
            "p_schema_version": 0,
            "p_source_id": "b09c205e-42af-4933-8b18-b910985eb7fb",
            "p_source_label": "dropbox1",
            "participants": [
                {
                    "user": {
                        "_tag": "non_team_member",
                        "account_id": "dbid:AABbWylBrTJ3Je-M37jeWShWuMAFHchEsKM",
                        "display_name": "david davidson",
                        "email": "david.davidson@example.com",
                    }
                }
            ],
            "timestamp": "2023-04-18 22:31:03",
        },
    ),
    PantherRuleTest(
        Name="external share",
        ExpectedResult=True,
        Log={
            "actor": {
                "_tag": "user",
                "user": {
                    "_tag": "team_member",
                    "account_id": "dbid:AAACjvKy90uezyOiLRadIuCy66dK5d1vGGw",
                    "display_name": "Alice Bob",
                    "email": "alice.bob@company.com",
                    "team_member_id": "dbmid:AADSERs2cAsByYt8yQEDU4_qdNQiSdxgCl8",
                },
            },
            "assets": [
                {
                    ".tag": "file",
                    "display_name": "paper1.paper",
                    "file_id": "id:lUP4ZxMYmc4AAAAAAAAAaA",
                    "path": {
                        "contextual": "/pathtest/paper1.paper",
                        "namespace_relative": {
                            "is_shared_namespace": True,
                            "ns_id": "3590048721",
                            "relative_path": "/paper1.paper",
                        },
                    },
                }
            ],
            "context": {
                "_tag": "team_member",
                "account_id": "dbid:AAACjvKy90uezyOiLRadIuCy66dK5d1vGGw",
                "display_name": "Alice Bob",
                "email": "alice.bob@company.com",
                "team_member_id": "dbmid:AADSERs2cAsByYt8yQEDU4_qdNQiSdxgCl8",
            },
            "details": {
                ".tag": "shared_content_add_member_details",
                "shared_content_access_level": {".tag": "viewer"},
            },
            "event_category": {"_tag": "sharing"},
            "event_type": {
                "_tag": "shared_content_add_member",
                "description": "Added users and/or groups to shared file/folder",
            },
            "involve_non_team_member": True,
            "origin": {
                "access_method": {
                    ".tag": "end_user",
                    "end_user": {
                        ".tag": "web",
                        "session_id": "dbwsid:237034608707419186011941491025532848312",
                    },
                },
                "geo_location": {
                    "city": "Austin",
                    "country": "US",
                    "ip_address": "1.2.3.4",
                    "region": "Texas",
                },
            },
            "p_any_emails": ["david.davidson@david.co", "alice.bob@company.com"],
            "p_any_ip_addresses": ["1.2.3.4"],
            "p_any_usernames": ["Alice Bob", "david davidson"],
            "p_event_time": "2023-04-18 22:31:03",
            "p_log_type": "Dropbox.TeamEvent",
            "p_parse_time": "2023-04-18 22:32:46.967",
            "p_row_id": "fe2163f14b45f3c1b9a49fd31799a504",
            "p_schema_version": 0,
            "p_source_id": "b09c205e-42af-4933-8b18-b910985eb7fb",
            "p_source_label": "dropbox1",
            "participants": [
                {
                    "user": {
                        "_tag": "non_team_member",
                        "account_id": "dbid:AABbWylBrTJ3Je-M37jeWShWuMAFHchEsKM",
                        "display_name": "david davidson",
                        "email": "david.davidson@david.co",
                    }
                }
            ],
            "timestamp": "2023-04-18 22:31:03",
        },
    ),
]


class DropboxExternalShare(PantherRule):
    Description = "Dropbox item shared externally"
    DisplayName = "Dropbox External Share"
    Reference = "https://help.dropbox.com/share/share-outside-dropbox"
    Severity = PantherSeverity.Medium
    LogTypes = [PantherLogType.Dropbox_TeamEvent]
    RuleID = "Dropbox.External.Share-prototype"
    Tests = dropbox_external_share_tests
    DROPBOX_ALLOWED_SHARE_DOMAINS = config.DROPBOX_ALLOWED_SHARE_DOMAINS

    def rule(self, event):
        if isinstance(self.DROPBOX_ALLOWED_SHARE_DOMAINS, MagicMock):
            self.DROPBOX_ALLOWED_SHARE_DOMAINS = set(
                json.loads(self.DROPBOX_ALLOWED_SHARE_DOMAINS())
            )  # pylint: disable=not-callable
        if deep_get(event, "event_type", "_tag", default="") == "shared_content_add_member":
            participants = event.get("participants", [{}])
            for participant in participants:
                email = participant.get("user", {}).get("email", "")
                if email.split("@")[-1] not in self.DROPBOX_ALLOWED_SHARE_DOMAINS:
                    return True
        return False

    def title(self, event):
        actor = deep_get(event, "actor", "user", "email", default="<ACTOR_NOT_FOUND>")
        assets = [e.get("display_name", "") for e in event.get("assets", [{}])]
        participants = event.get("participants", [{}])
        external_participants = []
        for participant in participants:
            email = participant.get("user", {}).get("email", "")
            if email.split("@")[-1] not in self.DROPBOX_ALLOWED_SHARE_DOMAINS:
                external_participants.append(email)
        return f"Dropbox: [{actor}] shared [{assets}] with external user [{external_participants}]."

    def alert_context(self, event):
        external_participants = []
        participants = event.get("participants", [{}])
        for participant in participants:
            email = participant.get("user", {}).get("email", "")
            if email.split("@")[-1] not in self.DROPBOX_ALLOWED_SHARE_DOMAINS:
                external_participants.append(email)
        return {"external_participants": external_participants}
