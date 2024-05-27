from tkinter import * 
from tkinter import filedialog

root = Tk()
root.geometry("200x160")

def encrypt_image():
    file1=filedialog.askopenfile(mode='r',filetypes=[
        ('jpg','*.jpg;*.jpeg'),
        ('png', '*.png')
        ])
    if file1 is None:
        return  # cancelled operation
    file_name=file1.name
    key=entry1.get(1.0,END).strip() # get key, remove white space
    if not key.isdigit():
        print("Invalid key. Please enter a numeric key.")
        return
    key = int(key)
    
    print(file_name,key)
    with open(file_name,'rb') as fi:
        image = fi.read()
    
    image = bytearray(image)
    
    for index,values in enumerate(image):
        image[index] = values^(key)
    
    with open(file_name,'wb') as fi1:
        fi1.write(image)

b1=Button(root,text="encrypt",command=encrypt_image)
b1.place(x=70,y=10)

entry1=Text(root,height=1,width=10)
entry1.place(x=50,y=50)

root.mainloop()