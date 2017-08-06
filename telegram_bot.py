import telepot
import pprint
import base_conv
import helpPage
import weatherMod
import timeMod

bot = telepot.Bot("433006211:AAHcdoTFaUOlVVqhqH8ii0XdZcwiQoDAo1U")

def initMessage():
    msg = "Opcoes permitidas:\nconv-Conversao de base\nclima- Clima em alguma cidade\nhelp-Ajuda em alguma funcao"
    return msg

def validateMessage(chat_id,message):
    opt = ['conv','Conv','help','Help','clima','Clima','hora','Hora']
    if(message not in opt):
        bot.sendMessage(chat_id,initMessage())
    else:
        return message


def handle(msg):
    content_type, chat_type,chat_id = telepot.glance(msg)
    flavor = telepot.flavor(msg)
    print(content_type, chat_type,chat_id,flavor)
    text = msg['text']
    print('\n* Question:',text,' *')
    if(content_type == 'text'):
        atts = []
        atts = text.split()
        init = atts[0]
        if(init == '/start'):
            answer = initMessage()
        else:
            answer = ''
            op = validateMessage(chat_id,init)

        if(atts[0] == '/start'):
            answer = initMessage()
        elif(atts[0] == 'conv' or atts[0] == 'Conv'):
            answer = base_conv.main(atts[1],int(atts[2]),int(atts[3]))
        elif(atts[0] == 'clima' or atts[0] == 'Clima'):
            answer = weatherMod.getWeather(atts[1])
        elif(atts[0] == 'hora' or atts[0] == 'Hora'):
            answer = timeMod.getCoord(atts[1])
        elif(atts[0] == 'help' or atts[0] == 'Help'):
            answer = helpPage.getHelp(atts[1])
#=====================================================================#

        print('\n*Reply:',answer,'*\n')
        bot.sendMessage(chat_id,answer)
        print('=========================')

bot.message_loop(handle)

bot.getUpdates(offset=100000001)

while True:
    pass
