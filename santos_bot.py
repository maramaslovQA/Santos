
import telebot

TOKEN = '6175249815:AAETXvUKfPMa0TPtYj-ldmvU1Bk7EA1sIBs'
show = 'https://myshows.me/view/'
film = 'https://www.kinopoisk.ru/film/'
mem = 'https://t.me/shutnikhuev/'
show_list = ['2', '8', '9', '10', '32', '32058', '50261','49654','39769','28939','28067','48114','28813','34435','42802','52584','69576' 
'20','60','71','142','3596','39626', '278', '220', '34737', '52910','6266','69157','39466','18286','43381','43547','68259','63752',
'188', '73223', '12122','59520','59512','44645','45124','781','64797','77697',
'57740','6300','51692','36596','55','298','9118','35540','24994',
'55213','45104','48177','35556','64689','1846','186', '41781','226','36513',
'234','55797','70224','53374','61718','72375','38750','65368','22410','66','62321','61381','42377','77468',
'70888','60530','70795','63820','73758','71531','53548','74562','48017','61524','55847','24283','65856',
'26428','62973','66461','65480','19638','56172','12122','73393','49133','55850','59520','59512','53681','82360','73604','73666',
'72351','70160','65743','74551','76372','78439','187','71995','54083','60164','55085','191','84772','78792','914','64796','838',
'25561','73838','70993','53493','50259','52794','304','42735','43551','57006','51230','37915','7718',
'597','69661','59711','58517','52620','66246','49283','35','63206','56452','59427','60018','60826',
'62195','58912','64689','58851','76672','77478','63474','44937','186','66531','66565','23486','62515','53374','17486','56293',
'49373','42707','31739','53370','14','72983','55869','38226','49873','58231','60174','18739','75482',
'51619','53485','62566','68906','44491','236','58320','192','54629','5476','64712','54972','39197','56961','72850',
'65309','56132','65101','58023','14979','16004','71126','55849','61693','34265','44090','38','57925','56405','39608','35595','49878',
'55851','58195','33416','65308','67366','48920','61487','63213','316','78123','73193','73609','1120','64258','36078','59623']
film_list = ['963016','77576','9617','571896','3231','45028','46638','302','4188','258687','5185','2408','326','42782','43423','5629','24682',
'24683','22854','4966','4182','5502','476','535341','21205','1933','2388','7103','231150','4067','518040','4064','391772','627','61439','279627',
'749','261157','1074910','925669','884376','4266','2821','462884','462606','195847','522','361','63717','586397','4304','406340','675','280174',
'8091','468937','391735','32898','481576','507817','522892','261005','417583','86326','81314','426001','4541','462732','81750','427122','427855',
'23956','7415','584405','453544','400906','432725','4853','253761','3956','1228069','464607','4328','1108556','997671','1072663','1093170',
'1049279','1052575','1108577','1105','606646','363','4275','4695','252156','462626', '3984','469','7466','2494','350','1167855','1234848','665107', 
'993591','461862','992605','909700','259251','922150','705350','645910','675498','808639','370','8239','963343','8221','399','4413489','1143242',
'1043758','645118','1108577','668169','568289','367','12198','46068','389','309397','8408','848894','5319','462360','342','462867','775727','63912',
'46708','447301','474','2127','573990','530','111543','770973','5492','408410','725190','824954','772017','1957','158786','751','258321','77531','448',
 '435','400094','184417','86206','414547','468102','355','48546','506444','104938','1008113','841152','4886','341','2361','276598','1311466','1188529','2056','81542',
 '1337788','913520','1171976','843649','959606','89219','42571','439','371','1134778','1365998','7724','835086','380','1048334','327','325','397667','324',
 '1047883','958519','47382','303999','369153','1234923','3561','1991','939411','1049775','1005852','1118095','395787','577899','301','1115541','1224694',
 '1197714','722951','961715','931677','6871','965754','502270','944098','494','5188','345','938643','45146','41431','915112','55942','261018','722995','41520','841263',
 '515','381','450213','557668','496','679830','464585','779602','351','77413','7328','407636','409600','279880','44156','803422','44290','48356','322',
 '689','602749','680824','252677','15139','592203','714074','645261','819101','409372','891509','195496','822708','679924','378140','817481','472',
 '453406','612','762484','195334','798068','839954','522941','44719','714888','5619','588672','518042','447','333','742026','354','616','505811','7640','462762',
 '739642','596125','61237','5286','2058','84014','437410','12244','94588','196707','740644','572035','468466','466844','519','584084','705162','546915',
 '634256','263531','4500','102328','276376','397671','382','437555','281251','395690','252626','278273','681849','1354524','1392550','1343908','4559710','2213',
 '1139373','1368311','4661216','4693245','1169291','1045942','462553','555','4841224','527','1069523','897725','2461','2467','156002','280932','1405778',
 '18347','1322324','4509133','1309570','8178','251879','4822000','428003','4815','425400','6973','401775','397','963343','1008445','1272469','2898',
 '1234826','838','24724','1318972','542581','496740','1338480','44691','46225','103355','1044731','1138856','409424','1263423','41047','1189859',
 '1245501','410597','413362','1379090','47040','1588','21275','1007049','1281999','1263705','1129900','843650','623250','1309596','22936','1262160',
 '770','1331982','1326397','1072788','707569','1235002','8335','1338525','77335','1421546','775273','43869','931127','1390163','1236063','94150','1230235','86604',
 '77444','6877','102130','826373','1333556','1256262','178722','526','263447','65770','573977','432403','403486','1080513','925389',
 '470553','21844','737859','679486','1209193','279707','428134','1220126','397774','1142654','232785','273302','462682','4466','6175','15933',
 '43700','416547','930442','9259','303998','409','893245','588105','916096','771403','988873','1024435','4561','16115','3563','510','910353','252641',
 '2868','395756','538225','2987','1118042','970196','1118214','86621','1040690','1115646','95382','44027','571892','3885','5909','103785',
 '424299','1161792','945037','939785','21503','980327','81844','8067','6039','41109','998317','465649','471','46100','5423','1721','39577',
 '61438','635772','893843','41830','584387','4807','5084','398239','78320','585','10851','992788','694646','42115','715','77203','1008362',
 '683481','966036','160914','75967','46089','43007','902939','726794','822709','9208','10179','55830','42799','4515','348','428457','409295',
 '42088','1976','18282','453397','963346','819','21606','280172','824437','576135','7115','24695','4002','864138','8130','15061','24693','24701',
 '22791','909898','24705','542484','944708','659909','1578','863','255611','56638','75871','44835','312','51481','535337','841081','328','880',
 '782','1828','610','2821','3690','4022','462883','490323','280826','468564','6187','43602','46368','842913','79834','340','259788','77720','46421',
 '678329','406408','37547','2022','45463','463354','760815','692861','485260','805650','567149','521526','797840','102376','397494','577529','743088',
 '757898','48162','719608','602677','662596','276762','455194','89515','544','2997','497','454','6236','799','557804','688','841147','569149',
 '45116','346','786958','4688','406543','424266','778218','756092','918087','678550','196617','77082','917496','394619','5622','723988','41982',
 '868982','694051','839818','428','414','9393','535304','677798','834394','1965','6374','438272','463893','102198','78378','840884','506490',
 '6875','2219','571','484428','591485','799128','8350','431294','261021','279580','395709','596227','9691','841700','7122','656093','594','402626',
 '498','442568','829368','749540','339','102474','595938','258941','47237','45660','770997','464281','777091','782792','470656','5012','408403','582391',
 '432791','651628','723','746480','708','251735','645087','678','719','588839','723270','4347','546244','461972','102838','4914','3230','582170','586399',
 '461981','586584','615823','517988','462737','493992','18805','390738','261370','485261','427202','1405508','1309166','44120','911088','765','46745','1190148',
 '2000127','262765','8420','1177510','161133','7732','1345617','4397114','4472625','2046399','1009251','1195477','648440','1355139','280225','583','46063',
 '832056','406477','1262931','501','18348','4709141','2001','468373','1320623','3795','4538','18294','255369','619','830906','972777','398405','93547','43949',
 '224871','4508879','690593','602409','160946','82441','1346514','507440','1211076','43545','104927','103356','42775','467','43911','44574','1114968',
 '8695','464168','44224','1199100','786','20908','20897','1009413','557837','12155','835877','1009434','994530','3809','195432','1238506','17602','1007058',
 '980367','749370','1060251','1202296','533','278171','45606','504484','995991','809570','810897','1055528','3478','3880','4220','46789','933307','662359','6111',
 '271802','402981','1267340','5065','954059','1178137','1245524','1236644','470191','714878','909848','977968','6345','812','683688','504488','272472','39259',
 '24702','43515','663','20590','860683','7353','196604','1115125','501821','391509','8085','394066','64021','1044906','726838','1261581','462305','1165077',
 '770634','987695','1574','1000414','1048255','1046033','335','1144300','1122114','466649','1221042','281449','679336','406186','410299','418847','28130','839744',
 '5007','996027','395523','916059','19249','437414','4472','221750','1121377','573869','1040748','196952','24719','442','1065805','980348','804714','42902',
 '1049653','1142526','1006742','632','1008486','6049','916699','406403','462654','840294','718811','607737','669260','972919','419200','4311','941914','41058','772380',
 '895502','554','470185','252475','259544','45822','935940','8158','1042556','984309','88144','972783','7650','24721','7374','991628','669275','977743','981230','4071','4619',
 '93377','978613','978956','669276','978838','104215','874941','4809','255368','277591','8131','320','6828','1889','971283','505799','104926','78261','38198',
 '567','37146','44849','466994','43147','817969','43977','331','902577','9580','470037','47018','102125','744776','5281','881723','760829','577806','102383','19273',
 '46080','13725','588','24708','24692','24717','44811','915270','24704','195195','915111','664','934923','939981','463694','46671','521647','24691','445191',
 '6987','24713','24726','403','13720','22777','696154','678999','718562','501958','8160','5901','2694','395410','43332','4879','934130','837530','181748','542600',
 '946883','966995','225011','840367','930534','4199','493390','256497','656294','11075','905058','41087','497707','513','40966','653696','126196','5475','46416',
 '930000','4881','315168','402550','42135','2962','43018','1803','765019','4190','4186','303','1794','450345','77577','279770','409348','4003','422882','467099','450765',
 '5330','470689','821','220617','462247','195239','580181','3669','607','195524','329','336','518214','252268','700096','518188','666951','727913','268593',
 '623744','5115','7101','841613','42905','51605','296203','770641','221368','41276','17040','4189','48039','18253','798110','720','843831','500','464290','541',
 '195460','523248','677683','391755','81557','1541','410','38904','866','251916','842493','1644','584385','770683','405609','466','923901','840818','585585',
 '634679','81691','214693','6642','770631','885372','744275','736204','590022','775276','716595','535254','736206','12192','415663','43259','566283','716891',
 '451','16466','409961','522876','736205','568258','677893','506058','302080','418762','147969','81845','4465','844','6066','746001','596643','3741','736',
 '746','6831','252130','85182','78871','804','465763','462466','762738','520648','867265','411924','721153','2738','1809','807','11579','2800','87161','4592',
 '10074','5140','6600','102510','484426','12252','523058','1978','722860','463210','5197','15995','6412','614227','676361','4346','523057','88198','497233','429827',
 '398624','143139','471628','9485','4675164','1348487','1313196','927898','4822281','15325','316376','1031953','105634','1993','1402927','7355','675413','1297211',
 '944814','590286','1283955','472362','3742','712','14287','412248','105741','50225','413080','47093','492174','290751','63920','321842','358','450237','455188',
 '406671','395739','258758','18973','77660','427198','2609','455338','464282','317889','420923','471587','416824','405602','391277','23275','1762','402979',
 '426004','279850','77439','495892','257898','406294','102531','502937','463046','160910','81289','450289','281006','373158','263984','430519','86573','397604',
 '463135','780','5232612','4710684','1246627','1725'] 
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
btn2 = types.KeyboardButton('Кино 🎬')
btn3 = types.KeyboardButton('Мем 🤡')
btn4 = types.KeyboardButton('Написать создателю 📝')
markup.add(btn1, btn2, btn3, btn4)

