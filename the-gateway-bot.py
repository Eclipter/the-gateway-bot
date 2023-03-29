import openai
import logging

from aiogram import Bot, Dispatcher, executor, types
from settings import TELEGRAM_BOT_API_KEY, OPENAI_API_KEY

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_API_KEY)
dp = Dispatcher(bot)
openai.api_key = OPENAI_API_KEY


async def chat_cmd_handler(message: types.Message):
    """Responds to a chat command by generating a response with OpenAI's GPT-3 model."""
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.get_args(),
        max_tokens=4096,
        stop=None,
        temperature=0
    )

    await message.answer('Генерирую ответ ...')
    response = completion.choices[0].text
    await message.reply(response)

dp.register_message_handler(chat_cmd_handler, commands=['chat'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
