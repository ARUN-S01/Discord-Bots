import os
import random
import requests, json
import google
from googletrans import Translator
import discord
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import datetime
import pyjokes
import asyncio
from discord.ext import commands
from googlesearch import search
import discordgame as dg
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import emoji
import webbrowser



load_dotenv()

TOKEN = os.environ.get('token')

client = discord.Client()
bot = commands.Bot(command_prefix='/')



class MadLib(dg.Game):
    game_name = 'MadLib'

    def __init__(self):
        # Creates a list of blanks
        self.word_blanks = ['(blank)'] * 8
        # Assign a MadLib string to a variable.
        self.lib = 'The {} {}ed across the {} to get to the {} {}. It wanted to get to the {} so it could {} with a {}.'
        # Initialize the Parent Game class with the MadLib specific values.
        super().__init__(self.game_name, [[self.lib.format(*self.word_blanks)]], ctx=ctx, needs_text_input=True)

    # Define events to be triggered on a user's message event.
    async def on_text_event(self, player: discord.User, text: str):
        try:
            next_index = self.word_blanks.index('(blank)')  # Finds the left-most blank in the list.
            self.word_blanks.pop(next_index)  # Pops that blank from the list.
            self.word_blanks.insert(next_index, text)  # Inserts the user's word into the said blank.
            self.stats['Blanks to Fill ->'] = len([word for word in self.word_blanks if word == '(blank)'])
            # ^^ Updates the Blanks to fill Counter.
            await self.update_layout([[self.lib.format(*self.word_blanks)]])  # Sends the changes to discord.
            if '(blank)' not in self.word_blanks:
                self.stop()
                await player.send(self.lib.format(*self.word_blanks))  # Sends the final MadLib to the channel.
        except ValueError:  # If there's no blank in the list.
            self.stop()
            await player.send(self.lib.format(*self.word_blanks))  # Sends the final MadLib to the channel.



def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

def fire(det):
  cred = credentials.Certificate(r'C:\Users\a2r0u\Desktop\MY PROJECTS\firebase234\ml-pro-2d953-firebase-adminsdk-nesq6-bdc0eadca7.json')
  firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://ml-pro-2d953-default-rtdb.firebaseio.com/'
  })
  
  root = db.reference()
  new_user = root.child('users').push({
    'content' : det
    })
  return "done"


def cricket():
  url ="https://static.cricinfo.com/rss/livescores.xml"
  while url:
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    data= soup.find_all("description")
    score = data[1].text
    break
  return score
 

def tran(n):
  translator = Translator()
  translated = translator.translate(str(n),src='cs',dest = 'ta')
  p = translated.text
 
  return p

def time():
   strTime = datetime.datetime.now().strftime("%H:%M:%S")
   return strTime

def date():
  mylist = []
  today = datetime.date.today()
  mylist.append("Today is ")
  return today

def jokes():
  r = pyjokes.get_jokes(language = "en",category = "all")
  r=list(r)
  return random.choice(r)

def emoi():
  arr = [":face_with_thermometer:",":face_with_raised_eyebrow:",":face_without_mouth:",":face_with_rolling_eyes:",":face_with_head-bandage:",
  ":face_with_thermometer:",":woozy_face:",":sneezing_face:",":face_with_monocle:",":confused_face:",":frowning_face:",":flushed_face:",":exploding_head:"
  ,":confounded_face:",":angry_face_with_horns:",":skull_and_crossbones:"]
  return random.choice(arr)

def lol():
  arr = [":rolling_on_the_floor_laughing:",":face_with_tears_of_joy:",":winking_face:",":smiling_face_with_horns:"]
  return random.choice(arr) 

def joyem():
  arr = [":slightly_smiling_face:",":upside-down_face:",":hugging_face:",":cowboy_hat_face:",":smiling_face_with_sunglasses:",":grinning_cat:"]
  return random.choice(arr)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@bot.command()

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('/hello'):
        await message.channel.send('/Hello!')
    elif message.content.startswith("/Gm"):
      await message.channel.send("Hey Good Morning")
    elif message.content.startswith("/gm"):
      await message.channel.send("/Hey Good Morning")
    elif message.content.startswith("/Nithin BOT"):
      await message.channel.send("/Fraud is Ready")
    
    elif message.content.startswith('/Who created you'):
        await message.channel.send("/I was created by ARUN")
    elif message.content.startswith('/Arun BOT'):
        await message.channel.send("/Ready to Deploy")


    elif message.content.startswith("/Inspire"):
         quote = get_quote()
         await message.channel.send(quote)

    elif message.content.startswith("/Cricket scores"):
      get = cricket()
      await message.channel.send(get)
    
    elif message.content.startswith("/lol"):
      get = emoji.emojize(lol())
      await message.channel.send(get)
    
    elif message.content.startswith("/emoji"):
      #emoj = ' '.join(message.content.lower().split()[1:])
      emo = emoji.emojize(joyem())
      await message.channel.send(emo)

    elif message.content.lower().split()[0]=="/translate":
      #msg = await client.wait_for('message')
      tr = tran(' '.join(message.content.lower().split()[1:]))
      await message.channel.send(tr)

    elif message.content.lower().split()[0]=="/database":
      #msg = await client.wait_for('message')
      tr = fire(' '.join(message.content.lower().split()[1:]))
      await message.channel.send(tr)
  

    elif message.content.startswith('/google'):
      #msg = await client.wait_for('message')
      tr = tran(' '.join(message.content.lower().split()[1:]))
      url = "https://google.com/search?q=" + tr
      we = webbrowser.open(url)
      await message.channel.send(we)
        

    elif message.content.startswith("/Time"):
      se = time()
      await message.channel.send(se)
    elif message.content.startswith("/bye"):
      se = emoji.emojize(":waving_hand:")
      await message.channel.send(se)
    elif message.content.startswith("/thanks"):
      se = emoji.emojize(":victory_hand:")
      await message.channel.send(se)

    elif message.content.startswith("/Game"):
      op = MadLib()
      await message.channel.send(op)
    
    elif message.content.startswith("/Date"):
      ge = date()
      await message.channel.send(ge)

    elif message.content.startswith("/Jokes"):
      ki = jokes()
      await message.channel.send(ki)

    elif message.content.startswith("/Who is Arun?"):
      await message.channel.send("He is my Boss")

    elif message.content.startswith("/What is your name?"):
      await message.channel.send("/KOF = King Of Friends")

    elif message.content.startswith("/Who are you?"):
      await message.channel.send("/I am your assistant deveoped by ARUN")

    elif message.content.startswith("/Why are you here?"):
      await message.channel.send("/I am here to answer your Question's ")
    elif message.content.startswith("/"):
      emo = emoji.emojize(emoi())
      await message.channel.send(emo)
      
      
    
  

client.run(TOKEN)
