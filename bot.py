import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = '8523112202:AAEaoiDoiHIHQV0405w_Ppah38LiLpXNVdU'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

MESSAGES = {
    'start': 'Привет, любимая!\nЭто мой для тебя подарочек)\nВ этом боте я приготовил для тебя несколько сюрпризов\nНо для начала ознакомься с правилами /rules',
    'help': 'Перечень сюрпризов(все завуалированы)\n'
            '/start - Начало работы\n'
            '/help - Помощь и список команд\n'
            '/info - Информация о боте\n'
            '/rules - Правила использования\n'
            '/contact - Контакты\n'
            '/price - Цены и тарифы\n'
            '/schedule - Расписание\n'
            '/faq - Частые вопросы\n'
            '/support - Техническая поддержка\n'
            '/news - Новости и обновления\n'
            '/tips - Полезные советы\n'
            '/links - Полезные ссылки\n'
            '/status - Статус системы\n'
            '/feedback - Оставить отзыв\n'
            '/donate - Поддержать проект',
    
    'info': 'ℹ️ Информация о боте:\n\nЭто демонстрационный бот с 15 командами, созданный для примера.',
    'rules': '📖 Правила использования:\n\n1. Можешь выбрать один сюрприз в месяц(там разное количество кайфушек, на месяц хватит)\n2. Не подсматривай содержание других сюрпризов\n3. Получай удовольствие, я очень старался',
    'contact': '📞 Контакты:\n\nEmail: example@email.com\nТелеграм: @username',
    'price': '💵 Цены и тарифы:\n\nБазовый: бесплатно\nПремиум: 10$/мес\nПро: 25$/мес',
    'schedule': '📅 Расписание:\n\nПн-Пт: 9:00-18:00\nСб: 10:00-16:00\nВс: выходной',
    'faq': '❓ Частые вопросы:\n\nQ: Как начать?\nA: Используйте /start\n\nQ: Где помощь?\nA: Используйте /help',
    'support': '🔧 Техническая поддержка:\n\nОпишите вашу проблему и мы поможем!',
    'news': '📰 Новости:\n\nПоследнее обновление: добавлено 15 команд!',
    'tips': '💡 Советы:\n\n1. Регулярно проверяйте /news\n2. Читайте /rules\n3. Используйте /faq',
    'links': '🔗 Полезные ссылки:\n\nСайт: example.com\nДокументация: docs.example.com',
    'status': '✅ Статус системы:\n\nВсе системы работают нормально\nБот онлайн',
    'feedback': '📝 Оставить отзыв:\n\nНапишите ваш отзыв в ответном сообщении',
    'donate': '❤️ Поддержать проект:\n\nКошелёк для донатов: 4100xxxxxx'
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
    application.add_handler(CommandHandler("contact", contact))
    application.add_handler(CommandHandler("price", price))
    application.add_handler(CommandHandler("schedule", schedule))
    application.add_handler(CommandHandler("faq", faq))
    application.add_handler(CommandHandler("support", support))
    application.add_handler(CommandHandler("news", news))
    application.add_handler(CommandHandler("tips", tips))
    application.add_handler(CommandHandler("links", links))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("feedback", feedback))
    application.add_handler(CommandHandler("donate", donate))
    
    print("Бот запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()