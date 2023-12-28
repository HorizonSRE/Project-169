from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Creating Buttons and Labels using Class")
root.geometry("900x900")

class CreatingElement:
    def __init__(self):
        print("This is a Class that Creates Elements")
    def createNewElement(self):
        label=Label(root, text="This label was created using a Class")
        label.pack()
        btn=Button(root, text="button", command=self.message)
        btn.pack(padx=20, pady=10)
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button that was made using Class")

obj_of_CreatingElement=CreatingElement()
btn1=Button(root, text="Click to create a label and button using Class", command=obj_of_CreatingElement.createNewElement)
btn1.pack(padx=20, pady=10)
root.mainloop()