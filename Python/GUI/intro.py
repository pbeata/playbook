# April 6, 2020
from tkinter import *


# LESSON 1
def lesson1():
	# opens a new window (creates a blank window)
	root = Tk()

	# to create a text label (what will hold it, text)
	theLabel = Label(root, text="this is easy")

	# where to place your label "just pack it in wherever you can fit it"
	theLabel.pack()  # puts your label in the root windows

	# need that window continuously on your screen (put in infinite loop)
	root.mainloop()


# LESSON 2 
def lesson2():
	# organize your layout like this: 

	# root = Tk()
	# (NEW STUFF IN HERE)
	# root.mainloop()

	# "FRAME" concept: rectangle invisible container on the screen 
	root = Tk()

	topFrame = Frame(root)
	topFrame.pack()
	
	bottomFrame = Frame(root)
	bottomFrame.pack(side=BOTTOM)  # specify where to put it

	# add widgets! let's make some buttons 
	# (where to put it, the text in the button, foreground button text color)
	
	# FIRST, create the widgets
	button1 = Button(topFrame, text="Button-1", fg="red")
	button2 = Button(topFrame, text="Button-2", fg="blue")
	button3 = Button(topFrame, text="Button-3", fg="green")
	button4 = Button(bottomFrame, text="Button-4", fg="purple")

	# SECOND, pack them in to display them
	button1.pack(side=LEFT)  # LEFT: place it as far left as possible
	button2.pack(side=LEFT)
	button3.pack(side=LEFT)
	button4.pack(side=BOTTOM)

	root.mainloop()


# LESSON 3
def lesson3():
	root = Tk()

	one = Label(root, text="one", bg="red", fg="white")
	one.pack()

	two = Label(root, text="two", bg="green", fg="black")
	two.pack(fill=X)  # fills the window in the x-direction

	three = Label(root, text="three", bg="blue", fg="white")	
	three.pack(side=LEFT, fill=Y)

	root.mainloop()


# LESSON 4
# how to organize stuff
def lesson4():
	root = Tk()

	label1 = Label(root, text="Username")
	label2 = Label(root, text="Password")

	# for user input: use ENTRY (empty box to enter in info)
	entry1 = Entry(root)	# for username
	entry2 = Entry(root)  	# for password

	# think about the organization like a spreadsheet: GRID
	label1.grid(row=0, column=0)  	# column is optional
	label2.grid(row=1)
	# label1 on top and label2 on bottom of column 0

	# now we want to put the entry boxes to the right of the labels
	entry1.grid(row=0, column=1)
	entry2.grid(row=1, column=1)

	root.mainloop()


# LESSON 5
# how to organize stuff further with GRID
def lesson5():
	root = Tk()

	label1 = Label(root, text="Username")
	label2 = Label(root, text="Password")

	# for user input: use ENTRY (empty box to enter in info)
	entry1 = Entry(root)	# for username
	entry2 = Entry(root)  	# for password

	# think about the organization like a spreadsheet: GRID
	label1.grid(row=0, sticky=E)  	# column is optional
	label2.grid(row=1, sticky=E)
	# label1 on top and label2 on bottom of column 0

	# now we want to put the entry boxes to the right of the labels
	entry1.grid(row=0, column=1)
	entry2.grid(row=1, column=1)

	# add a checkbox
	chkbox = Checkbutton(root, text="Keep me logged in")  # 1 create
	chkbox.grid(columnspan=2) # 2 place it to take up 2 cells

	root.mainloop()	


# LESSON 6 Binding Functions to Layouts
def lesson6():
	root = Tk()



	root.mainloop()


# ===============================================


# MAIN

lesson1()
lesson2()
lesson3()
lesson4()
lesson5()
lesson6()

