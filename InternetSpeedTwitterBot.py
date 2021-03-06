from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time


class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver_path, up, down):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.up = up
        self.down = down

    def get_internet_speed(self, URL):
        self.driver.get(URL)

        time.sleep(2)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        print("clicked")
        time.sleep(40)
        up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                  '3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        return up, down

    def tweet_at_provider(self, URL, email, password, message):
        self.driver.get(URL)

        time.sleep(2)
        login = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div['
                                                   '1]/div/div[3]/div[5]/a/div')
        login.click()

        time.sleep(2)
        email_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div['
                                                         '2]/div/input')
        email_field.send_keys(email)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div')
        next_button.click()

        time.sleep(2)
        password_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                            '2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                            '3]/div/label/div/div[2]/div[1]/input')
        password_field.send_keys(password)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        next_button.click()

        time.sleep(2)
        tweet_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                         '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                         '1]/div/div/div/div/div/div/div/div/div/label/div['
                                                         '1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_field.send_keys(message)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                          '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                          '3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()
