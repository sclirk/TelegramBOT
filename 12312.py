import telebot
from telebot import types
import time
import datetime

bot = telebot.TeleBot('TOKEN')
global operation
operation=0

@bot.message_handler(commands=['start'])
def start_message(message):

    markup = types.ReplyKeyboardMarkup(row_width=2)
    ite1 = types.KeyboardButton('/Лицо')
    ite2 = types.KeyboardButton('/Ногти')
    ite3 = types.KeyboardButton('/Волосы')
    markup.add(ite1, ite2, ite3)
    bot.send_message(message.chat.id,'Доброго времени суток! Выберите желаемую процедуру из списка:\n'
                                     '/Лицо - список возможных процедур, осуществляемых на лице\n'
                                     '/Ногти - список возможных процедур, осуществляемых на ногтях\n'
                                     '/Волосы - список возможных процедур, осуществляемых с волосами ', reply_markup=markup)

@bot.message_handler(commands=['Начало'])
def start_message(message):

    markup = types.ReplyKeyboardMarkup(row_width=2)
    ite1 = types.KeyboardButton('/Лицо')
    ite2 = types.KeyboardButton('/Ногти')
    ite3 = types.KeyboardButton('/Волосы')
    markup.add(ite1, ite2, ite3)
    bot.send_message(message.chat.id,'Доброго времени суток! Выберите желаемую процедуру из списка:\n'
                                     '/Лицо - список возможных процедур, осуществляемых на лице\n'
                                     '/Ногти - список возможных процедур, осуществляемых на ногтях\n'
                                     '/Волосы - список возможных процедур, осуществляемых с волосами ', reply_markup=markup)

@bot.message_handler(commands=['Лицо'])
def send_tex(message):
    bot.send_message(message.chat.id, 'Выберите желаемую процедуру ухода за лицом')
    markup = types.ReplyKeyboardMarkup(row_width=3)
    ite1 = types.KeyboardButton('/Брови')
    ite2 = types.KeyboardButton('/Массаж')
    ite3 = types.KeyboardButton('/Ресницы')
    ite4 = types.KeyboardButton('/Мезотерапия')
    ite5 = types.KeyboardButton('/Парафинотерапия')
    ite6 = types.KeyboardButton('/Пилинг')
    ite7 = types.KeyboardButton('/Чистка')
    ite8 = types.KeyboardButton('/Массаж')
    ite9 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite2, ite3, ite4, ite5, ite6, ite7, ite8, ite9)
    bot.send_message(message.chat.id, 'что-то еще?', reply_markup=markup)

@bot.message_handler(commands=['Брови'])
def send_tex(message):
    global operation
    operation = ['брови']
    bot.send_message(message.chat.id, 'Стоимость операции по работе с бровями=**')
    bot.send_message(message.chat.id, 'Нажмите /Время для продолжения или /Начало для возврата в главное меню')
    markup = types.ReplyKeyboardMarkup(row_width=1)
    ite1 = types.KeyboardButton('/Время')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор!', reply_markup=markup)

@bot.message_handler(commands=['Массаж'])
def send_tex(message):
    global operation
    operation = ['Массаж']
    bot.send_message(message.chat.id, 'Стоимость операции массажа=**')
    bot.send_message(message.chat.id, 'Нажмите /Время для продолжения или /Начало для возврата в главное меню')
    markup = types.ReplyKeyboardMarkup(row_width=1)
    ite1 = types.KeyboardButton('/Время')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор!', reply_markup=markup)

@bot.message_handler(commands=['Ресницы'])
def send_tex(message):
    global operation
    operation = ['Ресницы']
    bot.send_message(message.chat.id, 'Стоимость операции по работе с ресницами**')
    bot.send_message(message.chat.id, 'Нажмите /Время для продолжения или /Начало для возврата в главное меню')
    markup = types.ReplyKeyboardMarkup(row_width=1)
    ite1 = types.KeyboardButton('/Время')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор!', reply_markup=markup)

@bot.message_handler(commands=['Мезотерапия'])
def send_tex(message):
    global operation
    operation = ['Мезотерапия']
    bot.send_message(message.chat.id, 'Стоимость операции мезотерапии:**')
    bot.send_message(message.chat.id, 'Нажмите /Время для продолжения или /Начало для возврата в главное меню')
    markup = types.ReplyKeyboardMarkup(row_width=1)
    ite1 = types.KeyboardButton('/Время')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор!', reply_markup=markup)

@bot.message_handler(commands=['Парафинотерапия'])
def send_tex(message):
    global operation
    operation = ['Парафинотерапия']
    bot.send_message(message.chat.id, 'Стоимость операции парафинотерапии=**')
    bot.send_message(message.chat.id, 'Нажмите /Время для продолжения или /Начало для возврата в главное меню')
    markup = types.ReplyKeyboardMarkup(row_width=1)
    ite1 = types.KeyboardButton('/Время')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор!', reply_markup=markup)

