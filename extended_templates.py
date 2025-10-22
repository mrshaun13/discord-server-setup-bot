"""
Extended Discord Server Templates
10 additional templates for various community types
"""

# Import the existing templates to extend them
EXTENDED_TEMPLATES = {}

# Template 1: School/Education
EXTENDED_TEMPLATES["school"] = {
    "name": "School/Education Server",
    "description": "Complete setup for schools, universities, or educational communities",
    "config": {
        "categories": [
            {
                "name": "📢 ANNOUNCEMENTS",
                "position": 0,
                "channels": [
                    {"name": "welcome", "type": "text", "topic": "👋 Welcome to our educational community"},
                    {"name": "announcements", "type": "text", "topic": "📣 Important school announcements"},
                    {"name": "calendar", "type": "text", "topic": "📅 Upcoming events and deadlines"},
                    {"name": "rules", "type": "text", "topic": "📜 Server and academic conduct rules"},
                ],
            },
            {
                "name": "📚 ACADEMICS",
                "position": 1,
                "channels": [
                    {"name": "general-academic", "type": "text", "topic": "💬 General academic discussions"},
                    {"name": "homework-help", "type": "text", "topic": "📝 Get help with assignments"},
                    {"name": "study-groups", "type": "text", "topic": "👥 Form and coordinate study groups"},
                    {"name": "exam-prep", "type": "text", "topic": "📖 Exam preparation and tips"},
                    {"name": "resources", "type": "text", "topic": "📚 Textbooks, notes, and study materials"},
                ],
            },
            {
                "name": "�� SUBJECTS",
                "position": 2,
                "channels": [
                    {"name": "mathematics", "type": "text", "topic": "🔢 Math discussions and help"},
                    {"name": "science", "type": "text", "topic": "🔬 Science topics and experiments"},
                    {"name": "english-literature", "type": "text", "topic": "📖 English and literature"},
                    {"name": "history-social-studies", "type": "text", "topic": "🏛️ History and social sciences"},
                    {"name": "languages", "type": "text", "topic": "🌍 Foreign language practice"},
                    {"name": "computer-science", "type": "text", "topic": "💻 Programming and CS topics"},
                ],
            },
            {
                "name": "👨‍🏫 FACULTY & STAFF",
                "position": 3,
                "channels": [
                    {"name": "teacher-lounge", "type": "text", "topic": "☕ Faculty discussion (staff only)"},
                    {"name": "office-hours", "type": "text", "topic": "🕐 Schedule and attend office hours"},
                    {"name": "parent-teacher", "type": "text", "topic": "👪 Parent-teacher communication"},
                ],
            },
            {
                "name": "🎨 EXTRACURRICULAR",
                "position": 4,
                "channels": [
                    {"name": "clubs", "type": "text", "topic": "🎭 School clubs and activities"},
                    {"name": "sports", "type": "text", "topic": "⚽ Sports teams and events"},
                    {"name": "arts-music", "type": "text", "topic": "🎨 Art, music, and creative activities"},
                    {"name": "student-government", "type": "text", "topic": "🏛️ Student council and leadership"},
                ],
            },
            {
                "name": "💬 SOCIAL",
                "position": 5,
                "channels": [
                    {"name": "general-chat", "type": "text", "topic": "💭 Casual student conversations"},
                    {"name": "introductions", "type": "text", "topic": "�� Introduce yourself"},
                    {"name": "memes-fun", "type": "text", "topic": "😂 Memes and fun content"},
                    {"name": "mental-health", "type": "text", "topic": "💚 Mental health support and resources"},
                ],
            },
            {
                "name": "🔊 VOICE ROOMS",
                "position": 6,
                "channels": [
                    {"name": "Study Hall", "type": "voice", "topic": "�� Silent study sessions"},
                    {"name": "Group Study", "type": "voice", "topic": "👥 Collaborative study"},
                    {"name": "Office Hours", "type": "voice", "topic": "👨‍🏫 Meet with teachers"},
                    {"name": "Hangout", "type": "voice", "topic": "🎮 Social voice chat"},
                ],
            },
        ],
    },
    "roles": [
        {"name": "🎓 Principal", "color": 0x992D22, "permissions": ["administrator"], "hoist": True, "mentionable": True},
        {"name": "👨‍🏫 Teacher", "color": 0x3498DB, "permissions": ["manage_messages", "manage_channels"], "hoist": True, "mentionable": True},
        {"name": "📚 TA", "color": 0x1ABC9C, "permissions": ["manage_messages"], "hoist": False, "mentionable": True},
        {"name": "🎓 Senior", "color": 0x9B59B6, "permissions": [], "hoist": False, "mentionable": True},
        {"name": "📘 Junior", "color": 0xE67E22, "permissions": [], "hoist": False, "mentionable": True},
        {"name": "📗 Sophomore", "color": 0xF1C40F, "permissions": [], "hoist": False, "mentionable": True},
        {"name": "📙 Freshman", "color": 0x2ECC71, "permissions": [], "hoist": False, "mentionable": True},
        {"name": "👪 Parent", "color": 0x95A5A6, "permissions": [], "hoist": False, "mentionable": True},
    ],
    "rules": """# 📜 School Server Rules

## Academic Integrity
• No cheating or plagiarism
• Don't share answers to graded assignments
• Cite your sources properly
• Help others learn, don't just give answers

## Respectful Behavior
• Treat everyone with respect
• No bullying or harassment
• Be inclusive and welcoming
• Respect teacher authority

## Appropriate Content
• Keep content school-appropriate
• No NSFW content
• No excessive profanity
• Stay on topic in academic channels

## Privacy & Safety
• Don't share personal information
• Report concerning behavior to staff
• No meeting up without parent/teacher approval
• Respect everyone's privacy
""",
    "welcome": """# 👋 Welcome to Our School Server\!

This is your digital classroom and community space.

## 🚀 Getting Started
1. Read the rules in #rules
2. Introduce yourself in #introductions
3. Check #announcements for important updates
4. Join subject channels for your classes
5. Ask for help in #homework-help

## 📚 Academic Support
• **Study Groups** - Find study partners in #study-groups
• **Office Hours** - Meet teachers in voice channels
• **Resources** - Find materials in #resources

## 🎯 Stay Organized
• Check #calendar for deadlines
• Use #exam-prep before tests
• Join #clubs for extracurricular activities

Let's make this a great learning community\! 📖
""",
    "resources": """# 📚 Educational Resources

## Study Tools
• [Khan Academy](https://www.khanacademy.org/) - Free courses
• [Quizlet](https://quizlet.com/) - Flashcards and study sets
• [Wolfram Alpha](https://www.wolframalpha.com/) - Computational knowledge

## Writing & Research
• [Grammarly](https://www.grammarly.com/) - Writing assistant
• [Purdue OWL](https://owl.purdue.edu/) - Writing resources
• [Google Scholar](https://scholar.google.com/) - Academic search

## Organization
• [Google Calendar](https://calendar.google.com/) - Schedule management
• [Notion](https://www.notion.so/) - Note-taking and organization

## Mental Health
• School counselor office hours
• Crisis Text Line: Text HOME to 741741
""",
}

