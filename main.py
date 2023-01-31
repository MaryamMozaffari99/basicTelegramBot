import logging
import telebot 
from telebot import types


from constants import API_KEY

bot = telebot.TeleBot(API_KEY , parse_mode=None)
#---------------------------------------------------

@bot.message_handler(commands=["help","Hello"])
def send_help_message(message): #msg
    print(message)
    bot.reply_to(message , "Hello Maryam :), You DID it :)))") #msg
# ---------------------------------------
@bot.message_handler(content_types=["photo","sticker"])
#regexp , func
def send_content_message(message): #msg
    # print(message)
    bot.reply_to(message , "That's not a text Message!") #msg
# ---------------------------------------
@bot.message_handler(commands=["boo"])
# @bot.message_handler(func=lambda message : message.from_user.username == "Binnggoo" ) 
def send_boo_message(message): #msg
    bot.reply_to(message , "WOW! You Are Scary!")
# ---------------------------------------
@bot.message_handler(commands=["throw"])
def send_boo_message(message): #msg
    bot.send_dice(chat_id = message.chat.id)
# ---------------------------------------
@bot.edited_message_handler(commands=["noice"])
def send_edit_message(message): #msg
    bot.send_message(chat_id = message.chat.id , text="WOW! I saw what you did!")
# ---------------------------------------
@bot.message_handler(commands=["close"])
def send_game_message(message): #msg
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(chat_id = message.chat.id , text="Good Riddance!", reply_markup=markup)

#types
@bot.message_handler(commands=["game"])
def send_game_message(message): #msg
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1=types.KeyboardButton("/boo")
    btn2=types.KeyboardButton("/help")
    btn3=types.KeyboardButton("/close")
    markup.add(btn1,btn2,btn3)
    bot.send_message(chat_id = message.chat.id , text="What do you want!?", reply_markup=markup)


# ---------------------------------------
# Not Working
# @bot.message_handler(commands=["send_location"])
# def send_location_message (message):
#     print(message.location)
# ---------------------------------------





# ---------------------------------------

#make bot listen 
bot.polling()



