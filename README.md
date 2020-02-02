# House-Resource-Management-Tracking-and-Billing-HRMTB-System-Using-QRcode

This system is designed to manage the data of house resources
( Electricity , Water and Gas )
The volume of the resource consumed by the given consumer are recorded on daily basis and saved into the secure server.

Our system consist of two units : 
1. Client Based
2. Server Based 

The QR code assigned to the each and every house is scanned by the billing executive.
The data is fetched from the server and the bill is generated in real time.

The customer can also fetch his billing details in real time and can pay the bill as per his convenience ( Net banking, Credit/Debit Card, UPI etc. ).


The data of the resources used by the customer is saved on the server at the end of each day.
The process is repeated till the day user pays the bill.
When the bill is paid the value of each resource is set to zero (0), and the details of the bill is saved in the history.

The HRMTB system is entirely coded in python 3.8.1 programming language.
For maintaining the database in HRMTB system MySQL 8.0 is used.
Modules Used in HRMTB System :
1. OpenCV
2. Pyzbar
3. MySQL.connector
4. Tkinter
5. Pillow  

# OpenCV

OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products.
The library has more than 2500 optimized algorithms, which includes a comprehensive set of both classic and state-of-the-art computer vision and machine learning algorithms
We have used it to scan the Qrcode via our laptop’s webcam.

# Pyzbar

Read one-dimensional barcodes and QR codes from Python 3 using the zbar library.

We have used pyzbar to get the data (House Details) stored in QR code.

# Mysql.connector

Mysql.connector is a library of python used to connect the mysql database to the python environment and provides methods to access the databases

 We connect our “HouseData” database coded in mysql to python using this module.
 
 
# Tkinter

Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter is the fastest and easiest way to create the GUI applications. Creating a GUI using tkinter is an easy task.
Tkinter is one of the best GUI Module present in python 
Ease to use 
Ease to Code
Ease to Create Applications


# Pilow

 Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.
