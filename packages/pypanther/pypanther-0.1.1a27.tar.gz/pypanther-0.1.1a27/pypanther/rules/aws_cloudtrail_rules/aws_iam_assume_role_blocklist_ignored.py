from typing import List

from pypanther.base import PantherRule, PantherRuleTest, PantherSeverity
from pypanther.helpers.panther_base_helpers import aws_rule_context, deep_get
from pypanther.helpers.panther_default import aws_cloudtrail_success
from pypanther.log_types import PantherLogType

aws_cloud_trail_iam_assume_role_blacklist_ignored_tests: List[PantherRuleTest] = [
    PantherRuleTest(
        Name="IAM Blocklisted Role Assumed",
        ExpectedResult=True,
        Log={
            "awsRegion": "us-east-1",
            "eventID": "1111",
            "eventName": "AssumeRole",
            "eventSource": "sts.amazonaws.com",
            "eventTime": "2019-01-01T00:00:00Z",
            "eventType": "AwsApiCall",
            "eventVersion": "1.05",
            "recipientAccountId": "123456789012",
            "requestID": "1111",
            "requestParameters": {
                "durationSeconds": 900,
                "roleArn": "arn:aws:iam::123456789012:role/FullAdminRole",
                "roleSessionName": "1111",
            },
            "resources": [
                {
                    "ARN": "arn:aws:iam::123456789012:role/FullAdminRole",
                    "accountId": "123456789012",
                    "type": "AWS::IAM::Role",
                }
            ],
            "responseElements": {
                "assumedRoleUser": {
                    "arn": "arn:aws:sts::123456789012:assumed-role/FullAdminRole/1111",
                    "assumedRoleId": "ABCD:1111",
                },
                "credentials": {
                    "accessKeyId": "1111",
                    "expiration": "Jan 01, 2019 0:00:00 PM",
                    "sessionToken": "1111",
                },
            },
            "sharedEventID": "1111",
            "sourceIPAddress": "111.111.111.111",
            "userAgent": "aws-sdk-go/1.4.14 (go1.11.4; darwin; amd64)",
            "userIdentity": {
                "accesKeyId": "1111",
                "accessKeyId": "1111",
                "accountId": "123456789012",
                "arn": "arn:aws:iam::123456789012:user/example-user",
                "principalId": "1111",
                "sessionContext": {
                    "attributes": {
                        "creationDate": "2019-01-01T00:00:00Z",
                        "mfaAuthenticated": "true",
                    }
                },
                "type": "IAMUser",
                "userName": "example-user",
            },
        },
    ),
    PantherRuleTest(
        Name="IAM Non Blocklisted Role Assumed",
        ExpectedResult=False,
        Log={
            "awsRegion": "us-east-1",
            "eventID": "1111",
            "eventName": "AssumeRole",
            "eventSource": "sts.amazonaws.com",
            "eventTime": "2019-01-01T00:00:00Z",
            "eventType": "AwsApiCall",
            "eventVersion": "1.05",
            "recipientAccountId": "123456789012",
            "requestID": "1111",
            "requestParameters": {
                "durationSeconds": 900,
                "roleArn": "arn:aws:iam::123456789012:role/example-role",
                "roleSessionName": "1111",
            },
            "resources": [
                {
                    "ARN": "arn:aws:iam::123456789012:role/example-role",
                    "accountId": "123456789012",
                    "type": "AWS::IAM::Role",
                }
            ],
            "responseElements": {
                "assumedRoleUser": {
                    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/1111",
                    "assumedRoleId": "ABCD:1111",
                },
                "credentials": {
                    "accessKeyId": "1111",
                    "expiration": "Jan 01, 2019 0:00:00 PM",
                    "sessionToken": "1111",
                },
            },
            "sharedEventID": "1111",
            "sourceIPAddress": "111.111.111.111",
            "userAgent": "aws-sdk-go/1.4.14 (go1.11.4; darwin; amd64)",
            "userIdentity": {
                "accesKeyId": "1111",
                "accessKeyId": "1111",
                "accountId": "123456789012",
                "arn": "arn:aws:iam::123456789012:user/example-user",
                "principalId": "1111",
                "sessionContext": {
                    "attributes": {
                        "creationDate": "2019-01-01T00:00:00Z",
                        "mfaAuthenticated": "true",
                    }
                },
                "type": "IAMUser",
                "userName": "example-user",
            },
        },
    ),
    PantherRuleTest(
        Name="Error Assuming IAM Blocked Role",
        ExpectedResult=False,
        Log={
            "awsRegion": "us-east-1",
            "errorCode": "ExpiredToken",
            "eventID": "1111",
            "eventName": "AssumeRole",
            "eventSource": "sts.amazonaws.com",
            "eventTime": "2019-01-01T00:00:00Z",
            "eventType": "AwsApiCall",
            "eventVersion": "1.05",
            "recipientAccountId": "123456789012",
            "requestID": "1111",
            "requestParameters": {
                "durationSeconds": 900,
                "roleArn": "arn:aws:iam::123456789012:role/FullAdminRole",
                "roleSessionName": "1111",
            },
            "resources": [
                {
                    "ARN": "arn:aws:iam::123456789012:role/FullAdminRole",
                    "accountId": "123456789012",
                    "type": "AWS::IAM::Role",
                }
            ],
            "responseElements": {
                "assumedRoleUser": {
                    "arn": "arn:aws:sts::123456789012:assumed-role/FullAdminRole/1111",
                    "assumedRoleId": "ABCD:1111",
                },
                "credentials": {
                    "accessKeyId": "1111",
                    "expiration": "Jan 01, 2019 0:00:00 PM",
                    "sessionToken": "1111",
                },
            },
            "sharedEventID": "1111",
            "sourceIPAddress": "111.111.111.111",
            "userAgent": "aws-sdk-go/1.4.14 (go1.11.4; darwin; amd64)",
            "userIdentity": {
                "accesKeyId": "1111",
                "accessKeyId": "1111",
                "accountId": "123456789012",
                "arn": "arn:aws:iam::123456789012:user/example-user",
                "principalId": "1111",
                "sessionContext": {
                    "attributes": {
                        "creationDate": "2019-01-01T00:00:00Z",
                        "mfaAuthenticated": "true",
                    }
                },
                "type": "IAMUser",
                "userName": "example-user",
            },
        },
    ),
]


