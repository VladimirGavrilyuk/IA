from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from transformers import pipeline

# Отримання API токену бота та моделі мови
TOKEN = '5845532688:AAGS9waU4qQ5UT1x910Tt7rta21qSR32cag'
model_name = 'EleutherAI/gpt-neo-2.7B'

# Ініціалізація моделі
generator = pipeline('text-generation', model=model_name, device=0 if torch.cuda.is_available() else -1, max_length=30)

# Функція-обработчик команди /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привіт! Я бот, який використовує модель мови ChatGPT для генерації тексту. Надішліть мені своє запитання, і я спробую на нього відповісти!")

# Функція-обработчик повідомлень
def respond(update, context):
    # Отримання повідомлення користувача
    message = update.message.text

    # Генерація відповіді за допомогою моделі мови ChatGPT
    response = generator(message, max_length=50, do_sample=True, temperature=0.7)[0]['generated_text']

    # Надсилання відповіді користувачеві
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Функція-обработчик помилок
def error(update, context):
    print(f'Update {update} caused error {context.error}')

# Ініціалізація телеграм-бота
updater = Updater(token=TOKEN, use_context=True)

# Реєстрація функцій-обработчиків
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, respond))
updater.dispatcher.add_error_handler(error)

# Запуск телеграм-бота
updater.start_polling()
updater.idle()
