import asyncio
import aiohttp
import numpy
from os import system
from getpass import getpass
from colorama import init
from json import load
from sys import path, platform
from source import day_one, discord_webhook, resolve, spoof_title, unlock

path.insert(0, "/source")

if platform == "win32":
    global clear
    clear = "cls"
else:
    clear = "clear"

init(autoreset=True)

class Achievement_Unlocker():

    def __init__(self) -> None:
        self.token = ""
        self.xuid = ""
        self.gamertag = ""
        self.gamerscore = ""
        self.amount_to_add = 0
        self.total_amount = 0
        self.title_class = Title_Management()
        self.configs = self.title_class.collect_services()
        self.resolver = resolve.Resolve_Info()
        self.settings = Configuration_Settings()
        self.discord = discord_webhook.Discord_Webhook()
        self.spoofer = spoof_title.Title_Spoofer()
        self.unlocker = unlock.Unlock_Achievements()
        self.activity = day_one.Activity_Post()
        self.send_webhook, self.webhook_url, self.webhook_username, self.webhook_avatar_url, self.webhook_embed_thumbnail, self.send_post, self.post_text = self.settings.collect_config()
    

    async def get_token(self):
        self.token = getpass(" \x1b[1;37mAuthorization Token: \x1b[1;37m")


    async def main(self):
        print(" \x1b[1;37m[ Welcome to \x1b[1;36mX1.AU \x1b[1;37m]")

        await self.get_token()
        await asyncio.sleep(2)

        print(" \x1b[1;37m[\x1b[1;32m+\x1b[1;37m] Collecting Account Information..")
        self.xuid, self.gamertag, self.gamerscore = await self.resolver.get_info(self.token)
        print(f" \x1b[1;37m[\x1b[1;32m+\x1b[1;37m] XUID: \x1b[1;36m{self.xuid} \n \x1b[1;37m[\x1b[1;32m+\x1b[1;37m] Gamertag: \x1b[1;36m{self.gamertag} \n \x1b[1;37m[\x1b[1;32m+\x1b[1;37m] Current Gamerscore: \x1b[1;36m{self.gamerscore} \x1b[1;37m")
        await asyncio.sleep(2)

        self.amount_to_add = int(input(f" \x1b[1;37m[\x1b[1;35m?\x1b[1;37m] How Much Gamerscore Would You Like to Add To \x1b[1;36m{self.gamertag} \x1b[1;37m(\x1b[1;36m?\x1b[1;37m): \x1b[1;37m"))
        self.total_amount = int(self.gamerscore) + self.amount_to_add

        await asyncio.sleep(1)
        self.configs = await self.title_class.find_title(self.configs)

        if self.send_webhook is True:
            await self.discord.webhook(self.webhook_url, self.webhook_username, self.webhook_avatar_url, self.webhook_embed_thumbnail, f"New Thread For {self.gamertag}", f"**Gamertag:** `{self.gamertag}`\n**XUID:** `{self.xuid}`\n**Starting Amount:** `{self.gamerscore}`\n\n**Chosen Amount to Add:** `{self.amount_to_add}`")

        await self.start_process()
        
        await asyncio.sleep(1)

        if self.send_post is True:
            await self.activity.post_to_feed(self.token, self.post_text, self.xuid)

        _1, _2, gamerscore = await self.resolver.get_info(self.token)
        if self.send_webhook is True:
            await self.discord.webhook(self.webhook_url, self.webhook_username, self.webhook_avatar_url, self.webhook_embed_thumbnail, f"Thread For {self.gamertag} Finished", f"**Gamertag:** `{self.gamertag}`\n**XUID:** `{self.xuid}`\n**Starting Amount:** `{self.gamerscore}`\n\n**Chosen Amount to Add:** `{self.amount_to_add}`\n**Finishing Amount**: `{gamerscore}`")

        print(" \x1b[1;37m[\x1b[1;32m!\x1b[1;37m] Process Finished!                                        ")


    async def start_process(self):
        for title in self.configs:
            _1, _2, gamerscore = await self.resolver.get_info(self.token)

            if int(gamerscore) >= self.total_amount:
                break

            else:
                title_id, service_config = title.split(":")[0], title.split(":")[1]

                status = await self.spoofer.spoof_title_id(title_id, self.token, self.xuid)
                if status is True:
                    await self.unlocker.unlock(self.token, title_id, service_config, self.xuid)
                
            await asyncio.sleep(1.5)


class Title_Management():

    @staticmethod
    def collect_services():
        with open("title_data/services.json") as service_file:
            services = load(service_file)

        services = services["title_service_configurations"]  

        return services      

    @staticmethod
    async def find_title(title_list):
        start_from = input("\x1b[1;37m [\x1b[1;33m=\x1b[1;37m] Start From Title: \x1b[1;36m")
        a = numpy.array(title_list)
        found = False
        index = 0
        if start_from != "":
            for t in a:
                if t.find(str(start_from)) != -1:
                    print(f"\x1b[1;37m [\x1b[1;32m!\x1b[1;37m] Found Title! [\x1b[1;36m{start_from}\x1b[1;37m]")
                    found = True
                    break
                else:
                    a = numpy.delete(a, index)
                index + 1
            if found is True:
                return a
            else:
                print(f"\x1b[1;37m [\x1b[1;31m!\x1b[1;37m] Could Not Find [\x1b[1;36m{start_from}\x1b[1;37m] \x1b[1;37mStarting from Beginning...")
                return title_list
        else:
            return title_list
    


class Configuration_Settings():

    @staticmethod
    def collect_config():
        with open("configuration/config.json") as configuration_file:
            settings = load(configuration_file)

        send_webhook = settings["discord"][0]["Send_Webhook_Enabled"]  
        webhook_url = settings["discord"][0]["Webhook_URL"]
        webhook_username = settings["discord"][0]["Webhook_Username"]
        webhook_avatar_url = settings["discord"][0]["Webhook_Avatar_URL"]
        webhook_embed_thumbnail = settings["discord"][0]["Webhook_Embed_Thumbnail"]

        send_post = settings["xbox_feed"][0]["Send_Day_One_Post"]
        post_text = settings["xbox_feed"][0]["Post_Text"]

        return send_webhook, webhook_url, webhook_username, webhook_avatar_url, webhook_embed_thumbnail, send_post, post_text



if __name__ == "__main__":
    system(clear)
    unlocker = Achievement_Unlocker()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(unlocker.main())