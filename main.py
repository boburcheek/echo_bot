from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton

TOKEN = "5811443526:AAF9sm0VsDT-w7wI5xZDx24rwny0u1MtV9Y"
#
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
kb = ReplyKeyboardMarkup(resize_keyboard=True)
ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("👍", callback_data="like")],
    [InlineKeyboardButton("👎", callback_data="dislike")]
])

rkb = ReplyKeyboardMarkup(resize_keyboard=True)
rkb.add(KeyboardButton(text="/help", ))
rkb.add(KeyboardButton(text="/restart"))


# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await message.reply(text="Hello. How are you?")
# #
# @dp.message_handler()
# async def echo_answer(message: types.Message):
#     await message.reply(text=message.text)

# @dp.message_handler()
# async def upper_case(message: types.Message):
#     await message.answer(text=message.text.upper())
# @dp.message_handler(Text(equals="commands"))
# async def get_commands(message: types.Message):
#     text = """
#         /start - start bot
#         /help- help command
#
#     """
#     await message.answer(text=text)

#send_photo, Inline keyboard button, ReplyKeyboarBbutton

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://t.me/abyatun/16745",
                         caption="bu photo sizga yoqdimi",
                         reply_markup=rkb)



@dp.callback_query_handler(text='like')
async def like_button(callback: types.CallbackQuery):
    await callback.answer("you like it")

@dp.callback_query_handler(text='dislike')
async def like_button(callback: types.CallbackQuery):
    await callback.answer("you dislike it")



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)

