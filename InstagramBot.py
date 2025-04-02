from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

SIMILAR_ACCOUNT = os.environ["SIMILAR_ACCOUNT"]
USERNAME = os.environ["INSTAGRAM_USERNAME"]
PASSWORD = os.environ["INSTAGRAM_PASSWORD"]
URL = "https://www.instagram.com/?flo=true"

class InstagramBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(URL)

    def login(self):
        username_input = self.driver.find_element(By.NAME, value="username")
        username_input.send_keys(USERNAME)

        time.sleep(1)
        decline_cookies = self.driver.find_element(By.CLASS_NAME, value="_a9-- _ap36 _a9_1".replace(" ", "."))
        decline_cookies.click()

        time.sleep(1)
        password_input = self.driver.find_element(By.NAME, value="password")
        password_input.send_keys(PASSWORD)

        time.sleep(1)
        login_button = self.driver.find_element(By.CLASS_NAME, value="_acan _acap _acas _aj1- _ap30".replace(" ", "."))
        login_button.click()

        time.sleep(5)
        dont_save = self.driver.find_element(By.CLASS_NAME,
        value="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r "
        "x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n "
        "xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc "
        "xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l "
        "xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37".replace(" ", "."))
        dont_save.click()

    def search_account(self):
        self.driver.maximize_window()

        time.sleep(2)
        search_button = self.driver.find_element(By.CSS_SELECTOR, "a[role='link'] svg[aria-label='Search']")
        search_button = search_button.find_element(By.XPATH, "./ancestor::a")
        search_button.click()

        time.sleep(1)
        search = self.driver.find_element(By.TAG_NAME,
        # value='//*[@id="mount_0_0_eh"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input'.replace(" ", ".")
        value="input")
        search.send_keys(SIMILAR_ACCOUNT)

        time.sleep(3)
        chosen_account = self.driver.find_element(By.XPATH, "//a[contains(@href, '/" + SIMILAR_ACCOUNT + "')]")
        chosen_account.click()

    def follow_followers(self):
        followers = self.driver.find_element(By.CSS_SELECTOR, "a[role='link'] span[class='x1lliihq x1plvlek xryxfnj x1n2onr6 x1ji0vk5 x18bv5gf x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xl565be xo1l8bm x1roi4f4 x2b8uid x10wh9bi x1wdrske x8viiok x18hxmgj']")
        followers = followers.find_element(By.XPATH, "./ancestor::a")
        followers.click()

        time.sleep(3)
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="button[class=' _acan _acap _acas _aj1- _ap30']")
        # follow_buttons.click()
        for button in follow_buttons:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", button)
            time.sleep(1)

