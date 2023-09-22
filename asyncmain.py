#Thiết kế UI 1 bên danh sách token. 1 bên web nhúng của bên check. Table tab2 (1 bên danh sách ví, 1 bên list token)

from telethon.sync import TelegramClient, events
from PyQt5 import QtWidgets
from BotScannerTool import BotScannerToolWindow
import arrow
import threading
import sys
import asyncio
import time
import os
import logging
from PyQt5 import QtCore, QtWidgets
from EventBus import EventBus
api_id = '27535321'
api_hash = '7b915080f6c41357c2ad84ca6e84614a'
chanelId = -1001192416115
chanelName = 'PancakeswapLiquidity'
limit = 200
#open("token.txt", "w").close()
#client = TelegramClient('bot', api_id, api_hash)
# Configure the logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

async def listenTelegram(event_bus):
    print('dzo here')
    # await client.start()
    # try: assert await client.connect()
    # except Exception as e: print(str(e))
    # async for messageInterface in client.iter_messages('PancakeswapLiquidity', limit):
    #     message = messageInterface.message
    #     if " 0x" in message:
    #         tokenKey = str(message[message.index(" 0x"):(message.index(" 0x") + 43)]).replace(" ", "")
    #         amount = message[message.index("amount"):(message.index("amount") + 17)]
    #         isSwap = False
    #         if "Tests passed" in message:
    #             isSwap = True
    #         date = arrow.get(messageInterface.date).to('local').format()
    #         open("token.txt", 'a+').write("%s|%s|%s|%s\n"%(tokenKey, amount, isSwap, date))

    # time.sleep(2)
    # event_bus.publish("updateData")
    # @client.on(events.NewMessage(chats=[-1001192416115]))
    # async def my_event_handler(event):
    #     message = event.message.message
    #     print('first', event.message.message, event.message.date)
    #     if " 0x" in message:
    #         tokenKey = str(message[message.index(" 0x"):(message.index(" 0x") + 43)]).replace(" ", "")
    #         amount = message[message.index("amount"):(message.index("amount") + 17)]
    #         isSwap = False
    #         if "Tests passed" in message:
    #             isSwap = True
    #         date = arrow.get(event.message.date).to('local').format()
    #         print('token from Pancake:', tokenKey.strip(), amount.strip(), isSwap)
    #         open("token.txt", 'a+').write("%s|%s|%s|%s\n"%(tokenKey, amount, isSwap, date))
    #         args = f"{tokenKey}|{amount}|{isSwap}|{date}"
    #         event_bus.publish("newToken", args)

    # await client.run_until_disconnected()

async def main():
    #pyinstaller --noconsole --windowed --onefile .\asyncmain.py
    os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--enable-logging --log-level=3"
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = BotScannerToolWindow()
    event_bus = EventBus()
    thread = threading.Thread(target=asyncio.run,args=(listenTelegram(event_bus),))
    thread.start()
    ui.setupUi(MainWindow)
    MainWindow.show()
    time.sleep(1)
    ui.listenEvent(event_bus)
    #sys.exit(app.exec_(), client.disconnect())
    sys.exit(app.exec_())

asyncio.run(main())

# with client:
#     client.run_until_disconnected()
