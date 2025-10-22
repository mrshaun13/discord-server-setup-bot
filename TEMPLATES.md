# 📦 Discord Server Templates

This bot includes three pre-built templates for different use cases. Each template provides a complete server structure with channels, roles, and content tailored to specific needs.

---

## 🤖 AI Development Community (`ai-dev`)

**Use Case:** AI/ML development, research, and learning community

### Categories & Channels
- **WELCOME & INFO** (5 channels)
  - welcome, rules, announcements, resources, roles
- **GENERAL** (4 channels)
  - general, introductions, off-topic, showcase
- **AI DISCUSSION** (5 channels)
  - ai-news, research-papers, ethics-safety, industry-trends, hot-takes
- **DEVELOPMENT** (7 channels)
  - general-dev, llm-development, ml-engineering, computer-vision, agents-automation, code-review, debugging-help
- **TOOLS & FRAMEWORKS** (6 channels)
  - openai-api, anthropic-claude, local-models, langchain-llamaindex, vector-databases, devops-mlops
- **CREATIVE AI** (4 channels)
  - image-generation, video-audio, prompt-engineering, creative-showcase
- **LEARNING** (5 channels)
  - beginner-questions, tutorials-guides, study-group, paper-reading-club, project-ideas
- **COMMUNITY** (4 channels)
  - hackathons-events, job-opportunities, collaboration, feedback-suggestions
- **VOICE CHANNELS** (5 channels)
  - General Hangout, Deep Dive Sessions, Pair Programming, Study Hall, AI Demo Room

### Roles
- 🛡️ Admin, ⚔️ Moderator
- 🧠 ML Researcher, 💻 ML Engineer, 🎨 Creative AI, 🤖 Agent Builder, 📊 Data Scientist, 🔰 Learning
- 📰 News Ping, 📄 Paper Club, 🎯 Hackathon, 💼 Job Alerts

**Total:** 9 categories, 40+ channels, 12 roles

---

## ☁️ AWS ChatOps (`aws-chatops`)

**Use Case:** AWS infrastructure management and ChatOps for cloud operations

### Categories & Channels
- **GENERAL** (3 channels)
  - announcements, general, random
- **ALERTS & INCIDENTS** (5 channels)
  - critical-alerts, warning-alerts, info-alerts, incident-response, postmortems
- **AWS SERVICES** (6 channels)
  - ec2-compute, lambda-serverless, rds-databases, s3-storage, networking, security-iam
- **OPERATIONS** (6 channels)
  - deployments, ci-cd, infrastructure, monitoring, logs, backups-dr
- **COST & BILLING** (3 channels)
  - cost-alerts, cost-optimization, billing-reports
- **AUTOMATION** (3 channels)
  - bot-commands, scheduled-tasks, scripts-tools
- **DOCUMENTATION** (3 channels)
  - runbooks, architecture, knowledge-base
- **VOICE** (3 channels)
  - War Room, Team Standup, Pair Ops

### Roles
- 🔴 On-Call, 👑 SRE Lead, ⚙️ SRE
- ☁️ Cloud Engineer, �� DevOps, 🔒 Security, 📊 Platform, 🚨 Incident Commander

**Total:** 8 categories, 32 channels, 8 roles

### Key Features
- **Alert Management:** Separate channels for critical, warning, and info alerts
- **Service-Specific:** Dedicated channels for major AWS services
- **Incident Response:** War room voice channel and incident coordination
- **Cost Tracking:** Cost alerts and optimization discussions
- **ChatOps Ready:** Bot commands channel for automation
- **SRE Focus:** Roles and structure for SRE teams

---

## 💼 ITIL Business Operations (`itil-ops`)

**Use Case:** ITIL-based IT service management and business operations

### Categories & Channels
- **GENERAL** (3 channels)
  - announcements, general, water-cooler
- **SERVICE DESK** (5 channels)
  - incidents, service-requests, user-support, vip-support, ticket-overflow
- **CHANGE MANAGEMENT** (5 channels)
  - change-requests, change-advisory, standard-changes, emergency-changes, change-calendar
- **PROBLEM MANAGEMENT** (4 channels)
  - problem-records, root-cause-analysis, known-errors, trend-analysis
- **RELEASE MANAGEMENT** (4 channels)
  - release-planning, release-testing, deployment-status, rollback-procedures
- **CONFIGURATION MANAGEMENT** (3 channels)
  - cmdb-updates, asset-management, license-management
- **SERVICE LEVEL MANAGEMENT** (4 channels)
  - sla-monitoring, performance-metrics, service-reports, sla-breaches
- **SECURITY & COMPLIANCE** (4 channels)
  - security-incidents, access-management, compliance-audits, security-patches
- **BUSINESS CONTINUITY** (3 channels)
  - disaster-recovery, backup-monitoring, business-continuity
- **KNOWLEDGE MANAGEMENT** (4 channels)
  - knowledge-base, procedures, training, lessons-learned
