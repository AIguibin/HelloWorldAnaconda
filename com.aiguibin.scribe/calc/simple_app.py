import tkinter as tk

def on_click():
    label.config(text="你好，" + entry.get())

app = tk.Tk()
app.title("简单的桌面应用")

label = tk.Label(app, text="请输入你的名字：")
label.pack()

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="点击我", command=on_click)
button.pack()

app.mainloop()