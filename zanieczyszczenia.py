import discord
from discord.ext import commands
import random
import os

# Intencje
intents = discord.Intents.default()
intents.message_content = True

# Tworzenie bota
bot = commands.Bot(command_prefix="$", intents=intents)

# Event: gotowy
@bot.event
async def on_ready():
    print(f"Zalogowaliśmy się jako {bot.user}")

# Komenda: hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"Cześć, jestem bot {bot.user}!")

# Komenda: mem (losowy obraz z folderu)
@bot.command()
async def mem(ctx):
    folder = "images"
    if not os.path.exists(folder):
        await ctx.send("Folder 'images' nie istnieje")
        return

    pliki = os.listdir(folder)
    if not pliki:
        await ctx.send("Brak memów w folderze")
        return

    wybrany_plik = random.choice(pliki)
    sciezka = os.path.join(folder, wybrany_plik)
    with open(sciezka, "rb") as f:
        picture = discord.File(f)
    await ctx.send("Oto memik:", file=picture)

# Komenda: porada
@bot.command()
async def porada(ctx):
    porady = [
        "Nie wyrzucaj plastikowych butelek do zwykłego kosza — wrzucaj je do żółtego pojemnika!",
        "Papier z resztkami jedzenia nie nadaje się do recyklingu.",
        "Oddziel kapsel od butelki — recykling wtedy działa lepiej!",
        "Szkło wrzucaj do zielonego pojemnika, ale lustra i ceramiki nie!",
        "Nie musisz myć opakowań idealnie — wystarczy, że są puste i niezabrudzone resztkami.",
        "Baterie i elektronikę oddawaj do specjalnych punktów — nie do kosza!",
    ]
    losowa = random.choice(porady)
    await ctx.send(f"♻️ Porada recyklingowa:\n**{losowa}**")


bot.run("")
