import os
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
chrome_driver_path = os.environ['MY_DRIVER']
TWITTER_EMAIL = os.environ['MY_EMAIL']
TWITTER_PASSWORD = os.environ['MY_PASSWORD']

SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"

bot = InternetSpeedTwitterBot(chrome_driver_path, PROMISED_UP, PROMISED_DOWN)
up, down = bot.get_internet_speed(SPEED_TEST_URL)

message = f"Hey Internet provider, why is internet speed {down}down/{up}up when I pay for {PROMISED_DOWN}down/" \
          f"{PROMISED_UP}up?"

bot.tweet_at_provider(TWITTER_URL, TWITTER_EMAIL, TWITTER_PASSWORD, message)
