import telebot

TOKEN = '6175249815:AAETXvUKfPMa0TPtYj-ldmvU1Bk7EA1sIBs'
show = 'https://myshows.me/view/'
mem = 'https://t.me/shutnikhuev/'
sitcom_list = ["45104", "50259", "32058", "188", "32", "9", "50261", "20", "71","3596","39626", "278", "220", "34737", "52910","66565", "73223", "12122","59520","59512","44645","45124","57740","6300","51692","36596","55","298"]
from telebot import types
import random


bot = telebot.TeleBot(TOKEN, parse_mode='html') # создание бота

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message):
    sti = open ('lapenko_zdravo.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет {0.first_name}! Я помогу тебе справиться с дофаминовым голоданием \nНажми нужную кнопку🤓'.format(message.from_user, bot.get_me()), reply_markup=markup) # текст сообщения
    
#Кнопки
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Сериал 📺')
item2 = types.KeyboardButton('Мем 🤡')
item3 = types.KeyboardButton('Написать создателю 📝')

markup.add(item1,item2,item3)

#actions for keyboard
@bot.message_handler(content_types = ['text'])
def activity(message):
    if message.chat.type == 'private':
        if message.text == 'Сериал 📺':
            bot.send_message(message.chat.id,show+str(random.choice(sitcom_list)))
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Ок, попробую")
            item2 = types.KeyboardButton("Смотрел, давай другой")
            markup.add(item1, item2)
            
        elif message.text == 'Мем 🤡':
            bot.send_message(message.chat.id,mem+str(random.randint(35,6000)))
            
        elif message.text == 'Написать создателю 📝':
            bot.send_message(message.chat.id,'t.me/maramaslov')
            
        elif message.text == 'Ок, попробую':
            bot.send.video(message,chat.id, 'https://media.giphy.com/media/jtQpRa3y7S2Ke3JvQE/giphy.gif', None, 'Text')
            
        elif message.text == '"Смотрел, давай другой"':
            bot.send_message(message.chat.id,"А этот ?\n\n{0}".format(random.choice(sitcom_list)))
            
        else:
            bot.send_message(message.chat.id,'Я пока не понимаю текст, сорян 😕 тыкай кнопку')



# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()
if __name__ == '__main__':
    main()
    

