import cv2
import pyzbar.pyzbar as bar
import mysql.connector as sql
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests

dB = sql.connect(host="localhost", username="root", passwd=yourmysqlpassword, database="houseData")

accessId = dB.cursor()
accessId.execute("show tables")

hname = []

for i in accessId:
    hname.append(i[0])

accessId.execute("show tables")

houses = {}
mNo = [8077049606, 9760778113, 8218872092, 9012887831]

mnoi = 0

for i in accessId:
    houses[i[0]] = mNo[mnoi]
    mnoi += 1

print(houses)


def ScanFunc():
    cam = cv2.VideoCapture(0)
    while True:
        _, fr = cam.read()
        decodedObj = bar.decode(fr)
        for i in decodedObj:
            cv2.imwrite("C://Users//Shiv//PycharmProjects//Shiv//Hackathon//image.png", fr)
            print(i)
            hData = i.data.decode('ascii')
            cv2.rectangle(fr, (i.rect.left, i.rect.top), (i.rect.left + i.rect.width, i.rect.top + i.rect.height),
                          (255, 0, 0), 3)
            return hData

        cv2.imshow('QR code Scanner', fr)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cam.release()
    cv2.destroyAllWindows()


def payment_link(amt):
    headers = {'Host': 'dashboard.paytm.com',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0',
               'Accept': 'application/json', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate',
               'Referer': 'https://dashboard.paytm.com/next/payment-link', 'osVersion': '5.0 (Macintosh)',
               'client': 'UMP', 'customerId': '39327872', 'Content-Type': 'application/json', 'channel': 'web',
               'X-XSRF-TOKEN': '117f836c-a091-41bb-85cf-c6ea853af764', 'Origin': 'https://dashboard.paytm.com',
               'Content-Length': '90', 'Connection': 'close', 'Cookie': 'SESSION=702cbe68-4e62-4ce5-bf41-dc77431c1fbb;'}
    url = "https://dashboard.paytm.com/api/v1/payment/link"
    data = '{"amount":"' + str(amt) + '","linkDescription":"Bill Payment","linkName":20722,"previewAmount":"' + str(
        amt) + '"}'
    try:
        return requests.post(url, data=data, headers=headers, timeout=10).json()['shortUrl']
    except:
        return "https://www.paytm.com/"

def smsSender(totBill1):
    url = "https://api.msg91.com/api/v2/sendsms"
    data = '{"sender": "GNOIDA","route": "4","country": "91","sms": [{"message": "' + "Your has been generated successfully of Rs." + str(
        totBill1) + ", You can made payment by clicking in the following link " + str(
        payment_link(totBill1)) + '","to": [' + str(houses[Code]) + ']}]}'
    headers = {'authkey': "224179A4u1cZx15t5cdd109c", 'content-type': "application/json"}
    r = requests.post(url, data=data, headers=headers, timeout=10)
    print(data)
    print(r.text)

    root.destroy()
    confR = Tk()
    confR.title("SMS")
    img = Image.open("tick.png")
    photo = ImageTk.PhotoImage(img)
    Label(confR, image=photo).pack()
    Label(confR).pack()
    subLab = Label(confR, text='SMS send \n Successfully!!', font=('Times New Roman', 10)).pack()

    confR.geometry("200x200+500+200")
    confR.mainloop()


