from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import click
def send_message(message: any):
    index = 0
    while True:
        message_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p')
        for onebyone in message:
            message_bar.send_keys(onebyone)
        message_bar.send_keys(Keys.ENTER)
        if index == 5:
            break
        index += 1
        sleep(1)

def for_email_verif(search_in : any, message : any):
    gmail_writer = driver.find_element(By.NAME, search_in)
    for ele in message:
        gmail_writer.send_keys(ele)
    sleep(1)

def write_in_xpath(serch_for : any, message : any):
    finder = driver.find_element(By.XPATH, serch_for)
    for op in message:
        finder.send_keys(op)
    sleep(2)

def for_icons(message : any):
    the_icons = driver.find_element(By.XPATH, message)
    the_icons.click()
    sleep(2)

def click_button(location : any):
    clikc_icon = driver.find_element(By.CLASS_NAME, location)
    clikc_icon.click()
    sleep(1)
def click_on(location : any):
    try:
        clikc_icon = driver.find_element(By.XPATH, location)
        clikc_icon.click()
    except NoSuchElementException:
        print("no element found")
    sleep(1)
def for_the_optionts(var : any) -> str:
    var = input("Chose the Choices ===> \n  1:-search for freind.\n 2:-Send Direct message?\n")
    return var
string = input(" Please write The Gmail .... : ")
sleep(2)
passcode = input(" Please Write The Passcode ... : ")
sleep(2)
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login')
sleep(2)
for_email_verif('password', passcode)
for_email_verif('username', string)
search_bar = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]')
search_bar.click()
sleep(4)
int_type = 0
var = ""
while True:
    sleep(2)
    var = for_the_optionts(var)
    if var == '1':
        open_bar = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div')
        sleep(2)
        open_bar.click()
        sleep(2)
        name_fr = input("\nAccount Name @--:\n\n")
        sleep(2)
        write_in_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input', name_fr)
        see_result = input("Is the freind ur trying to reach is in the position :\n[1]\n[2]\n[3]\n[0]to_exit\n ")
        if see_result == '1':
            try:
                click_on('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]')
            except NoSuchElementException:
                print("Not Found")
            int_type = 1
        elif see_result == '2':
            try:
                click_on('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[3]/div[1]')
            except NoSuchElementException:
                print("Not Found")
            int_type = 1
        elif see_result == '3':
            try:
                click_on('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[3]/div[1]')
            except NoSuchElementException:
                print("Not found")
            int_type = 1
        sleep(2)
        if int_type == 1:
            var_options = input('Enter The Option U want ... \n\n-1)FOLLOW.. \n-2)Spam_messages\n-3)Report.. -0)To-exit')
            if (var_options == '1'):
                try:
                    for_icons("(//button[@class=' _acan _acap _acas _aj1- _ap30'])[1]")
                except NoSuchElementException:
                    print("Not Found")
            elif (var_options == '2'):
                try:
                    for_icons("//div[contains(text(),'Message')]")
                except NoSuchElementException:
                    print("Not found")
                sleep(1)
                try:
                    for_icons("//div[contains(text(),'Message')]")
                except NoSuchElementException:
                    print("Not Found")
            elif(var_options == '0'):
                var = for_the_optionts(var)
    elif var == '2':
        sleep(2)
        try:
            open_messag = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a/div')
        except NoSuchElementException:
            print("Not Found")
        open_messag.click()
        sleep(2)
input()
sleep(15)

string_message = "testing"
send_message(string_message)
sleep(3)

input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div/label/input')
friend = input("Freind Name ..?")
sleep(2)
for let in friend:
    input_search.send_keys(let)
this_person = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/div[2]/li/div/a/div')
sleep(1)
this_person.click()