- **VOICE CHANNELS** (4 channels)
  - Incident Bridge, CAB Meeting, Team Huddle, Training Room

### Roles
- 👑 IT Director, 🏛️ Service Manager
- 🎫 Incident Manager, 🔄 Change Manager, ⚠️ Problem Manager
- 👨‍💼 Service Desk Lead, 🎧 Service Desk Agent, 🔧 Technical Support, 🔒 Security Team, 📊 Service Analyst

**Total:** 11 categories, 43 channels, 10 roles

### Key Features
- **ITIL Compliant:** Follows ITIL v4 framework
- **Process-Oriented:** Separate channels for each ITIL process
- **CAB Support:** Change Advisory Board meeting coordination
- **SLA Tracking:** Dedicated channels for SLA monitoring
- **Incident Management:** Priority-based incident handling
- **Knowledge Base:** Structured knowledge management

---

## 🚀 Usage

### List Available Templates
```
\!templates
```

### Setup with Template
```
\!setup ai-dev        # AI Development (default)
\!setup aws-chatops   # AWS ChatOps
\!setup itil-ops      # ITIL Operations
```

### Switch Templates
To switch templates after initial setup:
```
\!cleanup                # Remove existing structure
\!confirm_cleanup        # Confirm deletion
\!setup <new-template>   # Set up with new template
```

---

## 🛠️ Customization

### Modify Existing Templates

**For `ai-dev`:**
Edit `server_config.py`

**For `aws-chatops` or `itil-ops`:**
Edit `templates.py`

### Create New Template

Add to `templates.py`:

```python
TEMPLATES["my-template"] = {
    "name": "My Custom Template",
    "description": "Description of what this template provides",
    "config": {
        "categories": [
            {
                "name": "📢 CATEGORY NAME",
                "position": 0,
                "channels": [
                    {
                        "name": "channel-name",
                        "type": "text",  # or "voice"
                        "topic": "Channel description"
                    }
                ]
            }
        ]
    },
    "roles": [
        {
            "name": "🎭 Role Name",
            "color": 0xFF5733,  # Hex color
            "permissions": ["manage_channels"],
            "hoist": True,
            "mentionable": True
        }
    ],
    "rules": "# Server Rules\n\nYour rules here...",
    "welcome": "# Welcome\!\n\nYour welcome message...",
    "resources": "# Resources\n\nYour resources..."
}
```

Then use it:
```
\!setup my-template
```

---

## 📊 Template Comparison

| Feature | ai-dev | aws-chatops | itil-ops |
|---------|--------|-------------|----------|
| **Categories** | 9 | 8 | 11 |
| **Channels** | 40+ | 32 | 43 |
| **Roles** | 12 | 8 | 10 |
| **Voice Channels** | 5 | 3 | 4 |
| **Focus** | Community | Operations | Service Mgmt |
| **Best For** | AI enthusiasts | DevOps/SRE | IT departments |

---

## 💡 Tips

1. **Preview Before Setup:** Use `\!templates` to see all options
2. **Test First:** Try in a test server before production
3. **Customize After:** Manually adjust channels/roles after setup
4. **Combine Templates:** Run multiple setups to combine structures
5. **Document Changes:** Keep notes on customizations

---

## 🔄 Migration Between Templates

If you want to change templates:

1. **Backup Important Content:** Copy messages from key channels
2. **Run Cleanup:** `\!cleanup` → `\!confirm_cleanup`
3. **Setup New Template:** `\!setup <new-template>`
4. **Restore Content:** Paste saved messages if needed
5. **Reassign Roles:** Manually assign roles to members

**Warning:** Cleanup deletes everything. Make sure you have backups\!

---

## 📝 Template Design Guidelines

When creating custom templates:

1. **Keep Categories Focused:** Group related channels
2. **Limit Channel Count:** 30-50 channels is optimal
3. **Use Clear Names:** Descriptive, lowercase, hyphenated
4. **Define Role Hierarchy:** Admin → Manager → Team → User
5. **Set Permissions:** Read-only for announcements, etc.
6. **Include Voice:** At least 2-3 voice channels
7. **Write Clear Rules:** Specific to your use case
8. **Provide Resources:** Links and documentation

---

## 🎯 Best Practices

### For AI Development
- Separate beginner and advanced channels
- Tool-specific channels for focused discussion
- Showcase channel for project sharing
- Paper reading club for research

### For AWS ChatOps
- Priority-based alert channels
- Service-specific channels for clarity
- War room for incident response
- Cost tracking for budget awareness

### For ITIL Operations
- Process-aligned channels
- SLA monitoring and reporting
- Knowledge base for documentation
- CAB meeting coordination

---

## 🆘 Support

**Template Not Working?**
- Check `setup_bot.log` for errors
- Verify bot has Administrator permission
- Ensure all intents are enabled

**Want to Contribute a Template?**
- Fork the repository
- Add your template to `templates.py`
- Test thoroughly
- Submit a pull request

---

**Happy server building\! 🚀**
