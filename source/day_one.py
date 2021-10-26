import asyncio
import aiohttp


class Activity_Post():
    def __init__(self) -> None:
        pass

    async def post_to_feed(self, token: str, post_text: str, xuid: str) -> None:
        session = aiohttp.ClientSession()
        
        headers = {
            "Authorization": token,
            "x-xbl-contract-version": "2",
            "content-type": "application/json"
        }

        payload = {
            "postType": "XboxLink",
            "postText": post_text,
            "postTypeData":{
                "locator": "achievements.xboxlive.com/users/me/achievements/12ab0100-8936-41c0-8ead-654a3ded352b/1"
            },
            "timelines":[
                {
                    "timelineType": "User",
                    "timelineOwner": xuid
                }
            ]
        }

        async with session.post("https://userposts.xboxlive.com/users/me/posts", headers=headers, json=payload) as activity_post:
            if activity_post.status in [200, 201, 202, 204]:
                print(" \x1b[1;37m[\x1b[1;32m+\x1b[1;37m] \x1b[1;32mDay One\x1b[1;37m Posted to Activity Feed                                       ")
            else:
                print(" \x1b[1;37m[\x1b[1;31m-\x1b[1;37m] \x1b[1;32mDay One\x1b[1;37m Failed to Post                                       ")

        await session.close()


def main():
    pass


if __name__ == "__main__":
    main()