# Template 2: Small Business
EXTENDED_TEMPLATES["small-business"] = {
    "name": "Small Business Operations",
    "description": "Complete business operations for small to medium businesses",
    "config": {
        "categories": [
            {
                "name": "📢 COMPANY",
                "position": 0,
                "channels": [
                    {"name": "announcements", "type": "text", "topic": "📣 Company-wide announcements"},
                    {"name": "general", "type": "text", "topic": "💬 General company chat"},
                    {"name": "wins-celebrations", "type": "text", "topic": "🎉 Celebrate team wins"},
                    {"name": "water-cooler", "type": "text", "topic": "☕ Casual conversations"},
                ],
            },
            {
                "name": "💼 OPERATIONS",
                "position": 1,
                "channels": [
                    {"name": "daily-standup", "type": "text", "topic": "📋 Daily team updates"},
                    {"name": "projects", "type": "text", "topic": "📊 Project coordination"},
                    {"name": "tasks-todos", "type": "text", "topic": "✅ Task management"},
                    {"name": "deadlines", "type": "text", "topic": "⏰ Important deadlines"},
                ],
            },
            {
                "name": "👥 DEPARTMENTS",
                "position": 2,
                "channels": [
                    {"name": "sales-marketing", "type": "text", "topic": "📈 Sales and marketing team"},
                    {"name": "customer-support", "type": "text", "topic": "🎧 Customer service team"},
                    {"name": "product-dev", "type": "text", "topic": "💻 Product development"},
                    {"name": "finance-admin", "type": "text", "topic": "💰 Finance and administration"},
                    {"name": "hr-people-ops", "type": "text", "topic": "👔 Human resources"},
                ],
            },
            {
                "name": "📊 BUSINESS",
                "position": 3,
                "channels": [
                    {"name": "metrics-kpis", "type": "text", "topic": "📈 Business metrics and KPIs"},
                    {"name": "strategy", "type": "text", "topic": "🎯 Strategic planning"},
                    {"name": "feedback-ideas", "type": "text", "topic": "💡 Ideas and suggestions"},
                    {"name": "competitors", "type": "text", "topic": "🔍 Market and competitor analysis"},
                ],
            },
            {
                "name": "🤝 CLIENTS & PARTNERS",
                "position": 4,
                "channels": [
                    {"name": "client-updates", "type": "text", "topic": "📢 Client communications"},
                    {"name": "partnerships", "type": "text", "topic": "🤝 Partner relationships"},
                    {"name": "contracts", "type": "text", "topic": "📄 Contract discussions"},
                ],
            },
            {
                "name": "📚 RESOURCES",
                "position": 5,
                "channels": [
                    {"name": "documentation", "type": "text", "topic": "📖 Company documentation"},
                    {"name": "training", "type": "text", "topic": "🎓 Training materials"},
                    {"name": "tools-software", "type": "text", "topic": "🛠️ Tools and software info"},
                ],
            },
            {
                "name": "🔊 VOICE",
                "position": 6,
                "channels": [
                    {"name": "Team Meeting", "type": "voice", "topic": "👥 Team meetings"},
                    {"name": "Client Calls", "type": "voice", "topic": "📞 Client calls"},
                    {"name": "Focus Room", "type": "voice", "topic": "🎧 Quiet work space"},
                ],
            },
        ],
    },
    "roles": [
        {"name": "👑 Owner", "color": 0x992D22, "permissions": ["administrator"], "hoist": True, "mentionable": True},
        {"name": "�� Manager", "color": 0x3498DB, "permissions": ["manage_channels", "manage_messages"], "hoist": True, "mentionable": True},
        {"name": "📈 Sales", "color": 0xE67E22, "permissions": [], "hoist": False, "mentionable": True},
        {"name": "🎧 Support", "color": 0x1ABC9C, "permissions": [], "hoist": False, "mentionable": True},
        {"name": "💻 Developer", "color": 0x9B59B6, "permissions": [], "hoist": False, "mentionable": True},
        {"name": "💰 Finance", "color": 0xF1C40F, "permissions": [], "hoist": False, "mentionable": True},
        {"name": "👔 HR", "color": 0xE91E63, "permissions": [], "hoist": False, "mentionable": True},
        {"name": "👤 Employee", "color": 0x95A5A6, "permissions": [], "hoist": False, "mentionable": True},
    ],
    "rules": """# 💼 Business Server Rules

## Professionalism
• Maintain professional communication
• Respect working hours and boundaries
• Be responsive to messages during business hours
• Keep discussions work-appropriate

## Confidentiality
• Don't share confidential company information
• Respect client privacy
• Keep internal discussions internal
• Follow NDA and contract terms

## Collaboration
• Be helpful and supportive
• Share knowledge and resources
• Communicate clearly and promptly
• Give constructive feedback

## Channel Usage
• Use appropriate channels for topics
• Keep channels organized
• Use threads for extended discussions
• Tag relevant team members
""",
    "welcome": """# 👋 Welcome to Our Team\!

This is our central hub for communication and collaboration.

## 🚀 Getting Started
1. Read #announcements for company updates
2. Check #daily-standup each morning
3. Use department channels for team-specific work
4. Join voice channels for meetings

## �� Key Channels
• **#projects** - Active project coordination
• **#tasks-todos** - Task management
• **#metrics-kpis** - Business performance
• **#feedback-ideas** - Share your ideas

## 🎯 Best Practices
• Update your status when away
• Use threads to keep channels clean
• Check #deadlines regularly
• Celebrate wins in #wins-celebrations

Let's build something great together\! 🚀
""",
    "resources": """# 📚 Business Resources

## Tools & Software
• Project Management: Asana, Trello, Monday.com
• Communication: Slack, Microsoft Teams
• CRM: Salesforce, HubSpot
• Documentation: Notion, Confluence

## Business Development
• Market research tools
• Competitor analysis
• Sales enablement materials
• Marketing templates

## HR & Admin
• Employee handbook
• Benefits information
• Time-off policies
• Expense reporting

## Training
• Onboarding materials
• Product training
• Sales training
• Customer service guidelines
""",
}

