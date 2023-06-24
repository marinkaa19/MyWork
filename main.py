import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.service import Service


s=Service('/Users/tomilova-m/PycharmProjects/pythonProject/safaridriver')
driver = webdriver.Safari(service=s)
driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true&state=%2Fwelcome")
time.sleep(3)
driver.set_window_size(1366,768)
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[3]/button").click()
time.sleep(3)
driver.find_element(By.ID, "login-otp-button").click()
time.sleep(2)
driver.find_element(By.ID, "cards-overview-index").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[6]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[7]/form/div[2]/button").click()
time.sleep(5)
driver.switch_to.frame(0)
driver.find_element(By.ID, "confirm").click()
time.sleep(2)
driver.quit()

