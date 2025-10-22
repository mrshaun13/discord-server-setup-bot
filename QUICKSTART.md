# 🚀 Quick Start Guide

Get your Discord AI server set up in 5 minutes!

---

## ⚡ Super Fast Setup

### 1. Create Discord Bot (2 minutes)

1. Go to https://discord.com/developers/applications
2. Click "New Application" → Name it → Create
3. Click "Bot" → "Add Bot"
4. **Enable these 3 intents:**
   - ✅ Presence Intent
   - ✅ Server Members Intent  
   - ✅ Message Content Intent
5. Click "Reset Token" → **Copy the token** (save it!)
6. Go to "OAuth2" → "URL Generator"
7. Select: `bot` + `applications.commands`
8. Select: `Administrator` permission
9. **Copy the URL** → Open in browser → Select your server → Authorize

### 2. Configure Bot (1 minute)

```bash
cd discord-ai-server-bot

# Copy example config
cp .env.example .env

# Edit and add your token
nano .env
```

Paste your token:
```env
DISCORD_BOT_TOKEN=paste_your_token_here
GUILD_ID=your_server_id_here
```

**Get Server ID:**
- Enable Developer Mode (Settings → Advanced → Developer Mode)
- Right-click your server → Copy ID

### 3. Run Bot (1 minute)

```bash
# Make script executable
chmod +x run.sh

# Run it!
./run.sh
```

### 4. Set Up Server (2 minutes)

In Discord:
```
!setup
```

Wait 2-5 minutes for completion.

### 5. Done! 🎉

```
!shutdown
```

Your server is configured! The bot is no longer needed.

---

## 🐳 Docker Quick Start

```bash
# Create .env file first (see step 2 above)
cp .env.example .env
nano .env

# Run with Docker
docker-compose up --build
```

In Discord:
```
!setup
```

Then:
```
!shutdown
```

---

## 🆘 Common Issues

**Bot won't start?**
```bash
# Check .env exists
ls -la .env

# Verify token is set
cat .env
```

**Bot online but not responding?**
- Check you enabled "Message Content Intent" in Developer Portal
- Verify bot has Administrator permission

**Setup fails?**
- Bot role must be high in role hierarchy
- Check logs: `cat setup_bot.log`
- Run `!setup` again (safe to retry)

---

## 📋 What Gets Created

- **9 categories** (Welcome, General, AI Discussion, Development, Tools, Creative, Learning, Community, Voice)
- **40+ channels** (organized by topic)
- **12+ roles** (admin, moderator, expertise, interests)
- **Welcome messages** in #welcome
- **Server rules** in #rules
- **Learning resources** in #resources

---

## ⚙️ Commands

| Command | Description |
|---------|-------------|
| `!setup` | Run server setup (one-time) |
| `!status` | Check server status |
| `!shutdown` | Stop the bot |
| `!cleanup` | Delete everything (requires confirmation) |
| `!help` | Show all commands |

---

## 🎯 Next Steps

After setup:

1. **Assign Moderators**
   - Right-click members → Roles → ⚔️ Moderator

2. **Add Moderation Bots**
   - [MEE6](https://mee6.xyz/) - Auto-mod & leveling
   - [Dyno](https://dyno.gg/) - Advanced moderation
   - [Carl-bot](https://carl.gg/) - Reaction roles

3. **Customize**
   - Edit channel topics
   - Reorder channels
   - Add custom emojis

4. **Invite Friends!**
   - Share server invite link
   - Post in #introductions

---

## 📚 Full Documentation

See [README.md](README.md) for complete documentation including:
- Detailed setup instructions
- Troubleshooting guide
- Customization options
- Architecture details
- Security best practices

---

**That's it! Your AI Discord server is ready to go! 🚀**