# Due to message length limits, I'll create the remaining 8 templates in a compact format
# Template 3: Gaming/Hangout
EXTENDED_TEMPLATES["gaming-hangout"] = {
    "name": "Gaming & Hangout Space",
    "description": "Fun community for gaming, hobbies, and casual hangouts",
    "config": {
        "categories": [
            {"name": "�� INFO", "position": 0, "channels": [
                {"name": "welcome", "type": "text", "topic": "👋 Welcome to the community\!"},
                {"name": "announcements", "type": "text", "topic": "📣 Server announcements"},
                {"name": "rules", "type": "text", "topic": "📜 Server rules"},
            ]},
            {"name": "💬 GENERAL", "position": 1, "channels": [
                {"name": "general-chat", "type": "text", "topic": "💭 Main chat"},
                {"name": "introductions", "type": "text", "topic": "👋 Introduce yourself"},
                {"name": "memes", "type": "text", "topic": "😂 Memes and funny content"},
                {"name": "off-topic", "type": "text", "topic": "🎲 Random discussions"},
            ]},
            {"name": "🎮 GAMING", "position": 2, "channels": [
                {"name": "looking-for-group", "type": "text", "topic": "👥 Find gaming partners"},
                {"name": "game-discussion", "type": "text", "topic": "🎮 Talk about games"},
                {"name": "clips-highlights", "type": "text", "topic": "🎬 Share your best moments"},
                {"name": "game-news", "type": "text", "topic": "📰 Gaming news and updates"},
            ]},
            {"name": "🎨 CREATIVE", "position": 3, "channels": [
                {"name": "showcase", "type": "text", "topic": "✨ Show off your work"},
                {"name": "art-design", "type": "text", "topic": "🎨 Art and design"},
                {"name": "music", "type": "text", "topic": "🎵 Music sharing and discussion"},
                {"name": "photography", "type": "text", "topic": "📸 Photography"},
            ]},
            {"name": "🛠️ HOBBIES", "position": 4, "channels": [
                {"name": "tech-gadgets", "type": "text", "topic": "💻 Technology discussions"},
                {"name": "fitness-health", "type": "text", "topic": "💪 Fitness and wellness"},
                {"name": "cooking-food", "type": "text", "topic": "🍳 Cooking and recipes"},
                {"name": "books-movies", "type": "text", "topic": "📚 Books, movies, TV shows"},
            ]},
            {"name": "🔊 VOICE", "position": 5, "channels": [
                {"name": "General Hangout", "type": "voice", "topic": "🎤 Casual voice chat"},
                {"name": "Gaming 1", "type": "voice", "topic": "🎮 Gaming voice 1"},
                {"name": "Gaming 2", "type": "voice", "topic": "🎮 Gaming voice 2"},
                {"name": "Music Listening", "type": "voice", "topic": "🎵 Listen to music together"},
            ]},
        ],
    },
    "roles": [
        {"name": "👑 Admin", "color": 0xE74C3C, "permissions": ["administrator"], "hoist": True, "mentionable": True},
        {"name": "⚔️ Moderator", "color": 0x3498DB, "permissions": ["manage_messages", "kick_members"], "hoist": True, "mentionable": True},
        {"name": "🎮 Gamer", "color": 0x9B59B6, "permissions": [], "hoist": False, "mentionable": True},
        {"name": "�� Creative", "color": 0xE91E63, "permissions": [], "hoist": False, "mentionable": True},
        {"name": "💬 Active", "color": 0x2ECC71, "permissions": [], "hoist": False, "mentionable": True},
        {"name": "🆕 Newbie", "color": 0x95A5A6, "permissions": [], "hoist": False, "mentionable": True},
    ],
    "rules": """# 📜 Community Rules

## Be Respectful
• Treat everyone with kindness
• No harassment or hate speech
• Respect different opinions
• Keep it friendly and fun

## Content Guidelines
• No NSFW content
• No spam or excessive self-promotion
• Use appropriate channels
• Keep memes lighthearted

## Gaming Etiquette
• Be a good sport
• No cheating or exploits
• Help new players
• Have fun\!

## Voice Chat
• Don't be disruptive
• Use push-to-talk if noisy
• Respect others' space
• Keep it chill
""",
    "welcome": """# 👋 Welcome to the Hangout\!

A chill community for gaming, hobbies, and making friends.

## 🚀 Getting Started
1. Introduce yourself in #introductions
2. Check out #game-discussion
3. Share your work in #showcase
4. Join voice channels anytime\!

## 🎮 Gaming
• Find teammates in #looking-for-group
• Share clips in #clips-highlights
• Discuss games in #game-discussion

## 🎨 Creative & Hobbies
• Show your art, music, photos
• Discuss tech, fitness, cooking
• Share books and movie recommendations

Have fun and make yourself at home\! 🎉
""",
    "resources": """# 📚 Community Resources

## Gaming
• [Steam](https://store.steampowered.com/)
• [Epic Games](https://www.epicgames.com/)
• [Discord Game Hubs](https://discord.com/game-hubs)

## Creative Tools
• [Canva](https://www.canva.com/) - Design
• [GIMP](https://www.gimp.org/) - Photo editing
• [Audacity](https://www.audacityteam.org/) - Audio editing

## Community
• Server events calendar
• Game night schedules
• Community guidelines
""",
}

