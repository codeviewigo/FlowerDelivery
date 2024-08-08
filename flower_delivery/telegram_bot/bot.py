# telegram_bot/bot.py
import os
from telebot import TeleBot
from telegram_bot.models import Manager
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
bot = TeleBot(API_TOKEN)

def send_order_notification(order):
    managers = Manager.objects.filter(is_active=True)
    for manager in managers:
        bot.send_message(
            manager.chat_id,
               f"Новый заказ\nБукет: {order.bouquet.name}\n"
               f"Цена: {order.bouquet.price}\n"
               f"Дата доставки: {order.delivery_date}\n"
               f"Время доставки: {order.delivery_time}\n"
               f"Адрес: {order.address}\n"
               f"Комментарий: {order.comment}"
        )
