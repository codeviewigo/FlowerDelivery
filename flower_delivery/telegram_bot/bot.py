import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, InputFile, FSInputFile
from asgiref.sync import sync_to_async, async_to_sync
from dotenv import load_dotenv

from .models import Manager
from orders.models import Order, OrderItem

from flower_delivery import settings

load_dotenv()

tbot = Bot(token=os.getenv('TELEGRAM_API_TOKEN'))
dp = Dispatcher()


async def run_bot():
    await tbot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(tbot)


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать! Я бот, который проинформирует Вас о новом заказе.\n"
        f"Пожалуйста, сообщите данный код админисратору Интернет-магазина: {message.chat.id}"
    )


class OrderItems:
    pass


def send_order_notification(order: Order, cart):
    managers = Manager.objects.filter(is_active=True)
    items = order.items.all().values('product__name', 'quantity', 'price', 'product__image')

    async_to_sync(send_notification_bot)(order, list(items), list(managers))


async def send_notification_bot(order, items, managers):
    try:
        text = (
            f"Новый заказ #{order.id}\n"
            f"Стоимость: {await sync_to_async(order.get_total_cost)()}\n"
            f"Имя клиента: {order.first_name} {order.last_name}\n"
            f"Место доставки: {order.address}\n\n"
            f"Состав заказа:\n"

        )

        for manager in managers:
            await tbot.send_message(chat_id=manager.chat_id, text=text)

            for item in items:
                product_image_path = os.path.join(settings.MEDIA_ROOT, item['product__image'])

                photo = FSInputFile(product_image_path)

                await tbot.send_photo(
                    chat_id=manager.chat_id,
                    photo=photo,
                    caption=f"{item['product__name']}\n"
                            f"Цена: {item['price']} руб.\n"
                            f"Количество: {item['quantity']}"
                )

    except Exception as e:
        print(f"Error sending notification: {e}")
    finally:
        await tbot.session.close()

# 652264131


# text = (
#     f"Новый заказ #{order.id}\n\n"
#     f"Место доставки: {order.address}\n"
#     f"Стоимость: {order.get_total_cost()}\n"
#     f"Имя клиента: {order.first_name} {order.last_name}\n"
#     f"Комментарий: {order.comment}\n\n"
#     f"Товары:\n"
# )

#    for item in order.items.all():
# text += (
#     f"- {item.product.name}\n"
#     f"  Количество: {item.quantity}\n"
#     f"  Цена за единицу: {item.price} руб.\n"
# )
