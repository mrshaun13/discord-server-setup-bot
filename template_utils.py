"""
Template Utilities
Dry-run previews, diffs, and channel management helpers
"""

def get_template_summary(template_config):
    """
    Get a summary of what a template will create
    
    Returns:
        dict with categories, channels, roles, and details
    """
    categories = template_config["config"]["categories"]
    roles = template_config["roles"]
    
    # Count channels by type
    text_channels = []
    voice_channels = []
    
    for category in categories:
        for channel in category["channels"]:
            channel_info = {
                "name": channel["name"],
                "category": category["name"],
                "topic": channel.get("topic", "")
            }
            if channel["type"] == "voice":
                voice_channels.append(channel_info)
            else:
                text_channels.append(channel_info)
    
    return {
        "name": template_config["name"],
        "description": template_config["description"],
        "categories": categories,
        "text_channels": text_channels,
        "voice_channels": voice_channels,
        "roles": roles,
        "total_categories": len(categories),
        "total_text_channels": len(text_channels),
        "total_voice_channels": len(voice_channels),
        "total_channels": len(text_channels) + len(voice_channels),
        "total_roles": len(roles),
    }


def format_preview(summary, show_details=True):
    """
    Format a template summary for display
    
    Args:
        summary: Template summary from get_template_summary()
        show_details: If True, show full channel list. If False, just counts.
    
    Returns:
        Formatted string for Discord message
    """
    lines = []
    lines.append(f"# 📋 Preview: {summary['name']}")
    lines.append(f"*{summary['description']}*\n")
    
    lines.append("## 📊 Summary")
    lines.append(f"• **Categories**: {summary['total_categories']}")
    lines.append(f"• **Text Channels**: {summary['total_text_channels']}")
    lines.append(f"• **Voice Channels**: {summary['total_voice_channels']}")
    lines.append(f"• **Total Channels**: {summary['total_channels']}")
    lines.append(f"• **Roles**: {summary['total_roles']}\n")
    
    if show_details:
        lines.append("## 📁 Structure")
        for category in summary['categories']:
            lines.append(f"\n**{category['name']}**")
            for channel in category['channels']:
                icon = "🔊" if channel['type'] == "voice" else "💬"
                lines.append(f"  {icon} {channel['name']}")
        
        lines.append("\n## 👥 Roles")
        for role in summary['roles']:
            lines.append(f"• {role['name']}")
    
    return "\n".join(lines)


def calculate_diff(current_guild, new_template_config):
    """
    Calculate what will be added/changed when applying a template
    
    Args:
        current_guild: Discord Guild object
        new_template_config: Template configuration to apply
    
    Returns:
        dict with to_add and existing items
    """
    new_summary = get_template_summary(new_template_config)
    
    # Get existing categories and channels
    existing_categories = {cat.name for cat in current_guild.categories}
    existing_channels = {ch.name for ch in current_guild.channels}
    existing_roles = {role.name for role in current_guild.roles}
    
    # Calculate what's new
    new_categories = []
    new_text_channels = []
    new_voice_channels = []
    new_roles = []
    
    for category in new_summary['categories']:
        if category['name'] not in existing_categories:
            new_categories.append(category['name'])
    
    for channel in new_summary['text_channels']:
        if channel['name'] not in existing_channels:
            new_text_channels.append(channel)
    
    for channel in new_summary['voice_channels']:
        if channel['name'] not in existing_channels:
            new_voice_channels.append(channel)
    
    for role in new_summary['roles']:
        if role['name'] not in existing_roles:
            new_roles.append(role['name'])
    
    return {
        "new_categories": new_categories,
        "new_text_channels": new_text_channels,
        "new_voice_channels": new_voice_channels,
        "new_roles": new_roles,
        "total_new_categories": len(new_categories),
        "total_new_text_channels": len(new_text_channels),
        "total_new_voice_channels": len(new_voice_channels),
        "total_new_channels": len(new_text_channels) + len(new_voice_channels),
        "total_new_roles": len(new_roles),
        "existing_categories": len(existing_categories),
        "existing_channels": len(existing_channels),
        "existing_roles": len(existing_roles),
    }


def format_diff(diff):
    """
    Format a diff for display
    
    Args:
        diff: Diff from calculate_diff()
    
    Returns:
        Formatted string for Discord message
    """
    lines = []
    lines.append("# 🔍 Setup Preview - What Will Change\n")
    
    lines.append("## 📊 Current Server")
    lines.append(f"• Categories: {diff['existing_categories']}")
    lines.append(f"• Channels: {diff['existing_channels']}")
    lines.append(f"• Roles: {diff['existing_roles']}\n")
    
    lines.append("## ➕ Will Be Added")
    lines.append(f"• **New Categories**: {diff['total_new_categories']}")
    lines.append(f"• **New Text Channels**: {diff['total_new_text_channels']}")
    lines.append(f"• **New Voice Channels**: {diff['total_new_voice_channels']}")
    lines.append(f"• **New Roles**: {diff['total_new_roles']}\n")
    
    if diff['total_new_categories'] > 0:
        lines.append("### New Categories")
        for cat in diff['new_categories']:
            lines.append(f"• {cat}")
        lines.append("")
    
    if diff['total_new_text_channels'] > 0:
        lines.append("### New Text Channels")
        for ch in diff['new_text_channels'][:10]:  # Limit to 10 for display
            lines.append(f"• #{ch['name']} (in {ch['category']})")
        if len(diff['new_text_channels']) > 10:
            lines.append(f"• ... and {len(diff['new_text_channels']) - 10} more")
        lines.append("")
    
    if diff['total_new_voice_channels'] > 0:
        lines.append("### New Voice Channels")
        for ch in diff['new_voice_channels'][:10]:
            lines.append(f"• 🔊 {ch['name']} (in {ch['category']})")
        if len(diff['new_voice_channels']) > 10:
            lines.append(f"• ... and {len(diff['new_voice_channels']) - 10} more")
        lines.append("")
    
    if diff['total_new_roles'] > 0:
        lines.append("### New Roles")
        for role in diff['new_roles'][:10]:
            lines.append(f"• {role}")
        if len(diff['new_roles']) > 10:
            lines.append(f"• ... and {len(diff['new_roles']) - 10} more")
    
    if (diff['total_new_categories'] == 0 and 
        diff['total_new_channels'] == 0 and 
        diff['total_new_roles'] == 0):
        lines.append("✅ **No changes needed** - Everything already exists!")
    
    return "\n".join(lines)


def get_available_channels_from_template(template_name, scale):
    """
    Get list of channels available in a template at a given scale
    For use in add-channel command
    
    Args:
        template_name: Name of template
        scale: Current scale percentage
    
    Returns:
        List of available channels that could be added
    """
    from templates import get_template
    
    # Get full template (100%)
    full_template = get_template(template_name, 100)
    if not full_template:
        return []
    
    # Get current scale template
    current_template = get_template(template_name, scale)
    
    # Get all channels from full template
    full_channels = []
    for category in full_template["config"]["categories"]:
        for channel in category["channels"]:
            full_channels.append({
                "name": channel["name"],
                "type": channel["type"],
                "topic": channel.get("topic", ""),
                "category": category["name"]
            })
    
    # Get channels in current scale
    current_channels = set()
    for category in current_template["config"]["categories"]:
        for channel in category["channels"]:
            current_channels.add(channel["name"])
    
    # Return channels not in current scale
    available = [ch for ch in full_channels if ch["name"] not in current_channels]
    return available