#actions for keyboard
@bot.message_handler(content_types = ['text'])
def activity(message):
        if message.text == 'Сериал 📺':
          bot.send_message(message.chat.id,show+str(random.choice(show_list)))
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          btn1 = types.KeyboardButton('Ок, попробую')
          btn2 = types.KeyboardButton('Не, давай другой')
          btn3 = types.KeyboardButton('Назад👆')
          markup.add(btn1,btn2,btn3)
          bot.send_message(message.chat.id,text='м ?',reply_markup=markup)
        elif message.text == 'Не, давай другой':
          bot.send_message(message.chat.id,show+str(random.choice(show_list)))
          bot.send_message(message.chat.id,text='а этот?')
            
        elif message.text == 'Кино 🎬':
          bot.send_message(message.chat.id,film+str(random.choice(film_list)))
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          btn1 = types.KeyboardButton('Буду')
          btn2 = types.KeyboardButton('Давай другой')
          btn3 = types.KeyboardButton('Назад👆')
          markup.add(btn1,btn2,btn3)
          bot.send_message(message.chat.id,text='Будешь смотреть?',reply_markup=markup)
            
        elif message.text == 'Давай другой':
          bot.send_message(message.chat.id,film+str(random.choice(film_list)))
          bot.send_message(message.chat.id,text='а этот будешь?')    
            
        elif message.text == 'Мем 🤡':
            bot.send_message(message.chat.id,mem+str(random.randint(35,6369)))
            
        elif message.text == 'Написать создателю 📝':
          markup = types.InlineKeyboardMarkup()
          markup.add(types.InlineKeyboardButton('Написать', url='https://t.me/maramaslov'))
          bot.reply_to(message, '👇', reply_markup=markup)
                      
                   
        elif message.text == 'Ок, попробую':
            bot.send_video(message.chat.id, 'https://media.giphy.com/media/jtQpRa3y7S2Ke3JvQE/giphy.gif', None, 'Text') 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Мем 🤡')
            btn2 = types.KeyboardButton('На главную ⤴️')
            markup.add(btn1,btn2)
            bot.send_message(message.chat.id,text='Приятного просмотра🍿',reply_markup=markup)  
            
        elif message.text == 'Буду':
            bot.send_video(message.chat.id, 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTNmZTllNDZlN2Y0Yzk3NzQxZDY5NGE3MDdmOTBjMzczNTI0NGM4YSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/Tf3wJ6e9k4xmWaH825/giphy.gif', None, 'Text') 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Мем 🤡')
            btn2 = types.KeyboardButton('На главную ⤴️')
            markup.add(btn1,btn2)
            bot.send_message(message.chat.id,text='Приятного просмотра🍿',reply_markup=markup) 
            
        elif message.text == 'Назад👆':
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          btn1 = types.KeyboardButton('Сериал 📺')
          btn2 = types.KeyboardButton('Кино 🎬')
          btn3 = types.KeyboardButton('Мем 🤡')
          btn4 = types.KeyboardButton('Написать создателю 📝')
          markup.add(btn1, btn2, btn3, btn4)
          bot.send_message(message.from_user.id, 'Давай попробуем ещё', reply_markup=markup)

        elif message.text == 'На главную ⤴️':
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          btn1 = types.KeyboardButton('Сериал 📺')
          btn2 = types.KeyboardButton('Кино 🎬')
          btn3 = types.KeyboardButton('Мем 🤡')
          btn4 = types.KeyboardButton('Написать создателю 📝')
          markup.add(btn1, btn2, btn3, btn4)
          bot.send_message(message.from_user.id, 'Тыкай кнопку', reply_markup=markup)
        else:
            bot.send_message(message.chat.id,'Я пока не понимаю текст, сорян 😕 тыкай кнопку')
            
@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    bot.send_message(message.chat.id, '<b>Тоже люблю стикеры, неплохой)</b>')


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()
if __name__ == '__main__':
    main()
    
