import random
import os
import asyncio


from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv

from prompts import NABOKOV_PROMPT

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "Привет ✨\n"
        "Я пишу стихи в стиле Владимира Набокова.\n\n"
        "Напиши тему — образ, чувство или воспоминание."
    )


def query_hf(theme: str) -> str:
    poems = [

        (
            f"Я помню {theme.lower()}, словно это было вчера.\n"
            "День оседал на подоконниках тишиной,\n"
            "и время шло осторожно, не спеша.\n\n"
            "Слова теряли форму в воздухе,\n"
            "мысли становились легче дыхания.\n"
            "Каждый шаг отзывался эхом,\n"
            "которое не хотело исчезать.\n\n"
            "Между тогда и сейчас — пауза,\n"
            "в которой всё ещё можно остаться,\n"
            "и прошлое смотрит издалека,\n"
            "не требуя ответа."
        ),

        (
            f"{theme.capitalize()} возвращается внезапно,\n"
            "как отражение в тёмном стекле.\n"
            "Память движется медленно,\n"
            "оставляя следы на поверхности дня.\n\n"
            "В этом мгновении нет слов,\n"
            "есть только ощущение хрупкости.\n"
            "Вещи стоят на своих местах,\n"
            "но время давно ушло вперёд.\n\n"
            "И всё, что остаётся —\n"
            "принять это тихое знание,\n"
            "не пытаясь его удержать."
        ),

        (
            f"{theme.capitalize()} — не событие,\n"
            "а состояние между вдохом и паузой.\n"
            "Оно живёт в неровном свете,\n"
            "где прошлое не имеет имени.\n\n"
            "Шаги растворяются в пространстве,\n"
            "мысли касаются друг друга вскользь.\n"
            "Каждый жест кажется знаком,\n"
            "но смысл ускользает.\n\n"
            "И всё же в этом есть ясность —\n"
            "тихая, как вечер,\n"
            "который не ждёт объяснений."
        )
    ]

    return random.choice(poems)


@dp.message()
async def generate_poem(message: types.Message):
    theme = message.text

    await message.answer("Пишу стих… ✍️")

    poem = query_hf(theme)
    await message.answer(poem)



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
