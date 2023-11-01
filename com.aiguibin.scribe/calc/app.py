import pyautogui
from tkinter import *
from PIL import ImageTk

root = Tk()
root.title("屏幕复制内容显示")

screenshot = pyautogui.screenshot()
image = ImageTk.PhotoImage(screenshot)
label = Label(root, image=image)
label.pack()

root.mainloop()