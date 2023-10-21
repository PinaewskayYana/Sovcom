
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from config import config
from handlers import registrat, entry, common, workphoto, admin

logging.basicConfig(level=logging.INFO)
async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_router(registrat.router)
    dp.include_router(entry.router)
    dp.include_router(common.router)
    dp.include_router(workphoto.router)
    dp.include_router(admin.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
 
    
'''
async def main():
    await dp.start_polling(bot)
'''

if __name__ == "__main__":
    asyncio.run(main())
'''
    @dp.message(F.photo)
    async def download_photo(message: types.Message, bot: Bot):
        await bot.download(
            message.photo[-1],
            destination=f"/photoes/{message.photo[-1].file_id}.jpg"
        )
 '''