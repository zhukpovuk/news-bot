import databa
import telebot
import requests
from peewee import *
from databa import *
import datfile
parameters = {
    #'q': 'dollar', # query phrase  # maximum is 100
    'country': 'gb',
    #'source': None,
    'category': 'business',
    'apiKey': '0b19c9bde21541859e8176ed2060de79' # your own API key
}

url = 'https://newsapi.org/v2/top-headlines?'
parameters = {
    #'q': 'dollar', # query phrase  # maximum is 100
    'country': 'gb',
    #'source': None,
    'category': 'business',
    'apiKey': '0b19c9bde21541859e8176ed2060de79' # your own API key
}
db = SqliteDatabase('db/database.db')
class sus():
    id = PrimaryKeyField(unique=True)
    country = CharField()
    category = CharField()
    ever = IntegerField()

bot = telebot.TeleBot('5247888467:AAH2hPIdtmH26P3mhdCKkpSua9Pt44mYoY0');


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Hello, I am news bot. Please enter your username:")
        bot.register_next_step_handler(message, start_search0);


def start_search0(message):
    global nick
    nick = message.text
    if asdasd.check_name(nick):
        asdasd.write_player(nick)
        bot.send_message(message.from_user.id, "I'm glad to see you, "+ nick +'''\n/get_some_news — choose the country whose news you want
        to receive,\n/help — Repeats this message,\n/stats - Get stats''')
        bot.register_next_step_handler(message, start_search)
    else:
        bot.send_message(message.from_user.id, "This user is taken, please enter another one")
        bot.register_next_step_handler(message, start_search0)
    if message.text == "/help":
        bot.send_message(message.from_user.id,
                         "I'm glad to see you, "+ nick +'''\n/get_some_news — choose the country whose news you want to receive,
                         \n/help — Repeats this message,\n/stats - Get stats''')
        bot.register_next_step_handler(message, start_search);


def start_search(message):
    #theBoard = [' '] * 10
    if message.text == "/get_some_news":
        bot.send_message(message.from_user.id,
                         "You want to recieve news according to  \n/category \n /keyword")
        bot.register_next_step_handler(message, ch_country);
    elif message.text == "/stats":
        bot.send_message(message.from_user.id,
                         "I've prepared for you some stats")
        #asdasd.get_stats(Stat.name)
        #bot.register_next_step_handler(message, start_search0);
        stats_set = asdasd.get_stats(nick)
        business_number_of_requests = str(int(stats_set[1]))
        entertainment_number_of_requests = str(int(stats_set[2]))
        bot.send_message(message.from_user.id,
                         'Stats for ' + nick + ':\n\nbusiness_number_of_requests: ' + business_number_of_requests + '''\nentertainment_number_of_requests: 
                         ''' + entertainment_number_of_requests)
        bot.register_next_step_handler(message, start_search)
    else:
        bot.send_message(message.from_user.id, "I don't understand you, please type /help.")
        bot.register_next_step_handler(message, get_text_messages);


def ch_country(message):
    if message.text == "/category":
        bot.send_message(message.from_user.id,
                         "Сhoose the category of preferable news \n\n/business\n/entertainment\n/general\n/health\n/science");
        bot.register_next_step_handler(message, sho);
    elif message.text == "/keyword":
        bot.send_message(message.from_user.id,
                         "I'm waiting for your word^^");
        bot.register_next_step_handler(message, sho2);
    else:
        bot.send_message(message.from_user.id, "I don't understand you, please type /help.")
        bot.register_next_step_handler(message, get_text_messages);


def sho(message):
    c = datfile.get_news_from_topic(message.text)
    asdasd.update_stats(nick, message.text)
    bot.send_message(message.from_user.id, c)
    #bot.register_next_step_handler(message, start_search0);
    bot.send_message(message.from_user.id, nick +''', I can offer\n/get_some_news — choose the country whose news you want to receive,
    \n/help — Repeats this message,\n/stats - Get stats''')
    bot.register_next_step_handler(message, start_search);

def sho2(message):
    c = datfile.get_news_from_keyword(message.text)
    bot.send_message(message.from_user.id, c)
    bot.register_next_step_handler(message, start_search0);
    bot.send_message(message.from_user.id, nick +'''\n/get_some_news — choose the country whose news you want to receive,
    \n/help — Repeats this message,\n/stats - Get stats''')
    bot.register_next_step_handler(message, start_search);


bot.polling(none_stop=True, interval=0)
