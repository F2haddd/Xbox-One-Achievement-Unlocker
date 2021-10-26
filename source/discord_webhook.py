from dhooks import Webhook, Embed

class Discord_Webhook():

    @staticmethod
    async def webhook(webhook_url, webhook_username, webhook_avatar_url, webhook_embed_thumbnail, embed_title, description):
        try:
            embed = Embed(description=description, color=0xEE82EE)
            embed.set_footer(text='Achievement Unlocker', icon_url='https://i.imgur.com/gA4QTTe.jpg')
            embed.set_author(name=embed_title)
            embed.set_thumbnail(url=webhook_embed_thumbnail)
            Webhook(webhook_url).send(embed=embed, username=webhook_username, avatar_url=webhook_avatar_url)
        except:
            pass

def main():
    pass

if __name__ == "__main__":
    main()