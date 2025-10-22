"""
Discord AI Server Configuration
Defines the complete server structure including categories, channels, and roles
"""

# Server structure configuration
SERVER_CONFIG = {
    "categories": [
        {
            "name": "📢 WELCOME & INFO",
            "position": 0,
            "channels": [
                {
                    "name": "welcome",
                    "type": "text",
                    "topic": "👋 Welcome to the AI Development community! Check out #rules and #resources to get started.",
                },
                {
                    "name": "rules",
                    "type": "text",
                    "topic": "📜 Server rules and guidelines - please read before participating",
                },
                {
                    "name": "announcements",
                    "type": "text",
                    "topic": "📣 Important server updates and announcements",
                },
                {
                    "name": "resources",
                    "type": "text",
                    "topic": "📚 Curated AI learning resources, papers, tools, and useful links",
                },
                {
                    "name": "roles",
                    "type": "text",
                    "topic": "🎭 Self-assign roles for your interests and expertise",
                },
            ],
        },
        {
            "name": "💬 GENERAL",
            "position": 1,
            "channels": [
                {
                    "name": "general",
                    "type": "text",
                    "topic": "💭 Main chat for casual AI discussions and general conversation",
                },
                {
                    "name": "introductions",
                    "type": "text",
                    "topic": "👋 Introduce yourself! Tell us about your AI interests and background",
                },
                {
                    "name": "off-topic",
                    "type": "text",
                    "topic": "🎮 Non-AI discussions, memes, and random chat",
                },
                {
                    "name": "showcase",
                    "type": "text",
                    "topic": "✨ Share your AI projects, achievements, and cool things you've built",
                },
            ],
        },
        {
            "name": "🤖 AI DISCUSSION",
            "position": 2,
            "channels": [
                {
                    "name": "ai-news",
                    "type": "text",
                    "topic": "📰 Latest AI developments, breakthroughs, and industry news",
                },
                {
                    "name": "research-papers",
                    "type": "text",
                    "topic": "📄 Discuss recent papers, research findings, and academic work",
                },
                {
                    "name": "ethics-safety",
                    "type": "text",
                    "topic": "⚖️ AI ethics, alignment, safety, and societal implications",
                },
                {
                    "name": "industry-trends",
                    "type": "text",
                    "topic": "💼 Commercial AI applications, startups, and business discussions",
                },
                {
                    "name": "hot-takes",
                    "type": "text",
                    "topic": "🔥 Controversial opinions and spicy AI debates - keep it respectful!",
                },
            ],
        },
        {
            "name": "🛠️ DEVELOPMENT",
            "position": 3,
            "channels": [
                {
                    "name": "general-dev",
                    "type": "text",
                    "topic": "💻 General AI development questions and discussions",
                },
                {
                    "name": "llm-development",
                    "type": "text",
                    "topic": "🧠 LLMs, transformers, fine-tuning, and language model development",
                },
                {
                    "name": "ml-engineering",
                    "type": "text",
                    "topic": "📊 Traditional ML, data science, model training and optimization",
                },
                {
                    "name": "computer-vision",
                    "type": "text",
                    "topic": "👁️ Computer vision, image generation, video AI, and visual models",
                },
                {
                    "name": "agents-automation",
                    "type": "text",
                    "topic": "🤖 AI agents, workflows, automation, and autonomous systems",
                },
                {
                    "name": "code-review",
                    "type": "text",
                    "topic": "🔍 Get feedback on your AI code and implementations",
                },
                {
                    "name": "debugging-help",
                    "type": "text",
                    "topic": "🐛 Troubleshooting assistance for AI development issues",
                },
            ],
        },
        {
            "name": "🔧 TOOLS & FRAMEWORKS",
            "position": 4,
            "channels": [
                {
                    "name": "openai-api",
                    "type": "text",
                    "topic": "🟢 ChatGPT, GPT-4, OpenAI API discussions and implementations",
                },
                {
                    "name": "anthropic-claude",
                    "type": "text",
                    "topic": "🟣 Claude, Anthropic tools, and API discussions",
                },
                {
                    "name": "local-models",
                    "type": "text",
                    "topic": "🏠 Ollama, LM Studio, local inference, and self-hosted models",
                },
                {
                    "name": "langchain-llamaindex",
                    "type": "text",
                    "topic": "🔗 LangChain, LlamaIndex, and AI framework discussions",
                },
                {
                    "name": "vector-databases",
                    "type": "text",
                    "topic": "🗄️ RAG, embeddings, vector databases, and semantic search",
                },
                {
                    "name": "devops-mlops",
                    "type": "text",
                    "topic": "⚙️ Deployment, scaling, infrastructure, and ML operations",
                },
            ],
        },
        {
            "name": "🎨 CREATIVE AI",
            "position": 5,
            "channels": [
                {
                    "name": "image-generation",
                    "type": "text",
                    "topic": "🖼️ Stable Diffusion, DALL-E, Midjourney, and image AI",
                },
                {
                    "name": "video-audio",
                    "type": "text",
                    "topic": "🎬 AI video and audio generation tools and techniques",
                },
                {
                    "name": "prompt-engineering",
                    "type": "text",
                    "topic": "✍️ Prompt techniques, sharing, and optimization strategies",
                },
                {
                    "name": "creative-showcase",
                    "type": "text",
                    "topic": "🎨 Share your AI-generated art, music, and creative projects",
                },
            ],
        },
        {
            "name": "🎓 LEARNING",
            "position": 6,
            "channels": [
                {
                    "name": "beginner-questions",
                    "type": "text",
                    "topic": "🌱 No question too basic! Ask anything about AI and ML",
                },
                {
                    "name": "tutorials-guides",
                    "type": "text",
                    "topic": "📖 Share and request tutorials, guides, and learning resources",
                },
                {
                    "name": "study-group",
                    "type": "text",
                    "topic": "👥 Organize learning sessions and study together",
                },
                {
                    "name": "paper-reading-club",
                    "type": "text",
                    "topic": "📚 Weekly paper discussions and reading group",
                },
                {
                    "name": "project-ideas",
                    "type": "text",
                    "topic": "💡 Brainstorm project ideas and find collaborators",
                },
            ],
        },
        {
            "name": "🎮 COMMUNITY",
            "position": 7,
            "channels": [
                {
                    "name": "hackathons-events",
                    "type": "text",
                    "topic": "🏆 Organize and share hackathons, competitions, and events",
                },
                {
                    "name": "job-opportunities",
                    "type": "text",
                    "topic": "💼 AI jobs, freelance work, and career opportunities",
                },
                {
                    "name": "collaboration",
                    "type": "text",
                    "topic": "🤝 Find project partners and collaborate on AI projects",
                },
                {
                    "name": "feedback-suggestions",
                    "type": "text",
                    "topic": "💬 Server improvement ideas and community feedback",
                },
            ],
        },
        {
            "name": "🔊 VOICE CHANNELS",
            "position": 8,
            "channels": [
                {
                    "name": "General Hangout",
                    "type": "voice",
                    "topic": "🎤 Casual voice chat and discussions",
                },
                {
                    "name": "Deep Dive Sessions",
                    "type": "voice",
                    "topic": "🧠 Focused technical discussions and deep dives",
                },
                {
                    "name": "Pair Programming",
                    "type": "voice",
                    "topic": "👨‍💻 Code together and collaborate in real-time",
                },
                {
                    "name": "Study Hall",
                    "type": "voice",
                    "topic": "📚 Work together silently - accountability sessions",
                },
                {
                    "name": "AI Demo Room",
                    "type": "voice",
                    "topic": "🎬 Live project demonstrations and showcases",
                },
            ],
        },
    ],
}

