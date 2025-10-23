# 🎮 Command Reference Guide

Quick reference for all bot commands with examples.

---

## 📋 Template Management

### `!templates`
List all available templates

```bash
!templates
```

**Output:** Shows all 13 templates with descriptions

---

### `!preview [template] [scale]`
Preview what a template will create (dry-run)

```bash
!preview school 50              # Preview school at 50%
!preview small-business 100     # Preview small-business at 100%
!preview gaming-hangout         # Preview at 100% (default)
```

**Shows:**
- All categories and channels
- All roles
- On existing servers: Shows diff (what will be added)

---

### `!setup [template] [scale]`
Set up your server with a template

```bash
!setup                          # Default: ai-dev at 100%
!setup school 50                # School template at 50%
!setup small-business 75        # Small business at 75%
!setup gaming-hangout           # Gaming at 100%
```

**Scale Guide:**
- `1-25%`: Minimal (essential channels only)
- `26-50%`: Basic (core functionality)
- `51-75%`: Standard (most features)
- `76-100%`: Full (complete setup)

**Duration:** 2-5 minutes

---

### `!rescale [template] [scale]`
Preview what will be added when scaling up

```bash
!rescale small-business 75      # See what 75% adds
!rescale school 100             # See what 100% adds
```

**Shows:**
- Current server state
- What will be added (new channels, roles)
- Detailed breakdown

**To apply:** Run `!setup [template] [scale]` after reviewing

---

## ➕ Channel Management

### `!add-channel [type] [name] [category]`
Add a custom channel with automatic bot tracking

```bash
!add-channel text project-updates          # Text channel
!add-channel voice Team Room                # Voice channel
!add-channel text announcements "📢 COMPANY"  # In specific category
```

**Types:**
- `text` - Text channel
- `voice` - Voice channel

**Features:**
- ✅ Automatically marked with `[DSBOT]`
- ✅ Tracked by bot (can be cleaned up)
- ✅ Optional category placement
- ✅ Helpful usage message if arguments missing

**Cleanup:**
```bash
!cleanup project-updates    # Remove this channel
!cleanup                    # Remove all bot-created channels
```

---

### `!add-category [name]`
Add a custom category to organize channels

```bash
!add-category 📁 PROJECTS
!add-category Custom Category
!add-category 🎮 GAMING
```

**After creating:**
```bash
# Add channels to the category
!add-channel text my-channel "📁 PROJECTS"
!add-channel voice Voice Room "📁 PROJECTS"
```

**Note:** Categories themselves are NOT tracked, but channels added with `!add-channel` are tracked.

---

## 🗑️ Cleanup & Management

### `!cleanup`
Remove ALL bot-created content (requires confirmation)

```bash
!cleanup
# Bot asks for confirmation
!confirm_cleanup
```

**What it deletes:**
- Channels with `[DSBOT]` marker
- Channels matching known patterns (legacy support)
- Roles with `[DSBOT]` marker

**What it preserves:**
- Manually created channels
- Manually created roles
- `@everyone` role
- Bot-managed roles

**Output:**
```
✅ Cleanup complete!
Deleted: 15 channels, 5 categories, 6 roles
Preserved: 3 manually-created channels, 2 manually-created roles
```

---

### `!cleanup [channel-name]`
Remove specific bot-created channel (no confirmation)

```bash
!cleanup homework-help          # Delete specific channel
!cleanup general-chat           # Delete specific channel
```

**Instant deletion** - No confirmation required

**Safety:** Only works on bot-created channels

---

### `!remove-channel [channel-name]`
Force delete ANY channel (bot or manual)

```bash
!remove-channel old-chat        # Delete any channel
!remove-channel test-channel    # Delete any channel
```

**⚠️ Warning:** No confirmation, works on any channel!

---

## 🔍 Debugging & Info

### `!check-detection`
See which channels will be detected as bot-created

```bash
!check-detection
```

**Shows:**
- ✅ Bot-created channels (will be deleted by cleanup)
- ❌ Manual channels (will be preserved)
- Reason for each detection

**Use this before cleanup** to see what will be deleted!

---

### `!status`
Check current server configuration

```bash
!status
```

**Shows:**
- Number of categories
- Number of text channels
- Number of voice channels
- Number of roles
- Member count

---

### `!migrate-markers`
Add `[DSBOT]` markers to existing channels

```bash
!migrate-markers
# Bot asks for confirmation
!confirm_migrate
```

