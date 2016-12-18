from tkinter import *
from subprocess import call

pyprog = 'tem2.py'
def callpy(): call(['python', '-i', pyprog] )

root = Tk()
Button(root, text='Run', command=callpy).pack()
root.mainloop()