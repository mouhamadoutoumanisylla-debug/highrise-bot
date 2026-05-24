import asyncio
from highrise import BaseBot
from highrise.__main__ import main, BotDefinition

class MonBot(BaseBot):
    async def on_chat(self, user: str, message: str) -> None:
        if message.lower().startswith("!bonjour"):
            await self.highrise.chat(f"Salut {user} ! 👋")

    async def on_ready(self):
        print("✅ Bot connecté, prêt à discuter !")

if __name__ == "__main__":
    token = "4e50979bb64929809417aac5c96f935375e0b4d4b3f41a2f235a18ea099c17b9"
    room_id = "64bd5ad90a55ecdc8bbdba06"

    # Créer le bot
    bot = MonBot()

    # Créer la définition avec les bons noms de paramètres
    definition = BotDefinition(
        bot=bot,
        room_id=room_id,
        api_token=token
    )

    # Lancer le bot
    asyncio.run(main([definition]))