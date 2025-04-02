import time
from InstagramBot import InstagramBot

bot = InstagramBot()
time.sleep(3)
bot.login()
time.sleep(5)
bot.search_account()
time.sleep(5)
bot.follow_followers()