# 🛡️ Cleanup Safety & Channel Management

## ✅ Safety Improvements

### Problem Solved
The original `\!cleanup` command deleted **ALL channels and roles** in the server, including manually created ones. This was dangerous\!

### Solution: Bot Tracking System

All bot-created content is now marked with `[DSBOT]` (Discord Server Bot):

- **Channels**: `[DSBOT]` added to channel topic
- **Voice Channels**: `[DSBOT]` added to channel topic  
- **Roles**: `[DSBOT]` added to role name
- **Categories**: Tracked via their bot-created channels

### How It Works

When you run `\!setup`, the bot now:
1. Creates channels with `[DSBOT] <original topic>` in the topic
2. Creates roles with `<role name> [DSBOT]` in the name
3. Tracks all created content automatically

When you run `\!cleanup`, the bot:
1. **Only deletes** items marked with `[DSBOT]`
2. **Preserves** all manually created channels and roles
3. **Reports** what was deleted vs preserved

---

## 📝 New Commands

### `\!cleanup` (Full Server Cleanup)

**Usage:**
```
\!cleanup
```

**Behavior:**
- Requires confirmation (`\!confirm_cleanup`)
- Only deletes bot-created content
- Shows counts of deleted vs preserved items
- **Safe**: Manually created channels are NOT touched

**Example Output:**
```
✅ Cleanup complete\!
Deleted: 15 channels, 5 categories, 6 roles
Preserved: 3 manually-created channels, 2 manually-created roles
```

---

### `\!cleanup [channel-name]` (Single Channel)

**Usage:**
```
\!cleanup general-chat
\!cleanup old-announcements
```

**Behavior:**
- No confirmation required
- Only works on bot-created channels
- Instant deletion
- If channel is not bot-created, suggests using `\!remove-channel`

**Example:**
```
\!cleanup general-chat
✅ Deleted channel: general-chat
```

**If not bot-created:**
```
\!cleanup my-custom-channel
⚠️ Channel my-custom-channel was not created by this bot.
Use \!remove-channel my-custom-channel to force delete it.
```

---

### `\!remove-channel [channel-name]` (Force Delete)

**Usage:**
```
\!remove-channel any-channel
\!remove-channel old-category
```

**Behavior:**
- No confirmation required
- Works on ANY channel (bot-created or manual)
- Use with caution\!

**Example:**
```
\!remove-channel old-chat
✅ Deleted channel: old-chat
```

---

## 🔍 How to Identify Bot-Created Content

### Check Channel Topic
Bot-created channels have `[DSBOT]` in their topic:
```
[DSBOT] 💬 General discussion for AI topics
```

### Check Role Name
Bot-created roles have `[DSBOT]` in their name:
```
🎓 Principal [DSBOT]
👨‍🏫 Teacher [DSBOT]
```

### Using Discord
1. Right-click a channel → Edit Channel
2. Look at the topic/description
3. If it starts with `[DSBOT]`, it was created by the bot

---

## 🎯 Use Cases

### Use Case 1: Clean Slate
**Scenario**: You want to remove all bot-created content and start over.

```bash
\!cleanup
\!confirm_cleanup
# Removes all bot-created content, preserves your manual channels
```

---

### Use Case 2: Remove One Channel
**Scenario**: You don't need the "homework-help" channel anymore.

```bash
\!cleanup homework-help
# Instant removal, no confirmation
```

---

### Use Case 3: Remove Manual Channel
**Scenario**: You manually created "test-channel" and want to remove it.

```bash
\!cleanup test-channel
# Bot says: "Not created by bot, use \!remove-channel"

\!remove-channel test-channel
# Deleted\!
```

---

### Use Case 4: Scale Up Safely
**Scenario**: You started at 50% scale, now want 100%.

```bash
# Current: school at 50%
\!preview school 100
# See what will be added

\!setup school 100
# Adds new channels, skips existing ones

# Later, if you want to go back to 50%:
\!cleanup
\!confirm_cleanup
\!setup school 50
```

---

## ⚠️ Important Notes

### Manually Created Channels
- **Always safe** from `\!cleanup`
- Not marked with `[DSBOT]`
- Must use `\!remove-channel` to delete

### Bot-Created Channels
- Marked with `[DSBOT]`
- Can be deleted with `\!cleanup`
- Can be deleted individually with `\!cleanup [name]`

### Categories
- Deleted if all channels inside are bot-created
- Preserved if any manual channels exist inside

### Roles
- Bot-created roles have `[DSBOT]` in name
- Manually created roles are never deleted
- `@everyone` and managed roles (bot roles) are never deleted

---

## 🔄 Migration from Old Version

If you used the old bot (before this update):

### Old Behavior
```
\!cleanup
# Deleted EVERYTHING (dangerous\!)
```

### New Behavior
```
\!cleanup
# Only deletes bot-created content (safe\!)
```

### What Changed
1. **Tracking added**: All new content is marked with `[DSBOT]`
2. **Safety added**: Only tracked content is deleted
3. **Reporting added**: Shows what was preserved

### Old Content
Content created before this update is **NOT marked** with `[DSBOT]`:
- Won't be deleted by `\!cleanup`
- Use `\!remove-channel` to delete if needed
- Or manually delete in Discord

---

## 📊 Command Comparison

| Command | Target | Confirmation | Safety |
|---------|--------|--------------|--------|
| `\!cleanup` | All bot content | Yes | ✅ Safe |
| `\!cleanup [name]` | One bot channel | No | ✅ Safe |
| `\!remove-channel [name]` | Any channel | No | ⚠️ Use caution |

---

## 🎉 Benefits

### Before (Dangerous)
- ❌ Deleted everything
- ❌ No way to preserve manual channels
- ❌ All-or-nothing approach
- ❌ Scary to use

### After (Safe)
- ✅ Only deletes bot content
- ✅ Preserves manual channels
- ✅ Granular control (single channels)
- ✅ Safe to use anytime

---

## 💡 Best Practices

1. **Preview before setup**: Use `\!preview` to see what will be created
2. **Start small**: Use 25-50% scale initially
3. **Scale up gradually**: Use `\!rescale` to see what will be added
4. **Clean up safely**: Use `\!cleanup` knowing manual content is safe
5. **Remove individually**: Use `\!cleanup [name]` for single channels
6. **Force delete carefully**: Only use `\!remove-channel` when necessary

---

## ❓ FAQ

**Q: Will `\!cleanup` delete my manually created channels?**
A: No\! Only channels marked with `[DSBOT]` are deleted.

**Q: How do I delete a manually created channel?**
A: Use `\!remove-channel [channel-name]` or delete it manually in Discord.

**Q: What if I want to delete everything?**
A: Use `\!cleanup` for bot content, then manually delete the rest in Discord.

**Q: Can I remove the `[DSBOT]` marker?**
A: Yes, edit the channel topic or role name. But then `\!cleanup` won't delete it.

**Q: What about old channels created before this update?**
A: They don't have `[DSBOT]`, so `\!cleanup` won't delete them. Use `\!remove-channel`.

**Q: Is there a way to see what will be deleted?**
A: Not yet, but you can check channel topics for `[DSBOT]` marker.

---

## 🚀 Summary

**Safe Cleanup System:**
- ✅ Bot tracks all created content with `[DSBOT]` marker
- ✅ `\!cleanup` only deletes tracked content
- ✅ Manual channels are always safe
- ✅ Granular control with `\!cleanup [name]`
- ✅ Force delete with `\!remove-channel [name]`

**Your manually created channels are now safe\!** 🎉
