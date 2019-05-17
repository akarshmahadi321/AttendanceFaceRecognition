from tkinter import *
from demo import *
from tkinter import messagebox


class Register(Frame):

    def __init__(self, master):  # Function to initialize the window
        # Initialize the frame
        super(Register, self).__init__(master)
        self.grid()
        self.configure(bg="lightblue")
        self.display_widgets()

    def display_widgets(self): # To display widgets in the frame
        Label(self, text=" ", bg="lightblue", width=6).grid(row=0, column=0, sticky=W)
        Label(self, text=" Student Registration ", font="Georgia 30 italic bold",bg="lightblue",underline=30).grid(row=0, column=1,columnspan=2, sticky=W)
        Label(self, text=" ",bg="lightblue").grid(row=1, column=0, sticky=W)
        Label(self, text=" ",bg="lightblue").grid(row=2, column=0, sticky=W)
        Label(self,text=" Student Name: ", font="Times 18",bg="lightblue", width=15,underline=30).grid(row=3,column=0,sticky=N)
        self.stud_name = Entry(self)
        self.stud_name.grid(row=3, column=1, sticky=W)
        Label(self, text=" ", bg="lightblue").grid(row=4, column=0, sticky=W)
        Label(self,text=" Roll Number: ", font="Times 18",bg="lightblue", width=15,underline=30).grid(row=5,column=0,sticky=N)
        self.roll_no = Entry(self)
        self.roll_no.grid(row=5, column=1, sticky=W)
        Label(self, text=" ", bg="lightblue").grid(row=6, column=0, sticky=W)
        Label(self, text=" ", bg="lightblue").grid(row=7, column=0, sticky=W)
        Label(self, text=" ", bg="lightblue").grid(row=8, column=0, sticky=W)
        self.submitButton = Button(self, command=self.captureAndVal, highlightbackground='lightblue',bg='grey',font="Georgia 15 bold", text="Capture & Register", width=20)
        self.submitButton.grid(row=9, column=1)

    def closeWindow(self):  # Function to close the window
        self.master.quit()
        self.master.destroy()

    def captureAndVal(self): # Util to capture & validate info
        print("\nCapturing image and Validating info...")
        count = 0

        if len(self.stud_name.get()) == 0:
            messagebox.showerror("Error", "Name can't be empty!")
            count = 1

        if len(self.roll_no.get()) == 0:
            messagebox.showerror("Error", "RollNo can't be empty!")
            count = 1

        file_obj = open('rollnumkeys', 'r+') # File to store and validate roll nos
        keys=file_obj.read().splitlines()
        roll_num=self.roll_no.get()

        if roll_num in keys:
            messagebox.showerror("Error","This RollNo has already been registered!")
            count = 1
        else:
            file_obj.write(roll_num + "\n")

        if count == 0:
            messagebox.showinfo("Success", "Opening Camera...")