class AWSCloudTrailIAMAssumeRoleBlacklistIgnored(PantherRule):
    RuleID = "AWS.CloudTrail.IAMAssumeRoleBlacklistIgnored-prototype"
    DisplayName = "IAM Assume Role Blocklist Ignored"
    Enabled = False
    LogTypes = [PantherLogType.AWS_CloudTrail]
    Tags = [
        "AWS",
        "Configuration Required",
        "Identity and Access Management",
        "Privilege Escalation:Abuse Elevation Control Mechanism",
    ]
    Reports = {"MITRE ATT&CK": ["TA0004:T1548"]}
    Severity = PantherSeverity.High
    Description = (
        "A user assumed a role that was explicitly blocklisted for manual user assumption.\n"
    )
    Runbook = "Verify that this was an approved assume role action. If not, consider revoking the access immediately and updating the AssumeRolePolicyDocument to prevent this from happening again.\n"
    Reference = "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html"
    SummaryAttributes = ["userAgent", "sourceIpAddress", "recipientAccountId", "p_any_aws_arns"]
    Tests = aws_cloud_trail_iam_assume_role_blacklist_ignored_tests
    # This is a list of role ARNs that should not be assumed by users in normal operations
    ASSUME_ROLE_BLOCKLIST = ["arn:aws:iam::123456789012:role/FullAdminRole"]

    def rule(self, event):
        # Only considering successful AssumeRole action
        if not aws_cloudtrail_success(event) or event.get("eventName") != "AssumeRole":
            return False
        # Only considering user actions
        if deep_get(event, "userIdentity", "type") not in ["IAMUser", "FederatedUser"]:
            return False
        return deep_get(event, "requestParameters", "roleArn") in self.ASSUME_ROLE_BLOCKLIST

    def alert_context(self, event):
        return aws_rule_context(event)
