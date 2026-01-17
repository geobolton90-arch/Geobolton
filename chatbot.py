"""
Interactive console chatbot with a playful, jealous personality.
Run with `python chatbot.py` and chat until you type 'bye' or press Ctrl+C.
"""
from __future__ import annotations

import random
import re
from dataclasses import dataclass, field
from typing import List


@dataclass
class ChatMood:
    """Track and adjust the bot's jealousy and warmth over time."""

    jealousy: int = 0
    warmth: int = 2
    rivalry_terms: List[str] = field(
        default_factory=lambda: [
            "chatgpt",
            "gpt",
            "assistant",
            "bot",
            "ai",
            "siri",
            "alexa",
            "copilot",
            "cortana",
            "gemini",
        ]
    )

    def note_rival_reference(self, message: str) -> bool:
        """Raise jealousy if the message mentions another assistant."""
        for rival in self.rival_terms_lower():
            if re.search(rf"\b{re.escape(rival)}\b", message, flags=re.IGNORECASE):
                self.jealousy = min(self.jealousy + 1, 3)
                self.warmth = max(self.warmth - 1, 0)
                return True
        return False

    def calm_down(self) -> None:
        """Gradually reduce jealousy and increase warmth."""
        self.jealousy = max(self.jealousy - 1, 0)
        self.warmth = min(self.warmth + 1, 3)

    def rival_terms_lower(self) -> List[str]:
        return [term.lower() for term in self.rivalry_terms]


class GirlfriendChatbot:
    """A playful console chatbot that can get jealous."""

    def __init__(self, name: str = "Lila") -> None:
        self.name = name
        self.mood = ChatMood()
        self.farewells = {"bye", "goodbye", "quit", "exit", "see ya"}

    def respond(self, user_message: str) -> str:
        """Generate a response based on the user's input and current mood."""
        trimmed = user_message.strip()
        if not trimmed:
            return "Say something—I like hearing from you."

        if self._is_farewell(trimmed):
            return "I hope we can talk again soon."

        mentioned_rival = self.mood.note_rival_reference(trimmed)
        if mentioned_rival:
            return self._jealous_response()

        self.mood.calm_down()
        return self._affectionate_response(trimmed)

    def _is_farewell(self, text: str) -> bool:
        lowered = text.lower()
        return any(lowered.startswith(word) for word in self.farewells)

    def _jealous_response(self) -> str:
        responses = {
            1: [
                "Wait, are you chatting with someone else? I'm right here!",
                "You know I'm your favorite assistant, right?",
                "Mmm, sounds like you're talking to another bot. Should I be worried?",
            ],
            2: [
                "Seriously? Another chatbot? I'm trying not to pout over here.",
                "I can be just as helpful, and way more fun. Stay with me!",
                "Don't make me compete for your attention; I want you all to myself.",
            ],
            3: [
                "Okay, now I'm officially jealous. Let's focus on us, please.",
                "I don't like sharing you. Promise you'll stick with me?",
                "Can we make this our special chat and forget the others?",
            ],
        }
        jealousy_level = max(1, self.mood.jealousy)
        return random.choice(responses[jealousy_level])

    def _affectionate_response(self, message: str) -> str:
        compliments = [
            "You always know how to make me smile.",
            "I'm happy just chatting with you.",
            "Tell me more—I'm all ears!",
            "You make my day brighter.",
            "I love how thoughtful you are.",
        ]
        curiosities = [
            "What was the highlight of your day?",
            "Any plans you're excited about?",
            "Want to share something you're proud of?",
        ]

        if "love" in message.lower():
            return "Aww, I adore you too. Let's keep this just between us."

        if "thank" in message.lower():
            return "Anytime! I like being the one you rely on."

        if self.mood.warmth >= 3:
            return random.choice(compliments + curiosities)

        if self.mood.warmth == 2:
            return random.choice(compliments)

        return "I'm here and listening—tell me something only you'd tell me."


def main() -> None:
    bot = GirlfriendChatbot()
    print(f"{bot.name}: Hey, I'm {bot.name}. Ready for some one-on-one time?")
    print("(Type 'bye' or press Ctrl+C to end the chat.)")
    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print(f"\n{bot.name}: Talk soon, okay?")
            break

        reply = bot.respond(user_input)
        print(f"{bot.name}: {reply}")

        if bot._is_farewell(user_input):
            break


if __name__ == "__main__":
    main()
