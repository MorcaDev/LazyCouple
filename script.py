# AUTOMATION - SELENIUM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# GENERATIVE AI - GEMINIPRO
import google.generativeai as genai

# PYTHON PAKCAGES
import time
from decouple import config

"""
CREATING MESSAGE
"""

def creating_message():

    # dates
    aniversary_day = "32" #str - pick your aniversary day
    current_day = str(time.strftime("%d", time.localtime()))

    # message types
    message_type = "happy aniversary" if aniversary_day == current_day else "good morning"

    # accessing gemini
    api_key = config('gemini_key')
    genai.configure(api_key = api_key) #str - using decouple and enviromental variables

    # creating message
    model = genai.GenerativeModel('gemini-pro')
    message_prompt = model.generate_content(f"generate a {message_type} message for a friend, do not include special characters")
    message_response = message_prompt.text

    # couple format
    message_response = message_response.replace("friend","couple")
    message_response = message_response.replace("friendship","relationship")

    # show message
    return message_response

"""
SENDING MESSAGE
"""
def sending_message():

    # initializing web driver
    driver = webdriver.Edge()
    driver.get("https://web.whatsapp.com/")

    # scanning qr section
    print("Scanning QR ....")
    time.sleep(30)

    # contact search bar
    contact_number = "+99 123456789" # str - pick a phone number 
    print("Looking for CONTACT....")
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(contact_number)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

    # message bar
    message = creating_message()
    print("Sending SMS....")
    msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    msg_box.clear()
    msg_box.send_keys(message)
    msg_box.send_keys(Keys.ENTER)
    time.sleep(5)

    # closing window and driver
    print("Closing ....")
    time.sleep(5)
    driver.quit()


if __name__ == "__main__":

    print("Executing code...")
    sending_message()
    print("😉")