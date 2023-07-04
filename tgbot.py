from aiogram import executor
from create_bot import dp

## Client Side

async def on_startup(_):
    print('Bot online')


from handlers import client, admin, other


client.register_handler_client(dp)
admin.register_handler_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
