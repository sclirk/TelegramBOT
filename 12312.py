from telebot import TeleBot
from telebot import types

import mysql.connector

from random import randint

import datetime


class connector:
    def __init__(self):
        self.myConnection = mysql.connector.connect(host="127.0.0.1",
                                                    user='root',
                                                    passwd='1111',
                                                    db='sclick_schema')
        self.bot = TeleBot('815071611:AAH5oTHw-ao0Q35WYHexfwMm-0p0WIvtR_o')
        self.quest = 0


class bot(connector):
    def __init__(self):
        super().__init__()

    def bot_funk(self):
        @self.bot.message_handler(commands=["start"])
        def send_mess(message):
            def click(conn):
                mycursor = conn.cursor()
                sql = "INSERT INTO new_table (id_users, clicks_per_day, username,  level, ratio) VALUES (%s, %s, %s, %s, %s)"
                val = ("{}".format(message.from_user.id), "{}".format(0), "{}".format(message.from_user.first_name),
                       "{}".format(0), 10)
                mycursor.execute(sql, val)
                self.myConnection.commit()
                self.bot.send_message(message.chat.id, " Добро пожаловать в систему,"
                                                       " {} !".format(message.from_user.first_name))

            try:
                click(self.myConnection)
            except Exception:
                self.bot.send_message(message.chat.id,
                                      "Добро пожаловать снова, {}".format(message.from_user.first_name))
            markup = types.ReplyKeyboardMarkup(row_width=2)
            ite1 = types.KeyboardButton('Курсы')
            ite2 = types.KeyboardButton('Информация')
            ite3 = types.KeyboardButton('Игра')
            markup.add(ite1, ite2, ite3)
            self.bot.send_message(message.chat.id,
                                  'Доброго времени суток! Бот предоставит вам возможность ознакомиться '
                                  'с содержанием курсов путем отправки Вам пробного урока\n',
                                  reply_markup=markup)

    def text_bot(self):
        @self.bot.message_handler(content_types=['text'])
        def send_tex(message):
            if message.text == "номер":
                markup = types.ReplyKeyboardMarkup(row_width=2)
                ite1 = types.KeyboardButton('оставить свой телефон', request_contact=True)
                ite2 = types.KeyboardButton('/start')
                markup.add(ite1, ite2)
                self.bot.send_message(message.chat.id, " слыш", reply_markup=markup)
            if message.text == "где я?":
                markup = types.ReplyKeyboardMarkup(row_width=2)
                ite1 = types.KeyboardButton('передать свои геоданные', request_location=True)
                ite2 = types.KeyboardButton('/start')
                markup.add(ite2, ite1)
                self.bot.send_message(message.chat.id, " локация", reply_markup=markup)
            global completed
            if message.text == "Игра":
                markup = types.ReplyKeyboardMarkup(row_width=2)
                ite1 = types.KeyboardButton('Счёт')
                ite3 = types.KeyboardButton('Узнать уровень')
                ite2 = types.KeyboardButton('Задача')
                ite4 = types.KeyboardButton('Купить левел')
                ite5 = types.KeyboardButton('/start')
                markup.add(ite1, ite2, ite3, ite5, ite4)
                self.bot.send_message(message.chat.id, 'выберите один из возможных варинтов \n'
                                                       'или нажмите /start для'
                                                       ' взвращения на главную страницу', reply_markup=markup)

            if message.text == "Узнать уровень":
                cursor = self.myConnection.cursor()
                cursor.execute("select level,ratio from sclick_schema.new_table "
                               "where id_users = '{}'".format(message.from_user.id))
                for level, ratio in cursor.fetchall():
                    self.bot.send_message(message.chat.id, 'Ваш нынешний уровень равен {}'.format(level))

            if message.text == "Купить левел":
                markup = types.ReplyKeyboardMarkup(row_width=2)
                ite1 = types.KeyboardButton('Обменять за решенные задачи')
                ite2 = types.KeyboardButton('Купить за наличные')
                ite3 = types.KeyboardButton('Игра')
                ite5 = types.KeyboardButton('/start')
                markup.add(ite1, ite2, ite5, ite3)
                self.bot.send_message(message.chat.id, 'выберите один из 2-х возможных варинтов \n'
                                                       'или нажмите /start для'
                                                       ' взвращения на главную страницу', reply_markup=markup)

            if message.text == "Обменять за решенные задачи":
                markup = types.ReplyKeyboardMarkup(row_width=2)
                ite1 = types.KeyboardButton('Продолжить обмен')
                ite3 = types.KeyboardButton('/start')
                ite4 = types.KeyboardButton('Игра')
                markup.add(ite1, ite3, ite4)
                self.bot.send_message(message.chat.id, "Внимание!\n"
                                                       "если вы приобритете уровень, ниже своего, то ваш конечный уровень"
                                                       "будет равен последнему приобретенному", reply_markup=markup)
                first_click = self.myConnection.cursor()
                first_click.execute("select clicks_per_day,ratio  from sclick_schema.new_table"
                                    " where id_users = '{}'".format(message.from_user.id))
                for clicks, ratio_1 in first_click.fetchall():
                    self.bot.send_message(message.chat.id, "у вас {} задач, этого"
                                                           " хватит на покупку: {} уровня".format(clicks,
                                                                                                  clicks // int(
                                                                                                      ratio_1)))

            if message.text == "Продолжить обмен":
                first_click = self.myConnection.cursor()
                first_click.execute("select clicks_per_day,ratio  from sclick_schema.new_table"
                                    " where id_users = '{}'".format(message.from_user.id))
                for clicks, ratio_1 in first_click.fetchall():
                    if clicks // int(ratio_1) == 0:
                        first_click.execute("select level,ratio from sclick_schema.new_table "
                                            "where id_users = '{}'".format(message.from_user.id))
                        for lev, rat in first_click.fetchall():
                            self.bot.send_message(message.chat.id, "вы и так имеете {} уровень,"
                                                                   " поднакопите задач на следующий)".format(lev))
                    else:
                        second_click = self.myConnection.cursor()
                        second_click.execute("UPDATE new_table"
                                             " set clicks_per_day = '{}',"
                                             " level = '{}'"
                                             " WHERE (id_users = '{}');".format(clicks - clicks // int(ratio_1) * 10,
                                                                                clicks // int(ratio_1),
                                                                                message.from_user.id))
                        self.bot.send_message(message.chat.id, "Поздравялем! Вы приобрели {}"
                                                               " уровень доступа!\n"
                                              .format(clicks // int(ratio_1)))

                self.myConnection.commit()

            if message.text == "Задача":
                completed = 0

                def question():
                    global a, b, c, znak, second_znak
                    a = randint(1, 25)
                    b = randint(10, 35)
                    c = randint(1, 10)
                    znak = randint(0, 1)
                    second_znak = randint(0, 1)
                    if znak == 1 and second_znak == 1:
                        second_znak = "+"
                        znak = '+'
                        self.quest = a + b + c
                    if znak == 0 and second_znak == 1:
                        second_znak = "+"
                        znak = "-"
                        self.quest = a - b + c
                    if znak == 1 and second_znak == 0:
                        second_znak = "-"
                        znak = "+"
                        self.quest = a + b - c
                    if znak == 0 and second_znak == 0:
                        second_znak = "-"
                        znak = "-"
                        self.quest = a - b - c

                question()
                self.bot.send_message(message.chat.id, "{}{}{}{}{}".format(a, znak, b, second_znak, c))

            if message.text == "{}".format(self.quest):
                if completed == 0:
                    completed = 1
                    first_click = self.myConnection.cursor()
                    first_click.execute("select clicks_per_day, username from sclick_schema.new_table"
                                        " where id_users = '{}'".format(message.from_user.id))
                    for clicks, name_user in first_click.fetchall():
                        if clicks >= 30:
                            self.bot.send_message(message.chat.id, 'максимальное количество доступных задач = 30')
                        else:
                            self.bot.send_message(message.chat.id, "+1 за сегодня, итого: "
                                                                   "{} решенных задач у '{}'".format(clicks + 1,
                                                                                                     name_user))
                            second_click = self.myConnection.cursor()
                            second_click.execute("UPDATE new_table"
                                                 " set clicks_per_day = '{}'"
                                                 " WHERE (id_users = '{}');".format(clicks + 1, message.from_user.id))

                    self.myConnection.commit()
                else:
                    self.bot.send_message(message.chat.id, "Вы уже отвечали на этот вопрос")

            if message.text == "Счёт":
                def doQuery():
                    cur = self.myConnection.cursor()
                    cur.execute("select clicks_per_day,username from sclick_schema.new_table where"
                                " id_users = {}".format(message.from_user.id))
                    for point, name_of_user in cur.fetchall():
                        self.bot.send_message(message.chat.id, 'Имя: {} общий счет составляет'
                                                               ' {} поитов'.format(name_of_user, point))

                doQuery()

            if message.text == "Информация":
                self.bot.send_message(message.chat.id,
                                      "Курсы являются платной версией курсов с оригинальных источников\n"
                                      "Выберите раздел 'Курсы' для продолжения\n"
                                      " Бот так же может отправить Вам всю информацию"
                                      " о стикере, если вы ему его отправите)"
                                      " \nнапишите номер, если хотите чтобы мы вам перезвонили\n"
                                      "или напишиите 'где я?' чтобы узнать свое местоположение")

            if message.text == "Обмен задач":
                def exchange():
                    second_click = self.myConnection.cursor()
                    second_click.execute("UPDATE new_table"
                                         " set clicks_per_day = clicks_per_day/ratio as coefficient,"
                                         " level = level + coefficient"
                                         " WHERE (id_users = '{}');".format(message.from_user.id))
                    self.myConnection.commit()

                exchange()

            if message.text == "Курсы" or message.text == "Вернуться":
                markup = types.ReplyKeyboardMarkup(row_width=2)
                ite1 = types.KeyboardButton('Курсы С#')
                ite2 = types.KeyboardButton('Курсы С++')
                ite3 = types.KeyboardButton('Курсы HTML/CSS')
                ite4 = types.KeyboardButton('Курсы JS')
                ite5 = types.KeyboardButton('/start')
                markup.add(ite1, ite2, ite3, ite4, ite5)
                self.bot.send_message(message.chat.id, 'выберите один из 4-х возможных варинтов \n'
                                                       'или нажмите /start для взвращения'
                                                       ' на главную страницу', reply_markup=markup)

            if message.text == "Курсы JS" or message.text == "Вернуться на выбор курсов JS":
                markup = types.ReplyKeyboardMarkup(row_width=2)
                ite1 = types.KeyboardButton('Курсы C# HTML Academy')
                ite2 = types.KeyboardButton('Курсы от Академии Верстки')
                ite3 = types.KeyboardButton('Телеграм боты на JC')
                ite4 = types.KeyboardButton('Курсы C# от ...')
                ite5 = types.KeyboardButton('Вернуться')
                markup.add(ite1, ite2, ite3, ite4, ite5)
                self.bot.send_message(message.chat.id, 'выберите один из 4-х возможных варинтов ', reply_markup=markup)

            if message.text == "Курсы C# HTML Academy":
                markup = types.ReplyKeyboardMarkup(row_width=2)
                ite1 = types.KeyboardButton('JS base')
                ite2 = types.KeyboardButton('JS Advanced')
                ite5 = types.KeyboardButton('Вернуться на выбор курсов JS')
                markup.add(ite1, ite2, ite5)
                self.bot.send_message(message.chat.id, 'выберите один из 3-х возможных варинтов ', reply_markup=markup)

            if message.text == "Курсы Android":
                markup = types.ReplyKeyboardMarkup(row_width=2)
                ite1 = types.KeyboardButton('Курсы Android от ...')
                ite5 = types.KeyboardButton('Вернуться')
                markup.add(ite1, ite5)
                self.bot.send_message(message.chat.id, 'выберите один из 4-х возможных варинтов ', reply_markup=markup)

            if message.text == "Курсы С#":
                markup = types.ReplyKeyboardMarkup(row_width=2)
                ite1 = types.KeyboardButton('Курсы C# Base')
                ite2 = types.KeyboardButton('Курсы C# professional')
                ite5 = types.KeyboardButton('Вернуться')
                markup.add(ite1, ite2, ite5)
                self.bot.send_message(message.chat.id, 'выберите один из 4-х возможных варинтов ', reply_markup=markup)

            if message.text == "Курсы HTML/CSS" or message.text == 'Вернуться к выбору HTML/CSS':
                markup = types.ReplyKeyboardMarkup(row_width=2)
                ite1 = types.KeyboardButton('Курсы HTML Academy')
                ite2 = types.KeyboardButton('Курсы Udemy')
                ite3 = types.KeyboardButton('Курсы "Типичный верстальщик"')
                ite4 = types.KeyboardButton('Курсы Citvdn')
                ite5 = types.KeyboardButton('Вернуться')
                markup.add(ite1, ite2, ite3, ite4, ite5)
                self.bot.send_message(message.chat.id, 'выберите один из 4-х возможных варинтов ', reply_markup=markup)

            if message.text == "Курсы HTML Academy":
                markup = types.ReplyKeyboardMarkup(row_width=2)
                ite1 = types.KeyboardButton('Курсы "Типичный верстальщик"')
                ite2 = types.KeyboardButton('Вернуться к выбору HTML/CSS')
                markup.add(ite1, ite2)
                self.bot.send_message(message.chat.id, 'выберите один из 2-х возможных варинтов ', reply_markup=markup)

            if message.text == 'Курсы C# от источник':
                doc = open("ist_01.txt")
                self.bot.send_document(message.from_user.id, doc)

            try:
                ranger = list(range(100))
                if int(message.text) in ranger or int(message.text) != self.quest:
                    self.bot.send_sticker(message.chat.id,
                                          'CAACAgIAAxkBAAIYll5j-fip9YzaPty-15f5mHd3dIGqAAJFAAOgayEa6Tj_AjvcOO8YBA')
                    self.bot.send_sticker(message.chat.id,
                                          'CAACAgIAAxkBAAIYl15j-fkIYAyfR2b5Zt8BKsaE3lUqAAI8AAOgayEapmwggmFMObEYBA')
                    self.bot.send_message(message.chat.id, 'Неправильный ответ!')

                    self.bot.send_audio(message.chat.id, open("B:/sirena.mp3", "rb"))
                    self.bot.send_audio(message.chat.id, open("B:/asshole.mp3", "rb"))
                    self.bot.send_audio(message.chat.id, open("B:/bad_joke.mp3", "rb"))
            except Exception:
                pass
            else:
                open('zapiski_boty.txt', 'a').write(
                    '\nимя польз: ' + message.from_user.first_name + ' написал нам: ' + message.text +
                    ' ID человека: ' + str(message.from_user.id) + " Никнейм: " + str(message.from_user.username) +
                    ' время отправки сообщения: ' + str(datetime.datetime.now()))

    def sticker_bot(self):
        @self.bot.message_handler(content_types=['sticker'])
        def sell_sticker(message):
            self.bot.send_message(message.chat.id, 'Эмоция стикера:' + message.sticker.emoji +
                                  '\nАйди стикера: ' + message.sticker.file_id)

    def phone(self):
        @self.bot.message_handler(content_types=['contact'])
        def number(message):
            open('number_users.txt', 'a').write('\n' + message.contact.phone_number + ' имя:' + str(message.from_user.username))
            self.bot.send_message(message.chat.id, ' Номер записан, спасибо за понимание')

    def locate(self):
        @self.bot.message_handler(content_types=['location'])
        def locate(message):
            self.bot.send_message(message.chat.id, "широта вашего места:" + message.location.latitude)
            self.bot.send_message(message.chat.id, "долгота вашего места" + message.location.longitude)

    def non_stop(self):
        self.bot.polling(none_stop=True)


b = bot()
b.sticker_bot(), b.bot_funk(), b.text_bot(), b.phone(), b.locate(), b.non_stop()
