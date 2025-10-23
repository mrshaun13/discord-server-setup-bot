"""
Discord AI Server Setup Bot
A one-time setup bot to automatically configure your Discord server
"""

import os
import asyncio
import logging
from typing import Optional
import discord
from discord.ext import commands
from dotenv import load_dotenv
from server_config import (
    SERVER_CONFIG,
    ROLES_CONFIG,
    RULES_CONTENT,
    WELCOME_CONTENT,
    RESOURCES_CONTENT,
)
from templates import get_template, list_templates

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('setup_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Bot configuration
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

if not DISCORD_BOT_TOKEN:
    raise ValueError("DISCORD_BOT_TOKEN not found in .env file")

# Bot setup with required intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Bot marker for tracking created content
BOT_MARKER = "[DSBOT]"  # Discord Server Bot marker


class ServerSetup:
    """Handles the server setup process"""
    
    def __init__(self, guild: discord.Guild, template_config=None):
        self.guild = guild
        self.created_categories = {}
        self.created_channels = {}
        self.created_roles = {}
        
        # Use template config if provided, otherwise use defaults
        if template_config:
            self.server_config = template_config["config"]
            self.roles_config = template_config["roles"]
            self.rules_content = template_config["rules"]
            self.welcome_content = template_config["welcome"]
            self.resources_content = template_config["resources"]
        else:
            self.server_config = SERVER_CONFIG
            self.roles_config = ROLES_CONFIG
            self.rules_content = RULES_CONTENT
            self.welcome_content = WELCOME_CONTENT
            self.resources_content = RESOURCES_CONTENT
        
    async def setup_roles(self) -> dict:
        """Create all roles defined in configuration"""
        logger.info("Creating roles...")
        
        for role_config in self.roles_config:
            try:
                # Check if role already exists
                existing_role = discord.utils.get(self.guild.roles, name=role_config["name"])
                if existing_role:
                    logger.info(f"Role '{role_config['name']}' already exists, skipping")
                    self.created_roles[role_config["name"]] = existing_role
                    continue
                
                # Create permissions object
                permissions = discord.Permissions()
                for perm in role_config.get("permissions", []):
                    setattr(permissions, perm, True)
                
                # Create the role with bot marker in name temporarily, then rename
                role = await self.guild.create_role(
                    name=f"{role_config['name']} {BOT_MARKER}",
                    color=discord.Color(role_config.get("color", 0)),
                    hoist=role_config.get("hoist", False),
                    mentionable=role_config.get("mentionable", True),
                    permissions=permissions
                )
                self.created_roles[role_config["name"]] = role
                logger.info(f"Created role: {role_config['name']}")
                
                # Rate limit protection
                await asyncio.sleep(0.5)
                
            except discord.HTTPException as e:
                logger.error(f"Failed to create role '{role_config['name']}': {e}")
            except Exception as e:
                logger.error(f"Unexpected error creating role '{role_config['name']}': {e}")
        
        return self.created_roles
    
    async def setup_channels(self) -> dict:
        """Create all categories and channels defined in configuration"""
        logger.info("Creating categories and channels...")
        
        for category_config in self.server_config["categories"]:
            try:
                # Check if category already exists
                existing_category = discord.utils.get(
                    self.guild.categories, 
                    name=category_config["name"]
                )
                
                if existing_category:
                    logger.info(f"Category '{category_config['name']}' already exists, skipping")
                    category = existing_category
                else:
                    # Create category
                    category = await self.guild.create_category(
                        name=category_config["name"],
                        position=category_config.get("position", 0),
                    )
                    logger.info(f"Created category: {category_config['name']}")
                    await asyncio.sleep(0.5)
                
                self.created_categories[category_config["name"]] = category
                
                # Create channels in this category
                for channel_config in category_config["channels"]:
                    try:
                        # Check if channel already exists
                        existing_channel = discord.utils.get(
                            self.guild.channels,
                            name=channel_config["name"],
                            category=category
                        )
                        
                        if existing_channel:
                            logger.info(f"Channel '{channel_config['name']}' already exists, skipping")
                            self.created_channels[channel_config["name"]] = existing_channel
                            continue
                        
                        # Create text or voice channel
                        if channel_config["type"] == "voice":
                            channel = await category.create_voice_channel(
                                name=channel_config["name"],
                                topic=f"{BOT_MARKER} {channel_config.get('topic', 'Created by setup bot')}"
                            )
                        else:
                            original_topic = channel_config.get("topic", "")
                            channel = await category.create_text_channel(
                                name=channel_config["name"],
                                topic=f"{BOT_MARKER} {original_topic}" if original_topic else BOT_MARKER,
                            )
                        
                        self.created_channels[channel_config["name"]] = channel
                        logger.info(f"Created channel: {channel_config['name']}")
                        
                        # Rate limit protection
                        await asyncio.sleep(0.5)
                        
                    except discord.HTTPException as e:
                        logger.error(f"Failed to create channel '{channel_config['name']}': {e}")
                    except Exception as e:
                        logger.error(f"Unexpected error creating channel '{channel_config['name']}': {e}")
                
            except discord.HTTPException as e:
                logger.error(f"Failed to create category '{category_config['name']}': {e}")
            except Exception as e:
                logger.error(f"Unexpected error creating category '{category_config['name']}': {e}")
        
        return self.created_channels
    
    async def post_initial_messages(self):
        """Post welcome messages, rules, and resources"""
        logger.info("Posting initial messages...")
        
        # Post rules
        if "rules" in self.created_channels:
            rules_channel = self.created_channels["rules"]
            try:
                await rules_channel.send(self.rules_content)
                logger.info("Posted rules message")
                await asyncio.sleep(1)
            except Exception as e:
                logger.error(f"Failed to post rules: {e}")
        
        # Post welcome message
        if "welcome" in self.created_channels:
            welcome_channel = self.created_channels["welcome"]
            try:
                # Replace channel mentions with actual mentions
                welcome_msg = self.welcome_content
                if "rules" in self.created_channels:
                    welcome_msg = welcome_msg.replace("<#rules>", self.created_channels["rules"].mention)
                if "introductions" in self.created_channels:
                    welcome_msg = welcome_msg.replace("<#introductions>", self.created_channels["introductions"].mention)
                if "roles" in self.created_channels:
                    welcome_msg = welcome_msg.replace("<#roles>", self.created_channels["roles"].mention)
                if "resources" in self.created_channels:
                    welcome_msg = welcome_msg.replace("<#resources>", self.created_channels["resources"].mention)
                if "showcase" in self.created_channels:
                    welcome_msg = welcome_msg.replace("<#showcase>", self.created_channels["showcase"].mention)
                if "general" in self.created_channels:
                    welcome_msg = welcome_msg.replace("<#general>", self.created_channels["general"].mention)
                if "feedback-suggestions" in self.created_channels:
                    welcome_msg = welcome_msg.replace("<#feedback-suggestions>", self.created_channels["feedback-suggestions"].mention)
                if "beginner-questions" in self.created_channels:
                    welcome_msg = welcome_msg.replace("<#beginner-questions>", self.created_channels["beginner-questions"].mention)
                
                await welcome_channel.send(welcome_msg)
                logger.info("Posted welcome message")
                await asyncio.sleep(1)
            except Exception as e:
                logger.error(f"Failed to post welcome message: {e}")
        
        # Post resources
        if "resources" in self.created_channels:
            resources_channel = self.created_channels["resources"]
            try:
                # Replace channel mentions
                resources_msg = self.resources_content
                if "feedback-suggestions" in self.created_channels:
                    resources_msg = resources_msg.replace("<#feedback-suggestions>", self.created_channels["feedback-suggestions"].mention)
                
                await resources_channel.send(resources_msg)
                logger.info("Posted resources message")
                await asyncio.sleep(1)
            except Exception as e:
                logger.error(f"Failed to post resources: {e}")
        
        # Post role selection message
        if "roles" in self.created_channels:
            roles_channel = self.created_channels["roles"]
            try:
                role_msg = "# 🎭 Role Selection\n\n"
                role_msg += "React to this message or use the buttons below to assign yourself roles!\n\n"
                role_msg += "## Expertise Roles\n"
                role_msg += "• 🧠 ML Researcher - Academic/research background\n"
                role_msg += "• 💻 ML Engineer - Production ML systems\n"
                role_msg += "• 🎨 Creative AI - Generative AI focus\n"
                role_msg += "• 🤖 Agent Builder - AI agents and automation\n"
                role_msg += "• 📊 Data Scientist - Data analysis and modeling\n"
                role_msg += "• 🔰 Learning - Still learning AI/ML\n\n"
                role_msg += "## Interest Roles\n"
                role_msg += "• 📰 News Ping - Get pinged for major AI news\n"
                role_msg += "• 📄 Paper Club - Participate in paper discussions\n"
                role_msg += "• 🎯 Hackathon - Interested in hackathons\n"
                role_msg += "• 💼 Job Alerts - See job postings\n\n"
                role_msg += "*Note: You can assign roles manually by right-clicking your name or asking an admin to set up reaction roles.*"
                
                await roles_channel.send(role_msg)
                logger.info("Posted roles message")
                await asyncio.sleep(1)
            except Exception as e:
                logger.error(f"Failed to post roles message: {e}")
    
    async def configure_permissions(self):
        """Configure special permissions for certain channels"""
        logger.info("Configuring channel permissions...")
        
        # Make announcements read-only for @everyone
        if "announcements" in self.created_channels:
            announcements = self.created_channels["announcements"]
            try:
                await announcements.set_permissions(
                    self.guild.default_role,
                    send_messages=False,
                    add_reactions=True,
                )
                logger.info("Set announcements to read-only")
            except Exception as e:
                logger.error(f"Failed to set announcements permissions: {e}")


@bot.event
async def on_ready():
    """Called when the bot is ready"""
    logger.info(f"Bot logged in as {bot.user.name} (ID: {bot.user.id})")
    logger.info(f"Connected to {len(bot.guilds)} guild(s)")
    
    for guild in bot.guilds:
        logger.info(f"  - {guild.name} (ID: {guild.id})")
    
    logger.info("\nBot is ready! Use !setup in your server to configure it.")
    logger.info("Use !status to check setup progress")
    logger.info("Use !help to see all commands\n")


@bot.command(name="setup")
@commands.has_permissions(administrator=True)
async def setup_server(ctx, template: str = "ai-dev", scale: int = 100):
    """
    Set up the entire server structure
    Usage: !setup [template] [scale]
    Templates: ai-dev, aws-chatops, itil-ops, school, small-business, gaming-hangout, etc.
    Scale: 1-100 (1=minimal, 100=full enterprise)
    Requires: Administrator permissions
    """
    # Check if command is used in a server (not DM)
    if ctx.guild is None:
        await ctx.send("❌ This command can only be used in a server, not in DMs.")
        return
    
    if GUILD_ID and str(ctx.guild.id) != GUILD_ID:
        await ctx.send("❌ This bot is configured for a specific server only.")
        return
    
    # Validate scale
    if scale < 1:
        scale = 1
    elif scale > 100:
        scale = 100
    
    # Get template with scaling
    template_config = get_template(template, scale)
    if not template_config:
        available = ", ".join(list_templates().keys())
        await ctx.send(f"❌ Unknown template: `{template}`\n"
                      f"Available templates: `{available}`\n"
                      f"Use `!templates` to see details.")
        return
    
    from template_scaler import get_scale_description
    scale_desc = get_scale_description(scale)
    
    await ctx.send(f"🚀 **Starting server setup with template: {template_config['name']}**\n"
                   f"_{template_config['description']}_\n"
                   f"**Scale:** {scale}% - {scale_desc}\n\n"
                   "This will create categories, channels, roles, and post initial messages.\n"
                   "This may take a few minutes. Please wait...")
    
    logger.info(f"Setup initiated by {ctx.author} in {ctx.guild.name} with template: {template}")
    
    try:
        setup = ServerSetup(ctx.guild, template_config)
        
        # Step 1: Create roles
        await ctx.send("📝 Creating roles...")
        roles = await setup.setup_roles()
        await ctx.send(f"✅ Created {len(roles)} roles")
        
        # Step 2: Create channels
        await ctx.send("📁 Creating categories and channels...")
        channels = await setup.setup_channels()
        await ctx.send(f"✅ Created {len(setup.created_categories)} categories and {len(channels)} channels")
        
        # Step 3: Configure permissions
        await ctx.send("🔒 Configuring permissions...")
        await setup.configure_permissions()
        await ctx.send("✅ Permissions configured")
        
        # Step 4: Post initial messages
        await ctx.send("📨 Posting welcome messages and resources...")
        await setup.post_initial_messages()
        await ctx.send("✅ Initial messages posted")
        
        # Final message
        await ctx.send(
            f"🎉 **Server setup complete!**\n\n"
            f"Your {template_config['name']} server is now configured with:\n"
            f"• {len(setup.created_categories)} categories\n"
            f"• {len(channels)} channels\n"
            f"• {len(roles)} roles\n\n"
            "**Next steps:**\n"
            "1. Review the channels and customize as needed\n"
            "2. Assign roles to team members\n"
            "3. Configure any additional integrations\n"
            "4. Start using your new server!\n\n"
            "**You can now shut down this bot** - it's only needed for initial setup.\n"
            "Use `!shutdown` when you're done."
        )
        
        logger.info("Setup completed successfully!")
        
    except discord.Forbidden:
        await ctx.send("❌ **Error:** Bot doesn't have sufficient permissions. "
                      "Make sure the bot role is high enough and has Administrator permissions.")
        logger.error("Insufficient permissions to complete setup")
    except Exception as e:
        await ctx.send(f"❌ **Error during setup:** {str(e)}\n"
                      "Check the logs for more details.")
        logger.error(f"Setup failed with error: {e}", exc_info=True)


@bot.command(name="templates")
async def list_available_templates(ctx):
    """List all available server templates"""
    templates = list_templates()
    
    msg = "📋 **Available Server Templates**\n\n"
    msg += "Use `!setup <template> [scale]` to set up your server.\n"
    msg += "Use `!preview <template> [scale]` to see what will be created.\n\n"
    
    for template_id, info in templates.items():
        msg += f"**`{template_id}`** - {info['name']}\n"
        msg += f"_{info['description']}_\n\n"
    
    msg += "**Examples:**\n"
    msg += "`!preview aws-chatops 50` - Preview 50% scale\n"
    msg += "`!setup aws-chatops 50` - Setup with 50% scale"
    
    await ctx.send(msg)


@bot.command(name="preview")
async def preview_template(ctx, template: str = "ai-dev", scale: int = 100):
    """
    Preview what a template will create (dry-run)
    Usage: !preview <template> [scale]
    Shows structure without making changes
    """
    if ctx.guild is None:
        await ctx.send("❌ This command can only be used in a server, not in DMs.")
        return
    
    # Validate scale
    scale = max(1, min(100, scale))
    
    # Get template
    template_config = get_template(template, scale)
    if not template_config:
        available = ", ".join(list_templates().keys())
        await ctx.send(f"❌ Unknown template: `{template}`\n"
                      f"Available: `{available}`")
        return
    
    from template_utils import get_template_summary, format_preview, calculate_diff, format_diff
    from template_scaler import get_scale_description
    
    # Check if this is a diff preview (server has existing content)
    has_content = len(ctx.guild.channels) > 1 or len(ctx.guild.roles) > 1
    
    if has_content:
        # Show diff - what will be added
        diff = calculate_diff(ctx.guild, template_config)
        scale_desc = get_scale_description(scale)
        
        msg = f"**Template:** {template_config['name']}\n"
        msg += f"**Scale:** {scale}% - {scale_desc}\n\n"
        msg += format_diff(diff)
        
        if diff['total_new_channels'] > 0 or diff['total_new_roles'] > 0:
            msg += f"\n\n✅ Run `!setup {template} {scale}` to apply these changes."
    else:
        # Show full preview - fresh server
        summary = get_template_summary(template_config)
        scale_desc = get_scale_description(scale)
        
        msg = format_preview(summary, show_details=True)
        msg += f"\n\n**Scale:** {scale}% - {scale_desc}"
        msg += f"\n\n✅ Run `!setup {template} {scale}` to create this structure."
    
    # Split message if too long
    if len(msg) > 2000:
        # Send summary first
        summary = get_template_summary(template_config)
        short_msg = format_preview(summary, show_details=False)
        short_msg += f"\n\n**Scale:** {scale}%"
        short_msg += f"\n\n_Full details too long for one message. Check logs or use smaller scale._"
        short_msg += f"\n\n✅ Run `!setup {template} {scale}` to apply."
        await ctx.send(short_msg)
    else:
        await ctx.send(msg)


@bot.command(name="add-channel")
@commands.has_permissions(administrator=True)
async def add_channel(ctx, channel_name: str = None):
    """
    Add a channel from the template that wasn't included in your scale
    Usage: !add-channel <channel-name>
    Lists available channels if no name provided
    """
    if ctx.guild is None:
        await ctx.send("❌ This command can only be used in a server, not in DMs.")
        return
    
    # Try to detect which template was used (store in channel topic or description)
    # For now, we'll ask the user to specify
    await ctx.send("⚠️ **Feature Coming Soon**\n\n"
                   "To add channels manually:\n"
                   "1. Use `!preview <template> 100` to see all available channels\n"
                   "2. Create channels manually in Discord\n"
                   "3. Or run `!setup <template> <higher-scale>` to add more channels\n\n"
                   "Example: If you used `!setup school 50`, run `!setup school 75` to add more.")


@bot.command(name="rescale")
@commands.has_permissions(administrator=True)
async def rescale_server(ctx, template: str, new_scale: int):
    """
    Change the scale of your server (add more channels/roles)
    Usage: !rescale <template> <new-scale>
    Shows preview of what will be added
    """
    if ctx.guild is None:
        await ctx.send("❌ This command can only be used in a server, not in DMs.")
        return
    
    # Validate scale
    new_scale = max(1, min(100, new_scale))
    
    # Get template
    template_config = get_template(template, new_scale)
    if not template_config:
        available = ", ".join(list_templates().keys())
        await ctx.send(f"❌ Unknown template: `{template}`\n"
                      f"Available: `{available}`")
        return
    
    from template_utils import calculate_diff, format_diff
    from template_scaler import get_scale_description
    
    # Calculate what will be added
    diff = calculate_diff(ctx.guild, template_config)
    scale_desc = get_scale_description(new_scale)
    
    if diff['total_new_channels'] == 0 and diff['total_new_roles'] == 0:
        await ctx.send(f"✅ Server already has all content from **{template}** at **{new_scale}%**\n\n"
                      f"Nothing to add!")
        return
    
    msg = f"# 🔄 Rescale Preview: {template} → {new_scale}%\n"
    msg += f"_{scale_desc}_\n\n"
    msg += format_diff(diff)
    msg += f"\n\n**To apply:** `!setup {template} {new_scale}`"
    
    # Split if too long
    if len(msg) > 2000:
        short_msg = f"# 🔄 Rescale: {template} → {new_scale}%\n\n"
        short_msg += f"**Will add:**\n"
        short_msg += f"• {diff['total_new_categories']} categories\n"
        short_msg += f"• {diff['total_new_channels']} channels\n"
        short_msg += f"• {diff['total_new_roles']} roles\n\n"
        short_msg += f"**To apply:** `!setup {template} {new_scale}`"
        await ctx.send(short_msg)
    else:
        await ctx.send(msg)


@bot.command(name="status")
async def check_status(ctx):
    """Check the current server setup status"""
    # Check if command is used in a server (not DM)
    if ctx.guild is None:
        await ctx.send("❌ This command can only be used in a server, not in DMs.")
        return
    
    guild = ctx.guild
    
    # Count existing elements
    categories = len(guild.categories)
    text_channels = len(guild.text_channels)
    voice_channels = len(guild.voice_channels)
    roles = len(guild.roles) - 1  # Exclude @everyone
    
    status_msg = f"📊 **Server Status for {guild.name}**\n\n"
    status_msg += f"📁 Categories: {categories}\n"
    status_msg += f"💬 Text Channels: {text_channels}\n"
    status_msg += f"🔊 Voice Channels: {voice_channels}\n"
    status_msg += f"🎭 Roles: {roles}\n"
    status_msg += f"👥 Members: {guild.member_count}\n\n"
    
    if categories == 0 and text_channels <= 1:
        status_msg += "⚠️ Server appears to be unconfigured. Run `!setup` to configure it."
    else:
        status_msg += "✅ Server has been configured!"
    
    await ctx.send(status_msg)


@bot.command(name="shutdown")
@commands.has_permissions(administrator=True)
async def shutdown_bot(ctx):
    """Shutdown the bot (admin only)"""
    await ctx.send("👋 Shutting down the setup bot. Thanks for using it!\n"
                   "Your server is all set. You can restart this bot anytime if you need to make changes.")
    logger.info(f"Bot shutdown initiated by {ctx.author}")
    await bot.close()


@bot.command(name="cleanup")
@commands.has_permissions(administrator=True)
async def cleanup_server(ctx, channel_name: str = None):
    """
    Remove channels and roles created by this bot
    Usage: !cleanup [channel-name]
    
    Without channel name: Removes ALL bot-created content (requires confirmation)
    With channel name: Removes specific channel (no confirmation needed)
    
    Only deletes items marked with [DSBOT] - manually created channels are safe!
    """
    # Check if command is used in a server (not DM)
    if ctx.guild is None:
        await ctx.send("❌ This command can only be used in a server, not in DMs.")
        return
    
    # Single channel cleanup (no confirmation needed)
    if channel_name:
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)
        
        if not channel:
            await ctx.send(f"❌ Channel `{channel_name}` not found.")
            return
        
        # Check if it's a bot-created channel
        is_bot_channel = False
        if hasattr(channel, 'topic') and channel.topic and BOT_MARKER in channel.topic:
            is_bot_channel = True
        elif isinstance(channel, discord.CategoryChannel):
            # Check if category has bot-created channels
            bot_channels_in_cat = [ch for ch in channel.channels 
                                   if hasattr(ch, 'topic') and ch.topic and BOT_MARKER in ch.topic]
            is_bot_channel = len(bot_channels_in_cat) > 0
        
        if not is_bot_channel:
            await ctx.send(f"⚠️ Channel `{channel_name}` was not created by this bot.\n"
                          f"Use `!remove-channel {channel_name}` to force delete it.")
            return
        
        try:
            await channel.delete()
            await ctx.send(f"✅ Deleted channel: `{channel_name}`")
            logger.info(f"Channel {channel_name} deleted by {ctx.author}")
        except Exception as e:
            await ctx.send(f"❌ Failed to delete channel: {str(e)}")
            logger.error(f"Failed to delete channel {channel_name}: {e}")
        return
    
    # Full cleanup (requires confirmation)
    await ctx.send("⚠️ **WARNING:** This will delete ALL channels and roles created by the setup bot!\n"
                   "Manually created channels will NOT be affected.\n\n"
                   "Type `!confirm_cleanup` within 30 seconds to proceed.")
    
    def check(m):
        return m.author == ctx.author and m.content == "!confirm_cleanup" and m.channel == ctx.channel
    
    try:
        await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        await ctx.send("❌ Cleanup cancelled - confirmation not received.")
        return
    
    await ctx.send("🗑️ Starting cleanup... This may take a while.")
    logger.info(f"Full cleanup initiated by {ctx.author}")
    
    deleted_channels = 0
    deleted_categories = 0
    deleted_roles = 0
    skipped_channels = 0
    skipped_roles = 0
    
    # Delete bot-created channels only
    for channel in ctx.guild.channels:
        if channel == ctx.channel:  # Don't delete the channel we're in
            continue
        
        # Check if channel was created by bot
        is_bot_created = False
        if hasattr(channel, 'topic') and channel.topic and BOT_MARKER in channel.topic:
            is_bot_created = True
        elif isinstance(channel, discord.CategoryChannel):
            # Delete empty categories or those with only bot channels
            bot_channels = [ch for ch in channel.channels 
                           if hasattr(ch, 'topic') and ch.topic and BOT_MARKER in ch.topic]
            if len(bot_channels) == len(channel.channels) and len(channel.channels) > 0:
                is_bot_created = True
        
        if is_bot_created:
            try:
                await channel.delete()
                if isinstance(channel, discord.CategoryChannel):
                    deleted_categories += 1
                else:
                    deleted_channels += 1
                await asyncio.sleep(0.5)
            except Exception as e:
                logger.error(f"Failed to delete channel {channel.name}: {e}")
        else:
            skipped_channels += 1
    
    # Delete bot-created roles only (those with BOT_MARKER)
    for role in ctx.guild.roles:
        if role.name == "@everyone" or role.managed:
            continue
        
        if BOT_MARKER in role.name:
            try:
                await role.delete()
                deleted_roles += 1
                await asyncio.sleep(0.5)
            except Exception as e:
                logger.error(f"Failed to delete role {role.name}: {e}")
        else:
            skipped_roles += 1
    
    await ctx.send(f"✅ Cleanup complete!\n"
                   f"**Deleted:** {deleted_channels} channels, {deleted_categories} categories, {deleted_roles} roles\n"
                   f"**Preserved:** {skipped_channels} manually-created channels, {skipped_roles} manually-created roles")
    logger.info(f"Cleanup completed: Deleted {deleted_channels} channels, {deleted_categories} categories, {deleted_roles} roles. "
                f"Skipped {skipped_channels} channels, {skipped_roles} roles")


