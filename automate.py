from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from setting import *


class CookieClickerBot:
    def __init__(self):
        self.get_browser()
        self.browser.get("https://orteil.dashnet.org/cookieclicker/")
        sleep(2)
        self.initialize_elements()

    def initialize_elements(self):
        self.lang = self.browser.find_element(By.ID, "langSelect-EN")
        self.lang.click()
        sleep(1)

        self.giant_cookie = self.browser.find_element(By.ID, "bigCookie")
        self.option_btn = self.browser.find_element(By.ID, "prefsButton")
        self.buildings = self.browser.find_element(By.ID, "products")
        self.second_timer = 0
        self.minute_timer = 0
        self.hour_timer = 0
        self.start()

    def get_browser(self):
        if browser.capitalize() == "Firefox":
            self.browser = webdriver.Firefox()
        elif browser.capitalize() == "Chrome":
            self.browser = webdriver.Chrome()
        elif browser.capitalize() == "Edge":
            self.browser = webdriver.Edge()
        elif browser.capitalize() == "Safari":
            self.browser = webdriver.Safari()

    def start(self):
        try:
            with open("./save.txt", "r") as file:
                save_data = file.read()
                self.option_btn.click()
                self.browser.find_element(
                    By.CSS_SELECTOR, "div.listing:nth-child(4) > a:nth-child(2)"
                ).click()
                self.browser.find_element(By.ID, "textareaPrompt").send_keys(save_data)
                self.browser.find_element(By.ID, "promptOption0").click()
                self.option_btn.click()
                sleep(3)
        except:
            pass

    def save(self):
        self.option_btn.click()
        self.export_btn = self.browser.find_element(
            By.CSS_SELECTOR, "div.listing:nth-child(4) > a:nth-child(1)"
        ).click()
        with open("./save.txt", "w") as file:
            self.prompt = self.browser.find_element(By.ID, "textareaPrompt").text
            file.write(self.prompt)
            self.agree = self.browser.find_element(By.ID, "promptOption0").click()
            self.option_btn.click()

    def golden_cookie_event(self):
        if get_golden_warth_cookie:
            try:
                golden_cookie = self.browser.find_element(
                    By.CSS_SELECTOR, ".shimmer"
                ).click()
            except:
                pass

    def buy_upgrade(self):
        try:
            self.parent_id = None
            num = 0
            while self.parent_id not in ["techUpgrades", "upgrades"]:
                if num > 10:
                    break
                self.upgrades = self.browser.find_element(By.ID, f"upgrade{num}")
                self.upgrade_id = self.upgrades.get_attribute("data-id")
                self.parent = self.upgrades.find_element(By.XPATH, "..")
                self.parent_id = self.parent.get_attribute("id")
                num += 1

            if self.upgrade_id == "69":
                self.upgrades.click()
                self.btn = self.browser.find_element(By.ID, "promptOption0").click()
            elif self.upgrade_id == "74" and not end_grandmapocalypse:
                self.upgrades = self.browser.find_element(By.ID, "upgrade2").click()
            elif (self.upgrade_id == "85" and end_grandmapocalypse) or (
                self.upgrade_id == "74" and end_grandmapocalypse
            ):
                self.upgrades = self.browser.find_element(By.ID, "upgrade1").click()
            else:
                self.upgrades.click()
        except:
            pass

    def purchase_buildings(self):
        for building in range(20, -1, -1):
            try:
                latest_building = self.buildings.find_element(
                    By.ID, f"product{building}"
                ).click()
            except:
                pass

    def autoclick(self):
        try:
            self.giant_cookie.click()
        except:
            pass

    def wizz_buff(self):
        try:
            if wizard_bonus == "Force the Hand of Fate":
                self.buff = self.browser.find_element(By.ID, "grimoireSpell1")
            elif wizard_bonus == "Conjure Baked Goods":
                self.buff = self.browser.find_element(By.ID, "grimoireSpell0")
            else:
                self.buff = self.browser.find_element(By.ID, "grimoireSpell3")

            self.buff.click()
        except:
            pass

    def collect_sugar_lumps(self):
        if get_sugar_lump_early:
            try:
                self.lumps = self.browser.find_element(By.ID, "lumps").click()
            except:
                pass

    def run(self):
        while True:
            self.second_timer += 1
            self.autoclick()
            if self.second_timer >= 50:
                self.buy_upgrade()
                self.golden_cookie_event()
                self.second_timer = 0
                self.minute_timer += 1
                if self.minute_timer >= 5:
                    self.minute_timer = 0
                    self.hour_timer += 1
                    self.purchase_buildings()
                    self.wizz_buff()
                    if self.hour_timer == 5:
                        self.hour_timer = 0
                        self.save()
                        self.collect_sugar_lumps()


bot = CookieClickerBot()
bot.run()
