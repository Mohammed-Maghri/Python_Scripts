from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep
import click
# **********j@gmail.com
# **********
# Mohammed Amine Ait Bahcine
string = input(" Please write The Gmail ....")
sleep(2)
passcode = input(" Please Write The Passcode ...")
sleep(2)
driver = webdriver.Chrome()
driver.get('https://www.facebook.com/messages/t/100029929764025')
search_bar = driver.find_element(By.NAME, 'email')
for_pass_code = driver.find_element(By.NAME, 'pass')
for letter in string:
    search_bar.send_keys(letter)
for pass_wod in passcode:
    for_pass_code.send_keys(pass_wod)
string_message = "testing"
search_bar.send_keys(Keys.ENTER)
sleep(15)
index = 0
while True:
    message_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p')
    for onebyone in string_message :
        message_bar.send_keys(onebyone)
    message_bar.send_keys(Keys.ENTER)
    if index == 5:
        break
    index += 1
    sleep(1)
sleep(3)
input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div/label/input')
friend = input("Freind Name ..?")
sleep(2)
for let in friend:
    input_search.send_keys(let)
this_person = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/div[2]/li/div/a/div')
this_person.click()
sleep(3)
input()
