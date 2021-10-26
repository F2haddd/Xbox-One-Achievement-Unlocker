import asyncio
import aiohttp
from sys import exit

class Title_Spoofer():

    def __init__(self) -> None:
        self.spoofed = False

    async def spoof_title_id(self, title: str, token: str, xuid: str) -> None:
        session = aiohttp.ClientSession()
        headers = {
            "Authorization": token,
            "x-xbl-contract-version": "3",
            "accept": "application/json",
        }

        payload = {
            "titles":[
                {
                    "expiration": 600,
                    "id": title,
                    "state": "active",
                    "sandbox": "RETAIL"
                }
            ]
        }
        try:
            async with session.post(f"https://presence-heartbeat.xboxlive.com/users/xuid({xuid})/devices/current", headers=headers, json=payload) as spoof_request:
                if spoof_request.status in [200, 201, 202, 204]:
                    print(f" \x1b[1;37m[\x1b[1;32m+\x1b[1;37m] Spoofed Title ID: [\x1b[1;36m{title}\x1b[1;37m]                                       ", end="\r", flush=True)
                    self.spoofed = True
                elif spoof_request.status == 401:
                    print(f" \x1b[1;37m[\x1b[1;33m!\x1b[1;37m] Authorization Token Expired!                                       ", end="\r", flush=True)
                    exit(0)
                elif spoof_request.status == 403:
                    print(f" \x1b[1;37m[\x1b[1;33m!\x1b[1;37m] Improper Token Type For This Process!                                       ", end="\r", flush=True)
                    exit(0)
                else:
                    print(f" \x1b[1;37m[\x1b[1;31m-\x1b[1;37m] Failed to Spoof Title ID: [\x1b[1;31m{title}\x1b[1;37m] Skipped.. {spoof_request.status}                                       ", end="\r", flush=True)
                    self.spoofed = False
        except:
            pass

        await session.close()
        return self.spoofed


def main():
    pass

if __name__ == "__main__":
    main()