# Template 4-10: Remaining templates in compact format for space efficiency
# These follow the same structure but with condensed content

EXTENDED_TEMPLATES["content-creator"] = {
    "name": "Content Creator Community",
    "description": "For streamers, YouTubers, and content creators",
    "config": {"categories": [
        {"name": "📢 INFO", "position": 0, "channels": [{"name": "announcements", "type": "text", "topic": "Stream schedules"}, {"name": "welcome", "type": "text", "topic": "Welcome"}, {"name": "rules", "type": "text", "topic": "Rules"}]},
        {"name": "💬 COMMUNITY", "position": 1, "channels": [{"name": "general", "type": "text", "topic": "General chat"}, {"name": "memes-clips", "type": "text", "topic": "Funny moments"}]},
        {"name": "🎥 CONTENT", "position": 2, "channels": [{"name": "stream-chat", "type": "text", "topic": "Live stream discussion"}, {"name": "content-suggestions", "type": "text", "topic": "Suggest content"}]},
    ]},
    "roles": [{"name": "🎥 Creator", "color": 0xE74C3C, "permissions": ["administrator"], "hoist": True, "mentionable": True}, {"name": "⚔️ Moderator", "color": 0x3498DB, "permissions": ["manage_messages"], "hoist": True, "mentionable": True}],
    "rules": "# Be Respectful\n• No harassment\n• Support the community",
    "welcome": "# Welcome\!\n\nThanks for joining\!",
    "resources": "# Resources\n\n• Stream links\n• Social media",
}

