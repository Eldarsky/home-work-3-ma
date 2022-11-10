from aiogram import  Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from  decouple import config
import logging
TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher (bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Здравствуйте!! {message.from_user.first_name}")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT',callback_data='button_call_1')
    markup.add(button_call_1)
    question = "в каком году распался ссср"
    answers = [
        "1995",
        '1993',
        '1992',
        '1991',
        '1999',
    ]




    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Правильный ответ '1991",
        reply_markup=markup

    )

@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)


    question = "В каком году умер Сталин ?"
    answers = [
        "1953 г.",
        "1952 г.",
        "1955 г.",
        "1954 г.",
        "1956 г.",
        "1957 г.",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Правильный ответ 1953 г.",
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_2(call: types.CallbackQuery):


    photo = open('media/cover_6.jpg', 'rb')
    await bot.send_photo(call.from_user.id,photo=photo)



@dp.message_handler()
async def echo(message: types.Message):
    try:
        z = message.text
        x = int(z)
        c = x ** 2
        await bot.send_message(message.from_user.id, str(c))
    except:
        await bot.send_message(message.from_user.id, message.text)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates= True)
