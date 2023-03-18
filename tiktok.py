import pyautogui
import time
from random import randint

class Var:
    nb_of_video = 0
    video_done = 0
    video_not_done = 0

def print_file_info(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return(content)

def comment_bot_tiktok(v):
    comment_to_post = print_file_info("comment.txt")
    comment_to_post = comment_to_post.split("\n")
    try:
        comment = pyautogui.locateCenterOnScreen('comment.jpg',confidence=0.8)
        next_video = pyautogui.locateCenterOnScreen('click.png',confidence=0.8)
        pyautogui.moveTo(comment)
        pyautogui.click(comment[0],comment[1])
        time.sleep(1)
        pyautogui.write(comment_to_post[randint(0,len(comment_to_post) - 1)])
        time.sleep(1.2)
        pyautogui.press('enter')
        next_video = pyautogui.locateCenterOnScreen('click.png',confidence=0.8)
        time.sleep(1)
        pyautogui.moveTo(next_video)
        pyautogui.click(next_video[0],next_video[1]) 
        v.nb_of_video += 1
        v.video_done += 1
      
    except:
       next_video = pyautogui.locateCenterOnScreen('click.png',confidence=0.8)
       time.sleep(1)
       pyautogui.moveTo(next_video)
       pyautogui.click(next_video[0],next_video[1])
       v.nb_of_video += 1
       v.video_not_done += 1
    print("Number of video in total: " + str(v.nb_of_video) + " video done: " + str(v.video_done) + " video not done: " + str(v.video_not_done))

def main():
    print("Starting the program...")
    time.sleep(10)
    v = Var()
    while True:
        comment_bot_tiktok(v)
        time.sleep(5)


if __name__ == "__main__":
    main()