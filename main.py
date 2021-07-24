import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("/Users/grishma/PycharmProjects/whatsapp_chat_bot/whatsapp/Smiley.png", confidence=0.5)
x = position1[0]
y = position1[1]


# get message
def get_message():
    global x, y

    position = pt.locateOnScreen("/Users/grishma/PycharmProjects/whatsapp_chat_bot/whatsapp/Smiley.png", confidence=0.5)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=0.5)
    pt.moveTo(x + 50, y-50, duration=0.5)
    pt.tripleClick()
    pt.rightClick
    pt.moveTo(x+70, y-70)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message is" + whatsapp_message)


# response
def response(message):
    global x, y

    position = pt.locateOnScreen("/Users/grishma/PycharmProjects/whatsapp/Smiley.png", confidence=0.75)
    x = position[0]
    y = position[1]
    pt.move(x + 100, y, duration=0.5)
    pt.click()
    pt.typewrite(message, interval=0.1)

    pt.typewrite("\n", interval=0.1)


# responses
def process_response(message):
    random_no = random.randrange(3)

    if "hii" in str(message).lower():
        return "hii"
    if random_no == 0:
        return "thats cool"
    elif random_no == 1:
        return "great"
    else:
        return "i want something to eat"

#check_for_messages
def check_for_message():
    pt.moveTo(x+50, y-50, duration=0.5)

     while True:
         #loop_for_cont_message_check
        try:
            position= pt.locateOnScreen("/Users/grishma/PycharmProjects/whatsapp_chat_bot/whatsapp/Green_dot", confidence=0.5)

            if position is not none:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(0.50)


        except():
            print("No New Message")


        if pt.pixelMatchesColor(int(x),int(y),(255,255,255), tolerance=15):
            print("is_white")  #make it gray
            processed_message = process_response(get_message())
            response(processed_message)
        else:
            print("No New Message yet...")
        sleep(5)



processed_message = process_response(get_message())
response(processed_message)
