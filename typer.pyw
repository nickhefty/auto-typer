from pyautogui import typewrite
from time import sleep
import tkinter as tk
import tkinter.font as font

DELAY = 2

def send_keys(string):
    if "#label:" in string:
        send_keys(string.split("#label:")[0])
    else:
        sleep(DELAY)
        typewrite(string)
        typewrite("\n")


def make_label(c, length=48):
    if "#label:" in c:
        num = c.split(")")[0]+") "
        return make_label(num + c.split("#label:")[-1])
    while len(c) < length:
        c += ' '
    while len(c) > length:
        c = c[:-1]
    if c[-2:] != "  ":
        c = c[:-2] + ".."
    return c


def main():
    with open("commands.txt", "r") as command_file:
        commands = command_file.read().splitlines()

    window = tk.Tk()
    window.title("Click to type")
    myFont = font.Font(family='Courier')

    #label = tk.Label(text=f"""Once you click a command below, you have {DELAY} seconds 
    #to move to the window you want to type commands into.""")
    #label.pack()

    buttons = [tk.Button(text=make_label(f"{i+1}) "+c), command= lambda c=c: send_keys(c))
     for i, c in enumerate(commands)]

    for b in buttons:
        b['font'] = myFont
        b.pack()

    window.mainloop()

if __name__ == '__main__':
    main()