@bot.message_handler(commands=['Пилинг'])
def send_tex(message):
    global operation
    operation = ['Пилинг']
    bot.send_message(message.chat.id, 'Стоимость операции пилинга=**')
    bot.send_message(message.chat.id, 'Нажмите /Время для продолжения или /Начало для возврата в главное меню')
    markup = types.ReplyKeyboardMarkup(row_width=1)
    ite1 = types.KeyboardButton('/Время')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор!', reply_markup=markup)

@bot.message_handler(commands=['Чистка'])
def send_tex(message):
    global operation
    operation = ['Чистка']
    bot.send_message(message.chat.id, 'Стоимость чистки=**')
    bot.send_message(message.chat.id, 'Нажмите /Время для продолжения или /Начало для возврата в главное меню')
    markup = types.ReplyKeyboardMarkup(row_width=1)
    ite1 = types.KeyboardButton('/Время')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор!', reply_markup=markup)

@bot.message_handler(commands=['Массаж'])
def send_tex(message):
    global operation
    operation = ['Массаж']
    bot.send_message(message.chat.id, 'Стоимость массажа=**')
    bot.send_message(message.chat.id, 'Нажмите /Время для продолжения или /Начало для возврата в главное меню')
    markup = types.ReplyKeyboardMarkup(row_width=1)
    ite1 = types.KeyboardButton('/Время')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор!', reply_markup=markup)

@bot.message_handler(commands=['Волосы'])
def send_tex(message):
    bot.send_message(message.chat.id, 'Выберите желаемую процедуру ухода за волосами')
    markup = types.ReplyKeyboardMarkup(row_width=3)
    ite1 = types.KeyboardButton('/пусто')
    ite2 = types.KeyboardButton('/пусто...')
    ite3 = types.KeyboardButton('/совсем пусто(')
    ite4=types.KeyboardButton('/Начало')
    markup.add(ite1, ite2, ite3,ite4)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор!', reply_markup=markup)

@bot.message_handler(commands=['Ногти'])
def send_tex(message):
    bot.send_message(message.chat.id, 'Выберите желаемую процедуру ухода за ногтями')
    markup = types.ReplyKeyboardMarkup(row_width=1)
    ite1 = types.KeyboardButton('/Маникюр')
    ite2 = types.KeyboardButton('/Педикюр')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite2, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор!', reply_markup=markup)

@bot.message_handler(commands=['Маникюр'])
def send_tex(message):
    bot.send_message(message.chat.id, 'стоимость маникюра = **'
                                      '\n выбирите желаемый вариант: с гелем - /Гель'
                                      '\n с лаком- /Лак')

    markup = types.ReplyKeyboardMarkup(row_width=2)
    ite1 = types.KeyboardButton('/Гель')
    ite2 = types.KeyboardButton('/Лак')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite2, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор! ', reply_markup=markup)

@bot.message_handler(commands=['Гель'])
def send_tex(message):
    global operation
    operation = ['Маникюр с Гелем']
    bot.send_message(message.chat.id, 'стоимость маникюра с гелем =**'
                                      '\n сообщите боту удобное для вас время и свой номер телефона')
    markup = types.ReplyKeyboardMarkup(row_width=2)
    ite1 = types.KeyboardButton('/Время')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор! ', reply_markup=markup)

@bot.message_handler(commands=['Лак'])
def send_tex(message):
    global operation
    operation = ['Маникюр с Лаком']
    bot.send_message(message.chat.id, 'стоимость маникюра с лаком =**'
                                      '\n сообщите боту удобное для вас время и свой номер телефона')
    markup = types.ReplyKeyboardMarkup(row_width=2)
    ite1 = types.KeyboardButton('/Время')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор! ', reply_markup=markup)

@bot.message_handler(commands=['Педикюр'])
def send_tex(message):
    bot.send_message(message.chat.id, 'стоимость маникюра = **'
                                      '\n выбирите желаемый вариант: с гелем - /гель'
                                      '\n с лаком- /лак')

    markup = types.ReplyKeyboardMarkup(row_width=2)
    ite1 = types.KeyboardButton('/гель')
    ite2 = types.KeyboardButton('/лак')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite2, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор! ', reply_markup=markup)

@bot.message_handler(commands=['гель'])
def send_tex(message):
    global operation
    operation = ['Педикюр с Гелем']
    bot.send_message(message.chat.id, 'стоимость педикюра с гелем =**'
                                      '\n сообщите боту удобное для вас время и свой номер телефона')
    markup = types.ReplyKeyboardMarkup(row_width=2)
    ite1 = types.KeyboardButton('/Время')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор! ', reply_markup=markup)

