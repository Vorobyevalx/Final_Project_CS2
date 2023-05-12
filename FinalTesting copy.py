from dotenv import load_dotenv
import os
import ssl
import certifi
import discord
import googletrans
from googletrans import Translator

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

ssl_context = ssl.create_default_context(cafile=certifi.where())

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(ssl=ssl_context, intents=intents)
translator = Translator()

text_char_limit = 14999

def translate(message, dest):
    translatation = translator.translate(message, dest=dest)
    return translatation.text

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # ensure the bot doesn't talk to itself and loop
    if message.author == client.user:
        return

    if message.content.startswith('!translate'):
        lang = message.content.split()[1]
        lang_to = lang.lower()
        # ensure language is in list
        if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODES:
            await message.channel.send("Language not recognized")
            return
        text = ' '.join(message.content.split()[2:])
        # ensure text is not empty
        if text == '':
            await message.channel.send("Text required in order to translate")
            return
        # ensure text character limit is not exceeded
        if len(text) > text_char_limit:
            await message.channel.send("Text is too long to translate")
            return

        translated_text = translate(text, lang)
        await message.channel.send(translated_text)

if __name__ == "__main__":
    client.run(DISCORD_TOKEN)