@bot.command(name="remove-channel")
@commands.has_permissions(administrator=True)
async def remove_channel(ctx, channel_name: str):
    """
    Force remove a specific channel (bot-created or manual)
    Usage: !remove-channel <channel-name>
    No confirmation required - use with caution!
    """
    if ctx.guild is None:
        await ctx.send("❌ This command can only be used in a server, not in DMs.")
        return
    
    channel = discord.utils.get(ctx.guild.channels, name=channel_name)
    
    if not channel:
        await ctx.send(f"❌ Channel `{channel_name}` not found.")
        return
    
    if channel == ctx.channel:
        await ctx.send(f"❌ Cannot delete the channel you're currently in!")
        return
    
    try:
        channel_type = "category" if isinstance(channel, discord.CategoryChannel) else "channel"
        await channel.delete()
        await ctx.send(f"✅ Deleted {channel_type}: `{channel_name}`")
        logger.info(f"Channel {channel_name} force-deleted by {ctx.author}")
    except Exception as e:
        await ctx.send(f"❌ Failed to delete channel: {str(e)}")
        logger.error(f"Failed to delete channel {channel_name}: {e}")


@bot.event
async def on_command_error(ctx, error):
    """Handle command errors"""
    # Get the original exception if it's wrapped
    if isinstance(error, commands.CommandInvokeError):
        error = error.original
    
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command. Administrator role required.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Unknown command. Use `!help` to see available commands.")
    elif isinstance(error, AttributeError) and "'NoneType' object has no attribute" in str(error):
        await ctx.send("❌ This command must be used in a server channel, not in DMs.")
        logger.warning(f"Command used in DM by {ctx.author}: {ctx.message.content}")
    else:
        await ctx.send(f"❌ An error occurred: {str(error)}")
        logger.error(f"Command error in {ctx.guild.name if ctx.guild else 'DM'} by {ctx.author}: {error}", exc_info=True)


def main():
    """Main entry point"""
    if not DISCORD_BOT_TOKEN:
        logger.error("DISCORD_BOT_TOKEN not found in environment variables!")
        logger.error("Please create a .env file with your bot token.")
        return
    
    logger.info("Starting Discord AI Server Setup Bot...")
    logger.info("Press Ctrl+C to stop the bot")
    
    try:
        bot.run(DISCORD_BOT_TOKEN)
    except discord.LoginFailure:
        logger.error("Failed to login - invalid bot token!")
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Bot crashed with error: {e}", exc_info=True)


if __name__ == "__main__":
    main()
