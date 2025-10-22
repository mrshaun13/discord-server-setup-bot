# 🔍 Dry-Run & Preview Guide

The bot now supports **dry-run previews** so you can see exactly what will be created before applying changes\!

---

## 🎯 New Commands

### `\!preview <template> [scale]`
**Preview what a template will create without making changes**

```bash
# Preview full template
\!preview school

# Preview at specific scale
\!preview school 50
\!preview aws-chatops 25

# Preview on existing server (shows diff)
\!preview school 100
```

**What it shows:**
- Total categories, channels, and roles
- Full structure breakdown
- All channel names organized by category
- Role list
- **On existing servers**: Shows what will be ADDED (diff)

---

### `\!rescale <template> <new-scale>`
**Preview what will be added when scaling up**

```bash
# After setting up at 60%, preview scaling to 100%
\!rescale school 100

# Preview scaling from 50% to 75%
\!rescale aws-chatops 75
```

**What it shows:**
- Current server state
- What will be added (new categories, channels, roles)
- Detailed breakdown of additions
- Command to apply changes

---

### `\!add-channel <channel-name>`
**Add individual channels from template** _(Coming Soon)_

For now, use:
1. `\!preview <template> 100` to see all channels
2. Run `\!setup <template> <higher-scale>` to add more

---

## 📊 Use Cases

### 1. Preview Before First Setup

**Scenario**: You want to see what a template looks like before creating it.

```bash
# See full school template
\!preview school 100

# See minimal version
\!preview school 25

# Compare different scales
\!preview gaming-hangout 50
\!preview gaming-hangout 75
```

**Result**: Full structure preview with all channels and roles listed.

---

### 2. Preview Scale Upgrade

**Scenario**: You set up `school` at 60% and want to see what 100% adds.

```bash
# Current setup
\!setup school 60

# Later, preview upgrade
\!preview school 100
```

**Result**: Shows ONLY what will be added (diff):
- New categories
- New channels
- New roles
- Existing items are not shown

---

### 3. Use Rescale Command

**Scenario**: Dedicated command for scaling up.

```bash
# After initial setup at 50%
\!setup school 50

# Preview scaling to 75%
\!rescale school 75

# Apply if you like it
\!setup school 75
```

**Result**: Clear diff showing exactly what will be added.

---

### 4. Compare Templates

**Scenario**: Deciding between templates.

```bash
# Compare different templates
\!preview school 50
\!preview small-business 50
\!preview gaming-hangout 50
```

**Result**: See structure of each to make informed decision.

---

## 🎨 Preview Output Examples

### Fresh Server (No Existing Content)

```
# 📋 Preview: School/Education Server (50%)
*Complete setup for schools, universities, or educational communities*

## 📊 Summary
• Categories: 3
• Text Channels: 7
• Voice Channels: 0
• Total Channels: 7
• Roles: 4

## 📁 Structure

**📢 ANNOUNCEMENTS**
  💬 welcome
  💬 announcements

**📚 ACADEMICS**
  💬 general-academic
  💬 homework-help

**🎓 SUBJECTS**
  💬 mathematics
  💬 science
  💬 english-literature

## 👥 Roles
• 🎓 Principal
• 👨‍🏫 Teacher
• 📚 TA
• 🎓 Senior

Scale: 50% - Basic - Core functionality

✅ Run `\!setup school 50` to create this structure.
```

---

### Existing Server (Shows Diff)

```
**Template:** School/Education Server (100%)
**Scale:** 100% - Full - Complete enterprise setup

# 🔍 Setup Preview - What Will Change

## 📊 Current Server
• Categories: 3
• Channels: 7
• Roles: 4

## ➕ Will Be Added
• New Categories: 4
• New Text Channels: 23
• New Voice Channels: 4
• New Roles: 4

### New Categories
• 👨‍🏫 FACULTY & STAFF
• 🎨 EXTRACURRICULAR
• 💬 SOCIAL
• 🔊 VOICE ROOMS

### New Text Channels
• #teacher-lounge (in 👨‍🏫 FACULTY & STAFF)
• #office-hours (in 👨‍🏫 FACULTY & STAFF)
• #parent-teacher (in 👨‍🏫 FACULTY & STAFF)
• #clubs (in 🎨 EXTRACURRICULAR)
• #sports (in 🎨 EXTRACURRICULAR)
... and 18 more

### New Voice Channels
• 🔊 Study Hall (in 🔊 VOICE ROOMS)
• 🔊 Group Study (in 🔊 VOICE ROOMS)
• 🔊 Office Hours (in 🔊 VOICE ROOMS)
• 🔊 Hangout (in 🔊 VOICE ROOMS)

### New Roles
• 📘 Junior
• 📗 Sophomore
• 📙 Freshman
• 👪 Parent

✅ Run `\!setup school 100` to apply these changes.
```

