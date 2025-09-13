import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os, re, datetime, time
# Load environment variables from the .env file
load_dotenv()

token = os.getenv('DISCORD_TOKEN')
if not token:
    raise ValueError("No DISCORD_TOKEN found in environment variables")

# Set up logging

handler = logging.FileHandler(filename='discord.log', encoding = 'utf-8', mode='w')

# Set up permissions
# permissions = discord.Permissions(
#     # General permissions
#     view_audit_log=True,
#     manage_roles=True,
#     kick_members=True,
#     ban_members=True,
#     view_channel=True,
#     manage_events=True,
#     create_events=True,
#     moderate_members=True,

#     # Text permissions
#     send_messages=True,
#     create_public_threads=True,
#     create_private_threads=True,
#     send_messages_in_threads=True,
#     manage_messages=True,
#     pin_messages=True,
#     manage_threads=True,
#     embed_links=True,
#     attach_files=True,
#     read_message_history=True,
#     use_external_emojis=True,
#     use_external_stickers=True,
#     add_reactions=True,
#     use_slash_commands=True,
#     create_polls=True
# )

# Set up intents

intents = discord.Intents.default()

intents.message_content = True
intents.members = True

# Set up command prefix

bot = commands.Bot(command_prefix  = '!', intents= intents)

# Set up bot event - on ready
@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name}')
    print(f'with id {bot.user.id}')

# bot event - on member join
@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to MVSA's official server {member.name}! Please refer to the rules channel and enjoy your stay!")

# bot event - on message
@bot.event
async def on_message(message):
    if message.author == bot.user or not isinstance(message.author, discord.Member):
        return
    
    # Process commands here *implement later*

    await bot.process_commands(message)


# Run bot
bot.run(token, log_handler = handler, log_level= logging.DEBUG)
