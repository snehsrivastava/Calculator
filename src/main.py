"""
    Calculator (GUI) using Tkinter and Python 3.10.5
     * author: Suraj Kumar Giri.
     * Date: 05-09-2022 (Started)
     * Time: 02: 34: 39 (Started)
     * last modified: 19th Sep 2022
"""

from tkinter import *
from sys import path
from PlaceIcons import PlaceIcons
import calculation as cal
path[0] = "D:\\Programming\\Projects\\Python\\GUI Projects\\Calculator"


def main():
    """
        Summary:
            Main function of the program from where execution of the program starts.
    """
    root = Tk()  # master/root windows
    root.title("Calculator")
    root.geometry("570x850")
    root.minsize(560, 760)
    # Creating a Canvas on root then place the icons on it instead of root. So that icons will also change it's position if we resize the root window.
    # Because when window is resized (restore down, maximize, minimize) then canvas will also resize according to it and icons placed on canvas, so by default will move with it.
    iconsArea = Canvas(root, width=600, height=850)
    iconsArea.create_rectangle(
        30, 50, 540, 690, outline="#2575fc", fill=None, width=10)
    iconsArea.pack()
    # PlaceIcons(iconsArea, cursorType="hand2").placeIconsOnGUI()
    PlaceIcons(iconsArea, cursorType="hand2").placeIconsOnGUI()

    userText = StringVar(iconsArea, value="")
    resultText = StringVar(iconsArea, value="")

    inputArea = Entry(iconsArea, width=17, font="Calibri 30",
                      textvariable=userText)
    inputArea.place(x=25, y=700)

    resultLabel = Label(iconsArea, width=8,
                        font="Calibri 30", bg="black", fg="magenta", textvariable=resultText)
    resultLabel.place(x=380, y=700)
    cal.setIdentifiers(userText, resultText, inputArea)
    root.mainloop()
    # root.configure(bg="black")


if __name__ == '__main__':
    main()
