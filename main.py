import subprocess
import telebot

# Замените 'YOUR_BOT_TOKEN' на токен, который вы получили от @BotFather
TOKEN = '6072402897:AAHRUjm80GsUWrh_wKJLFSX6rYfrq98AYhY'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

delimiter = 'DeLiMiTeR'
command_delimiter = 'echo ' + delimiter

commands = ['cd']

@bot.message_handler(func=lambda message: True)
def run_command(message):
    # Получаем текст сообщения от пользователя
    command = message.text.strip()
    print("running", command)
    commands.append(command)

    try:
        # Выполняем команду на сервере и получаем результат
        curr_command = (" && " + command_delimiter + " && ").join(commands)
        all_results = subprocess.check_output(curr_command, shell=True, text=True).split(delimiter)
        result = all_results[-1].strip()
        print("output:", result, '\n')
        if result:  # Проверяем, что результат не пустой
            bot.reply_to(message, result)
        else:
            bot.reply_to(message, "clear output")
    except Exception as e:
        bot.reply_to(message, f"exception: {str(e)}")

# Запускаем бота
bot.polling()









