# 🤖 Discord Server Setup Bot

A one-time setup bot that automatically configures your Discord server with pre-built templates for different use cases.

**This bot is NOT stateful** - it only runs once to set up your server, then you can shut it down. No need to keep it running!

## 📦 Available Templates

- **`ai-dev`** - AI Development Community (default)
- **`aws-chatops`** - AWS Infrastructure & ChatOps
- **`itil-ops`** - ITIL Business Operations

---

## 📋 Table of Contents

1. [What This Does](#what-this-does)
2. [Quick Start](#quick-start)
3. [Detailed Setup Instructions](#detailed-setup-instructions)
4. [Configuration](#configuration)
5. [Commands](#commands)
6. [Troubleshooting](#troubleshooting)
7. [Customization](#customization)
8. [Architecture](#architecture)
9. [Security](#security)
10. [FAQ](#faq)

---

## 🎯 What This Does

This bot automatically creates complete Discord server structures based on templates:

- **Multiple categories** with organized channels
- **Role hierarchies** tailored to your use case
- **Welcome messages** with server guidelines
- **Detailed rules** posted in appropriate channels
- **Curated resources** specific to the template
- **Proper permissions** configured automatically

### Template: AI Development Community (`ai-dev`)

Default template for AI/ML development, research, and learning.

#### Channel Structure

```
📢 WELCOME & INFO
├── welcome
├── rules
├── announcements
├── resources
└── roles

💬 GENERAL
├── general
├── introductions
├── off-topic
└── showcase

🤖 AI DISCUSSION
├── ai-news
├── research-papers
├── ethics-safety
├── industry-trends
└── hot-takes

🛠️ DEVELOPMENT
├── general-dev
├── llm-development
├── ml-engineering
├── computer-vision
├── agents-automation
├── code-review
└── debugging-help

🔧 TOOLS & FRAMEWORKS
├── openai-api
├── anthropic-claude
├── local-models
├── langchain-llamaindex
├── vector-databases
└── devops-mlops

🎨 CREATIVE AI
├── image-generation
├── video-audio
├── prompt-engineering
└── creative-showcase

🎓 LEARNING
├── beginner-questions
├── tutorials-guides
├── study-group
├── paper-reading-club
└── project-ideas

🎮 COMMUNITY
├── hackathons-events
├── job-opportunities
├── collaboration
└── feedback-suggestions

🔊 VOICE CHANNELS
├── General Hangout
├── Deep Dive Sessions
├── Pair Programming
├── Study Hall
└── AI Demo Room
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ OR Docker
- A Discord account
- Administrator access to your Discord server

### 1. Create a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Give it a name (e.g., "AI Server Setup Bot")
4. Go to "Bot" section
5. Click "Add Bot"
6. **Enable these Privileged Gateway Intents:**
   - ✅ Presence Intent
   - ✅ Server Members Intent
   - ✅ Message Content Intent
7. Click "Reset Token" and copy your bot token (you'll need this!)

### 2. Invite Bot to Your Server

1. Go to "OAuth2" → "URL Generator"
2. Select scopes:
   - ✅ `bot`
   - ✅ `applications.commands`
3. Select bot permissions:
   - ✅ Administrator (or at minimum: Manage Roles, Manage Channels, Send Messages, Manage Messages)
4. Copy the generated URL and open it in your browser
5. Select your server and authorize

### 3. Configure the Bot

```bash
# Clone or download this repository
cd discord-ai-server-bot

# Copy the example environment file
cp .env.example .env

# Edit .env and add your bot token
nano .env  # or use your preferred editor
```

Your `.env` file should look like:
```env
DISCORD_BOT_TOKEN=your_actual_bot_token_here
GUILD_ID=your_server_id_here  # Optional - leave empty to work on any server
```

**To get your Server ID:**
1. Enable Developer Mode in Discord (User Settings → Advanced → Developer Mode)
2. Right-click your server icon → Copy ID

### 4. Run the Bot

**Option A: Using the Quick Start Script (Recommended)**
```bash
chmod +x run.sh
./run.sh
```

**Option B: Using Docker**
```bash
docker-compose up --build
```

**Option C: Using Python Directly**
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the bot
python setup_bot.py
```

### 5. Set Up Your Server

Once the bot is running and online:

1. **List available templates:**
   ```
   !templates
   ```

2. **Choose and run setup:**
   ```
   !setup ai-dev        # AI Development (default)
   !setup aws-chatops   # AWS ChatOps
   !setup itil-ops      # ITIL Operations
   ```

3. Wait 2-5 minutes for the setup to complete
4. Review the created channels and roles
5. Type `!shutdown` to stop the bot

**That's it!** Your server is now fully configured. You can shut down the bot - it's no longer needed.

---

## 📖 Detailed Setup Instructions

### Step 1: Discord Bot Creation

#### Creating the Application

1. Navigate to https://discord.com/developers/applications
2. Click "New Application" (top right)
3. Enter a name: "AI Server Setup Bot" (or your preference)
4. Accept the Terms of Service
5. Click "Create"

#### Configuring the Bot

1. In the left sidebar, click "Bot"
2. Click "Add Bot" → "Yes, do it!"
3. Under "Token", click "Reset Token" → "Yes, do it!"
4. **IMPORTANT:** Copy this token immediately and save it securely
   - You'll need this for your `.env` file
   - Never share this token publicly
   - If compromised, reset it immediately

#### Setting Privileged Intents

Still in the "Bot" section:

1. Scroll down to "Privileged Gateway Intents"
2. Enable ALL three intents:
   - ✅ **Presence Intent**
   - ✅ **Server Members Intent**
   - ✅ **Message Content Intent**
3. Click "Save Changes"

**Why these are needed:**
- **Server Members Intent**: To see and manage server members
- **Message Content Intent**: To read and respond to commands
- **Presence Intent**: For future features (optional but recommended)

#### Generating Invite Link

1. Go to "OAuth2" → "URL Generator" in the left sidebar
2. Under "Scopes", select:
   - ✅ `bot`
   - ✅ `applications.commands`
3. Under "Bot Permissions", select:
   - ✅ **Administrator** (easiest option)
   
   OR if you prefer minimal permissions:
   - ✅ Manage Roles
   - ✅ Manage Channels
   - ✅ View Channels
   - ✅ Send Messages
   - ✅ Manage Messages
   - ✅ Read Message History
   - ✅ Add Reactions

4. Copy the "Generated URL" at the bottom
5. Open this URL in your browser
6. Select your server from the dropdown
7. Click "Authorize"
8. Complete the CAPTCHA

### Step 2: Environment Configuration

Create your `.env` file:

```bash
cp .env.example .env
```

Edit `.env` with your favorite text editor:

```env
# Required: Your bot token from Discord Developer Portal
DISCORD_BOT_TOKEN=your_bot_token_here

# Optional: Restrict bot to specific server (recommended for security)
GUILD_ID=your_server_id_here
```

**Security Notes:**
- Never commit `.env` to git (it's in `.gitignore`)
- Never share your bot token
- If token is compromised, reset it in Discord Developer Portal
- Use `GUILD_ID` to restrict the bot to your specific server

### Step 3: Installation

#### Option 1: Quick Start Script (Easiest)

```bash
# Make the script executable
chmod +x run.sh

# Run it
./run.sh
```

This script will:
- Check for `.env` file
- Create a virtual environment
- Install dependencies
- Start the bot

#### Option 2: Docker (Recommended for Production)

```bash
# Build and run with docker-compose
docker-compose up --build

# Or run in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the bot
docker-compose down
```

**Docker Benefits:**
- Isolated environment
- No Python version conflicts
- Easy to deploy anywhere
- Consistent behavior across systems

#### Option 3: Manual Python Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate  # Windows

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run the bot
python setup_bot.py
```

### Step 4: Running the Setup

1. **Start the bot** using one of the methods above
2. **Verify bot is online** - you should see it in your server's member list
3. **Check the console** for "Bot is ready!" message
4. **Run the setup command** in any channel:
   ```
   !setup
   ```
5. **Wait for completion** (2-5 minutes depending on Discord API rate limits)
6. **Review the results** - check that all channels and roles were created
7. **Shut down the bot**:
   ```
   !shutdown
   ```

### Step 5: Post-Setup Configuration

After the bot completes setup:

1. **Assign Moderator Roles**
   - Right-click trusted members → Roles → ⚔️ Moderator

2. **Customize Channel Topics**
   - Edit any channel descriptions to fit your community

3. **Set Up Additional Bots** (Optional)
   - MEE6 for auto-moderation and leveling
   - Dyno for advanced moderation
   - Carl-bot for reaction roles

4. **Configure Reaction Roles** (Optional)
   - Use a bot like Carl-bot or YAGPDB
   - Set up in #roles channel for easy role assignment

5. **Invite Your Friends!**
   - Share your server invite link
   - Post in #welcome and #introductions

---

## ⚙️ Configuration

### Using Templates

The bot includes three pre-built templates:

#### 1. AI Development (`ai-dev`)
- AI/ML research and development
- Learning resources and study groups
- Tool-specific channels (OpenAI, Claude, local models)
- Creative AI and prompt engineering
- Community events and collaboration

#### 2. AWS ChatOps (`aws-chatops`)
- Critical alerts and incident response
- AWS service-specific channels (EC2, Lambda, RDS, S3)
- Operations and monitoring
- Cost management and optimization
- Automation and runbooks
- SRE team structure

#### 3. ITIL Operations (`itil-ops`)
- ITIL-compliant service management
- Incident, problem, and change management
- Service desk and user support
- Release and configuration management
- SLA monitoring and compliance
- Business continuity and DR

### Creating Custom Templates

Edit `templates.py` to add your own templates. Each template requires:

```python
"my-template": {
    "name": "Display Name",
    "description": "Short description",
    "config": {"categories": [...]},
    "roles": [...],
    "rules": "Rules content",
    "welcome": "Welcome message",
    "resources": "Resources content",
}
```

### Customizing Existing Templates

Edit `server_config.py` (for ai-dev) or `templates.py` (for others) to customize:

#### Adding a New Channel

```python
{
    "name": "my-new-channel",
    "type": "text",  # or "voice"
    "topic": "Description of the channel",
}
```

#### Adding a New Category

```python
{
    "name": "🆕 MY CATEGORY",
    "position": 10,  # Higher number = lower in the list
    "channels": [
        # ... your channels here
    ],
}
```

#### Adding a New Role

```python
{
    "name": "🌟 My Role",
    "color": 0xFF5733,  # Hex color code
    "permissions": ["send_messages", "read_messages"],
    "hoist": True,  # Display separately in member list
    "mentionable": True,  # Can be @mentioned
}
```

**Available Permissions:**
- `administrator`
- `manage_channels`
- `manage_roles`
- `manage_messages`
- `kick_members`
- `ban_members`
- `send_messages`
- `read_messages`
- And many more - see [Discord.py Permissions](https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions)

### Customizing Messages

Edit these variables in `server_config.py`:

- `RULES_CONTENT` - Server rules
- `WELCOME_CONTENT` - Welcome message
- `RESOURCES_CONTENT` - Learning resources

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `DISCORD_BOT_TOKEN` | ✅ Yes | Your Discord bot token |
| `GUILD_ID` | ❌ No | Restrict bot to specific server (recommended) |

---

## 🎮 Commands

All commands require **Administrator** permissions.

### `!templates`
**Description:** List all available server templates

**Usage:**
```
!templates
```

**Output:**
- Template IDs and names
- Brief descriptions
- Usage examples

---

### `!setup [template]`
**Description:** Run the complete server setup process with a template

**Usage:**
```
!setup              # Uses default (ai-dev)
!setup ai-dev       # AI Development Community
!setup aws-chatops  # AWS ChatOps
!setup itil-ops     # ITIL Operations
```

**What it does:**
1. Creates all roles from template
2. Creates all categories and channels
3. Configures permissions
4. Posts welcome messages, rules, and resources

**Duration:** 2-5 minutes

**Note:** Safe to run multiple times - will skip existing channels/roles

---

### `!status`
**Description:** Check current server configuration status

**Usage:**
```
!status
```

**Output:**
- Number of categories
- Number of text channels
- Number of voice channels
- Number of roles
- Member count
- Setup status

---

### `!shutdown`
**Description:** Gracefully shut down the bot

**Usage:**
```
!shutdown
```

**Note:** Use this after setup is complete. The bot is no longer needed.

---

### `!cleanup`
**Description:** **DANGER!** Remove all channels and roles created by the bot

**Usage:**
```
!cleanup
```

Then confirm with:
```
!confirm_cleanup
```

**Warning:** This will delete EVERYTHING. Use only if you want to start over.

---

### `!help`
**Description:** Show all available commands

**Usage:**
```
!help
```

---

## 🔧 Troubleshooting

### Bot Won't Start

**Error: `DISCORD_BOT_TOKEN not found`**
- **Solution:** Create `.env` file with your bot token
  ```bash
  cp .env.example .env
  nano .env  # Add your token
  ```

**Error: `Failed to login - invalid bot token`**
- **Solution:** Check your token in `.env` is correct
- Reset token in Discord Developer Portal if needed

**Error: `ModuleNotFoundError: No module named 'discord'`**
- **Solution:** Install dependencies
  ```bash
  pip install -r requirements.txt
  ```

### Bot is Online But Not Responding

**Commands don't work**
- Check bot has "Message Content Intent" enabled in Developer Portal
- Verify bot has permissions in the channel
- Check bot role is high enough in role hierarchy

**`!setup` says "Missing Permissions"**
- Bot needs Administrator permission OR
- Bot needs: Manage Roles, Manage Channels, Send Messages
- Bot's role must be ABOVE the roles it's trying to create

### Setup Fails Partway Through

**"Rate limited" or "Too many requests"**
- Normal! Discord has rate limits
- The bot has built-in delays, just wait
- If it crashes, run `!setup` again - it will skip existing items

**Some channels/roles not created**
- Check bot permissions
- Check Discord server boost level (affects limits)
- Check logs: `cat setup_bot.log`

**Channels created in wrong order**
- Discord doesn't guarantee order during bulk creation
- Manually drag channels to reorder after setup

### Permission Issues

**"Missing Access" or "Forbidden"**
- Bot role must be high in role hierarchy
- Bot needs Administrator OR specific permissions
- Re-invite bot with correct permissions

**Can't create roles**
- Bot's role must be ABOVE roles it's creating
- Move bot role to top of role list (below your role)

### Docker Issues

**"Cannot connect to Docker daemon"**
- Start Docker: `sudo systemctl start docker`
- Add user to docker group: `sudo usermod -aG docker $USER`

**"Port already in use"**
- Bot doesn't use ports, this shouldn't happen
- Check for other containers: `docker ps`

### Logs and Debugging

**Enable debug logging:**

Edit `setup_bot.py`:
```python
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    # ...
)
```

**View logs:**
```bash
# Console output
python setup_bot.py

# Log file
cat setup_bot.log
tail -f setup_bot.log  # Follow in real-time
```

**Common log messages:**

- `"Bot logged in as..."` - ✅ Bot started successfully
- `"Setup initiated by..."` - ✅ Setup command received
- `"Created role: ..."` - ✅ Role created successfully
- `"Role '...' already exists, skipping"` - ℹ️ Normal, not an error
- `"Failed to create..."` - ❌ Permission or rate limit issue
- `"Insufficient permissions"` - ❌ Bot needs more permissions

---

## 🎨 Customization

### Changing Channel Names

Edit `server_config.py`:

```python
{
    "name": "your-channel-name",  # Change this
    "type": "text",
    "topic": "Your channel description",
}
```

**Naming conventions:**
- Use lowercase
- Use hyphens instead of spaces
- Keep it short and descriptive
- Emojis in category names only (not channel names)

### Changing Colors

Role colors use hex codes:

```python
{
    "name": "🎨 My Role",
    "color": 0xFF5733,  # Orange
}
```

**Popular colors:**
- Red: `0xE74C3C`
- Blue: `0x3498DB`
- Green: `0x2ECC71`
- Purple: `0x9B59B6`
- Orange: `0xE67E22`
- Yellow: `0xF1C40F`
- Teal: `0x1ABC9C`
- Pink: `0xE91E63`

[Color picker tool](https://www.color-hex.com/)

### Adding Custom Welcome Messages

Edit `WELCOME_CONTENT` in `server_config.py`:

```python
WELCOME_CONTENT = """
# 👋 Welcome to My Awesome Server!

Your custom welcome message here...
"""
```

**Tips:**
- Use Markdown formatting
- Include channel mentions: `<#channel-name>`
- Keep it concise but informative
- Add emojis for visual appeal

### Modifying Permissions

Example: Make a channel read-only for specific role:

```python
# In setup_bot.py, add to configure_permissions():
if "my-channel" in self.created_channels:
    channel = self.created_channels["my-channel"]
    role = discord.utils.get(self.guild.roles, name="My Role")
    await channel.set_permissions(
        role,
        send_messages=False,
        read_messages=True,
    )
```

### Creating Custom Commands

Add to `setup_bot.py`:

```python
@bot.command(name="mycommand")
@commands.has_permissions(administrator=True)
async def my_command(ctx):
    """Description of my command"""
    await ctx.send("Hello from my custom command!")
```

---

## 🏗️ Architecture

### Project Structure

```
discord-ai-server-bot/
├── setup_bot.py          # Main bot application
├── server_config.py      # Server structure configuration
├── requirements.txt      # Python dependencies
├── .env.example          # Environment template
├── .env                  # Your secrets (gitignored)
├── .gitignore           # Git ignore rules
├── Dockerfile           # Docker container definition
├── docker-compose.yml   # Docker orchestration
├── run.sh               # Quick start script
├── README.md            # This file
└── setup_bot.log        # Runtime logs (created on first run)
```

### Component Overview

#### `setup_bot.py`
Main bot application with:
- Discord.py bot initialization
- Command handlers (!setup, !status, etc.)
- ServerSetup class for configuration logic
- Error handling and logging

#### `server_config.py`
Configuration data:
- `SERVER_CONFIG`: Categories and channels
- `ROLES_CONFIG`: Role definitions
- `RULES_CONTENT`: Server rules text
- `WELCOME_CONTENT`: Welcome message
- `RESOURCES_CONTENT`: Learning resources

#### Environment Files
- `.env.example`: Template with placeholders
- `.env`: Your actual secrets (never commit!)

### Data Flow

```
1. Bot starts → Loads .env → Connects to Discord
2. User runs !setup → Validates permissions
3. ServerSetup.setup_roles() → Creates roles
4. ServerSetup.setup_channels() → Creates categories & channels
5. ServerSetup.configure_permissions() → Sets special permissions
6. ServerSetup.post_initial_messages() → Posts welcome/rules/resources
7. Completion message → User runs !shutdown
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| discord.py | 2.3.2 | Discord API wrapper |
| python-dotenv | 1.0.0 | Environment variable management |
| aiohttp | 3.9.1 | Async HTTP (discord.py dependency) |

### Rate Limiting

Discord API rate limits:
- **Channels:** 50 per 10 seconds
- **Roles:** 250 per 10 seconds
- **Messages:** 5 per 5 seconds per channel

The bot includes `asyncio.sleep()` delays to respect these limits.

### Logging

**Log Levels:**
- `INFO`: Normal operations (channel created, setup complete)
- `ERROR`: Failures (permission denied, API errors)
- `DEBUG`: Detailed debugging (enable manually)

**Log Destinations:**
- Console (stdout)
- `setup_bot.log` file

---

## 🔒 Security

### Best Practices

1. **Never Share Your Bot Token**
   - Treat it like a password
   - Don't commit to git
   - Don't share in Discord
   - Reset immediately if compromised

2. **Use GUILD_ID Restriction**
   ```env
   GUILD_ID=your_server_id
   ```
   This prevents the bot from working on other servers if token leaks

3. **Minimal Permissions**
   - Only grant Administrator if you trust the code
   - Review `server_config.py` before running
   - Use specific permissions if preferred

4. **Environment Security**
   - `.env` is in `.gitignore`
   - Never commit secrets
   - Use different tokens for dev/prod

5. **Code Review**
   - This is open source - review before running
   - Check for malicious code
   - Understand what it does

### What This Bot Can Do

With Administrator permission, the bot can:
- ✅ Create/delete channels and categories
- ✅ Create/delete roles
- ✅ Send messages
- ✅ Manage permissions
- ❌ Cannot DM users without their interaction
- ❌ Cannot access message content in other servers
- ❌ Cannot perform actions outside configured server (if GUILD_ID set)

### What This Bot CANNOT Do

- Access your Discord password
- Read DMs
- Access other servers (if GUILD_ID is set)
- Persist data outside logs
- Make external network requests (except Discord API)

### Resetting Compromised Token

1. Go to Discord Developer Portal
2. Select your application
3. Go to "Bot" section
4. Click "Reset Token"
5. Update `.env` with new token
6. Restart the bot

---

## ❓ FAQ

### General Questions

**Q: Do I need to keep the bot running after setup?**
A: No! This is a one-time setup bot. Run it, configure your server, then shut it down.

**Q: Can I run the setup multiple times?**
A: Yes! The bot will skip existing channels and roles. Safe to re-run.

**Q: Will this delete my existing channels?**
A: No. It only creates new channels. Use `!cleanup` to remove (with confirmation).

**Q: Can I customize the channels before running?**
A: Yes! Edit `server_config.py` (for ai-dev) or `templates.py` (for other templates) before running the bot.

**Q: Can I switch templates after setup?**
A: Yes, but you'll need to run `!cleanup` first to remove existing structure, then run `!setup <new-template>`.

**Q: How long does setup take?**
A: 2-5 minutes depending on Discord API rate limits.

### Technical Questions

**Q: What Python version do I need?**
A: Python 3.8 or higher. Tested on 3.11.

**Q: Can I run this on Windows?**
A: Yes! Use `venv\Scripts\activate` instead of `source venv/bin/activate`.

**Q: Do I need Docker?**
A: No, Docker is optional. You can run with Python directly.

**Q: Can I use this for multiple servers?**
A: Yes, but remove `GUILD_ID` from `.env` or run separate instances.

**Q: How do I update the bot?**
A: Pull latest code, update dependencies: `pip install -r requirements.txt --upgrade`

### Discord Questions

**Q: What's a bot token?**
A: A secret key that authenticates your bot with Discord. Get it from Developer Portal.

**Q: What are Privileged Intents?**
A: Special permissions bots need to access certain data. Enable in Developer Portal.

**Q: Why does my bot show as offline?**
A: Check token is correct, intents are enabled, and bot is running.

**Q: Can I change the bot's name/avatar?**
A: Yes, in Discord Developer Portal under "General Information".

**Q: How do I get my Server ID?**
A: Enable Developer Mode → Right-click server icon → Copy ID.

### Troubleshooting Questions

**Q: Setup failed halfway, what now?**
A: Run `!setup` again. It will skip existing items and continue.

**Q: Bot says "Missing Permissions"?**
A: Bot needs Administrator OR Manage Roles + Manage Channels. Check role hierarchy.

**Q: Some channels weren't created?**
A: Check logs (`setup_bot.log`). Likely rate limit or permission issue.

**Q: How do I see error messages?**
A: Check console output or `setup_bot.log` file.

**Q: Can I undo the setup?**
A: Yes, use `!cleanup` command (requires confirmation).

### Customization Questions

**Q: Can I add more channels?**
A: Yes! Edit `server_config.py` and run `!setup` again.

**Q: Can I change channel names?**
A: Yes, edit `server_config.py` before running, or manually after.

**Q: Can I change role colors?**
A: Yes, edit `ROLES_CONFIG` in `server_config.py`.

**Q: Can I modify the welcome message?**
A: Yes, edit `WELCOME_CONTENT` in `server_config.py`.

**Q: Can I add custom commands?**
A: Yes, but you'll need to keep the bot running. Add to `setup_bot.py`.

---

## 📊 Metrics & Monitoring

### Setup Metrics

The bot logs:
- Number of roles created
- Number of categories created
- Number of channels created
- Errors and failures
- Execution time

### Health Checks

**Check bot status:**
```
!status
```

**Check logs:**
```bash
tail -f setup_bot.log
```

### Performance

**Typical setup time:**
- Small server (20 channels): ~1-2 minutes
- Medium server (40 channels): ~2-4 minutes
- Large server (60+ channels): ~4-6 minutes

**Rate limits:**
- Discord enforces rate limits
- Bot includes delays to prevent hitting limits
- If rate limited, bot will retry automatically

---

## 🚀 Deployment Options

### Local Development

```bash
python setup_bot.py
```

**Pros:**
- Easy to debug
- Fast iteration
- No container overhead

**Cons:**
- Requires Python installed
- Environment-specific issues

### Docker

```bash
docker-compose up --build
```

**Pros:**
- Isolated environment
- Reproducible
- No Python version issues

**Cons:**
- Requires Docker installed
- Slightly slower startup

### Cloud Deployment

**Not recommended** for this bot since it's one-time use, but possible:

- **AWS EC2**: Run on a small instance
- **Google Cloud Run**: Deploy as container
- **Heroku**: Use hobby dyno
- **DigitalOcean**: Droplet or App Platform

**Note:** For one-time setup, local execution is most cost-effective.

---

## 🧪 Testing

### Manual Testing

1. Create a test Discord server
2. Run the bot with test configuration
3. Verify all channels created
4. Check permissions
5. Test cleanup command

### Verification Checklist

After running `!setup`:

- [ ] All categories created
- [ ] All channels created in correct categories
- [ ] All roles created with correct colors
- [ ] Welcome message posted in #welcome
- [ ] Rules posted in #rules
- [ ] Resources posted in #resources
- [ ] Announcements channel is read-only
- [ ] Voice channels are accessible
- [ ] No errors in logs

---

## 📝 Logging

### Log Levels

```python
# In setup_bot.py
logging.basicConfig(level=logging.INFO)  # Change to DEBUG for more detail
```

**Levels:**
- `DEBUG`: Detailed debugging information
- `INFO`: General informational messages
- `WARNING`: Warning messages
- `ERROR`: Error messages
- `CRITICAL`: Critical errors

### Log Format

```
2025-01-22 12:00:00 - setup_bot - INFO - Bot logged in as AI Setup Bot
2025-01-22 12:00:05 - setup_bot - INFO - Setup initiated by User#1234
2025-01-22 12:00:10 - setup_bot - INFO - Created role: 🛡️ Admin
```

### Log Locations

- **Console**: Real-time output
- **File**: `setup_bot.log` (persists across runs)

### Viewing Logs

```bash
# View entire log
cat setup_bot.log

# Follow log in real-time
tail -f setup_bot.log

# Search logs
grep "ERROR" setup_bot.log

# Last 50 lines
tail -n 50 setup_bot.log
```

---

## 🔄 Updates & Maintenance

### Updating Dependencies

```bash
# Update all dependencies
pip install -r requirements.txt --upgrade

# Update specific package
pip install discord.py --upgrade
```

### Updating Configuration

1. Edit `server_config.py`
2. Run `!setup` again
3. Bot will skip existing items and create new ones

### Version Control

```bash
# Check current version
git log -1

# Pull latest changes
git pull origin main

# View changes
git diff
```

---

## 🤝 Contributing

This is a personal project, but contributions are welcome!

### How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Code Style

- Follow PEP 8
- Use type hints
- Add docstrings
- Include error handling
- Add logging statements

---

## 📄 License

This project is provided as-is for personal use. Feel free to modify and distribute.

---

## 🙏 Acknowledgments

- Built with [discord.py](https://github.com/Rapptz/discord.py)
- Inspired by the AI development community
- Thanks to Discord for their excellent API

---

## 📞 Support

**Issues?**
- Check [Troubleshooting](#troubleshooting) section
- Review logs: `setup_bot.log`
- Check Discord Developer Portal for bot status

**Questions?**
- Read the [FAQ](#faq)
- Check Discord.py documentation
- Review the code - it's well-commented!

---

## 🎉 You're All Set!

Your Discord AI server is ready to go. Enjoy building your community!

**Next Steps:**
1. ✅ Invite your friends
2. ✅ Customize channels as needed
3. ✅ Add moderation bots (MEE6, Dyno)
4. ✅ Set up reaction roles
5. ✅ Start discussions!

**Happy building! 🚀**
