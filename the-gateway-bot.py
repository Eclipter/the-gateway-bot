import openai
import logging

from aiogram import Bot, Dispatcher, executor, types
from settings import TELEGRAM_BOT_API_KEY, OPENAI_API_KEY

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_API_KEY)
openai.api_key = OPENAI_API_KEY
dp = Dispatcher(bot)


async def chat_cmd_handler(message: types.Message):
    """Responds to a chat command by generating a response with OpenAI's GPT-3 model."""
    prompt_text = message.get_args()
    model_engine = "text-davinci-003"
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_text,
        max_tokens=1024,
        stop=None,
        temperature=0
    )
    response = completion.choices[0].text
    await message.reply(response)

dp.register_message_handler(chat_cmd_handler, commands=['chat'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
