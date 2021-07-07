import cv2
import os
import numpy
import QR
import mysql.connector
import tkinter
import id_generator
from tkinter import *
from tkinter import messagebox
from mysql.connector import Error
from mysql.connector import errorcode

def remove_img():  #func to remove the test file after
    try:
        os.remove('subject/subject.jpg')
    except:
        pass

def detect_faces(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faceCasc = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
	faces = faceCasc.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
	graylist = []
	faceslist = []

	if len(faces) == 0 :
		return None, None

	for i in range(0, len(faces)):
		(x, y, w, h) = faces[i]
		graylist.append(gray[y:y+w, x:x+h])
		faceslist.append(faces[i])

	return graylist, faceslist

def predict(img):
    face, rect = detect_faces(img)
    if face is not None:
        for i in range(0,len(face)):
            label, conf = face_recognizer.predict(face[i])
            if conf<40:
                label_text = subjects[label]
            else:
                label_text = "Unknown"
            (x,y,w,h) = rect[i]
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0))
            cv2.putText(img, label_text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    else:
        return img,"None"
    return img,label_text

def Guest():
    Page1.destroy()

    def retrieve_input():
        inp = text1.get(1.0,'end-1c')

        if not inp:
            messagebox.showwarning("Warning", "Parameter Missing!\nEnter Full Name")
            return 0
        global subject
        global code
        subject = inp.lower().strip()
        code = id_generator.generateID()
        messagebox.showinfo("Validation","Name Recorded, ID Generated!\nAccess Granted")
        Page6.destroy()

    Page6 = tkinter.Tk()
    Page6.geometry("733x422")
    Page6.title("Security App using Biometric and QR Code Scanning")
    # Page2.configure(bg="SteelBlue1") used to give bg color

    bg = PhotoImage(file = "new.png")
    canvas = Canvas(Page6, width = 750, height = 422)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image = bg, anchor = "nw")

    t1 = Label(Page6,text="Security App",font=("Times New Roman",35,"italic","bold"))
    t1.configure(relief=RAISED, bg="chartreuse2", padx='35', pady='4', fg='red', bd='6')
    t1.place(relx = 0.5, y = 80, anchor = 'center')

    t2 = Label(Page6, text="Enter Your Full Name Below", font=("Times New Roman",18,"italic","bold"))
    t2.configure(bg="Yellow", fg="black", bd='2', padx='20', pady='3', relief=RAISED)
    t2.place(relx = 0.5, rely = 0.4, anchor = 'center')

    text1 = Text(Page6,height=5,width=52,relief=RAISED,border=("2"))
    text1.place(relx = 0.5, rely = 0.55, anchor = 'center')

    button1 = tkinter.Button(Page6, text = "OK", command=retrieve_input)
    button1.place(relx = 0.5, rely = 0.68, anchor = 'center')

    Page6.mainloop()


# ****Page5****
def Page5():
    Page5 = tkinter.Tk()
    Page5.geometry("733x422")
    Page5.title("Security App using Biometric and QR Code Scanning")

    bg = PhotoImage(file = "new.png")
    canvas = Canvas(Page5, width = 750, height = 422)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image = bg, anchor = "nw")

    t1 = Label(Page5,text="Access Granted",font=("Times New Roman",35,"italic","bold"))
    t1.configure(relief=RAISED, bg="chartreuse2", padx='35', pady='4', fg='red', bd='6')
    t1.place(relx = 0.5, y = 80, anchor = 'center')

    t2 = Label(Page5, text="Welcome to the College\n"+"\""+subject.capitalize()+"\"", font=("Times New Roman",20,"italic","bold"))
    t2.configure(bg="Yellow", fg="black", bd='2', padx='20', pady='3', relief=RAISED)
    t2.place(relx = 0.5, rely = 0.5, anchor = 'center')

    button1 = tkinter.Button(Page5, text = "Enter", command=Page5.destroy)
    button1.configure(font=('Times New Roman',18,'bold'),bd='3',padx='43',pady='5',bg="White",fg="green")
    button1.place(relx = 0.5, rely = 0.9, anchor = 'center')

    Page5.mainloop()
# ****Close5****


