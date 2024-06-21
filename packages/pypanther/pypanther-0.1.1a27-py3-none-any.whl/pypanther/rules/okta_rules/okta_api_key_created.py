from typing import List

from pypanther.base import PantherRule, PantherRuleTest, PantherSeverity
from pypanther.helpers.panther_base_helpers import deep_get, okta_alert_context
from pypanther.log_types import PantherLogType

okta_api_key_created_tests: List[PantherRuleTest] = [
    PantherRuleTest(
        Name="API Key Created",
        ExpectedResult=True,
        Log={
            "uuid": "2a992f80-d1ad-4f62-900e-8c68bb72a21b",
            "published": "2021-01-08 21:28:34.875",
            "eventType": "system.api_token.create",
            "version": "0",
            "severity": "INFO",
            "legacyEventType": "api.token.create",
            "displayMessage": "Create API token",
            "actor": {
                "alternateId": "user@example.com",
                "displayName": "Test User",
                "id": "00u3q14ei6KUOm4Xi2p4",
                "type": "User",
            },
            "outcome": {"result": "SUCCESS"},
            "request": {},
            "debugContext": {},
            "target": [
                {
                    "id": "00Tpki36zlWjhjQ1u2p4",
                    "type": "Token",
                    "alternateId": "unknown",
                    "displayName": "test_key",
                    "details": None,
                }
            ],
        },
    )
]


class OktaAPIKeyCreated(PantherRule):
    RuleID = "Okta.APIKeyCreated-prototype"
    DisplayName = "Okta API Key Created"
    LogTypes = [PantherLogType.Okta_SystemLog]
    Tags = [
        "Identity & Access Management",
        "Okta",
        "Credential Access:Steal Application Access Token",
    ]
    Reports = {"MITRE ATT&CK": ["TA0006:T1528"]}
    Severity = PantherSeverity.Info
    Description = "A user created an API Key in Okta"
    Reference = "https://help.okta.com/en/prod/Content/Topics/Security/API.htm"
    Runbook = "Reach out to the user if needed to validate the activity."
    SummaryAttributes = ["eventType", "severity", "displayMessage", "p_any_ip_addresses"]
    Tests = okta_api_key_created_tests

    def rule(self, event):
        return (
            event.get("eventType", None) == "system.api_token.create"
            and deep_get(event, "outcome", "result") == "SUCCESS"
        )

    def title(self, event):
        target = event.get("target", [{}])
        key_name = (
            target[0].get("displayName", "MISSING DISPLAY NAME") if target else "MISSING TARGET"
        )
        return f"{deep_get(event, 'actor', 'displayName')} <{deep_get(event, 'actor', 'alternateId')}>created a new API key - <{key_name}>"

    def alert_context(self, event):
        return okta_alert_context(event)