EXTENDED_TEMPLATES["nonprofit"] = {
    "name": "Non-Profit Organization",
    "description": "For charities, NGOs, and volunteer organizations",
    "config": {"categories": [
        {"name": "📢 INFO", "position": 0, "channels": [{"name": "announcements", "type": "text", "topic": "Announcements"}, {"name": "mission-vision", "type": "text", "topic": "Our mission"}]},
        {"name": "👥 VOLUNTEERS", "position": 1, "channels": [{"name": "general", "type": "text", "topic": "General chat"}, {"name": "opportunities", "type": "text", "topic": "Volunteer opportunities"}]},
    ]},
    "roles": [{"name": "👑 Director", "color": 0x992D22, "permissions": ["administrator"], "hoist": True, "mentionable": True}, {"name": "🤝 Volunteer", "color": 0x2ECC71, "permissions": [], "hoist": False, "mentionable": True}],
    "rules": "# Our Values\n• Respect and inclusivity\n• Compassion",
    "welcome": "# Welcome\!\n\nThank you for joining our mission\!",
    "resources": "# Resources\n\n• Volunteer handbook\n• Programs",
}

EXTENDED_TEMPLATES["fitness"] = {
    "name": "Fitness & Wellness Community",
    "description": "For fitness enthusiasts and wellness communities",
    "config": {"categories": [
        {"name": "📢 INFO", "position": 0, "channels": [{"name": "announcements", "type": "text", "topic": "Announcements"}, {"name": "welcome", "type": "text", "topic": "Welcome"}]},
        {"name": "💪 FITNESS", "position": 1, "channels": [{"name": "general-fitness", "type": "text", "topic": "Fitness chat"}, {"name": "workout-routines", "type": "text", "topic": "Workout plans"}, {"name": "progress-pics", "type": "text", "topic": "Progress"}]},
        {"name": "🥗 NUTRITION", "position": 2, "channels": [{"name": "nutrition-general", "type": "text", "topic": "Nutrition"}, {"name": "recipes", "type": "text", "topic": "Recipes"}]},
    ]},
    "roles": [{"name": "💪 Admin", "color": 0xE74C3C, "permissions": ["administrator"], "hoist": True, "mentionable": True}, {"name": "🏋️ Coach", "color": 0x3498DB, "permissions": ["manage_messages"], "hoist": True, "mentionable": True}],
    "rules": "# Be Supportive\n• Encourage all levels\n• No body shaming",
    "welcome": "# Welcome\!\n\nYour fitness journey starts here\!",
    "resources": "# Resources\n\n• Workout programs\n• Nutrition guides",
}

