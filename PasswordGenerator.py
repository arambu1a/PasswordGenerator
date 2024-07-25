from tkinter import *
import string
import random




def generator():
    lowercaseletters = string.ascii_lowercase 
    capitalletters = string.ascii_uppercase
    num = string.digits 
    special = string.punctuation 

    all = lowercaseletters + capitalletters + num + special
    password_length = int(lengthBox.get())

    password = random.sample(all, password_length)
    passwordField.insert(0,password)



root = Tk ()
root.config(bg='gray20')
choice = IntVar()
Font = ('arial nova', 10)

passwordLabel = Label(root, text = 'Password Generator', font=('arial nova', 32, 'bold'), bg='gray20', fg = 'sky blue')
passwordLabel.grid()
generatebutton = Radiobutton(root, text = 'Adobe', value = 1, variable = choice, font = Font)
generatebutton.grid()
generatebutton = Radiobutton(root, text = 'FastField', value = 2, variable = choice, font = Font)
generatebutton.grid()
generatebutton = Radiobutton(root, text = 'iCloud', value = 3, variable = choice, font = Font)
generatebutton.grid()
generatebutton = Radiobutton(root, text = 'Microsoft', value = 4, variable = choice, font = Font)
generatebutton.grid()

passwordLength = Label(root, text = 'Password Length', font=('arial nova', 24, 'bold'), bg='gray20', fg = 'sky blue')
passwordLength.grid()

lengthBox = Spinbox(root, from_=0, to_=20, width = 5, font = Font)
lengthBox.grid()

actualbutton = Button(root, text= 'Generate', font = Font, command = generator)
actualbutton.grid()

passwordField = Entry(root, width = 25, bd = 2, font = Font)
passwordField.grid()

copybutton = Button(root, text= 'Copy', font = Font)
copybutton.grid()

root.mainloop()