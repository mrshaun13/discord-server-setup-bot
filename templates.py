"""
Discord Server Templates
Multiple pre-configured server templates for different use cases
"""

# Import the original AI Dev template
from server_config import SERVER_CONFIG as AI_DEV_CONFIG, ROLES_CONFIG as AI_DEV_ROLES, RULES_CONTENT as AI_DEV_RULES, WELCOME_CONTENT as AI_DEV_WELCOME, RESOURCES_CONTENT as AI_DEV_RESOURCES

# Template registry
TEMPLATES = {
    "ai-dev": {
        "name": "AI Development Community",
        "description": "AI/ML development, research, and learning community",
        "config": AI_DEV_CONFIG,
        "roles": AI_DEV_ROLES,
        "rules": AI_DEV_RULES,
        "welcome": AI_DEV_WELCOME,
        "resources": AI_DEV_RESOURCES,
    },
    "aws-chatops": {
        "name": "AWS ChatOps",
        "description": "AWS infrastructure management and ChatOps for cloud operations",
        "config": {
            "categories": [
                {
                    "name": "📢 GENERAL",
                    "position": 0,
                    "channels": [
                        {"name": "announcements", "type": "text", "topic": "📣 Important team announcements and updates"},
                        {"name": "general", "type": "text", "topic": "💬 General team chat"},
                        {"name": "random", "type": "text", "topic": "�� Off-topic and water cooler chat"},
                    ],
                },
                {
                    "name": "🚨 ALERTS & INCIDENTS",
                    "position": 1,
                    "channels": [
                        {"name": "critical-alerts", "type": "text", "topic": "🔴 P0/P1 critical production alerts"},
                        {"name": "warning-alerts", "type": "text", "topic": "🟡 P2/P3 warning level alerts"},
                        {"name": "info-alerts", "type": "text", "topic": "🟢 Informational alerts and notifications"},
                        {"name": "incident-response", "type": "text", "topic": "🚒 Active incident coordination and response"},
                        {"name": "postmortems", "type": "text", "topic": "📝 Incident postmortems and lessons learned"},
                    ],
                },
                {
                    "name": "☁️ AWS SERVICES",
                    "position": 2,
                    "channels": [
                        {"name": "ec2-compute", "type": "text", "topic": "🖥️ EC2, Auto Scaling, ECS, EKS discussions"},
                        {"name": "lambda-serverless", "type": "text", "topic": "⚡ Lambda, API Gateway, serverless architecture"},
                        {"name": "rds-databases", "type": "text", "topic": "🗄️ RDS, Aurora, DynamoDB, database operations"},
                        {"name": "s3-storage", "type": "text", "topic": "📦 S3, EBS, EFS, Glacier storage management"},
                        {"name": "networking", "type": "text", "topic": "🌐 VPC, Route53, CloudFront, Load Balancers"},
                        {"name": "security-iam", "type": "text", "topic": "🔒 IAM, Security Groups, KMS, Secrets Manager"},
                    ],
                },
                {
                    "name": "🔧 OPERATIONS",
                    "position": 3,
                    "channels": [
                        {"name": "deployments", "type": "text", "topic": "🚀 Deployment notifications and coordination"},
                        {"name": "ci-cd", "type": "text", "topic": "⚙️ CI/CD pipeline discussions and updates"},
                        {"name": "infrastructure", "type": "text", "topic": "🏗️ Terraform, CloudFormation, IaC discussions"},
                        {"name": "monitoring", "type": "text", "topic": "📊 CloudWatch, metrics, dashboards, observability"},
                        {"name": "logs", "type": "text", "topic": "📋 Log analysis, CloudWatch Logs, troubleshooting"},
                        {"name": "backups-dr", "type": "text", "topic": "💾 Backup operations and disaster recovery"},
                    ],
                },
                {
                    "name": "💰 COST & BILLING",
                    "position": 4,
                    "channels": [
                        {"name": "cost-alerts", "type": "text", "topic": "💸 Cost anomaly alerts and budget notifications"},
                        {"name": "cost-optimization", "type": "text", "topic": "📉 Cost reduction strategies and optimization"},
                        {"name": "billing-reports", "type": "text", "topic": "📊 Monthly billing reports and analysis"},
                    ],
                },
                {
                    "name": "🔄 AUTOMATION",
                    "position": 5,
                    "channels": [
                        {"name": "bot-commands", "type": "text", "topic": "🤖 ChatOps bot commands and automation"},
                        {"name": "scheduled-tasks", "type": "text", "topic": "⏰ Cron jobs, EventBridge, scheduled operations"},
                        {"name": "scripts-tools", "type": "text", "topic": "🛠️ Automation scripts and tooling discussions"},
                    ],
                },
                {
                    "name": "📚 DOCUMENTATION",
                    "position": 6,
                    "channels": [
                        {"name": "runbooks", "type": "text", "topic": "📖 Operational runbooks and procedures"},
                        {"name": "architecture", "type": "text", "topic": "🏛️ Architecture diagrams and design docs"},
                        {"name": "knowledge-base", "type": "text", "topic": "💡 Tips, tricks, and institutional knowledge"},
                    ],
                },
                {
                    "name": "🔊 VOICE",
                    "position": 7,
                    "channels": [
                        {"name": "War Room", "type": "voice", "topic": "🚨 Incident response war room"},
                        {"name": "Team Standup", "type": "voice", "topic": "👥 Daily standups and team meetings"},
                        {"name": "Pair Ops", "type": "voice", "topic": "👨‍💻 Pair operations and troubleshooting"},
                    ],
                },
            ],
        },
        "roles": [
            {"name": "🔴 On-Call", "color": 0xE74C3C, "permissions": [], "hoist": True, "mentionable": True},
            {"name": "👑 SRE Lead", "color": 0x9B59B6, "permissions": ["administrator"], "hoist": True, "mentionable": True},
            {"name": "⚙️ SRE", "color": 0x3498DB, "permissions": ["manage_channels", "manage_messages"], "hoist": True, "mentionable": True},
            {"name": "☁️ Cloud Engineer", "color": 0x1ABC9C, "permissions": [], "hoist": False, "mentionable": True},
            {"name": "💻 DevOps", "color": 0xE67E22, "permissions": [], "hoist": False, "mentionable": True},
            {"name": "🔒 Security", "color": 0xE91E63, "permissions": [], "hoist": False, "mentionable": True},
            {"name": "📊 Platform", "color": 0x95A5A6, "permissions": [], "hoist": False, "mentionable": True},
            {"name": "🚨 Incident Commander", "color": 0xC0392B, "permissions": [], "hoist": False, "mentionable": True},
        ],
        "rules": """# 📜 AWS ChatOps Server Rules

## Rule 1: Alert Hygiene 🚨
• Acknowledge alerts promptly in appropriate channels
• Use threads for alert investigation
• Update incident channels with status
• Close alerts when resolved

## Rule 2: On-Call Protocol 📞
• On-call engineers must respond within SLA
• Escalate if you need help - don't struggle alone
• Hand off properly during shift changes
• Document all actions taken

## Rule 3: Change Management 🔄
• Announce deployments in #deployments
• Follow change approval process for production
• Have rollback plan ready
• No cowboy changes in production

## Rule 4: Security First 🔒
• Never share credentials or API keys
• Use AWS Secrets Manager for sensitive data
• Report security issues immediately
• Follow least privilege principle

## Rule 5: Documentation 📚
• Document your fixes in #knowledge-base
• Update runbooks after incidents
• Share learnings in #postmortems
• Keep architecture docs current

## Rule 6: Cost Awareness 💰
• Monitor your resource costs
• Clean up unused resources
• Use appropriate instance sizes
• Report cost anomalies

## Rule 7: Collaboration 🤝
• Help teammates troubleshoot
• Share knowledge freely
• Be patient with questions
• Celebrate wins together

## Rule 8: Professionalism 💼
• Keep discussions professional
• No blame culture - focus on systems
• Respect on-call boundaries
• Maintain work-life balance
""",
        "welcome": """# 👋 Welcome to AWS ChatOps\!

This server is your central hub for AWS infrastructure management and operations.

## 🚀 Quick Start

1. **Check Alerts** - Monitor #critical-alerts and #warning-alerts
2. **On-Call** - Check who's on-call in the team roster
3. **Deployments** - Follow #deployments for changes
4. **Documentation** - Bookmark #runbooks and #architecture

## 📱 ChatOps Commands

Use bot commands in #bot-commands:
• `/aws status` - Check service health
• `/ec2 list` - List EC2 instances
• `/deploy status` - Check deployment status
• `/incident create` - Start incident response
• `/cost report` - Get cost summary

## 🚨 Incident Response

1. Create incident in #incident-response
2. Join War Room voice channel
3. Assign Incident Commander
4. Follow incident runbook
5. Post postmortem in #postmortems

## 💡 Best Practices

• Acknowledge alerts within 5 minutes
• Use threads to keep channels clean
• Document everything
• Ask for help early
• Automate repetitive tasks

Let's keep our AWS infrastructure running smoothly\! ☁️
""",
        "resources": """# 📚 AWS Resources

## 🎓 AWS Documentation
• [AWS Documentation](https://docs.aws.amazon.com/)
• [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
• [AWS Best Practices](https://aws.amazon.com/architecture/best-practices/)

## 🛠️ Tools
• [AWS CLI](https://aws.amazon.com/cli/)
• [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
• [AWS CDK](https://aws.amazon.com/cdk/)
• [LocalStack](https://localstack.cloud/) - Local AWS testing

## 📊 Monitoring
• [CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)
• [X-Ray Tracing](https://aws.amazon.com/xray/)
• [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

## 💰 Cost Management
• [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
• [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)
• [Cost Optimization Best Practices](https://aws.amazon.com/pricing/cost-optimization/)

## 🔒 Security
• [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
• [AWS Security Hub](https://aws.amazon.com/security-hub/)
• [AWS GuardDuty](https://aws.amazon.com/guardduty/)

## 📖 Runbooks
• EC2 Instance Troubleshooting
• RDS Failover Procedure
• S3 Bucket Recovery
• Lambda Cold Start Optimization
• VPC Connectivity Issues

*Internal runbooks available in #runbooks*
""",
    },
    "itil-ops": {
        "name": "ITIL Business Operations",
        "description": "ITIL-based IT service management and business operations",
        "config": {
            "categories": [
                {
                    "name": "📢 GENERAL",
                    "position": 0,
                    "channels": [
                        {"name": "announcements", "type": "text", "topic": "📣 Company-wide IT announcements"},
                        {"name": "general", "type": "text", "topic": "💬 General IT team discussion"},
                        {"name": "water-cooler", "type": "text", "topic": "☕ Casual chat and breaks"},
                    ],
                },
                {
                    "name": "🎫 SERVICE DESK",
                    "position": 1,
                    "channels": [
                        {"name": "incidents", "type": "text", "topic": "🚨 Active incident tracking and resolution"},
                        {"name": "service-requests", "type": "text", "topic": "📝 Service request fulfillment"},
                        {"name": "user-support", "type": "text", "topic": "👥 End user support and questions"},
                        {"name": "vip-support", "type": "text", "topic": "⭐ Executive and VIP user support"},
                        {"name": "ticket-overflow", "type": "text", "topic": "📊 High volume ticket coordination"},
                    ],
                },
                {
                    "name": "🔄 CHANGE MANAGEMENT",
                    "position": 2,
                    "channels": [
                        {"name": "change-requests", "type": "text", "topic": "📋 Change request submissions and tracking"},
                        {"name": "change-advisory", "type": "text", "topic": "🏛️ CAB meetings and approvals"},
                        {"name": "standard-changes", "type": "text", "topic": "✅ Pre-approved standard changes"},
                        {"name": "emergency-changes", "type": "text", "topic": "🚨 Emergency change coordination"},
                        {"name": "change-calendar", "type": "text", "topic": "📅 Scheduled changes and maintenance windows"},
                    ],
                },
                {
                    "name": "⚠️ PROBLEM MANAGEMENT",
                    "position": 3,
                    "channels": [
                        {"name": "problem-records", "type": "text", "topic": "🔍 Problem investigation and tracking"},
                        {"name": "root-cause-analysis", "type": "text", "topic": "🎯 RCA discussions and findings"},
                        {"name": "known-errors", "type": "text", "topic": "📚 Known error database and workarounds"},
                        {"name": "trend-analysis", "type": "text", "topic": "📈 Incident trend analysis"},
                    ],
                },
                {
                    "name": "📦 RELEASE MANAGEMENT",
                    "position": 4,
                    "channels": [
                        {"name": "release-planning", "type": "text", "topic": "📅 Release planning and scheduling"},
                        {"name": "release-testing", "type": "text", "topic": "🧪 UAT and release testing coordination"},
                        {"name": "deployment-status", "type": "text", "topic": "🚀 Live deployment tracking"},
                        {"name": "rollback-procedures", "type": "text", "topic": "⏪ Rollback coordination if needed"},
                    ],
                },
                {
                    "name": "🏗️ CONFIGURATION MANAGEMENT",
                    "position": 5,
                    "channels": [
                        {"name": "cmdb-updates", "type": "text", "topic": "🗄️ Configuration item updates"},
                        {"name": "asset-management", "type": "text", "topic": "💻 Hardware and software asset tracking"},
                        {"name": "license-management", "type": "text", "topic": "📜 Software license compliance"},
                    ],
                },
                {
                    "name": "📊 SERVICE LEVEL MANAGEMENT",
                    "position": 6,
                    "channels": [
                        {"name": "sla-monitoring", "type": "text", "topic": "⏱️ SLA compliance monitoring"},
                        {"name": "performance-metrics", "type": "text", "topic": "📈 KPI and metric tracking"},
                        {"name": "service-reports", "type": "text", "topic": "📊 Monthly service reports"},
                        {"name": "sla-breaches", "type": "text", "topic": "🚨 SLA breach notifications and actions"},
                    ],
                },
                {
                    "name": "🔐 SECURITY & COMPLIANCE",
                    "position": 7,
                    "channels": [
                        {"name": "security-incidents", "type": "text", "topic": "🔒 Security incident response"},
                        {"name": "access-management", "type": "text", "topic": "🔑 User access requests and reviews"},
                        {"name": "compliance-audits", "type": "text", "topic": "✅ Audit coordination and findings"},
                        {"name": "security-patches", "type": "text", "topic": "🛡️ Security patch management"},
                    ],
                },
                {
                    "name": "💼 BUSINESS CONTINUITY",
                    "position": 8,
                    "channels": [
                        {"name": "disaster-recovery", "type": "text", "topic": "🆘 DR planning and testing"},
                        {"name": "backup-monitoring", "type": "text", "topic": "💾 Backup status and verification"},
                        {"name": "business-continuity", "type": "text", "topic": "📋 BCP planning and exercises"},
                    ],
                },
                {
                    "name": "📚 KNOWLEDGE MANAGEMENT",
                    "position": 9,
                    "channels": [
                        {"name": "knowledge-base", "type": "text", "topic": "💡 KB articles and documentation"},
                        {"name": "procedures", "type": "text", "topic": "📖 Standard operating procedures"},
                        {"name": "training", "type": "text", "topic": "🎓 Team training and development"},
                        {"name": "lessons-learned", "type": "text", "topic": "📝 Post-incident learnings"},
                    ],
                },
                {
                    "name": "🔊 VOICE CHANNELS",
                    "position": 10,
                    "channels": [
                        {"name": "Incident Bridge", "type": "voice", "topic": "🚨 Major incident bridge line"},
                        {"name": "CAB Meeting", "type": "voice", "topic": "🏛️ Change Advisory Board meetings"},
                        {"name": "Team Huddle", "type": "voice", "topic": "👥 Quick team sync-ups"},
                        {"name": "Training Room", "type": "voice", "topic": "🎓 Training sessions"},
                    ],
                },
            ],
        },
        "roles": [
            {"name": "👑 IT Director", "color": 0x992D22, "permissions": ["administrator"], "hoist": True, "mentionable": True},
            {"name": "🏛️ Service Manager", "color": 0x9B59B6, "permissions": ["manage_channels", "manage_messages"], "hoist": True, "mentionable": True},
            {"name": "🎫 Incident Manager", "color": 0xE74C3C, "permissions": [], "hoist": True, "mentionable": True},
            {"name": "🔄 Change Manager", "color": 0x3498DB, "permissions": [], "hoist": True, "mentionable": True},
            {"name": "⚠️ Problem Manager", "color": 0xE67E22, "permissions": [], "hoist": True, "mentionable": True},
            {"name": "👨‍💼 Service Desk Lead", "color": 0x1ABC9C, "permissions": [], "hoist": False, "mentionable": True},
            {"name": "🎧 Service Desk Agent", "color": 0x16A085, "permissions": [], "hoist": False, "mentionable": True},
            {"name": "🔧 Technical Support", "color": 0x27AE60, "permissions": [], "hoist": False, "mentionable": True},
            {"name": "🔒 Security Team", "color": 0xC0392B, "permissions": [], "hoist": False, "mentionable": True},
            {"name": "📊 Service Analyst", "color": 0x2980B9, "permissions": [], "hoist": False, "mentionable": True},
        ],
        "rules": """# 📜 ITIL Operations Server Rules

## Rule 1: ITIL Process Adherence 📋
• Follow established ITIL processes
• Document all actions in ticketing system
• Escalate according to escalation matrix
• Maintain process integrity

## Rule 2: Incident Management 🚨
• Log all incidents immediately
• Categorize and prioritize correctly
• Update tickets with progress
• Close incidents only when resolved and verified

## Rule 3: Change Management 🔄
• All changes require CAB approval (except standard/emergency)
• Submit change requests 5 business days in advance
• Include rollback plan in all changes
• Document actual vs planned outcomes

## Rule 4: Communication Standards 💬
• Use professional language
• Provide clear status updates
• CC relevant stakeholders
• Respond to escalations within SLA

## Rule 5: SLA Compliance ⏱️
• Monitor SLA timers actively
• Escalate before SLA breach
• Document reasons for any breaches
• Prioritize by business impact

## Rule 6: Security & Compliance 🔒
• Follow access control procedures
• Never share credentials
• Report security incidents immediately
• Maintain audit trail

## Rule 7: Knowledge Management 📚
• Document solutions in KB
• Update procedures after changes
• Share learnings from incidents
• Keep documentation current

## Rule 8: Customer Service 🤝
• Treat all users with respect
• Set realistic expectations
• Provide regular updates
• Follow up on resolutions
""",
        "welcome": """# 👋 Welcome to IT Operations\!

This server is the central hub for ITIL-based IT service management.

## 🚀 Getting Started

1. **Check Your Role** - Verify your role assignments
2. **Review Processes** - Read procedures in #procedures
3. **Monitor Channels** - Watch relevant channels for your role
4. **Update Status** - Keep your availability status current

## 🎫 Service Desk

**Incident Priority:**
• P1 (Critical) - Business stopped, resolve in 1 hour
• P2 (High) - Major impact, resolve in 4 hours
• P3 (Medium) - Limited impact, resolve in 1 business day
• P4 (Low) - Minor issue, resolve in 5 business days

**Escalation Path:**
Service Desk → Technical Support → Subject Matter Expert → Management

## 🔄 Change Management

**Change Types:**
• **Standard** - Pre-approved, low risk
• **Normal** - Requires CAB approval
• **Emergency** - Critical business need, expedited approval

**CAB Meetings:** Every Tuesday and Thursday at 10 AM

## 📊 Key Metrics

• First Call Resolution Rate
• Mean Time To Resolve (MTTR)
• SLA Compliance %
• Customer Satisfaction Score
• Change Success Rate

## 💡 Quick Tips

• Always log tickets - if it's not logged, it didn't happen
• Use templates for common requests
• Escalate early if unsure
• Document everything
• Communicate proactively

Let's deliver excellent IT service\! 💼
""",
        "resources": """# 📚 ITIL Resources

## 📖 ITIL Framework
• [ITIL 4 Foundation](https://www.axelos.com/certifications/itil-service-management/itil-4-foundation)
• [ITIL Process Guide](https://wiki.en.it-processmaps.com/index.php/ITIL_Processes)
• [ITIL Best Practices](https://www.bmc.com/blogs/itil-best-practices/)

## 🎫 Service Desk Tools
• ServiceNow Documentation
• Incident Management Guide
• Problem Management Guide
• Change Management Guide

## 📊 ITSM Metrics
• [ITSM KPIs](https://www.atlassian.com/itsm/kpis-metrics)
• [SLA Best Practices](https://www.bmc.com/blogs/sla-best-practices/)
• [Service Level Management](https://wiki.en.it-processmaps.com/index.php/Service_Level_Management)

## 🔒 Security & Compliance
• ISO 27001 Standards
• SOC 2 Compliance Guide
• Access Control Procedures
• Incident Response Plan

## 📚 Internal Documentation
• Standard Operating Procedures
• Escalation Matrix
• Contact Directory
• Service Catalog
• CMDB Access

## 🎓 Training
• ITIL Foundation Certification
• ServiceNow Administrator Training
• Incident Management Workshop
• Change Management Workshop
• Problem Management Training

*Access internal wiki for detailed procedures*
""",
    },
}

def get_template(template_name, scale_percent=100):
    """
    Get a template by name with optional scaling
    
    Args:
        template_name: Name of the template
        scale_percent: Scale percentage (1-100), default 100
    
    Returns:
        Template configuration (scaled if scale_percent < 100)
    """
    from template_scaler import scale_template
    from extended_templates import EXTENDED_TEMPLATES
    
    # Merge extended templates
    all_templates = {**TEMPLATES, **EXTENDED_TEMPLATES}
    
    template = all_templates.get(template_name)
    if not template:
        return None
    
    # Scale if needed
    if scale_percent < 100:
        return scale_template(template, scale_percent)
    
    return template

def list_templates():
    """List all available templates"""
    from extended_templates import EXTENDED_TEMPLATES
    
    # Merge all templates
    all_templates = {**TEMPLATES, **EXTENDED_TEMPLATES}
    
    return {name: {"name": t["name"], "description": t["description"]} 
            for name, t in all_templates.items()}
