from tkinter import *

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def lcm(a,b):
    l = a if a>b else b
    while l<= a*b:
        if l%a==0 and l%b==0:
            return l
        l+=1

def hcf(a,b):
    h = a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1

def factorial(a):
    temp=1
    i=1
    while i<=a:
        temp=temp*i
        i+=1
    return temp

def root(a):
    return a**(1/2)

def square(a):
    return a*a

def croot(a):
    return a**(1/3)

def cube(a):
    return a*a*a

def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)
                r = operations[word.upper()](l[0],l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'Something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0, END)
            list.insert(END, 'Something went wrong please enter again')


operations = {"ADD":add, "ADDITION":add, "SUM":add, "PLUS":add,
              "SUB":sub, "DIFFERENCE":sub, "MINUS":sub, "SUBTRACT":sub,
              "LCM":lcm, "HCF":hcf, "PRODUCT":mul, "MULTIPLY":mul, "MULTIPLICATION":mul,
              "DIVISION":div, "DIVIDE":div, "MOD":mod, "REMAINDER":mod, "MODULUS":mod, "FACTORIAL":factorial,
              "ROOT":root, "SQ":square, "CROOT":croot, "CUBE":cube}
win = Tk()
win.geometry('500x300')
win.title('Smart Prosky')
win.configure(bg='lightskyblue')

l1 = Label(win, text="I am a Smart Calculator",width=20,padx=3 )
l1.place(x=160,y=10)
l2 = Label(win, text="My name is PROSKY",padx=3 )
l2.place(x=180,y=40)
l3 = Label(win, text="What can, I do for U?",padx=3 )
l3.place(x=175,y=130)

textin = StringVar()
e1 = Entry(win , width=45 , textvariable = textin)
e1.place(x=100,y=160)

b1 = Button(win,text="ANSWER",command=calculate)
b1.place(x=210,y=200)

list = Listbox(win,width=30,height=3)
list.place(x=150,y=230)

win.mainloop()