**What it does:**
- Scans all channels
- Identifies bot-created channels using patterns
- Adds `[DSBOT]` marker to topics/names
- Reports results

**When to use:**
- After updating from old version
- Want explicit tracking
- Have pre-existing bot setup

---

## 🛠️ System Commands

### `!shutdown`
Gracefully shut down the bot

```bash
!shutdown
```

**Use after setup is complete** - Bot is no longer needed

---

### `!help`
Show all available commands

```bash
!help
```

---

## 📊 Common Workflows

### Workflow 1: Fresh Server Setup

```bash
# Step 1: Preview
!preview school 50

# Step 2: Setup
!setup school 50

# Step 3: Verify
!status

# Step 4: Shutdown (optional)
!shutdown
```

---

### Workflow 2: Scale Up Existing Server

```bash
# Step 1: Check current state
!status

# Step 2: Preview scaling
!rescale school 100

# Step 3: Apply scaling
!setup school 100
```

---

### Workflow 3: Clean Up and Start Over

```bash
# Step 1: Check what will be deleted
!check-detection

# Step 2: Clean up
!cleanup
!confirm_cleanup

# Step 3: New setup
!setup small-business 75
```

---

### Workflow 4: Add Custom Channels

```bash
# Step 1: Create a category
!add-category 📁 PROJECTS

# Step 2: Add channels to it
!add-channel text project-alpha "📁 PROJECTS"
!add-channel text project-beta "📁 PROJECTS"
!add-channel voice Project Meetings "📁 PROJECTS"

# Step 3: Verify
!status

# Step 4: Remove if needed
!cleanup project-alpha
```

---

### Workflow 5: Migrate Pre-Existing Setup

```bash
# Step 1: Check detection
!check-detection

# Step 2: Migrate markers (optional)
!migrate-markers
!confirm_migrate

# Step 3: Verify
!check-detection

# Step 4: Now cleanup works properly
!cleanup
!confirm_cleanup
```

---

## ⚠️ Important Notes

### Command Permissions
**All commands require Administrator permissions**

### Rate Limits
- Bot is rate-limited to avoid Discord API issues
- Large setups may take 2-5 minutes
- Be patient during setup/cleanup

### Safety Features
- Cleanup only deletes bot-created content
- Manual channels are always safe
- Confirmation required for destructive actions
- Can check detection before cleanup

### Pattern Detection
Bot recognizes 100+ channel patterns from all templates:
- Core templates (ai-dev, aws-chatops, itil-ops)
- School, small-business, gaming-hangout
- Content-creator, nonprofit, fitness
- Music-band, book-club, podcast, esports

---

## 🆘 Troubleshooting

### "Unknown command" error
**Solution:** Check spelling, use `!help` to see all commands

### "template is a required argument"
**Solution:** Provide template name
```bash
!rescale small-business 75      # Correct
!rescale 75                     # Wrong
```

### Cleanup deleted 0 channels
**Solution:** Run `!check-detection` to see what's detected
- If nothing detected, run `!migrate-markers`
- Or use `!remove-channel` for individual channels

### Channel not recognized as bot-created
**Solution:** 
1. Check if it matches patterns: `!check-detection`
2. Add marker manually: Edit channel → Add `[DSBOT]` to topic
3. Or use `!remove-channel` to force delete

---

## 📚 Quick Examples

```bash
# List templates
!templates

# Preview before setup
!preview school 50

# Setup server
!setup school 50

# Check what's detected
!check-detection

# Scale up
!rescale school 100
!setup school 100

# Remove one channel
!cleanup homework-help

# Full cleanup
!cleanup
!confirm_cleanup

# Migrate old setup
!migrate-markers
!confirm_migrate

# Force delete
!remove-channel old-channel

# Check status
!status

# Shutdown
!shutdown
```

---

## 🎯 Pro Tips

1. **Always preview first** - Use `!preview` before `!setup`
2. **Start small** - Use 25-50% scale initially, scale up later
3. **Check detection** - Run `!check-detection` before cleanup
4. **Migrate once** - Run `!migrate-markers` on pre-existing setups
5. **Use rescale** - Preview scaling changes before applying
6. **Single channel cleanup** - Use `!cleanup [name]` for quick removal
7. **Document your scale** - Remember what scale you used for future reference

---

**Need more help?** Check the full documentation:
- `README.md` - Complete guide
- `CLEANUP_SAFETY.md` - Cleanup system details
- `MIGRATION_GUIDE.md` - Pre-existing setup migration
- `SCALING_GUIDE.md` - Scaling system details
