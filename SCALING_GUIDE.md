# 📊 Template Scaling Guide

The bot now supports **percentage-based scaling** (1-100%) to create lightweight or full-featured servers based on your needs.

---

## 🎯 How Scaling Works

### Scale Levels

| Scale | Name | Description | Use Case |
|-------|------|-------------|----------|
| **1-25%** | Minimal | Essential channels only (1-2 categories) | Testing, small teams, minimal setup |
| **26-50%** | Basic | Core functionality (~50% of content) | Small communities, focused purpose |
| **51-75%** | Standard | Most features (~75% of content) | Medium communities, growing servers |
| **76-100%** | Full | Complete enterprise setup | Large communities, full feature set |

### What Gets Scaled

- **Categories**: Number of category sections
- **Channels**: Number of channels per category  
- **Roles**: Number of roles created
- **Content**: Welcome messages, rules, and resources remain full

---

## �� Usage

### Basic Setup (100% - Full)
```
\!setup school
\!setup aws-chatops
\!setup gaming-hangout
```

### Scaled Setup
```
\!setup school 50          # 50% scale - basic school setup
\!setup aws-chatops 25     # 25% scale - minimal AWS monitoring
\!setup gaming-hangout 75  # 75% scale - most gaming features
```

### Examples by Scale

#### School Template at Different Scales

**1% (Minimal)**
```
1 category, 2 channels, 2 roles
Perfect for: Testing, very small class
```

**25% (Minimal)**
```
1 category, 2 channels, 2 roles  
Perfect for: Single class, small study group
```

**50% (Basic)**
```
3 categories, 7 channels, 4 roles
Perfect for: Small school, department, club
```

**75% (Standard)**
```
5 categories, 16 channels, 6 roles
Perfect for: Medium school, multiple classes
```

**100% (Full)**
```
7 categories, 30 channels, 8 roles
Perfect for: Large school, university, full campus
```

---

## 💡 Scaling Strategy

### When to Use Each Scale

#### 1-25% (Minimal)
**Best for:**
- Testing templates before full deployment
- Very small teams (5-10 people)
- Single-purpose servers
- Proof of concept

**Includes:**
- Essential announcement channels
- 1-2 core discussion channels
- Admin/moderator roles only

#### 26-50% (Basic)
**Best for:**
- Small communities (10-50 people)
- Focused single-topic servers
- Budget-conscious setups
- Growing communities

**Includes:**
- Core categories (50%)
- Main discussion channels
- Essential roles
- Basic structure

#### 51-75% (Standard)
**Best for:**
- Medium communities (50-200 people)
- Multi-purpose servers
- Most common use case
- Balanced feature set

**Includes:**
- Most categories (75%)
- Majority of channels
- Most roles
- Well-rounded setup

#### 76-100% (Full)
**Best for:**
- Large communities (200+ people)
- Enterprise/professional use
- Feature-rich environments
- Maximum organization

**Includes:**
- All categories
- All channels
- All roles
- Complete feature set

---

## 📊 Template Scaling Examples

### AWS ChatOps Scaling

| Scale | Categories | Channels | Roles | Best For |
|-------|------------|----------|-------|----------|
| 25% | 2 | 6 | 2 | Single service monitoring |
| 50% | 4 | 16 | 4 | Small DevOps team |
| 75% | 6 | 24 | 6 | Medium SRE team |
| 100% | 8 | 32 | 8 | Full enterprise operations |

### Gaming Hangout Scaling

| Scale | Categories | Channels | Roles | Best For |
|-------|------------|----------|-------|----------|
| 25% | 1 | 3 | 2 | Small friend group |
| 50% | 3 | 8 | 3 | Gaming clan |
| 75% | 4 | 12 | 5 | Large gaming community |
| 100% | 6 | 16 | 6 | Multi-game community |

---

## 🔄 Changing Scale

### Upgrading Scale
To add more channels/roles later:
```
\!setup school 100    # Run with higher scale
```
The bot will skip existing channels and add new ones.

### Downgrading Scale
To reduce channels/roles:
```
\!cleanup              # Remove everything
\!confirm_cleanup      # Confirm
\!setup school 50      # Rebuild at lower scale
```

---

## 🎯 Best Practices

### 1. Start Small, Scale Up
- Begin with 25-50% for new communities
- Add more as community grows
- Easier to add than remove

### 2. Match Scale to Community Size
- **< 20 members**: 25-50%
- **20-100 members**: 50-75%
- **100+ members**: 75-100%

### 3. Consider Activity Level
- High activity: Higher scale (more channels to organize)
- Low activity: Lower scale (avoid empty channels)

### 4. Purpose-Driven Scaling
- Single purpose: 25-50%
- Multi-purpose: 50-75%
- Enterprise/Professional: 75-100%

---

## 🛠️ Technical Details

### Scaling Algorithm

The scaling system intelligently reduces:

1. **Categories**: Keeps first N categories based on scale
2. **Channels**: Keeps proportional channels per category
3. **Roles**: Prioritizes admin/mod roles, then others
4. **Content**: Full rules/welcome/resources at all scales

### Minimum Guarantees

Even at 1%, you get:
- At least 1 category
- At least 2 channels
- At least 2 roles (admin + one other)
- Full welcome and rules content

---

## 📝 Examples

### Example 1: Small Study Group
```
\!setup school 25
```
Creates: Welcome, announcements, general-academic, homework-help
Perfect for: 10-15 students studying together

### Example 2: Growing Startup
```
\!setup small-business 50
```
Creates: Company info, operations, key departments
Perfect for: 20-30 employee startup

### Example 3: Gaming Community
```
\!setup gaming-hangout 75
```
Creates: Most gaming and hobby channels
Perfect for: 50-100 member gaming community

### Example 4: Enterprise IT
```
\!setup itil-ops 100
```
Creates: Full ITIL-compliant structure
Perfect for: Large IT department

---

## 🔍 Checking Your Scale

After setup, use:
```
\!status
```

This shows:
- Number of categories created
- Number of channels created
- Number of roles created

Compare with the scaling table to verify your scale.

---

## ❓ FAQ

**Q: Can I change scale after setup?**
A: Yes\! Run `\!setup <template> <new-scale>` and it will add missing items.

**Q: What if I want specific channels from different scales?**
A: Start with your desired scale, then manually add/remove channels in Discord.

**Q: Does scaling affect performance?**
A: No, it only affects what gets created. Fewer channels = cleaner server.

**Q: Can I scale down without cleanup?**
A: No, you must use `\!cleanup` first, then setup with lower scale.

**Q: What scale should I use?**
A: Start with 50% for most use cases. Scale up as needed.

---

## 🎉 Summary

- **1-25%**: Minimal - Testing & tiny teams
- **26-50%**: Basic - Small communities
- **51-75%**: Standard - Medium communities (recommended)
- **76-100%**: Full - Large/enterprise

**Default**: 100% (full setup)

**Recommendation**: Start at 50-75% and scale up as your community grows\!