# ****Page4****
def Page4():
    Page4 = tkinter.Tk()
    Page4.geometry("733x422")
    Page4.title("Security App using Biometric and QR Code Scanning")

    bg = PhotoImage(file = "new.png")
    canvas = Canvas(Page4, width = 750, height = 422)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image = bg, anchor = "nw")

    t1 = Label(Page4,text="Face Verification",font=("Times New Roman",35,"italic","bold"))
    t1.configure(relief=RAISED, bg="chartreuse2", padx='35', pady='4', fg='red', bd='6')
    t1.place(relx = 0.5, y = 80, anchor = 'center')

    t2 = Label(Page4, text="Scanning Photo for Face Verification", font=("Times New Roman",20,"italic","bold"))
    t2.configure(bg="Yellow", fg="black", bd='2', padx='20', pady='3', relief=RAISED)
    t2.place(relx = 0.5, rely = 0.5, anchor = 'center')

    t3 = Label(Page4, text="Recognizing...", font=("Times New Roman",17,"italic","bold"))
    t3.configure(bg="grey", fg="white", bd='2', padx='14', pady='3', relief=RAISED)
    t3.place(relx = 0.5, rely = 0.9, anchor = 'center')

    # face recogntion code here
    global face_recognizer
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('trainner/trainner.yml')

    # error handling
    img = cv2.imread('subject/subject.jpg') #person image
    if img is None:
        messagebox.showinfo("Attention","No Image Passed!\nAccess Denied")
        Page4.destroy()
        print("\n-----** Security App using Bio-metric and QR Code Scanning **-----\n")
        quit()

    img,status = predict(img)
    if status == "None":
        messagebox.showinfo("Attention","No Face Found!\nAccess Denied")
        Page4.destroy()
        remove_img()
        print("\n-----** Security App using Bio-metric and QR Code Scanning **-----\n")
        quit()

    cv2.imshow('Recognition',img)
    cv2.waitKey(4000)
    cv2.destroyAllWindows()

    # status = 'hritik roshan'
    if status==subject:
        messagebox.showinfo("Validation","Face Matched!\nAccess Granted")
        Page4.destroy()
        remove_img()
    else:
        messagebox.showinfo("Validation","Face Not Matched!\nAccess Denied")
        Page4.destroy()
        remove_img()
        print("\n-----** Security App using Bio-metric and QR Code Scanning **-----\n")
        quit()
    Page4.mainloop()
# ****Close4****


# ****Page3****
def Page3():
    Page3 = tkinter.Tk()
    Page3.geometry("733x422")
    Page3.title("Security App using Biometric and QR Code Scanning")

    bg = PhotoImage(file = "new.png")
    canvas = Canvas(Page3, width = 750, height = 422)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image = bg, anchor = "nw")

    t1 = Label(Page3,text="QR Code Verification",font=("Times New Roman",35,"italic","bold"))
    t1.configure(relief=RAISED, bg="chartreuse2", padx='35', pady='4', fg='red', bd='6')
    t1.place(relx = 0.5, y = 80, anchor = 'center')

    t2 = Label(Page3, text="Please Keep Your QR Code at Camera for Scanning", font=("Times New Roman",20,"italic","bold"))
    t2.configure(bg="Yellow", fg="black", bd='2', padx='20', pady='3', relief=RAISED)
    t2.place(relx = 0.5, rely = 0.5, anchor = 'center')

    t3 = Label(Page3, text="Verifying...", font=("Times New Roman",17,"italic","bold"))
    t3.configure(bg="grey", fg="white", bd='2', padx='14', pady='3', relief=RAISED)
    t3.place(relx = 0.5, rely = 0.9, anchor = 'center')

    # link to qr scanner
    global code
    try:
        code = QR.QRinit()
    except:
        messagebox.showinfo("Validation","No Code Passed!\nAccess Denied")
        Page3.destroy()
        remove_img()
        print("\n-----** Security App using Bio-metric and QR Code Scanning **-----\n")
        quit()

    try:
    	code=int(code)
    except:
        messagebox.showinfo("Validation","Absurd Code!\nAccess Denied")
        Page3.destroy()
        remove_img()
        print("\n-----** Security App using Bio-metric and QR Code Scanning **-----\n")
        quit()

    if index == code:
        messagebox.showinfo("Validation","QR Code Matched!\nPass to Face Recognition")
        Page3.destroy()
        Page4()
    else:
        messagebox.showinfo("Validation","QR Code Not Matched!\nAccess Denied")
        Page3.destroy()
        remove_img()
        print("\n-----** Security App using Bio-metric and QR Code Scanning **-----\n")
        quit()

    Page3.mainloop()
# ****Close3****


