#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Tkinter hesap makinesi örneği
#Try-Expect Metodu kullanımı
from tkinter import *
global label3
def hesapla():
  try:
    num1=float(enter1.get())
    num2=float(enter2.get())
    result=num1*num2
    label3.config(text=str(result))
    label3.grid()
  except ValueError:
      label3.config(text="Sayısal Değer Giriniz !")
      label3.grid()
def hesapla2():
  try:
    num1=float(enter1.get())
    num2=float(enter2.get())
    result=num1/num2
    label3.config(text=str(result))
  except ValueError:
    label3.config(text="Sayısal Değer Giriniz !")
    label3.grid()
def hesapla3():
  try:
    num1=float(enter1.get())
    num2=float(enter2.get())
    result=num1+num2
    label3.config(text=str(result))
    label3.grid()
  except ValueError:
    label3.config(text="Sayısal Değer Giriniz !")
    label3.grid()
def hesapla4():
  try:
    num1=float(enter1.get())
    num2=float(enter2.get())
    result=num1-num2
    label3.config(text=str(result))
    label3.grid()
  except ValueError:
    label3.config(text="Sayısal Değer Giriniz !")


pencere=Tk()
global giris
global giris2
etiket1=Label(text="Birinci sayiyi giriniz")
etiket1.grid()

enter1=Entry()
enter1.grid()

etiket2=Label(text="İkinci Sayiyi giriniz ")
etiket2.grid()

enter2=Entry()
enter2.grid()

btn1 = Button( text='X', command=hesapla).grid(row=4, column=1)

btn2 = Button( text='/', command=hesapla2).grid(row=5, column=1)

btn3 = Button( text='+', command=hesapla3).grid(row=5, column=2)

btn4 = Button( text='-', command=hesapla4).grid(row=4, column=2)

label3 = Label()
label3.grid(row=6, column=1)







mainloop()