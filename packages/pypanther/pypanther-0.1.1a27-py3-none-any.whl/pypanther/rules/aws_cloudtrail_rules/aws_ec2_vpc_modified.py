from typing import List

from pypanther.base import PantherRule, PantherRuleTest, PantherSeverity
from pypanther.helpers.panther_base_helpers import aws_rule_context
from pypanther.helpers.panther_default import aws_cloudtrail_success
from pypanther.log_types import PantherLogType

awsec2_vpc_modified_tests: List[PantherRuleTest] = [
    PantherRuleTest(
        Name="VPC Modified",
        ExpectedResult=True,
        Log={
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "1111:tester",
                "arn": "arn:aws:sts::123456789012:assumed-role/tester",
                "accountId": "123456789012",
                "accessKeyId": "1",
                "sessionContext": {
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "1111",
                        "arn": "arn:aws:iam::123456789012:role/tester",
                        "accountId": "123456789012",
                        "userName": "tester",
                    },
                    "webIdFederationData": {},
                    "attributes": {
                        "mfaAuthenticated": "true",
                        "creationDate": "2019-01-01T00:00:00Z",
                    },
                },
            },
            "eventTime": "2019-01-01T00:00:00Z",
            "eventSource": "ec2.amazonaws.com",
            "eventName": "CreateVpc",
            "awsRegion": "us-west-2",
            "sourceIPAddress": "111.111.111.111",
            "userAgent": "console.ec2.amazonaws.com",
            "requestParameters": {
                "cidrBlock": "0.0.0.0/26",
                "instanceTenancy": "default",
                "amazonProvidedIpv6CidrBlock": False,
            },
            "responseElements": {
                "requestID": "1",
                "vpc": {
                    "vpcId": "vpc-1",
                    "state": "pending",
                    "ownerId": "123456789012",
                    "cidrBlock": "0.0.0.0/26",
                    "cidrBlockAssociationSet": {
                        "items": [
                            {
                                "cidrBlock": "0.0.0.0/26",
                                "associationId": "vpc-cidr-assoc-1",
                                "cidrBlockState": {"state": "associated"},
                            }
                        ]
                    },
                    "ipv6CidrBlockAssociationSet": {},
                    "dhcpOptionsId": "dopt-1",
                    "instanceTenancy": "default",
                    "tagSet": {},
                    "isDefault": False,
                },
            },
            "requestID": "1",
            "eventID": "1",
            "eventType": "AwsApiCall",
            "recipientAccountId": "123456789012",
        },
    ),
    PantherRuleTest(
        Name="VPC Not Modified",
        ExpectedResult=False,
        Log={
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "1111:tester",
                "arn": "arn:aws:sts::123456789012:assumed-role/tester",
                "accountId": "123456789012",
                "accessKeyId": "1",
                "sessionContext": {
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "1111",
                        "arn": "arn:aws:iam::123456789012:role/tester",
                        "accountId": "123456789012",
                        "userName": "tester",
                    },
                    "webIdFederationData": {},
                    "attributes": {
                        "mfaAuthenticated": "false",
                        "creationDate": "2019-01-01T00:00:00Z",
                    },
                },
            },
            "eventTime": "2019-01-01T00:00:00Z",
            "eventSource": "ec2.amazonaws.com",
            "eventName": "DescribeVpcs",
            "awsRegion": "us-west-2",
            "sourceIPAddress": "111.111.111.111",
            "userAgent": "Mozilla",
            "requestParameters": {"vpcSet": {}, "filterSet": {}},
            "responseElements": None,
            "requestID": "1",
            "eventID": "1",
            "eventType": "AwsApiCall",
            "recipientAccountId": "123456789012",
        },
    ),
    PantherRuleTest(
        Name="Error Modifying VPC",
        ExpectedResult=False,
        Log={
            "errorCode": "UnknownParameter",
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "1111:tester",
                "arn": "arn:aws:sts::123456789012:assumed-role/tester",
                "accountId": "123456789012",
                "accessKeyId": "1",
                "sessionContext": {
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "1111",
                        "arn": "arn:aws:iam::123456789012:role/tester",
                        "accountId": "123456789012",
                        "userName": "tester",
                    },
                    "webIdFederationData": {},
                    "attributes": {
                        "mfaAuthenticated": "true",
                        "creationDate": "2019-01-01T00:00:00Z",
                    },
                },
            },
            "eventTime": "2019-01-01T00:00:00Z",
            "eventSource": "ec2.amazonaws.com",
            "eventName": "CreateVpc",
            "awsRegion": "us-west-2",
            "sourceIPAddress": "111.111.111.111",
            "userAgent": "console.ec2.amazonaws.com",
            "requestParameters": {
                "cidrBlock": "0.0.0.0/26",
                "instanceTenancy": "default",
                "amazonProvidedIpv6CidrBlock": False,
            },
            "responseElements": {
                "requestID": "1",
                "vpc": {
                    "vpcId": "vpc-1",
                    "state": "pending",
                    "ownerId": "123456789012",
                    "cidrBlock": "0.0.0.0/26",
                    "cidrBlockAssociationSet": {
                        "items": [
                            {
                                "cidrBlock": "0.0.0.0/26",
                                "associationId": "vpc-cidr-assoc-1",
                                "cidrBlockState": {"state": "associated"},
                            }
                        ]
                    },
                    "ipv6CidrBlockAssociationSet": {},
                    "dhcpOptionsId": "dopt-1",
                    "instanceTenancy": "default",
                    "tagSet": {},
                    "isDefault": False,
                },
            },
            "requestID": "1",
            "eventID": "1",
            "eventType": "AwsApiCall",
            "recipientAccountId": "123456789012",
        },
    ),
]


class AWSEC2VPCModified(PantherRule):
    RuleID = "AWS.EC2.VPCModified-prototype"
    DisplayName = "EC2 VPC Modified"
    LogTypes = [PantherLogType.AWS_CloudTrail]
    Tags = ["AWS", "Security Control", "Defense Evasion:Impair Defenses"]
    Reports = {"CIS": ["3.14"], "MITRE ATT&CK": ["TA0005:T1562"]}
    Severity = PantherSeverity.Info
    DedupPeriodMinutes = 720
    Description = "An EC2 VPC was modified."
    Runbook = "https://docs.runpanther.io/alert-runbooks/built-in-rules/aws-ec2-vpc-modified"
    Reference = "https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html"
    SummaryAttributes = [
        "eventName",
        "userAgent",
        "sourceIpAddress",
        "recipientAccountId",
        "p_any_aws_arns",
    ]
    Tests = awsec2_vpc_modified_tests
    # API calls that are indicative of an EC2 VPC modification
    EC2_VPC_MODIFIED_EVENTS = {
        "CreateVpc",
        "DeleteVpc",
        "ModifyVpcAttribute",
        "AcceptVpcPeeringConnection",
        "CreateVpcPeeringConnection",
        "DeleteVpcPeeringConnection",
        "RejectVpcPeeringConnection",
        "AttachClassicLinkVpc",
        "DetachClassicLinkVpc",
        "DisableVpcClassicLink",
        "EnableVpcClassicLink",
    }

    def rule(self, event):
        return (
            aws_cloudtrail_success(event) and event.get("eventName") in self.EC2_VPC_MODIFIED_EVENTS
        )

    def dedup(self, event):
        return event.get("recipientAccountId")

    def alert_context(self, event):
        return aws_rule_context(event)
