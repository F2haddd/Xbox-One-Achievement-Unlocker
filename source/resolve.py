import asyncio
import aiohttp
from sys import exit

class Resolve_Info():

    def __init__(self) -> None:
        pass

    async def get_info(self, token: str):
        session = aiohttp.ClientSession()
        headers = {
            "Authorization": token,
            "x-xbl-contract-version": "2"
        }
        try:
            async with session.get("https://profile.xboxlive.com/users/me/profile/settings?settings=Gamertag,Gamerscore", headers=headers) as request_info:
                if request_info.status in [200, 201, 202, 204]:

                    response_data = await request_info.json()

                    xuid = response_data["profileUsers"][0]["id"]
                    gamertag = response_data["profileUsers"][0]["settings"][0]["value"]
                    gamerscore = response_data["profileUsers"][0]["settings"][1]["value"]

                elif request_info.status == 401:
                    print(" \x1b[1;37m[\x1b[1;33m!\x1b1[1;37m] Authorization Token Invalid!                                       ", end="\r", flush=True)
                    exit(0)
                else:
                    print(" \x1b[1;37m[\x1b[1;31m!\x1b1[1;37m] Encountered An Error While Retrieving Account Information!                                       ", end="\r", flush=True)  
                    exit(0)
        except:
            pass
        
        await session.close()
        return xuid, gamertag, gamerscore
                


def main():
    pass

if __name__ == "__main__":
    main()