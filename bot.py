import time
from multiprocessing import Lock
from random import random, randrange
import telebot
import matplotlib.pyplot as plt
import psycopg2
import os
import pandas as pd
import pandas.io.sql as sqlio

from telebot import types

bot = telebot.TeleBot("bot code here")
lock = Lock()
conn = psycopg2.connect(
    host="localhost",
    database="stock_predicting",
    user="stock",
    password="stock",
    port="5433"
)
cursor = conn.cursor()


def select_from_company():
    return sqlio.read_sql_query('select id, ticker from companies', conn)


def select_quote(company_id, date_time):
    return sqlio.read_sql_query(f'select date_, time_, open_ from quotes where company_id = {company_id} and date_<\'{date_time}\'::date order by date_ desc, time_ desc limit 100;', conn)


def select_news(company_id):
    return sqlio.read_sql_query(
        f'select news.id, news.content, news.title, news.date_time from news left join craudsource c on news.id = c.news_id where c.news_id IS NULL and news.company_id={company_id}', conn
    )

def insert_craudsource(news_id, positive, negative, neutral):
    cursor.execute(f'insert into craudsource(news_id, positive, negative, neutral) values ({news_id}, {positive}, {negative}, {neutral})')
    conn.commit()
    pass



@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    send_task(chat_id)
    pass


@bot.callback_query_handler(func=lambda call: True)
def save_answer(call):
    data = call.data.split(', ')
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=None)
    positive = 0
    negative = 0
    neutral = 0
    if data[0] == '1':
        positive = 1
    elif data[0] == '2':
        negative = 1
    else:
        neutral = 1
    insert_craudsource(data[1], positive, negative, neutral)

    send_task(call.from_user.id)
    pass


def send_task(chat_id):
    with lock:
        companies = select_from_company()
        company_id = companies.loc[randrange(companies.shape[0]), 'id']

        news = select_news(company_id)
        news_id = news.loc[randrange(news.shape[0]), 'id']
        news_item = news.loc[news['id'] == news_id]
        news_date_time = news_item.iloc[0]['date_time']

        quotes = select_quote(company_id, news_date_time)
        quotes.loc[:, 'date_time'] = pd.to_datetime(quotes['date_'].astype(str) + ' ' + quotes['time_'].astype(str))

        fig = plt.figure()
        plt.plot(quotes['date_time'], quotes['open_'])
        plt.ylabel('price')
        plt.xticks(rotation=45)
        filename = f'plot{chat_id}.png'
        fig.savefig(filename)
        fig.clf()

        photo = open(filename, "rb")
        topic = news_item.iloc[0]['title']
        news_text = news_item.iloc[0]['content']
        text = f"\t{topic}" \
               f"\n\t{news_text}"

        markup = types.InlineKeyboardMarkup(row_width=3)
        item_1 = types.InlineKeyboardButton('buy', callback_data=f'1, {news_id}')
        item_2 = types.InlineKeyboardButton("save", callback_data=f'2, {news_id}')
        item_3 = types.InlineKeyboardButton("sell", callback_data=f'3, {news_id}')
        markup.add(item_1, item_2, item_3)

        bot.send_photo(chat_id, photo, caption=text, reply_markup=markup)
        # plt.clf()
        photo.close()
        os.remove(photo.name)
    pass


while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except:
        time.sleep(0.1)
