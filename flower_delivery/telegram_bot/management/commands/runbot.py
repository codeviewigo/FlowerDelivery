# telegram_bot/management/commands/runbot.py
import asyncio
from django.core.management.base import BaseCommand
from telegram_bot.bot import run_bot

class Command(BaseCommand):
    help = 'Запуск Telegram бота'

    def handle(self, *args, **kwargs):
        try:
            asyncio.run(run_bot())
        except KeyboardInterrupt:
            print('Бот остановлен пользователем!')
