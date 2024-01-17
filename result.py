import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

location_input = input("Enter the location: ")

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.accuweather.com/"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.CLASS_NAME, 'fc-cta-consent')
find.click()

search_input = driver.find_element(By.NAME, 'query')
search_input.send_keys(location_input)

time.sleep(1)

search = driver.find_element(By.CLASS_NAME, 'search-result')
search.click()

time.sleep(2)

temperature_element = driver.find_element(By.CLASS_NAME, 'temp')
temperature = temperature_element.text

feels_like_element = driver.find_element(By.CLASS_NAME, 'real-feel')
feels_like = feels_like_element.text

print(f'Current Temperature in {location_input.capitalize()}: {temperature}, {feels_like}')