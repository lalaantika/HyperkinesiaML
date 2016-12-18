import tkinter as tk
from tkinter import ttk
import os
import crossvalidation as cv
import numpy as np
import re
import sys
import csv
import tkinter
import pickle
from threading import Thread
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import inspect


class Program(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (MainFile, Requirements, Softwarerequirements, Predictionalgo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(MainFile)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainFile(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        innerFrame = tk.Frame(self)
        innerFrame.place(relx=.5, rely=.5, anchor="c")
        intros = ttk.Button(innerFrame, text="Hyperkinesia ML (Prediction Tool) -Home")
        intros.grid(row=0, column=2, columnspan=5, sticky="N", padx=40)
        intro = ttk.Button(innerFrame, text="Instructions", command=lambda: controller.show_frame(Requirements))
        intro.grid(row=3, column=0, columnspan=3, sticky="W", padx=40)
        software = ttk.Button(innerFrame, text="Software Requirements",
                              command=lambda: controller.show_frame(Softwarerequirements))
        software.grid(row=3, column=6, columnspan=4, sticky="E", pady=30)
        introz = ttk.Button(innerFrame, text="Cellprofiler", command=self.openFile)
        introz.grid(row=5, column=0, columnspan=3, sticky="W", padx=40)
        softwarez = ttk.Button(innerFrame, text="Prediction Algorithms",
                               command=lambda: controller.show_frame(Predictionalgo))
        softwarez.grid(row=5, column=6, columnspan=4, sticky="E", pady=30)
        edit = ttk.Button(innerFrame, text="Start", width='30', command=lambda: controller.show_frame(Predictionalgo))
        edit.grid(row=7, columnspan=9)

    def openFile(self):
        os.startfile("C:\Program Files\CellProfiler\CellProfiler.exe")


class Requirements(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        innerFrame = tk.Frame(self)
        innerFrame.place(relx=.4, rely=.4, anchor="c")
        namedate = tk.Label(innerFrame,
                            text="- Install all the software required First.\n - Change the CellProfiler two directories in preferences Plugin \n Directory with CP-Charm Modules \n and ImageJ Plugins to imagej plugin path \n- Import pipeline of CP-charm from file menu. \n - To specify classes name as “NegCtrl” and “PosCtrl” as \n for the classification and training part create folder of these name \n and place the data there for training \n  - Edit extensions in metadata and in name and types \n according to image format.\n - Edit regular expression in meta data from \n (?P<Key>.*)-(?P<HoldOut>[A-Z])-.*.tif  and make it \n (?p&lt;Key&gt;.*).<image Format> and click update \n - Change File Extension in Nameand type of Cellprofiler then click update.\n - Click Analyze Images and it will give output in CSV Format.\n - Then give output of CellProfiler as input for training testing algorithm.")
        namedate.grid(row=2, columnspan=9, sticky="W" + "E")
        update = ttk.Button(innerFrame, text="Instructions for Hyperkinesia ML Tool", width='150')
        update.grid(row=0, columnspan=9)
        edit = ttk.Button(innerFrame, text="Back Home", width='50', command=lambda: controller.show_frame(MainFile))
        edit.grid(row=4, columnspan=9)


class Softwarerequirements(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        innerFrame = tk.Frame(self)
        innerFrame.place(relx=.4, rely=.4, anchor="c")
        update = ttk.Button(innerFrame, text="Software Requirments ", width='150')
        update.grid(row=0, columnspan=9)
        namedata = tk.Label(innerFrame,
                            text="These are the software required to run the prediction tool for \n Hyperkinesia. To use this tool efficently we have to install them \n Step by Step \n - Windows 7/8/10 \n - Anaconda2 \n- Python 2.7 \n - Numpy 1.10 \n - Scipy 0.17 \n  - Scikit-learn \n  - ImageJ \n  - CellProfiler \n - Cp-Charm \n ")
        namedata.grid(row=2, columnspan=9, sticky="W" + "E")
        edit = ttk.Button(innerFrame, text="Back Home", width='50', command=lambda: controller.show_frame(MainFile))
        edit.grid(row=4, columnspan=9, padx=20)


class Predictionalgo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        innerFrame = tk.Frame(self)
        innerFrame.place(relx=.4, rely=.4, anchor="c")
        update = ttk.Button(innerFrame, text="Prediction Algorithms For Machine Learning ", width='150')
        update.grid(row=0, columnspan=9)
        label = ttk.Label(innerFrame, text="Page Two!!!")
        label.grid(row=2, pady=10, padx=10)
        intro = ttk.Button(innerFrame, text="Train Test", command=self.openFile)
        intro.grid(row=3, column=0, columnspan=3, sticky="W", padx=40)
        software = ttk.Button(innerFrame, text="Classfy Algorithms", command=self.OpenFiles)
        software.grid(row=3, column=6, columnspan=4, sticky="E", pady=30)
        edit = ttk.Button(innerFrame, text="Back Home", width='50', command=lambda: controller.show_frame(MainFile))
        edit.grid(row=4, columnspan=9, padx=20)

    def openFile(self):
        os.startfile("GUItraintest.py")

    def OpenFiles(self):
        os.startfile("GUIclassify.py")


app = Program()
app.state('zoomed')
app.mainloop()