@bot.message_handler(commands=['лак'])
def send_tex(message):
    global operation
    operation = ['Педикюр с Лаком']
    bot.send_message(message.chat.id, 'стоимость педикюра с лаком =**'
                                      '\n сообщите боту удобное для вас время и свой номер телефона')
    markup = types.ReplyKeyboardMarkup(row_width=2)
    ite1 = types.KeyboardButton('/Время')
    ite3 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite3)
    bot.send_message(message.chat.id, 'Спасибо за Ваш выбор! ', reply_markup=markup)

@bot.message_handler(commands=['Время'])
def send_tex(message):
    bot.send_message(message.chat.id, 'выберите один из 4-х возможных варинтов ')
    markup = types.ReplyKeyboardMarkup(row_width=2)
    ite1 = types.KeyboardButton('9:00-12:00')
    ite2 = types.KeyboardButton('12:00-14:00')
    ite3 = types.KeyboardButton('14:00-16:00')
    ite4 = types.KeyboardButton('16:00-19:00')
    ite5 = types.KeyboardButton('/Начало')
    markup.add(ite1, ite2, ite3, ite4,ite5)
    bot.send_message(message.chat.id, 'оставьте свой номер телефона боту', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def send_mess(message):
    if message.text == '9:00-12:00':
        global operation
        markup = types.ReplyKeyboardMarkup(row_width=2)
        ite1 = types.KeyboardButton('оставить свой телефон',request_contact=True)
        ite2 = types.KeyboardButton('/Начало')
        markup.add(ite1,ite2)
        bot.send_message(message.chat.id, 'оставьте номер телефона', reply_markup=markup)
        name = message.from_user.first_name
        name1=str(message.from_user.id)
        opi = open('zapis.txt', 'a').write('\n\nимя пользователя: '+name+ ' предпочтительное время: '+message.text+" Название работы: "+ str(operation)+ " ID пользователя: "+name1+' время получения заявки: '+str(datetime.datetime.now()) +' номер пользователя  ')
        bot.send_message(message.chat.id, '  ', reply_markup=opi)
    if message.text == '12:00-14:00':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        ite1 = types.KeyboardButton('оставить свой телефон',request_contact=True)
        ite2 = types.KeyboardButton('/Начало')
        markup.add(ite1,ite2)
        bot.send_message(message.chat.id, 'оставьте номер телефона', reply_markup=markup)
        name = message.from_user.first_name
        name1=str(message.from_user.id)
        opi = open('zapis.txt', 'a').write('\n\nимя пользователя: '+name+ ' предпочтительное время: '+message.text+" Название работы: "+ str(operation)+ " ID пользователя: "+name1+' время получения заявки: '+str(datetime.datetime.now()) +' номер пользователя  ')
        bot.send_message(message.chat.id, '  ', reply_markup=opi)
    if message.text == '14:00-16:00':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        ite1 = types.KeyboardButton('оставить свой телефон',request_contact=True)
        ite2 = types.KeyboardButton('/Начало')
        markup.add(ite1,ite2)
        bot.send_message(message.chat.id, 'оставьте номер телефона', reply_markup=markup)
        name = message.from_user.first_name
        name1=str(message.from_user.id)
        opi = open('zapis.txt', 'a').write('\n\nимя пользователя: '+name+ ' предпочтительное время: '+message.text+" Название работы: "+ str(operation)+ " ID пользователя: "+name1+' время получения заявки: '+str(datetime.datetime.now()) +' номер пользователя  ')
        bot.send_message(message.chat.id, '  ', reply_markup=opi)
    if message.text == '16:00-19:00':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        ite1 = types.KeyboardButton('оставить свой телефон',request_contact=True)
        ite2 = types.KeyboardButton('/Начало')
        markup.add(ite1,ite2)
        bot.send_message(message.chat.id, 'оставьте номер телефона', reply_markup=markup)
        name = message.from_user.first_name
        name1=str(message.from_user.id)
        opi = open('zapis.txt', 'a').write('\n\nимя пользователя: '+name+ ' предпочтительное время: '+message.text+" Название работы: "+ str(operation)+ " ID пользователя: "+name1+' время получения заявки: '+str(datetime.datetime.now()) +' номер пользователя  ')
        bot.send_message(message.chat.id, '  ', reply_markup=opi)
    else:
        txt=message.text
        name = message.from_user.first_name
        name1=str(message.from_user.id)
        name2=str(message.from_user.last_name)
        name3=str(message.from_user.username)
        open('note_from_zapis_bot.txt', 'a').write('\nимя польз: '+name+' написал нам: '+txt+' ID человека: '+name1+" Фамилия: "+name2+" Никнейм: "+name3+' время отправки сообщения: '+str(datetime.datetime.now()))

@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    open('zapis.txt', 'a').write(message.contact.phone_number)
    bot.send_message(message.chat.id, ' Спасибо, ваша заявка принята, хорошего дня')

if __name__ == '__main__':
    bot.polling(none_stop=True)
