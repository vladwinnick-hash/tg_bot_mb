import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = '8523112202:AAEaoiDoiHIHQV0405w_Ppah38LiLpXNVdU'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

MESSAGES = {
    'start': 'Привет, любимая!\nЭто мои извинения...\nЯ отвратительно поступал и вел себя с тобой\nТы заслуживаешь всех звезд с неба'
    '\nВ мире нет таких слов, что бы я мог извиниться, но они мне и не нужны\nЯ хочу снова заслужить, завоевать твою любовь'
    '\nЭтот сюрприз я длжен был сделать еще давно, как и многое другое...\nТак же, как я начал делать его, так же я исправлю все свои ошибки'
    '\nНо для начала ознакомься с правилами /rules',
    'help': 'Основные команды и помощь:\n\n'
            '/start - Начало работы\n'
            '/help - Помощь\n'
            '/rules - Правила использования\n'
            '/surprises - Тут список сюрпризов)\nНапоминаю, один в месяц, в остальные не подглядывай',
    'surprises': 'Здесь я хочу исправить все свои ошибки, которые привели к краху\n\n'
            '/lips'
            '/feet'
            '/strawberrry'
            '/pearl'
            '/dishwasher',
            
    
    'rules': '📖 Правила использования:\n\n',
    'lips': 'Пора подкачать губки!\n10 минетов в любое время дня и ночи)',
    'feet': 'Сделаю все, что бы ты могла ходить на работу)\n10 сеансов массажа ног для самой любимой)',
    'strawberrry': 'Я покажу, что такое настоящая клубника в шоколаде',
    'pearl': 'Отправлюсь на поиски самой прелестной жемчужины\n10 куни в любое время дня и ночи)',
    'dishwasher': 'Я тебя очень люблю, поэтому готов помыть за тебя посуду...\nВсю неделю...',
    'queen': 'Пусть мы и разные, но весь месяц меня это не волнует\nСлушаюсь и повинуюсь',
    'bouquet': 'Это будет интересно)\nТебе понравится)',
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['start'])

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['help'])
    
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['info'])

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['rules'])

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['contact'])

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['price'])

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['schedule'])

async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['faq'])

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['support'])

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['news'])

async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['tips'])

async def links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['links'])

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['status'])

async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['feedback'])

async def donate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGES['donate'])

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("rules", rules))
    
    print("Бот запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()