def getdta(event=""):
    _list = root.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    for item in _list:
        item.pack_forget()

    global serInp
    serInp = serInpEnt.get()
    print(serInp)
    getData = "SELECT * FROM h1 WHERE serial > 0 and Serial < " + serInp
    print(getData)
    accessId.execute(getData)
    res = accessId.fetchall()

    totGas = 0
    totWat = 0
    totElec = 0
    for i in res:
        totWat += int(i[3][8:10])
        totGas += int(i[2][0])
        totElec += int(i[4])

    gas = "Total Gas Used* =  " + str(totGas) + " KG"
    water = "Total Water Used* =  " + str(totWat) + " L"
    elec = "Total Electricity Used* =  " + str(totElec) + " Unit"

    gasBill = "The Cost for Gas Consumed this month = ₹" + str(totGas * 20)
    watBill = "The Cost for Water Consumed this month = ₹" + str(totWat * 0.95)
    elecBill = "The Cost for Electricity Consumed this month = ₹" + str(totElec * 4.5)
    totBill1 = totGas * 20 + totWat * 0.85 + totElec * 4.5
    totBill = "The amount payable for this month resource consumption = ₹" + str(
        totGas * 20 + totWat * 0.85 + totElec * 4.5)

    gasLbl = Label(root, text=gas).pack()
    gasLbl = Label(root).pack()
    waterLbl = Label(root, text=water).place(x=315, y=20)
    waterLbl = Label(root).pack()
    elecLbl = Label(root, text=elec).place(x=315, y=40)
    elecLbl = Label(root).pack()
    gasLbl = Label(root, text=gasBill).place(x=0, y=143)
    gasLbl = Label(root).pack()
    waterLbl = Label(root, text=watBill).place(x=0, y=169)
    waterLbl = Label(root).pack()
    elecLbl = Label(root, text=elecBill).place(x=0, y=195)
    elecLbl = Label(root).pack()
    elecLbl = Label(root, text=totBill, bg='yellow').place(x=0, y=225)
    elecLbl = Label(root).pack()

    elecLbl = Label(root,
                    text="*You can Pay the amount Now via CC/DC, or through Net Banking etc online payment option").place(
        x=0, y=265)
    elecLbl = Label(root).pack()
    elecLbl = Label(root, text="*You can complain for any kind of mistake or error in out system").place(x=0, y=285)
    elecLbl = Label(root).pack()
    elecLbl = Label(root, text="*Sorry for any kind of inconvenience").place(x=0, y=315)
    elecLbl = Label(root).pack()
    elecLbl = Label(root, text="Bill Generated by Gnida").place(x=300, y=325)
    elecLbl = Label(root).pack()
    elecLbl = Label(root).pack()
    elecLbl = Label(root).pack()
    elecLbl = Label(root).pack()
    elecLbl = Label(root).pack()
    elecLbl = Label(root).pack()
    elecLbl = Label(root).pack()
    elecLbl = Label(root).pack()
    elecLbl = Label(root).pack()
    elecLbl = Label(root).pack()

    subLab = Label(root, text='Send SMS', font=('Times New Roman', 10))
    subLab.place(x=673, y=325)

    serBut.place(x=685, y=290)
    photo2 = PhotoImage(file='sms.png')
    serBut.config(image=photo2)
    serBut.config(command=lambda: smsSender(totBill1))

    root.geometry("768x350+300+0")
    root.mainloop()


Code = ScanFunc()
cv2.destroyAllWindows()
if Code in hname:
    root = Tk()
    root.title("House Resource Management, Tracking and Billing System 🤩😎")
    root.iconbitmap(False, "5.ico")

    frane = Frame(root)
    frane.pack()
    img = Image.open("image.png")
    img = img.resize((250, 220))
    photo = ImageTk.PhotoImage(img)
    Label(frane, image=photo).pack()
    Label(frane).pack()
    Label(frane).pack()

    photo2 = PhotoImage(file='submit.png')

    Label(root, text="Upto how many Days??").pack()
    serInpEnt = ttk.Entry(root, width=40)
    serInpEnt.pack()
    Label(root).pack()
    subLab = Label(root, text='SUBMIT', font=('Times New Roman', 10))
    subLab.place(x=95, y=315)
    serBut = ttk.Button(root, width=40, image=photo2, command=getdta)
    serBut.place(x=158, y=310)
    root.bind("<Return>", getdta)

    Label(root).pack()

    root.geometry("300x350+500+200")
    root.mainloop()
