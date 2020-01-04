from telegram.ext import Updater
updater = Updater(token='******', use_context=True)
#get token from @BotFather on telegram

dispatcher = updater.dispatcher

#logging from tutorial, not used right now
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#functions defined, start() sends text, getid() sends chatid, ip() gets IPv4 and IPv6 from ipify.org
def start(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def getid(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text=update.effective_chat.id)

from requests import get

def ip(update, context):
   ip4Addr = get('https://api6.ipify.org').text
   ip6Addr = get('https://api.ipify.org').text
   context.bot.send_message(chat_id=update.effective_chat.id, text=ip4Addr)
   context.bot.send_message(chat_id=update.effective_chat.id, text=ip6Addr)

from telegram.ext import CommandHandler
from telegram.ext import Filters
#command defined and corresponding function called, Filters.user only defined username gets answer
start_handler = CommandHandler('start', start, Filters.user(username="@***"))
dispatcher.add_handler(start_handler)
ip_handler = CommandHandler('ip', ip, Filters.user(username="@***"))
#bot only answers to account specified in username
dispatcher.add_handler(ip_handler)
getid_handler = CommandHandler('getid', getid)
dispatcher.add_handler(getid_handler)

#DO NOT RENAME dlLink.py, save() needs to import dlLink() from there
#save() checks for correct chat_id, if correct calls dlLink(), else prints in commandline what wrong user sent
from dlLink import dlLink

def save(update, context):
   link = update.message.text
   if update.message.chat_id == ****:
      dlLink(str(link))
   else:
      print('wrong user sent: '+link)
#bot processses only links send from account with correct chat_id

from telegram.ext import MessageHandler, Filters
#messages get passed to save()
link_handler = MessageHandler(Filters.text, save)
dispatcher.add_handler(link_handler)

#starts bot
updater.start_polling()
