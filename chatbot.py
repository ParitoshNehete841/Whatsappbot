import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(5)

position1 = pt.locateonsccreen("whatsapp/smiley.jpg", confidence=0.75)
x = position1[0]
y = position1[1]


# get message
def get_message():
    global x, y

    position = pt.locateOnScreen("whatsapp/Smiley.jpg", confidence=0.75)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=0.5)
    pt.moveTo(x + 100, y, duration=0.5)
    pt.tripleClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message is"+ whatsapp_message)

# response
def response(message):
    global x , y

    position = pt.locateOnScreen("whatsapp/Smiley.jpg", confidence=0.75)
    x = position[0]
    y = position[1]
    pt.move(x+100, y, duration=0.5)
    pt.click()
    pt.typewrite(message,interval=0.1)
    
    #pt.typewriter("n\", interval=0.1)

# responses
def process_response(message):
    random_no = random.randrange(3)

    if "hii"in str(message).lower():
        return"hii"

    else:
    if random_no== 0:
        return"that's cool"
    elif random_no ==1:
        return "great"
    else:
        return"i want something to eat"

processed_message =process_response(get_message())
response (processed_message)