# ****Page2****
def Page2():
    Page1.destroy()

    global subjects
    subjects = ["","hritik roshan","salman khan","amitabh bachchan","alvin solomon"]  #dataset of persons registered entered here
    def name_veri(fname):
        global subject
        subject = fname.lower().strip()
        if subject not in subjects:
            return 0
        else:
            global index
            index = subjects.index(subject)
            root = str(index)
            return 1

    def retrieve_input():
        inp = text1.get(1.0,'end-1c')
        if not inp:
            messagebox.showwarning("Warning", "Parameter Missing!\nEnter Full Name")
            return 0
        check1 = name_veri(inp)
        if check1 == 1:
            messagebox.showinfo("Validation","Name Found!\nPass to QR Code")
            Page2.destroy()
            Page3()
        else:
            messagebox.showinfo("Validation","Name Not Found!\nAccess Denied")
            Page2.destroy()
            remove_img()
            print("\n-----** Security App using Bio-metric and QR Code Scanning **-----\n")
            quit()

    Page2 = tkinter.Tk()
    Page2.geometry("733x422")
    Page2.title("Security App using Biometric and QR Code Scanning")
    # Page2.configure(bg="SteelBlue1") used to give bg color

    bg = PhotoImage(file = "new.png")
    canvas = Canvas(Page2, width = 750, height = 422)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image = bg, anchor = "nw")

    t1 = Label(Page2,text="Security App",font=("Times New Roman",35,"italic","bold"))
    t1.configure(relief=RAISED, bg="chartreuse2", padx='35', pady='4', fg='red', bd='6')
    t1.place(relx = 0.5, y = 80, anchor = 'center')

    t2 = Label(Page2, text="Enter Your Full Name Below", font=("Times New Roman",18,"italic","bold"))
    t2.configure(bg="Yellow", fg="black", bd='2', padx='20', pady='3', relief=RAISED)
    t2.place(relx = 0.5, rely = 0.4, anchor = 'center')

    text1 = Text(Page2,height=5,width=52,relief=RAISED,border=("2"))
    text1.place(relx = 0.5, rely = 0.55, anchor = 'center')

    button1 = tkinter.Button(Page2, text = "OK", command=retrieve_input)
    button1.place(relx = 0.5, rely = 0.68, anchor = 'center')

    Page2.mainloop()
# ****Close2****


# ****Part1****
Page1 = tkinter.Tk()

Page1.geometry("733x422")
Page1.title("Security App using Biometric and QR Code Scanning")

bg = PhotoImage(file = "new.png")
canvas = Canvas(Page1, width = 750, height = 422)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image = bg, anchor = "nw")

t1 = Label(Page1,text="Welcome to Security App",font=("Times New Roman",35,"italic","bold"))
t1.configure(relief=RAISED, bg="chartreuse2", padx='15', pady='4', fg='red', bd='6')
t1.place(relx = 0.5, y = 80, anchor = 'center')

t2 = Label(Page1, text="Select College Person or Guest", font=("Times New Roman",18,"italic","bold"))
t2.configure(bg="Yellow", fg="black", bd='2', padx='20', pady='3', relief=RAISED)
t2.place(relx = 0.5, rely = 0.43, anchor = 'center')

button1 = tkinter.Button(Page1, text = "College Person", command=Page2)
button1.configure(font=('Times New Roman',18,'bold'),bd='3',padx='8',pady='5')
button1.place(relx = 0.38, rely = 0.59, anchor = 'center')

button2 = tkinter.Button(Page1, text = "Guest", command=Guest)
button2.configure(font=('Times New Roman',18,'bold'),bd='3',padx='43',pady='5')
button2.place(relx = 0.62, rely = 0.59, anchor = 'center')

Page1.mainloop()
# ****Close1****

Page5()


#  ***** Record Entry Starts here *****
firstname,lastname = subject.split()
firstname = firstname.capitalize()
lastname = lastname.capitalize()
try:
	conn = mysql.connector.connect(
		host="localhost",
		database="security",
		user="root",
		password=""
	)
	cursor = conn.cursor()
	mysql_insert_query = ("INSERT INTO entry (id,first_name,last_name) VALUES(%s, %s, %s)",(code,firstname,lastname,))
	cursor.execute(*mysql_insert_query)
	conn.commit()
	print(cursor.rowcount,"Entry Recorded!")
	cursor.close()
except mysql.connector.Error as error:
	print("Connection Failed to Record {}".format(error))
	print("No Record Saved")
finally:
	if (conn.is_connected()):
		conn.close()
		print("MySQL Connection is closed")
print("\n\t    Entry Stored In Database")
print("\n-----** Security App using Bio-metric and QR Code Scanning **-----\n")

print("Name:",subject)
print("ID:",code)
print()
