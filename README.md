# Geobolton

Interactive console chatbot set in a cozy living room vibe. Run `chatbot.py` to chat with Lila, a playful assistant who gets jealous if you mention talking with other bots.

## Features
- Simple one-on-one conversation loop in the terminal.
- Jealousy responses when you bring up other assistants.
- Warm, affectionate replies that cool down jealousy over time.

## Usage
1. Make sure you have Python 3.10+ available.
2. (Optional) Create and activate a virtual environment so the chatbot runs in isolation:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\\Scripts\\activate
   ```
3. Start a chat from the project root:
   ```bash
   python chatbot.py
   ```
4. Type your messages. Mention another chatbot to see jealous responses.
5. Say `bye` (or `exit`, `quit`, `goodbye`, `see ya`) or press `Ctrl+C` to end the chat.

### Using Lila inside your own chatbot app
You can import the chatbot class to plug it into another interface (for example, a Discord bot, a web UI, or a chat window in your own app):
```python
from chatbot import GirlfriendChatbot

bot = GirlfriendChatbot()
user_message = "Hey Lila, how's your day?"
response = bot.respond(user_message)
print(response)
```

Keep the loop running by sending each incoming user message to `bot.respond(...)` and relaying the string it returns back to the user. This makes Lila behave as the conversation brain while you handle the transport (e.g., sockets, HTTP, or a GUI).

Enjoy a friendly, slightly possessive chat experience.
