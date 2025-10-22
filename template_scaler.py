"""
Template Scaling Logic
Scales templates from 1% (minimal) to 100% (full enterprise)
"""

def scale_template(template_config, scale_percent):
    """
    Scale a template based on percentage (1-100)
    
    Scaling tiers:
    - 1-25%: Minimal (essential channels only, 1-2 categories)
    - 26-50%: Basic (core functionality, ~50% of content)
    - 51-75%: Standard (most features, ~75% of content)
    - 76-100%: Full (all features, complete setup)
    
    Args:
        template_config: Full template configuration
        scale_percent: Integer 1-100 representing scale
    
    Returns:
        Scaled template configuration
    """
    # Clamp scale_percent to valid range
    scale_percent = max(1, min(100, scale_percent))
    
    scaled_config = {"categories": []}
    scaled_roles = []
    
    categories = template_config["config"]["categories"]
    roles = template_config["roles"]
    
    if scale_percent <= 25:
        # MINIMAL: Bare essentials only
        # Keep first category + 1-2 essential channels per category
        num_categories = max(1, len(categories) // 4)
        for cat in categories[:num_categories]:
            scaled_cat = cat.copy()
            # Keep minimum 2 channels, maximum 3
            num_channels = min(3, max(2, len(cat["channels"]) // 3))
            scaled_cat["channels"] = cat["channels"][:num_channels]
            scaled_config["categories"].append(scaled_cat)
        # Keep only admin/mod roles (minimum 2)
        admin_roles = [r for r in roles if any(keyword in r["name"].lower() 
                                               for keyword in ["admin", "mod", "owner", "manager"])]
        scaled_roles = admin_roles[:2] if len(admin_roles) >= 2 else roles[:2]
        
    elif scale_percent <= 50:
        # BASIC: Core functionality
        # Keep ~50% of categories with ~50% of channels
        num_categories = max(2, len(categories) // 2)
        for cat in categories[:num_categories]:
            scaled_cat = cat.copy()
            num_channels = max(2, len(cat["channels"]) // 2)
            scaled_cat["channels"] = cat["channels"][:num_channels]
            scaled_config["categories"].append(scaled_cat)
        # Keep ~50% of roles (minimum 3)
        scaled_roles = roles[:max(3, len(roles) // 2)]
        
    elif scale_percent <= 75:
        # STANDARD: Most features
        # Keep ~75% of categories with ~75% of channels
        num_categories = max(3, int(len(categories) * 0.75))
        for cat in categories[:num_categories]:
            scaled_cat = cat.copy()
            num_channels = max(3, int(len(cat["channels"]) * 0.75))
            scaled_cat["channels"] = cat["channels"][:num_channels]
            scaled_config["categories"].append(scaled_cat)
        # Keep ~75% of roles (minimum 4)
        scaled_roles = roles[:max(4, int(len(roles) * 0.75))]
        
    else:
        # FULL: Everything (76-100%)
        scaled_config = template_config["config"].copy()
        scaled_roles = roles.copy()
    
    # Return scaled template
    return {
        "name": f"{template_config['name']} ({scale_percent}%)",
        "description": template_config["description"],
        "config": scaled_config,
        "roles": scaled_roles,
        "rules": template_config["rules"],
        "welcome": template_config["welcome"],
        "resources": template_config["resources"],
    }


def get_scale_description(scale_percent):
    """Get human-readable description of scale level"""
    if scale_percent <= 25:
        return "Minimal - Essential channels only"
    elif scale_percent <= 50:
        return "Basic - Core functionality"
    elif scale_percent <= 75:
        return "Standard - Most features"
    else:
        return "Full - Complete enterprise setup"
