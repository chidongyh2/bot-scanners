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
import datetime
from telethon.tl.types import InputMessagesFilterDocument
from FastTelethonhelper import fast_download
from rarfile import RarFile
api_id = '27535321'
api_hash = '7b915080f6c41357c2ad84ca6e84614a'
chanelId = -1001192416115
channelIds = []
limit = 5
open("sources/source.txt", "w").close()
client = TelegramClient('bot', api_id, api_hash)
# Configure the logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

async def listenTelegram(event_bus):
    await client.start()
    def progress_callback(current, total):
        last_current = 0
        last_time = 0
        now = time.time()
        speed = round(((current-last_current)/(now-last_time))/1000)
        last_current = current
        last_time = now
        percent = int((current/total)*100)
        logging.info('{} % .... {} KB/s'.format(percent, speed))

    try: assert await client.connect()
    except Exception as e: print(str(e))

    tokenFile = open("TelegramChannel.txt", 'r')
    if tokenFile: 
        list_channel_id = tokenFile.readlines()
        if list_channel_id and len(list_channel_id) > 0:
            for channel_id in list_channel_id:
                channelIds.append(int(channel_id.split("|")[0]))
                async for messageInterface in client.iter_messages(int(channel_id.split("|")[0]), limit=limit, filter=InputMessagesFilterDocument):
                    if arrow.get(messageInterface.date) > arrow.get(datetime.datetime.now()) + datetime.timedelta(days=-2):
                        if not messageInterface.media == None and messageInterface.media.document:
                            #path = await client.download_media(messageInterface.media, f"data-source", progress_callback=progress_callback)
                            path = await fast_download(client, messageInterface, messageInterface, None, progress_callback)
                            print(path, channel_id.split("|")[1].replace("\n", ""))
                            if ".rar" in path:
                                with RarFile(path, 'r') as myrar:
                                    myrar.extractall(pwd=channel_id.split("|")[1].replace("\n", ""))
                            pathSave = path.replace(".rar", "")
                            open("sources/source.txt", 'a+').write("%s\n"%(f"{pathSave}"))
                            time.sleep(2)
                            event_bus.publish("updateData")

        
    @client.on(events.NewMessage(chats=channelIds))
    async def my_event_handler(event):
        try:
            if not event.message.media == None and event.message.media.document:
                path = await client.download_media(event.message.media, None, progress_callback=progress_callback)
                print(path)
                open("sources/source.txt", 'a+').write("%s\n"%(f"downloads/{str(event.message.file.name)}"))
                time.sleep(2)
                event_bus.publish("newToken")
        except:
            pass

    await client.run_until_disconnected()

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
    sys.exit(app.exec_(), client.disconnect())

asyncio.run(main())

with client:
    client.run_until_disconnected()
