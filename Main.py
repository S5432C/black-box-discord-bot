import discord
import openai
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@client.event
async def on_ready():
    print(f"[ONI // ONLINE] BB is live as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()

    if content.startswith("!status"):
        await message.channel.send("[ONI // STATUS] BB is online and watching. GPT protocol is active.")

    elif content.startswith("!briefing"):
        prompt = message.content.replace("!briefing", "").strip()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Write a tactical Halo-style mission briefing about: {prompt}"}],
            max_tokens=250
        )
        await message.channel.send(f"[ONI // BRIEFING]\n{response['choices'][0]['message']['content']}")

    elif content.startswith("!intel"):
        prompt = message.content.replace("!intel", "").strip()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Answer this like a Halo AI: {prompt}"}],
            max_tokens=200
        )
        await message.channel.send(f"[ONI // INTEL]\n{response['choices'][0]['message']['content']}")

client.run(os.environ.get("DISCORD_TOKEN"))