# Role configuration
ROLES_CONFIG = [
    # Administrative roles (created but not auto-assigned)
    {
        "name": "🛡️ Admin",
        "color": 0xE74C3C,  # Red
        "permissions": ["administrator"],
        "hoist": True,
        "mentionable": False,
    },
    {
        "name": "⚔️ Moderator",
        "color": 0x3498DB,  # Blue
        "permissions": ["manage_messages", "kick_members", "ban_members", "manage_channels"],
        "hoist": True,
        "mentionable": True,
    },
    # Expertise roles (self-assignable)
    {
        "name": "🧠 ML Researcher",
        "color": 0x9B59B6,  # Purple
        "permissions": [],
        "hoist": False,
        "mentionable": True,
    },
    {
        "name": "💻 ML Engineer",
        "color": 0x1ABC9C,  # Teal
        "permissions": [],
        "hoist": False,
        "mentionable": True,
    },
    {
        "name": "🎨 Creative AI",
        "color": 0xE91E63,  # Pink
        "permissions": [],
        "hoist": False,
        "mentionable": True,
    },
    {
        "name": "🤖 Agent Builder",
        "color": 0x00BCD4,  # Cyan
        "permissions": [],
        "hoist": False,
        "mentionable": True,
    },
    {
        "name": "📊 Data Scientist",
        "color": 0xFF9800,  # Orange
        "permissions": [],
        "hoist": False,
        "mentionable": True,
    },
    {
        "name": "🔰 Learning",
        "color": 0x4CAF50,  # Green
        "permissions": [],
        "hoist": False,
        "mentionable": True,
    },
    # Interest roles (self-assignable)
    {
        "name": "📰 News Ping",
        "color": 0x607D8B,  # Blue Grey
        "permissions": [],
        "hoist": False,
        "mentionable": True,
    },
    {
        "name": "📄 Paper Club",
        "color": 0x795548,  # Brown
        "permissions": [],
        "hoist": False,
        "mentionable": True,
    },
    {
        "name": "🎯 Hackathon",
        "color": 0xF44336,  # Red
        "permissions": [],
        "hoist": False,
        "mentionable": True,
    },
    {
        "name": "💼 Job Alerts",
        "color": 0x009688,  # Teal
        "permissions": [],
        "hoist": False,
        "mentionable": True,
    },
]