---

## 🔄 Workflow Examples

### Workflow 1: Cautious Setup

```bash
# Step 1: Preview minimal version
\!preview school 25

# Step 2: Set up minimal
\!setup school 25

# Step 3: Test and evaluate

# Step 4: Preview next scale
\!preview school 50

# Step 5: Scale up
\!setup school 50

# Step 6: Continue as needed
\!rescale school 75
\!setup school 75
```

---

### Workflow 2: Direct Setup with Preview

```bash
# Step 1: Preview target scale
\!preview school 75

# Step 2: If satisfied, apply
\!setup school 75

# Done\!
```

---

### Workflow 3: Gradual Growth

```bash
# Start small
\!setup gaming-hangout 25

# Community grows, preview upgrade
\!rescale gaming-hangout 50

# Apply upgrade
\!setup gaming-hangout 50

# Keep growing
\!rescale gaming-hangout 75
\!setup gaming-hangout 75

# Eventually go full
\!rescale gaming-hangout 100
\!setup gaming-hangout 100
```

---

## 💡 Best Practices

### 1. Always Preview First
```bash
# Good practice
\!preview school 60
\!setup school 60

# Risky (no preview)
\!setup school 60
```

### 2. Preview Scale Changes
```bash
# Before scaling up
\!rescale school 100

# Review the diff, then apply
\!setup school 100
```

### 3. Compare Scales
```bash
# See different scales
\!preview school 25
\!preview school 50
\!preview school 75
\!preview school 100

# Choose the right one
\!setup school 60
```

### 4. Use Rescale for Clarity
```bash
# Clearer intent
\!rescale school 100

# vs generic preview
\!preview school 100
```

---

## 🎯 Command Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `\!preview` | See what will be created | `\!preview school 50` |
| `\!rescale` | Preview scale upgrade | `\!rescale school 75` |
| `\!setup` | Apply template/scale | `\!setup school 75` |
| `\!status` | Check current state | `\!status` |
| `\!templates` | List all templates | `\!templates` |

---

## ❓ FAQ

**Q: Does `\!preview` make any changes?**
A: No\! It's completely safe and read-only.

**Q: What's the difference between `\!preview` and `\!rescale`?**
A: `\!preview` is general-purpose. `\!rescale` is specifically for scaling up and makes the intent clearer.

**Q: Can I preview scaling down?**
A: No, you must use `\!cleanup` to remove content. Preview only shows additions.

**Q: Why does preview show different output on existing servers?**
A: It automatically detects existing content and shows a diff (what will be added) instead of the full structure.

**Q: Can I preview multiple templates?**
A: Yes\! Run `\!preview` multiple times with different templates to compare.

**Q: How do I see ALL channels in a template?**
A: Use `\!preview <template> 100` to see the full 100% version.

---

## 🚀 Quick Reference

```bash
# Preview fresh setup
\!preview school 50

# Preview on existing server (shows diff)
\!preview school 100

# Preview scale upgrade
\!rescale school 75

# Apply changes
\!setup school 75

# Check current state
\!status
```

---

## 🎉 Summary

**Dry-run capabilities:**
- ✅ Preview before setup
- ✅ See diffs on existing servers
- ✅ Preview scale upgrades
- ✅ Compare templates and scales
- ✅ Zero risk - no changes made

**Benefits:**
- Make informed decisions
- Avoid surprises
- Plan server growth
- Compare options easily
- Safe experimentation

**Remember**: Always preview before applying\! 🔍
