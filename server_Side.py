import cv2
import pyzbar.pyzbar as bar
import mysql.connector as sql
from tkinter import *
from tkinter import ttk
import datetime
from PIL import Image, ImageTk
import time

dB = sql.connect(host="localhost", username="root", passwd=yourmysqlpassword, database="houseData")

accessId = dB.cursor(buffered=True)
accessId.execute("show tables")

houses = {}
mNo = [4521369785, 5412593785, 4521369856, 5412589632]

mnoi = 0

for i in accessId:
    global moni
    houses[i[0]] = mNo[mnoi]
    mnoi += 1

print(houses)

dateVar = 0
gasVar = 0
waterVar = 0
elecVar = 0


def ScanFunc():
    cam = cv2.VideoCapture(0)

    while True:
        _, fr = cam.read()
        decodedObj = bar.decode(fr)
        for i in decodedObj:
            # print("Data =", i.data.decode('ascii'))
            print(i)
            hData = i.data.decode('ascii')
            cv2.rectangle(fr, (i.rect.left, i.rect.top), (i.rect.left + i.rect.width, i.rect.top + i.rect.height),
                          (255, 0, 0), 3)
            return hData

        cv2.imshow('fr', fr)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cam.release()
    cv2.destroyAllWindows()


def nextDate():
    global dateVar
    dateVar += 1
    print(dateVar)
    base = datetime.datetime.today()
    date = str(base + datetime.timedelta(dateVar))
    print(date)
    date = date[0:10]
    time.sleep(2)
    accessId.execute("SELECT max(Serial) FROM h1")
    res = accessId.fetchall()
    serial = res[0][0] + 1
    gas = str(gasVar) + " Kg"
    water = "3-4PM, " + str(waterVar) + "L"
    a = (serial, date, gas, water, elecVar)
    incm = "insert into " + Code + "(Serial, date, Gas, Water, Electricity) values(%s,%s,%s,%s,%s)"
    accessId.execute(incm, a)
    progBar.insert(INSERT, "Done👍👍\n")
    dB.commit()


def incGas():
    global gasVar
    gasVar = gasVar + 1
    print(gasVar)
    progBar.insert(INSERT, "Total Gas used till now " + str(gasVar) + " Kg\n")


def incWat():
    global waterVar
    waterVar = waterVar + 2
    print(waterVar)
    progBar.insert(INSERT, "Total Water used till now " + str(waterVar) + " Lt.\n")


def incElec():
    global elecVar
    elecVar = elecVar + 1
    print(elecVar)
    progBar.insert(INSERT, "Total Electricity consumed till now " + str(elecVar) + " Unit\n")


Code = ScanFunc()
cv2.destroyAllWindows()
if Code in houses:
    root = Tk()
    root.title("House Resource Management, Tracking and Billing System 🤩😎")

    img = Image.open("bu.jpg")
    photo = ImageTk.PhotoImage(img)
    Label(image=photo).pack()

    dateBut = ttk.Button(root, text="Update Date", width=30, command=nextDate)
    dateBut.place(relx=0.66, rely=0.20, relheight=0.1, relwidth=0.3)
    gasBut = ttk.Button(root, text="Gas", width=30, command=incGas)
    gasBut.place(relx=0.66, rely=0.35, relheight=0.1, relwidth=0.3)
    waterBut = ttk.Button(root, text="Water", width=30, command=incWat)
    waterBut.place(relx=0.66, rely=0.50, relheight=0.1, relwidth=0.3)
    elecBut = ttk.Button(root, text="Electricity", width=30, command=incElec)
    elecBut.place(relx=0.66, rely=0.65, relheight=0.1, relwidth=0.3)
    exitBut = ttk.Button(root, text="Exit", width=30, command=exit)
    exitBut.place(relx=0.85, rely=0.88, relheight=0.05, relwidth=0.1)

    # Status Frame
    satFrame = ttk.LabelFrame(root, text="Progress...")
    satFrame.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.6)
    progBar = Text(satFrame, wrap=WORD)
    progBar.config(state="normal")
    progBar.place(relx=0.05, rely=0.02, relheight=0.97, relwidth=0.9)
    scrllBar = ttk.Scrollbar(progBar)
    scrllBar.pack(side=RIGHT, fill=Y)
    scrllBar.config(command=progBar.yview)
    scrllBar = ttk.Scrollbar(progBar)
    # End Status Frame

    root.geometry("1366x768")
    root.mainloop()