# Server rules content
RULES_CONTENT = """
# 📜 Server Rules

Welcome to our AI Development community! Please read and follow these rules to keep our server a great place for everyone.

## Rule 1: Be Respectful 🤝
• Treat everyone with respect and kindness
• No harassment, hate speech, or discrimination
• Disagree with ideas, not people
• Keep discussions constructive

## Rule 2: Stay On Topic 🎯
• Use appropriate channels for discussions
• Keep off-topic chat in #off-topic
• Don't spam or flood channels
• No excessive self-promotion

## Rule 3: Quality Over Quantity 💎
• Search before asking - your question may be answered
• Provide context when asking for help (code, error messages, what you've tried)
• Share quality resources, not clickbait
• Use threads for extended discussions

## Rule 4: No Illegal or Harmful Content 🚫
• No piracy, leaked content, or copyright violations
• No malicious code or harmful AI applications
• No sharing of API keys or credentials
• Respect terms of service for AI platforms

## Rule 5: Respect Privacy 🔒
• Don't share others' personal information
• Don't DM members without permission
• Keep private conversations private
• Use spoiler tags for sensitive content

## Rule 6: AI Ethics ⚖️
• Consider ethical implications of AI projects
• Don't create or share harmful AI applications
• Respect content policies of AI platforms
• Discuss controversial topics respectfully in #ethics-safety

## Rule 7: Give Credit 🏆
• Cite sources for research and code
• Credit original creators
• Don't plagiarize or claim others' work
• Share knowledge freely but acknowledge origins

## Rule 8: Help the Community 💪
• Answer questions when you can
• Share your knowledge and experience
• Welcome newcomers
• Report rule violations to moderators

---

**Questions?** Ask in #feedback-suggestions
**Report Issues:** DM a moderator or admin
"""

