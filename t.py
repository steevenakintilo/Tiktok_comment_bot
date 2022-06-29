import pyautogui
import time
from random import randint

time.sleep(10)
def comment_bot_tiktok():
    comment_to_post = ["Une Orange orange","une orange orange","une Orange orange","une orange Orange","UNE ORANGE ORANGE","UnE oRaNgE oRaNgE","uNe OrAnGe OrAnGe"]
    try:
        quit_tiktok = pyautogui.locateCenterOnScreen('quit.png',confidence=0.8)
        comment = pyautogui.locateCenterOnScreen('comment.png',confidence=0.8)#If the file is not a png file it will not work
        next_video = pyautogui.locateCenterOnScreen('click.png',confidence=0.8)#If the file is not a png file it will not work
        if str(quit_tiktok) != "None":
            pyautogui.moveTo(quit_tiktok)#Moves the mouse to the coordinates of the image
            pyautogui.click(quit_tiktok[0],quit_tiktok[1])
            time.sleep(3)
        pyautogui.moveTo(comment)#Moves the mouse to the coordinates of the image
        pyautogui.click(comment[0],comment[1])
        time.sleep(1)
        pyautogui.write(comment_to_post[randint(0,len(comment_to_post) - 1)])
        time.sleep(1.2)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.moveTo(next_video)#Moves the mouse to the coordinates of the image
        pyautogui.click(next_video[0],next_video[1])
    except:
        next_video = pyautogui.locateCenterOnScreen('click.png',confidence=0.8)#If the file is not a png file it will not work
        time.sleep(1)
        pyautogui.moveTo(next_video)#Moves the mouse to the coordinates of the image
        pyautogui.click(next_video[0],next_video[1])
idx = 0
while True:
    comment_bot_tiktok()
    time.sleep(1)
    idx = idx + 1
    print(idx)