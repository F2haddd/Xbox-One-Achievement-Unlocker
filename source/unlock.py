import asyncio
import aiohttp
from sys import exit


class Unlock_Achievements():
    def __init__(self) -> None:
        self.range = 0

    async def unlock(self, token: str, title: str, service: str, xuid: str):
        session = aiohttp.ClientSession()
        self.range = 0

        headers = {
            "Accept-Language": "en-US,en",
            "Authorization": token,
            "x-xbl-contract-version": "2",
            "Content-Type": "application/json; charset=utf-8"
        }


        payloads = [
            {
                "action":"progressUpdate",
                "serviceConfigId": service,
                "titleId": title,
                "userId": xuid,
                "achievements":[{"id":1,"percentComplete":"100"},{"id":2,"percentComplete":"100"},{"id":3,"percentComplete":"100"},{"id":4,"percentComplete":"100"},{"id":5,"percentComplete":"100"},{"id":6,"percentComplete":"100"},{"id":7,"percentComplete":"100"},{"id":8,"percentComplete":"100"},{"id":9,"percentComplete":"100"},{"id":10,"percentComplete":"100"},{"id":11,"percentComplete":"100"},{"id":12,"percentComplete":"100"},{"id":13,"percentComplete":"100"},{"id":14,"percentComplete":"100"},{"id":15,"percentComplete":"100"},{"id":16,"percentComplete":"100"},{"id":17,"percentComplete":"100"},{"id":18,"percentComplete":"100"},{"id":19,"percentComplete":"100"},{"id":20,"percentComplete":"100"},{"id":21,"percentComplete":"100"},{"id":22,"percentComplete":"100"},{"id":23,"percentComplete":"100"},{"id":24,"percentComplete":"100"},{"id":25,"percentComplete":"100"},{"id":26,"percentComplete":"100"},{"id":27,"percentComplete":"100"},{"id":28,"percentComplete":"100"},{"id":29,"percentComplete":"100"},{"id":30,"percentComplete":"100"},{"id":31,"percentComplete":"100"},{"id":32,"percentComplete":"100"},{"id":33,"percentComplete":"100"},{"id":34,"percentComplete":"100"},{"id":35,"percentComplete":"100"},{"id":36,"percentComplete":"100"},{"id":37,"percentComplete":"100"},{"id":38,"percentComplete":"100"},{"id":39,"percentComplete":"100"},{"id":40,"percentComplete":"100"},{"id":41,"percentComplete":"100"},{"id":42,"percentComplete":"100"},{"id":43,"percentComplete":"100"},{"id":44,"percentComplete":"100"},{"id":45,"percentComplete":"100"},{"id":46,"percentComplete":"100"},{"id":47,"percentComplete":"100"},{"id":48,"percentComplete":"100"},{"id":49,"percentComplete":"100"},{"id":50,"percentComplete":"100"}]
            },
            {
                "action": "progressUpdate",
                "serviceConfigId": service,
                "titleId": title,
                "userId": xuid,
                "achievements":[{"id":51,"percentComplete":"100"},{"id":52,"percentComplete":"100"},{"id":53,"percentComplete":"100"},{"id":54,"percentComplete":"100"},{"id":55,"percentComplete":"100"},{"id":56,"percentComplete":"100"},{"id":57,"percentComplete":"100"},{"id":58,"percentComplete":"100"},{"id":59,"percentComplete":"100"},{"id":60,"percentComplete":"100"},{"id":61,"percentComplete":"100"},{"id":62,"percentComplete":"100"},{"id":63,"percentComplete":"100"},{"id":64,"percentComplete":"100"},{"id":65,"percentComplete":"100"},{"id":66,"percentComplete":"100"},{"id":67,"percentComplete":"100"},{"id":68,"percentComplete":"100"},{"id":69,"percentComplete":"100"},{"id":70,"percentComplete":"100"},{"id":71,"percentComplete":"100"},{"id":72,"percentComplete":"100"},{"id":73,"percentComplete":"100"},{"id":74,"percentComplete":"100"},{"id":75,"percentComplete":"100"},{"id":76,"percentComplete":"100"},{"id":77,"percentComplete":"100"},{"id":78,"percentComplete":"100"},{"id":79,"percentComplete":"100"},{"id":80,"percentComplete":"100"},{"id":81,"percentComplete":"100"},{"id":82,"percentComplete":"100"},{"id":83,"percentComplete":"100"},{"id":84,"percentComplete":"100"},{"id":85,"percentComplete":"100"},{"id":86,"percentComplete":"100"},{"id":87,"percentComplete":"100"},{"id":88,"percentComplete":"100"},{"id":89,"percentComplete":"100"},{"id":90,"percentComplete":"100"},{"id":91,"percentComplete":"100"},{"id":92,"percentComplete":"100"},{"id":93,"percentComplete":"100"},{"id":94,"percentComplete":"100"},{"id":95,"percentComplete":"100"},{"id":96,"percentComplete":"100"},{"id":97,"percentComplete":"100"},{"id":98,"percentComplete":"100"},{"id":99,"percentComplete":"100"},{"id":100,"percentComplete":"100"},{"id":101,"percentComplete":"100"}]
            },
            {
                "action": "progressUpdate",
                "serviceConfigId": service,
                "titleId": title,
                "userId": str(xuid),
                "achievements":[{"id":102,"percentComplete":"100"},{"id":103,"percentComplete":"100"},{"id":104,"percentComplete":"100"},{"id":105,"percentComplete":"100"},{"id":106,"percentComplete":"100"},{"id":107,"percentComplete":"100"},{"id":108,"percentComplete":"100"},{"id":109,"percentComplete":"100"},{"id":110,"percentComplete":"100"},{"id":111,"percentComplete":"100"},{"id":112,"percentComplete":"100"},{"id":113,"percentComplete":"100"},{"id":114,"percentComplete":"100"},{"id":115,"percentComplete":"100"},{"id":116,"percentComplete":"100"},{"id":117,"percentComplete":"100"},{"id":118,"percentComplete":"100"},{"id":119,"percentComplete":"100"},{"id":120,"percentComplete":"100"},{"id":121,"percentComplete":"100"},{"id":122,"percentComplete":"100"},{"id":123,"percentComplete":"100"},{"id":124,"percentComplete":"100"},{"id":125,"percentComplete":"100"},{"id":126,"percentComplete":"100"},{"id":127,"percentComplete":"100"},{"id":128,"percentComplete":"100"},{"id":129,"percentComplete":"100"},{"id":130,"percentComplete":"100"},{"id":131,"percentComplete":"100"},{"id":132,"percentComplete":"100"},{"id":133,"percentComplete":"100"},{"id":134,"percentComplete":"100"},{"id":135,"percentComplete":"100"},{"id":136,"percentComplete":"100"},{"id":137,"percentComplete":"100"},{"id":138,"percentComplete":"100"},{"id":139,"percentComplete":"100"},{"id":140,"percentComplete":"100"},{"id":141,"percentComplete":"100"},{"id":142,"percentComplete":"100"},{"id":143,"percentComplete":"100"},{"id":144,"percentComplete":"100"},{"id":145,"percentComplete":"100"},{"id":146,"percentComplete":"100"},{"id":147,"percentComplete":"100"},{"id":148,"percentComplete":"100"},{"id":149,"percentComplete":"100"},{"id":150,"percentComplete":"100"}]
            },
            {
                "action": "progressUpdate",
                "serviceConfigId": service,
                "titleId": title,
                "userId": xuid,
                "achievements":[{"id":151,"percentComplete":"100"},{"id":152,"percentComplete":"100"},{"id":153,"percentComplete":"100"},{"id":154,"percentComplete":"100"},{"id":155,"percentComplete":"100"},{"id":156,"percentComplete":"100"},{"id":157,"percentComplete":"100"},{"id":158,"percentComplete":"100"},{"id":159,"percentComplete":"100"},{"id":160,"percentComplete":"100"},{"id":161,"percentComplete":"100"},{"id":162,"percentComplete":"100"},{"id":163,"percentComplete":"100"},{"id":164,"percentComplete":"100"},{"id":165,"percentComplete":"100"},{"id":166,"percentComplete":"100"},{"id":167,"percentComplete":"100"},{"id":168,"percentComplete":"100"},{"id":169,"percentComplete":"100"},{"id":170,"percentComplete":"100"},{"id":171,"percentComplete":"100"},{"id":172,"percentComplete":"100"},{"id":173,"percentComplete":"100"},{"id":174,"percentComplete":"100"},{"id":175,"percentComplete":"100"},{"id":176,"percentComplete":"100"},{"id":177,"percentComplete":"100"},{"id":178,"percentComplete":"100"},{"id":179,"percentComplete":"100"}]
            },
            {
                "action": "progressUpdate",
                "serviceConfigId": service,
                "titleId": title,
                "userId": xuid,
                "achievements":[{"id":180,"percentComplete":"100"},{"id":181,"percentComplete":"100"},{"id":182,"percentComplete":"100"},{"id":183,"percentComplete":"100"},{"id":184,"percentComplete":"100"},{"id":185,"percentComplete":"100"},{"id":186,"percentComplete":"100"},{"id":187,"percentComplete":"100"},{"id":188,"percentComplete":"100"},{"id":189,"percentComplete":"100"},{"id":190,"percentComplete":"100"},{"id":191,"percentComplete":"100"},{"id":192,"percentComplete":"100"},{"id":193,"percentComplete":"100"},{"id":194,"percentComplete":"100"},{"id":195,"percentComplete":"100"},{"id":196,"percentComplete":"100"},{"id":197,"percentComplete":"100"},{"id":198,"percentComplete":"100"},{"id":199,"percentComplete":"100"},{"id":200,"percentComplete":"100"},{"id":201,"percentComplete":"100"},{"id":202,"percentComplete":"100"},{"id":203,"percentComplete":"100"},{"id":204,"percentComplete":"100"},{"id":205,"percentComplete":"100"},{"id":206,"percentComplete":"100"},{"id":207,"percentComplete":"100"},{"id":208,"percentComplete":"100"},{"id":209,"percentComplete":"100"},{"id":210,"percentComplete":"100"},{"id":211,"percentComplete":"100"},{"id":212,"percentComplete":"100"},{"id":213,"percentComplete":"100"},{"id":214,"percentComplete":"100"},{"id":215,"percentComplete":"100"},{"id":216,"percentComplete":"100"},{"id":217,"percentComplete":"100"},{"id":218,"percentComplete":"100"},{"id":219,"percentComplete":"100"},{"id":220,"percentComplete":"100"}]
            },
            {
                "action": "progressUpdate",
                "serviceConfigId": service,
                "titleId": title,
                "userId": xuid,
                "achievements":[{"id":221,"percentComplete":"100"},{"id":222,"percentComplete":"100"},{"id":223,"percentComplete":"100"},{"id":224,"percentComplete":"100"},{"id":225,"percentComplete":"100"},{"id":226,"percentComplete":"100"},{"id":227,"percentComplete":"100"},{"id":228,"percentComplete":"100"},{"id":229,"percentComplete":"100"},{"id":230,"percentComplete":"100"},{"id":231,"percentComplete":"100"},{"id":232,"percentComplete":"100"},{"id":233,"percentComplete":"100"},{"id":234,"percentComplete":"100"},{"id":235,"percentComplete":"100"},{"id":236,"percentComplete":"100"},{"id":237,"percentComplete":"100"},{"id":238,"percentComplete":"100"},{"id":239,"percentComplete":"100"},{"id":240,"percentComplete":"100"},{"id":241,"percentComplete":"100"},{"id":242,"percentComplete":"100"},{"id":243,"percentComplete":"100"},{"id":244,"percentComplete":"100"},{"id":245,"percentComplete":"100"},{"id":246,"percentComplete":"100"},{"id":247,"percentComplete":"100"},{"id":248,"percentComplete":"100"},{"id":249,"percentComplete":"100"},{"id":250,"percentComplete":"100"},{"id":251,"percentComplete":"100"},{"id":252,"percentComplete":"100"},{"id":253,"percentComplete":"100"},{"id":254,"percentComplete":"100"},{"id":255,"percentComplete":"100"},{"id":256,"percentComplete":"100"},{"id":257,"percentComplete":"100"},{"id":258,"percentComplete":"100"},{"id":259,"percentComplete":"100"},{"id":260,"percentComplete":"100"},{"id":261,"percentComplete":"100"},{"id":262,"percentComplete":"100"},{"id":263,"percentComplete":"100"},{"id":264,"percentComplete":"100"},{"id":265,"percentComplete":"100"},{"id":266,"percentComplete":"100"},{"id":267,"percentComplete":"100"},{"id":268,"percentComplete":"100"},{"id":269,"percentComplete":"100"},{"id":270,"percentComplete":"100"}]
            }
        ]

        for payload in payloads:
            try:
                async with session.post(f"https://achievements.xboxlive.com/users/xuid({xuid})/achievements/{service}/update", headers=headers, json=payload) as unlock_request:
                    self.range += 1

                    if unlock_request.status in [200, 201, 202, 204]:
                        print(f" \x1b[1;37m[\x1b[1;32m✓\x1b[1;37m] Range [\x1b[1;36m{self.range}\x1b[1;37m] Unlocked Successfully                                       ", end="\r", flush=True)
                    elif unlock_request.status == 401:
                        print(f" \x1b[1;37m[\x1b[1;33m!\x1b[1;37m] Authorization Token Expired!                                       ", end="\r", flush=True)
                        exit(0)
                    elif unlock_request.status == 403:
                        print(f" \x1b[1;37m[\x1b[1;33m!\x1b[1;37m] Improper Token Type For This Process!                                       ", end="\r", flush=True)
                        exit(0)
                    elif unlock_request.status == 304:
                        print(f" \x1b[1;37m[\x1b[1;36m✓\x1b[1;37m] Range [\x1b[1;36m{self.range}\x1b[1;37m] Already Unlocked                                       ", end="\r", flush=True)
                    elif unlock_request.status == 400:
                        print(f" \x1b[1;37m[\x1b[1;31mX\x1b[1;37m] Range [\x1b[1;36m{self.range}\x1b[1;37m] No Achievements Exist In Range                                       ", end="\r", flush=True)
                    else:
                        print(f" \x1b[1;37m[\x1b[1;31mX\x1b[1;37m] Range [\x1b[1;36m{self.range}\x1b[1;37m] Failed to Unlock                                       ", end="\r", flush=True)
            except:
                pass
            await asyncio.sleep(1.25)

        await session.close()


def main():
    pass


if __name__ == "__main__":
    main()