# Welcome message content
WELCOME_CONTENT = """
# 👋 Welcome to the AI Development Community!

We're excited to have you here! This server is dedicated to AI enthusiasts, developers, researchers, and anyone passionate about artificial intelligence.

## 🚀 Getting Started

1. **Read the Rules** - Check out <#rules> to understand our community guidelines
2. **Introduce Yourself** - Head to <#introductions> and tell us about yourself!
3. **Assign Roles** - Visit <#roles> to select roles that match your interests
4. **Explore Resources** - Check <#resources> for curated learning materials
5. **Join Discussions** - Jump into any channel that interests you!

## 📚 Channel Guide

• **💬 GENERAL** - Casual chat and introductions
• **🤖 AI DISCUSSION** - News, research, ethics, and trends
• **🛠️ DEVELOPMENT** - Technical discussions and help
• **🔧 TOOLS & FRAMEWORKS** - Specific platforms and tools
• **🎨 CREATIVE AI** - Generative AI and creative projects
• **🎓 LEARNING** - Resources and study groups
• **🎮 COMMUNITY** - Events, jobs, and collaboration

## 💡 Tips

• Use threads to keep conversations organized
• Search before asking - your question might be answered
• Be helpful and welcoming to newcomers
• Share your projects in <#showcase>!

## 🤝 Community Values

We believe in:
• **Open collaboration** - Share knowledge freely
• **Respectful discourse** - Disagree constructively
• **Continuous learning** - No question is too basic
• **Ethical AI** - Build responsibly

---

**Have questions?** Ask in <#general> or <#feedback-suggestions>
**Need help?** Check <#beginner-questions> or ping a moderator

Let's build amazing things together! 🚀
"""

# Resources content
RESOURCES_CONTENT = """
# 📚 AI Learning Resources

A curated collection of resources for learning AI and ML.

## 🎓 Courses

**Beginner-Friendly:**
• [Fast.ai Practical Deep Learning](https://course.fast.ai/) - Free, practical approach
• [Andrew Ng's Machine Learning](https://www.coursera.org/learn/machine-learning) - Classic introduction
• [Google's Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)

**Advanced:**
• [Stanford CS229: Machine Learning](https://cs229.stanford.edu/)
• [MIT 6.S191: Introduction to Deep Learning](http://introtodeeplearning.com/)
• [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course/)

## 📖 Books

• **"Deep Learning" by Goodfellow, Bengio, Courville** - The bible of deep learning
• **"Hands-On Machine Learning" by Aurélien Géron** - Practical ML with Scikit-Learn and TensorFlow
• **"The Hundred-Page Machine Learning Book" by Andriy Burkov** - Concise overview

## 🛠️ Tools & Frameworks

**LLM Development:**
• [OpenAI API](https://platform.openai.com/docs)
• [Anthropic Claude](https://www.anthropic.com/api)
• [Hugging Face Transformers](https://huggingface.co/docs/transformers)
• [LangChain](https://python.langchain.com/)
• [LlamaIndex](https://www.llamaindex.ai/)

**Local Models:**
• [Ollama](https://ollama.ai/) - Run LLMs locally
• [LM Studio](https://lmstudio.ai/) - Desktop app for local models
• [Text Generation WebUI](https://github.com/oobabooga/text-generation-webui)

**ML Frameworks:**
• [PyTorch](https://pytorch.org/)
• [TensorFlow](https://www.tensorflow.org/)
• [JAX](https://github.com/google/jax)
• [Scikit-learn](https://scikit-learn.org/)

**Vector Databases:**
• [Pinecone](https://www.pinecone.io/)
• [Weaviate](https://weaviate.io/)
• [Chroma](https://www.trychroma.com/)
• [Qdrant](https://qdrant.tech/)

## 📰 Stay Updated

• [Papers with Code](https://paperswithcode.com/) - Latest research with implementations
• [Hugging Face Papers](https://huggingface.co/papers) - Daily AI papers
• [arXiv AI](https://arxiv.org/list/cs.AI/recent) - Research preprints
• [AI News Subreddit](https://www.reddit.com/r/artificial/)

## 🎨 Creative AI Tools

• [Stable Diffusion](https://stability.ai/)
• [Midjourney](https://www.midjourney.com/)
• [DALL-E](https://openai.com/dall-e-3)
• [RunwayML](https://runwayml.com/) - Video AI

## 💻 Practice Platforms

• [Kaggle](https://www.kaggle.com/) - Competitions and datasets
• [Google Colab](https://colab.research.google.com/) - Free GPU notebooks
• [Replicate](https://replicate.com/) - Run models via API

---

**Have a resource to add?** Share it in <#feedback-suggestions>!
"""