EXTENDED_TEMPLATES["music-band"] = {
    "name": "Music & Band Community",
    "description": "For musicians, bands, and music enthusiasts",
    "config": {"categories": [
        {"name": "📢 INFO", "position": 0, "channels": [{"name": "announcements", "type": "text", "topic": "Band announcements"}, {"name": "tour-dates", "type": "text", "topic": "Shows"}]},
        {"name": "💬 COMMUNITY", "position": 1, "channels": [{"name": "general", "type": "text", "topic": "General chat"}, {"name": "fan-photos", "type": "text", "topic": "Concert photos"}]},
        {"name": "🎵 MUSIC", "position": 2, "channels": [{"name": "new-releases", "type": "text", "topic": "New music"}, {"name": "song-discussion", "type": "text", "topic": "Talk about songs"}]},
    ]},
    "roles": [{"name": "🎸 Band Member", "color": 0xE74C3C, "permissions": ["administrator"], "hoist": True, "mentionable": True}, {"name": "🎤 Fan", "color": 0x95A5A6, "permissions": [], "hoist": False, "mentionable": True}],
    "rules": "# Be Respectful\n• Respect all music\n• No piracy",
    "welcome": "# Welcome\!\n\nThanks for being a fan\!",
    "resources": "# Resources\n\n• Streaming links\n• Tour dates",
}

