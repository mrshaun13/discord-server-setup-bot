# Changelog

## [2.0.0] - Template System Release

### Added
- **Multi-template support** - Choose from 3 pre-built server templates
- **`\!templates` command** - List all available templates
- **`\!setup <template>` command** - Setup with specific template
- **AWS ChatOps template** - Complete AWS infrastructure management setup
  - 8 categories, 32 channels, 8 roles
  - Alert management, incident response, cost tracking
  - Service-specific channels (EC2, Lambda, RDS, S3, etc.)
- **ITIL Operations template** - ITIL-compliant service management
  - 11 categories, 43 channels, 10 roles
  - Incident, problem, change, release management
  - SLA monitoring, service desk, CAB support
- **Template system architecture** - Extensible framework for custom templates
- **TEMPLATES.md** - Comprehensive template documentation

### Changed
- **`\!setup` command** - Now accepts optional template parameter (defaults to `ai-dev`)
- **README.md** - Updated with template documentation
- **Bot description** - Now "Discord Server Setup Bot" (was "Discord AI Server Setup Bot")
- **ServerSetup class** - Now accepts template configuration

### Technical
- New `templates.py` module with template registry
- Template structure includes: config, roles, rules, welcome, resources
- Backward compatible - existing `ai-dev` template uses original `server_config.py`

---

## [1.0.0] - Initial Release

### Features
- Single AI Development Community template
- 9 categories, 40+ channels, 12 roles
- Commands: `\!setup`, `\!status`, `\!cleanup`, `\!shutdown`
- Docker support
- Comprehensive documentation
