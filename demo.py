from telegram.ext import Updater
import telegram

TOKEN = '313645318:AAFDuySwzhlaD7EUhJ885bB1seta4-D11qo'

bot = telegram.Bot(token=TOKEN)
chat_id = 199392648
print(bot.getMe())

bot.sendMessage(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")

bot.sendMessage(chat_id=chat_id,
                text="*bold* _italic_ `fixed width font` [link](http://google.com).",
                parse_mode=telegram.ParseMode.MARKDOWN)

bot.sendMessage(chat_id=chat_id,
                 text='<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.',
                 parse_mode=telegram.ParseMode.HTML)

bot.sendPhoto(chat_id=chat_id, photo='http://www.jqueryscript.net/images/Simplest-Responsive-jQuery-Image-Lightbox-Plugin-simple-lightbox.jpg')

# updates = bot.getUpdates()
#
# chat_id = bot.getUpdates()[-1].message.chat_id


# print([u.message.text for u in updates])