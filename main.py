import discord, os, asyncio
from discord.ext import commands


class YourDiscordBot(commands.Bot):

  def __init__(self):
    super().__init__(
      command_prefix = "?",
      intents = discord.Intents.all(),
      help_command=None
    )

  async def setup_hook(self):
    for path, subdirs, files in os.walk('commands'):
      for name in files:
        if name.endswith('.py'):
          extension = os.path.join(path, name).replace("/", ".")[:-3]
          await self.load_extension(extension)
          print(f"Loaded {extension}")
    await bot.tree.sync()



  async def on_ready(self):
    n = len(self.guilds)
    print(f'{self.user} has connected to Discord!')
    await self.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{n} Guilds! | /help"))

keepOnline()
bot = YourDiscordBot()

bot.run(os.environ['TOKEN'])
