from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb 


root=Tk()
root.title("στεγαυω")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="black")

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetype=(("PNG file","*.png"),("JPG file","*.jpg"),("All file","*.txt" )))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

    
def Hide():
     global secret
     message=text1.get(1.0,END)
     secret = lsb.hide(str(filename), message)

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)

def save():
    secret.save("hidden.png")



#icons
image_icon=PhotoImage(file="C:\Github\Python\Stagnography_Python\skull.png")
root.iconphoto(False,image_icon)


#logo
image = Image.open("C:\Github\Python\Stagnography_Python\cyber-security.png")
 
# Resize the image using resize() method
resize_image = image.resize((60, 60))
 
img = ImageTk.PhotoImage(resize_image)

Label(root,image=img,bg="black").place(x=10,y=10)

Label(root,text="STEGAVO",bg="black",fg="white",font="arial 24 bold").place(x=100,y=20)

#firstframe
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

#secondframe
frame2=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#thirdframe
frame3=Frame(root,bd=3,bg="black",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="OPEN",width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=30)
Button(frame3,text="SAVE",width=10,height=2,font="arial 14 bold",command=save).place(x=180,y=30)
Label(frame3,text="Select the Image",bg="black",fg="green").place(x=20,y=5)

#fourthframe
frame4=Frame(root,bd=3,bg="black",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="HIDE",width=10,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="SHOW",width=10,height=2,font="arial 14 bold",command=Show).place(x=180,y=30)
Label(frame4,text="Select the Image",bg="black",fg="green").place(x=20,y=5)


root.mainloop()
