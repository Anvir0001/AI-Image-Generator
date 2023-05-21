import discord, time, datetime, openai, asyncio
from discord import app_commands
from discord.ext import commands

class img(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot



  @app_commands.command(
    name = "image",
    description = "Generate an image using Dall-e 2",
  )
  async def image(self, interaction: discord.Interaction, prompt: str):
    query = prompt
    openai.api_key = 'OpenAI_Api Key'
    response = openai.Image.create(
      prompt=query,
      n=1,
      size="1024x1024"
    )
  
    image_url = response['data'][0]['url']
    embed = discord.Embed()
    embed.set_image(url=f'{image_url}')
    m = await interaction.channel.send('Generating image...')
    await m.edit(embed=embed)
  
    await interaction.response.send_message(f'{prompt}')



    
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(img(bot))