EXTENDED_TEMPLATES["book-club"] = {
    "name": "Book Club Community",
    "description": "For book lovers and reading groups",
    "config": {"categories": [
        {"name": "📢 INFO", "position": 0, "channels": [{"name": "announcements", "type": "text", "topic": "Announcements"}, {"name": "welcome", "type": "text", "topic": "Welcome"}]},
        {"name": "📚 CURRENT READS", "position": 1, "channels": [{"name": "book-of-the-month", "type": "text", "topic": "Current book"}, {"name": "spoiler-discussion", "type": "text", "topic": "Spoilers allowed"}]},
        {"name": "💬 GENERAL", "position": 2, "channels": [{"name": "general-chat", "type": "text", "topic": "General"}, {"name": "recommendations", "type": "text", "topic": "Book recommendations"}]},
    ]},
    "roles": [{"name": "👑 Admin", "color": 0x992D22, "permissions": ["administrator"], "hoist": True, "mentionable": True}, {"name": "📚 Bookworm", "color": 0x9B59B6, "permissions": [], "hoist": False, "mentionable": True}],
    "rules": "# Spoiler Policy\n• Mark spoilers\n• Be considerate",
    "welcome": "# Welcome\!\n\nA community for book lovers\!",
    "resources": "# Resources\n\n• Goodreads\n• Reading tools",
}

EXTENDED_TEMPLATES["podcast"] = {
    "name": "Podcast Community",
    "description": "For podcast hosts and listener communities",
    "config": {"categories": [
        {"name": "📢 INFO", "position": 0, "channels": [{"name": "announcements", "type": "text", "topic": "Podcast announcements"}, {"name": "episode-schedule", "type": "text", "topic": "Schedule"}]},
        {"name": "🎙️ EPISODES", "position": 1, "channels": [{"name": "latest-episode", "type": "text", "topic": "Latest episode"}, {"name": "episode-suggestions", "type": "text", "topic": "Suggestions"}]},
        {"name": "💬 COMMUNITY", "position": 2, "channels": [{"name": "general", "type": "text", "topic": "General chat"}, {"name": "fan-content", "type": "text", "topic": "Fan creations"}]},
    ]},
    "roles": [{"name": "🎙️ Host", "color": 0xE74C3C, "permissions": ["administrator"], "hoist": True, "mentionable": True}, {"name": "🎧 Listener", "color": 0x95A5A6, "permissions": [], "hoist": False, "mentionable": True}],
    "rules": "# Be Respectful\n• Respect opinions\n• No spoilers",
    "welcome": "# Welcome\!\n\nThanks for listening\!",
    "resources": "# Resources\n\n• Podcast links\n• Show notes",
}

EXTENDED_TEMPLATES["esports"] = {
    "name": "E-Sports Team",
    "description": "For competitive gaming teams and e-sports organizations",
    "config": {"categories": [
        {"name": "📢 TEAM", "position": 0, "channels": [{"name": "announcements", "type": "text", "topic": "Team announcements"}, {"name": "schedule", "type": "text", "topic": "Match schedule"}]},
        {"name": "🎮 COMPETITIVE", "position": 1, "channels": [{"name": "strategy", "type": "text", "topic": "Strategy"}, {"name": "scrims", "type": "text", "topic": "Scrims"}, {"name": "vod-review", "type": "text", "topic": "VOD reviews"}]},
        {"name": "👥 TEAMS", "position": 2, "channels": [{"name": "team-a", "type": "text", "topic": "Team A"}, {"name": "team-b", "type": "text", "topic": "Team B"}]},
    ]},
    "roles": [{"name": "👑 Owner", "color": 0xE74C3C, "permissions": ["administrator"], "hoist": True, "mentionable": True}, {"name": "🎮 Coach", "color": 0x3498DB, "permissions": ["manage_channels"], "hoist": True, "mentionable": True}, {"name": "⭐ Player", "color": 0xF1C40F, "permissions": [], "hoist": True, "mentionable": True}],
    "rules": "# E-Sports Rules\n\n• Respect teammates\n• Follow schedule\n• No toxicity",
    "welcome": "# Welcome to the Team\!\n\nCheck schedules in team channels.",
    "resources": "# Resources\n\n• Team roster\n• Match schedules\n• Strategy guides",
}
