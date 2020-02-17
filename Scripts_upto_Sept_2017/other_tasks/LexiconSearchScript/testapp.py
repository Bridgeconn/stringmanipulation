#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import json
import codecs
import pdb
import csv
import os
import sys
import glob
import errno
from tkinter import *



class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()


    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter Strongs number")

        button = Tkinter.Button(self,text=u"Search",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable0 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable0,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')

        self.labelVariable1 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable1,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=2,columnspan=2,sticky='EW')

        self.labelVariable2 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable2,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=3,columnspan=2,sticky='EW')

        self.labelVariable3 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable3,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=4,columnspan=2,sticky='EW')

        self.labelVariable4 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable4,
                              anchor="w",fg="black",bg="white", wraplength=400)
        label.grid(column=0,row=5,columnspan=2,sticky='EW')

        self.labelVariable5 = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable5,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=6,columnspan=2,sticky='EW')

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True, False)
        self.update()
        # self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        pron = ""
        lex = ""
        trans = ""
        define = ""
        stro = ""
        flag = False
        files = glob.glob('**/*.json')
        for name in files:
            f = codecs.open(name, mode="r", encoding="utf-8")
            data=json.loads(f.read())

            for item in data.items():
                key = item[0].encode('utf-8')
                if key == self.entryVariable.get():
                    flag = True
                    status = "Found !"

                    if item[1]['pronunciation'] != None:
                        pron = item[1]['pronunciation'].encode('utf-8')
                    else:
                        pron = ""

                    if item[1]['unicode'] != None:
                        lex = item[1]['unicode'].encode('utf-8')
                    else:
                        lex = ""

                    if item[1]['translit'] != None:
                        trans = item[1]['translit'].encode('utf-8')
                    else:
                        trans = ""

                    if item[1]['definition'] != None:
                        define = item[1]['definition'].encode('utf-8')
                        define = " ".join(define.split())
                    else:
                        define = ""

                    stro = item[1]['strongs_number'].encode('utf-8')
                else:
                    if flag != True:
                        status = "Not found in Lexicon"

        self.labelVariable0.set("'" + status + "'")
        self.labelVariable1.set("Pronunciation: " + pron)
        self.labelVariable2.set("Lexeme: " + lex)
        self.labelVariable3.set("Transliteration: " + trans)
        self.labelVariable4.set(("Definition: " + define).strip())
        self.labelVariable5.set("Strongs number: " + stro)

        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self, event):
        pron = ""
        lex = ""
        trans = ""
        define = ""
        stro = ""
        flag = False
        files = glob.glob('**/*.json')
        for name in files:
            f = codecs.open(name, mode="r", encoding="utf-8")
            data=json.loads(f.read())

            for item in data.items():
                key = item[0].encode('utf-8')
                if key == self.entryVariable.get():
                    flag = True
                    status = "Found !"

                    if item[1]['pronunciation'] != None:
                        pron = item[1]['pronunciation'].encode('utf-8')
                    else:
                        pron = ""

                    if item[1]['unicode'] != None:
                        lex = item[1]['unicode'].encode('utf-8')
                    else:
                        lex = ""

                    if item[1]['translit'] != None:
                        trans = item[1]['translit'].encode('utf-8')
                    else:
                        trans = ""

                    if item[1]['definition'] != None:
                        define = item[1]['definition'].encode('utf-8')
                        define = " ".join(define.split())
                    else:
                        define = ""

                    stro = item[1]['strongs_number'].encode('utf-8')
                else:
                    if flag != True:
                        status = "Not found in Lexicon"

        self.labelVariable0.set("'" + status + "'")
        self.labelVariable1.set("Pronunciation: " + pron)
        self.labelVariable2.set("Lexeme: " + lex)
        self.labelVariable3.set("Transliteration: " + trans)
        self.labelVariable4.set("Definition: " + define)
        self.labelVariable5.set("Strongs number: " + stro)

        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Strongs Lexicon')
    app.mainloop()
