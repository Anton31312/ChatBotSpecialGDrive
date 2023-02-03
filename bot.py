#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import os 
import sys
import codecs
from telebot import types
import schedule
import time
from datetime import datetime

targetFormat = 'utf-8'
outputDir = 'converted'

TOKEN = '5531806054:AAG_m9EfGaEo74w033LQMa4aoLftzxeFDbQ'
bot = telebot.TeleBot('TOKEN');
photo_planarea = 'https://disk.yandex.ru/i/iyyblTQDl0K5Gg'
photo_timetable = 'https://disk.yandex.ru/i/XZfy9bzYsVp_Iw'
photo_results = 'https://disk.yandex.ru/i/hmDl3nmFDqn5uQ'
photo_zones = 'https://disk.yandex.ru/i/19ZnNaGoV0mw0w'
photo_club = 'https://disk.yandex.ru/i/pkl9PpaDWnO64Q'
photo_game = 'https://disk.yandex.ru/i/dTqguiLgyIBQXg'



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_planarea = types.KeyboardButton("\xf0 ОБ АРЕНЕ")
    btn_timetable = types.KeyboardButton("⏰ ОТКРЫТИЕ")
    btn_zones = types.KeyboardButton("🏒 ЗОНЫ АКТИВНОСТЕЙ")
    btn_results = types.KeyboardButton("📷 ФОТОРЕПОРТАЖ")
    btn_club = types.KeyboardButton("🥅 ХК «АВАНГАРД»")
    btn_game = types.KeyboardButton("🎁 РОЗЫГРЫШ")
    markup.add(btn_planarea)
    markup.add(btn_timetable)
    markup.add(btn_zones)
    markup.add(btn_results)
    markup.add(btn_club)
    markup.add(btn_game)
    bot.send_message(message.chat.id, text= "Добро пожаловать в бот G-Drive Arena! 🔥\n\nСегодня это твой персональный путеводитель по G-Drive Арене. С его помощью ты всегда будешь в курсе самых важных событий, происходящих на арене.\n\nВключай уведомления, чтобы ничего не пропустить!" .format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.InlineKeyboardMarkup() 
    if (message.text == "⏰ ОТКРЫТИЕ" or message.text == '/timetable'):
        bot.send_photo(message.chat.id,photo_timetable, caption="Расписание сегодняшнего дня, от входа до финальной сирены!\n\nВ программе тебя ждет торжественная церемония открытия, автограф-сессия с амбассадорами бренда G-Drive, шоу на льду и, конечно, долгожданное #СибирскоеДерби – многолетнее противостояние между двумя крупнейшими хоккейными городами Сибири – Омском и Новосибирском.", reply_markup=keyboard)
        
    elif (message.text == "📣 ОБ АРЕНЕ" or message.text == '/area'):
        keyboard = types.InlineKeyboardMarkup() 
        key_link_area = types.InlineKeyboardButton("ПОДРОБНЕЕ", url='https://telegra.ph/O-G-Drive-Arena-09-29')
        keyboard.add(key_link_area) 
        bot.send_photo(message.chat.id, photo_planarea,caption="G-Drive Арена — новый дом хоккейного клуба «Авангард». Четыре года команда базировалась в подмосковном городе Балашиха, но сейчас она вернулась в родной город, на новую Арену, которая стала одной из самых современных в нашей стране.⬇️️", reply_markup=keyboard)
    
    elif (message.text == "🏒 ЗОНЫ АКТИВНОСТЕЙ" or message.text == '/activation'):
        keyboard = types.InlineKeyboardMarkup()
        key_link_area = types.InlineKeyboardButton("ЗОНЫ АКТИВНОСТЕЙ", url='https://telegra.ph/Zony-aktivnosti-v-G-Drive-Arena-09-29')
        keyboard.add(key_link_area) 
        bot.send_photo(message.chat.id, photo_zones ,caption="️Собрали самые важные точки на  G-Drive Арене. Сегодня важно не пропустить ни одну из локаций!\n\nСмотри где можно перекусить, поучаствовать в гонках на автосимуляторах G-Drive, поиграть в аэрохоккей, посмотреть на гоночные болиды и многое другое ⬇️", reply_markup=keyboard)
    
    elif (message.text == "🥅 ХК «АВАНГАРД»" or message.text == '/club'):
        keyboard = types.InlineKeyboardMarkup() 
        key_link_abonement = types.InlineKeyboardButton("АБОНЕМЕНТ", url='https://season.hawk.ru/?utm_source=telegram&utm_medium=g-drive-arena-bot&utm_campaign=button') 
        key_link_shop = types.InlineKeyboardButton("МАГАЗИН", url='https://shop.hawk.ru/?utm_source=telegram&utm_medium=g-drive-arena-bot&utm_campaign=button') 
        key_link_afisha = types.InlineKeyboardButton("АФИША", url='https://gdrive-arena.ru/afisha/?utm_source=telegram&utm_medium=g-drive-arena-bot&utm_campaign=button') 
        key_link_tickets = types.InlineKeyboardButton("КУПИТЬ БИЛЕТЫ", url='https://tickets.hawk.ru/tickets?utm_source=telegram&utm_medium=g-drive-arena-bot&utm_campaign=button&webTypeId=1&monthText=2022-10')
        keyboard.add(key_link_abonement) 
        keyboard.add(key_link_shop)
        keyboard.add(key_link_afisha)
        keyboard.add(key_link_tickets) 
        bot.send_photo(message.chat.id, photo_club ,caption="️Смотри расписание матчей на сезон и оформляй абонемент, чтобы стать особым гостем на Арене, приобрести индивидуальное место на трибунах и получать скидки на билеты для друзей!\n\nА в фирменном магазине тебя ждут сувениры и одежда с символикой команды. А если приобрести футболку Good Job, можно получить автограф Боба Хартли 😉", reply_markup=keyboard)
    
    elif (message.text == "📷 ФОТОРЕПОРТАЖ" or message.text == '/photo'):
        keyboard = types.InlineKeyboardMarkup()
        key_link_photo = types.InlineKeyboardButton("ФОТО", url='https://disk.yandex.ru/d/iZxCdba3gxHS4g')
        keyboard.add(key_link_photo)
        bot.send_photo(message.chat.id, photo_results, caption="На Арене работает фотограф, найди его и он сделает крутые снимки с тобой. 📸\n\nСохраняем на память эмоции, делимся ими в социальных сетях и не забываем отмечать G-Drive Арену! 🔥", reply_markup=keyboard)
    
    elif (message.text == "🎁 РОЗЫГРЫШ" or message.text == '/game'):
        keyboard = types.InlineKeyboardMarkup()
        key_link_game = types.InlineKeyboardButton("УЧАСТВУЮ!", url='https://forms.gle/AnaS4V9W31mqpT9h8')
        keyboard.add(key_link_game) 
        bot.send_photo(message.chat.id, photo_game ,caption="Уникальная возможность выиграть билеты на открытие Арены Возможностей и насладиться игрой на креслах G-Drive 🎉", reply_markup=keyboard)

bot.polling(none_stop=True)

