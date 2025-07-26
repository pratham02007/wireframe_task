# Student Name :- Pratham Koshti


# import tkinter
# m = tkinter.Tk()
# m.mainloop()



# from tkinter import *
# root = Tk()
# w = Label(root, text='Hello Everyone..!, My Name Is Pratham')
# w.pack()
# root.mainloop()



# import tkinter as tk

# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()


# from tkinter import *

# master = Tk()
# Label(master, text='First Name').grid(row=0)
# Label(master, text='Last Name').grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# mainloop()




# from tkinter import *

# master = Tk()
# var1 = IntVar()
# Checkbutton(master, text='Red', variable=var1).grid(row=0, sticky=W)
# var2 = IntVar()
# Checkbutton(master, text='Green', variable=var2).grid(row=1, sticky=W)
# var3 = IntVar()
# Checkbutton(master, text='Blue', variable=var3).grid(row=2, sticky=W)
# mainloop()



# from tkinter import *

# root = Tk()
# v = IntVar()
# Radiobutton(root, text='Male', variable=v, value=1).pack(anchor=W)
# Radiobutton(root, text='Female', variable=v, value=2).pack(anchor=W)
# Radiobutton(root, text='Transgender', variable=v, value=3).pack(anchor=W)
# mainloop()



# from tkinter import *

# top = Tk()
# Lb = Listbox(top)
# Lb.insert(1, 'Python')
# Lb.insert(2, 'Java')
# Lb.insert(3, 'C++')
# Lb.insert(4, 'Any other')
# Lb.pack()
# top.mainloop()





from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
    
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()