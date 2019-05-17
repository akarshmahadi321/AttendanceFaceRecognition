from tkinter import *
from tkinter import font
from regGUI import *


class GUI(Frame):

    def __init__(self,master):
        self.master=master
        self.frame = Frame(self.master)
        super(GUI, self).__init__()
        self.frame.configure(bg='lightblue')
        self.Geor10 = font.Font(family='Georgia', size=20, weight='bold')
        self.canvas = Canvas(self.frame, width=880, height=170, bg="lightblue")
        self.canvas.grid(row=1,column=1)
        self.img = PhotoImage(file="logo.gif")
        self.canvas.create_image(20, 20, anchor=NW, image=self.img)
        Label(self.frame, text="   ", bg="lightblue", width=25).grid(row=2, column=2, sticky=W)
        self.submitButton = Button(self.frame, command=self.openRegWindow, highlightbackground="lightblue",font=self.Geor10, text="Student Registration",width=20)
        self.submitButton.grid(row=3,column=1)
        Label(self.frame, text="   ", bg="lightblue", width=25).grid(row=4, column=2, sticky=W)
        Label(self.frame, text="   ", bg="lightblue", width=25).grid(row=5, column=3, sticky=W)
        self.recordButton = Button(self.frame, command=self.recordVideo,highlightbackground='lightblue',font=self.Geor10, text="Take Attendance",width=20)
        self.recordButton.grid(row=6,column=1)
        self.frame.pack()

    def openRegWindow(self):# Function to open registration window
        print("\nOpening Student Registration Window...")
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("Student Registration")
        self.newWindow.geometry("600x400")
        self.newWindow.configure(bg="lightblue")
        self.app = Register(self.newWindow)

    def recordVideo(self):# Function to record video to take attendance
        print("\nOpening Student Registration Window...")

    def closeWindow(self):  # Function to close the window
        self.master.quit()
        self.master.destroy()

def main(): #Main Function
    root = Tk()
    root.geometry("888x400")
    root.title("Face Recognition Based Attendance System")
    root['bg']='lightblue'
    app = GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
