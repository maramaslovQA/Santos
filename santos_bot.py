
import telebot

TOKEN = '6175249815:AAETXvUKfPMa0TPtYj-ldmvU1Bk7EA1sIBs'
show = 'https://myshows.me/view/'
mem = 'https://t.me/shutnikhuev/'
show_list = ['2', '8', '9', '10', '32', '32058', '50261', 
'20', '71','3596','39626', '278', '220', '34737', '52910',
'188', '73223', '12122','59520','59512','44645','45124',
'57740','6300','51692','36596','55','298','9118','35540',
'55213','45104','48177','35556','64689','1846','186', '41781','226',
'234','55797','70224','53374','61718','72375','65368','22410','66','62321','61381',
'70888','60530','70795','63820','73758','71531','53548','74562','48017','61524','55847',
'26428','62973','66461','65480','19638','56172','12122','73393','55850','59520','59512',
'72351','70160','65743','74551','76372','78439','187','71995','54083','60164','55085','191',
'25561','73838','70993','53493','50259','52794','304','42735','43551','57006','51230','37915','7718',
'597','69661','59711','58517','52620','66246','49283','35','63206','56452','59427','60018','60826',
'62195','58912','64689','58851','76672','77478','63474','44937','186','66531','66565','','62515','53374','17486','56293',
'49373','42707','31739','53370','14','72983','55869','38226','49873','58231','60174','18739','75105','75482',
'51619','53485','62566','68906','44491','236','58320','192','54629','5476','64712','54972','39197','56961','72850',
'65309','56132','65101','58023','14979','16004','71126','61693','34265','44090','38','57925','56405','39608','35595','49878',
'55851','58195','33416','65308','67366','48920','61487','63213','316','78123','73193','73609','1120','64258','36078']
from telebot import types
import random


bot = telebot.TeleBot(TOKEN, parse_mode='html') # создание бота

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message):
    sti = open('lapenko_zdravo.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id,  # id чата, в который необходимо направить сообщение
        text='Привет {0.first_name}! Я помогу тебе справиться с дофаминовым голоданием \nНажми нужную кнопку 🤓'.format(
            message.from_user, bot.get_me()), reply_markup=markup)  # текст сообщения


# Кнопки
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Сериал 📺')
btn2 = types.KeyboardButton('Мем 🤡')
btn3 = types.KeyboardButton('Написать создателю 📝')
markup.add(btn1, btn2, btn3)

#actions for keyboard
@bot.message_handler(content_types = ['text'])
def activity(message):
        if message.text == 'Сериал 📺':
          bot.send_message(message.chat.id,show+str(random.choice(show_list)))
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          btn1 = types.KeyboardButton('Ок, попробую')
          btn2 = types.KeyboardButton('Смотрел, давай другой')
          markup.add(btn1,btn2)
          bot.send_message(message.chat.id,text='м ?',reply_markup=markup)
        elif message.text == 'Смотрел, давай другой':
          bot.send_message(message.chat.id,show+str(random.choice(show_list)))
          bot.send_message(message.chat.id,text="А этот?")
            
        elif message.text == 'Мем 🤡':
            bot.send_message(message.chat.id,mem+str(random.randint(35,5701)))
            
        elif message.text == 'Написать создателю 📝':
            bot.send_message(message.chat.id,'t.me/maramaslov')
                   
        elif message.text == 'Ок, попробую':
            bot.send_video(message.chat.id, 'https://media.giphy.com/media/jtQpRa3y7S2Ke3JvQE/giphy.gif', None, 'Text') 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Мем 🤡')
            btn2 = types.KeyboardButton('На главную ⤴️')
            markup.add(btn1,btn2)
            bot.send_message(message.chat.id,text='Приятного просмотра🍿',reply_markup=markup)  

        elif message.text == 'На главную ⤴️':
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          btn1 = types.KeyboardButton('Сериал 📺')
          btn2 = types.KeyboardButton('Мем 🤡')
          btn3 = types.KeyboardButton('Написать создателю 📝')
          markup.add(btn1, btn2, btn3)
          bot.send_message(message.from_user.id, 'Йо', reply_markup=markup)
        else:
            bot.send_message(message.chat.id,'Я пока не понимаю текст, сорян 😕 тыкай кнопку')



# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()
if __name__ == '__main__':
    main()
    
