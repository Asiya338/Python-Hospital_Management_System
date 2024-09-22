from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector 

window = Tk() #root
window.title('Hospital management system')
window.geometry('1258x950+0+0') #width, height, coloum & row position = 0


title = Label(window, bd=12, relief='ridge',
              text="Hospital Management System", fg='blue', bg='white', font='arial 25')
title.pack(side=TOP, fill=X)

NamesofTablet = StringVar()
patientId = StringVar()
IssueDate = StringVar()
Dose = StringVar()
Tablets = StringVar()
bloodPressure = StringVar()
patientname = StringVar()
DOB1 = StringVar()
Address1 = StringVar()
ExpDate = StringVar()

dataFrame = Frame(window, bd=12, relief=RIDGE)
dataFrame.place(x=0, y=65, width=1244, height=722)

dataFrameLeft = LabelFrame(dataFrame, bd=7, relief=RIDGE, padx=10, font=(
    'arial 22'), text='Patient Information')
dataFrameLeft.place(x=5, y=5, width=600, height=220)

dataFrameRight = LabelFrame(dataFrame, bd=7, relief=RIDGE, padx=10,
                            font='arial 22', text='Prescription')
dataFrameRight.place(x=644, y=5, width=555, height=220)


buttonFrame = Frame(window, bd=10, relief=RIDGE)
buttonFrame.place(x=15, y=320, width=1200, height=60)


detailsFrame = Frame(window, bd=10, relief=RIDGE)
detailsFrame.place(x=15, y=400, width=1200, height=222)


tablet = Label(dataFrameLeft, text='Names of Tablet:',
               font='arial 12', padx=10, pady=6)
tablet.grid(row=0, column=0)

comboBox = ttk.Combobox(
    dataFrameLeft, textvariable=NamesofTablet, font='arial 10', width=15)
comboBox['values'] = ('paracetamal', 'dolo 650', 'ativan', 'flexotan')
comboBox.grid(row=0, column=1)

patient_id = Label(dataFrameLeft, text="patientID:", font='bold 12')
patient_id.grid(row=1, column=0, padx=10, pady=5)
patient_id = Entry(dataFrameLeft, textvariable=patientId)
patient_id.grid(row=1, column=1, padx=10, pady=5)

issueDateLabel = Label(dataFrameLeft, text="IssueDate:", font='bold 12')
issueDateLabel.grid(row=2, column=0, padx=10, pady=5)
issueDateLabelEntry = DateEntry(dataFrameLeft, textvariable=IssueDate)
issueDateLabelEntry.grid(row=2, column=1, padx=10, pady=5)


DosE = Label(dataFrameLeft, text="Dose", font='bold 12')
DosE.grid(row=3, column=0, padx=10, pady=5)
DoseE = Entry(dataFrameLeft, textvariable=Dose)
DoseE.grid(row=3, column=1, padx=10, pady=5)


TabletsE = Label(dataFrameLeft, text="no. of tablets", font='bold 12')
TabletsE.grid(row=4, column=0, padx=10, pady=5)
TabletsE = Entry(dataFrameLeft, textvariable=Tablets)
TabletsE.grid(row=4, column=1, padx=10, pady=5)


bloodPressureE = Label(dataFrameLeft, text="bloodPressure", font='bold 12')
bloodPressureE.grid(row=0, column=3, padx=10, pady=5)
bloodPressureE = Entry(dataFrameLeft, textvariable=bloodPressure)
bloodPressureE.grid(row=0, column=4, padx=10, pady=5)

patientnameE = Label(dataFrameLeft, text="patientname", font='bold 12')
patientnameE.grid(row=1, column=3, padx=10, pady=5)
patientnameE = Entry(dataFrameLeft, textvariable=patientname)
patientnameE.grid(row=1, column=4, padx=10, pady=5)

DOB1E = Label(dataFrameLeft, text="DOB", font='bold 12')
DOB1E.grid(row=2, column=3, padx=10, pady=5)
DOB1E = DateEntry(dataFrameLeft, textvariable=DOB1)
DOB1E.grid(row=2, column=4, padx=10, pady=5)

Address1E = Label(dataFrameLeft, text="Address", font='bold 12')
Address1E.grid(row=3, column=3, padx=10, pady=5)
Address1E = Entry(dataFrameLeft, textvariable=Address1)
Address1E.grid(row=3, column=4, padx=10, pady=5)

ExpDateE = Label(dataFrameLeft, text="ExpDate", font='bold 12')
ExpDateE.grid(row=4, column=3, padx=10, pady=5)
ExpDateE = DateEntry(dataFrameLeft, textvariable=ExpDate)
ExpDateE.grid(row=4, column=4, padx=10, pady=5)

prescriptionFrame = Text(dataFrameRight, font='bold 15',
                    width=45, height=7, padx=2, pady=4)
prescriptionFrame.grid(row=0, column=0)


def prescription():
    if NamesofTablet.get() == "" or patientId.get() == "":
        messagebox.showerror('Error', 'Fields cannot be empty')
    else:
        con = mysql.connector.connect(
            host="localhost", username="root", password="asiyacse504@", database="pythondata")
        myCurser = con.cursor()
        myCurser.execute("insert into patientdata values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            NamesofTablet.get(),
            patientId.get(),
            IssueDate.get(),
            Dose.get(),
            Tablets.get(),
            bloodPressure.get(),
            patientname.get(),
            DOB1.get(),
            Address1.get(),
            ExpDate.get(),
        ))
        con.commit()
        fetchData()
        con.close()
        messagebox.showinfo('success','Data has been Recorded')

def fetchData():
    con=mysql.connector.connect(
    host="localhost", username="root", password="asiyacse504@", database="pythondata")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM patientdata")

    rows = cursor.fetchall()

    for row in rows:
        hmsTable.insert("", END, values=row)
    con.commit()
    con.close()

def getCursor(event):
    cursorRow = hmsTable.focus()
    content = hmsTable.item(cursorRow)
    row = content["values"]
    NamesofTablet.set(row[0])
    patientId.set(row[1])
    IssueDate.set([2])
    Dose.set([3])
    Tablets.set([4])
    bloodPressure.set([5])
    patientname.set([6])
    DOB1.set([7])
    Address1.set([8])
    ExpDate.set([9])
    
def update():
    con = mysql.connector.connect(host="localhost", username="root", password="asiyacse504@", database="pythondata")
    myCurser = con.cursor()
    sqlUpdate = ("update patientdata set NamesofTablet=%s, IssueDate=%s, Dose=%s, Tablets=%s ,bloodPressure=%s, patientname=%s,  DOB1=%s, Address1=%s,  ExpDate=%s where patientId = %s")
    val = (
    NamesofTablet,
    IssueDate,
    Dose,
    Tablets,
    bloodPressure,
    patientname,
    DOB1,
    Address1,
    ExpDate,
    patientId
    )
    myCurser.execute(sqlUpdate, val)

    con.commit()
    #myCurser.close()
    con.close()
    messagebox.showinfo('success', 'data updated successfully')

def prescriptionDetails():
    prescriptionFrame.insert(END, 'Name of Tablet:'+NamesofTablet.get()+'\t\t\t')
    prescriptionFrame.insert(END, 'Patient Id:'+patientId.get()+'\n')
    prescriptionFrame.insert(END, 'Issue Date:'+IssueDate.get()+'\t\t\t')
    prescriptionFrame.insert(END, 'Dose:'+Dose.get()+'\n')
    prescriptionFrame.insert(END, 'Tablets:'+Tablets.get()+'\t\t\t')
    prescriptionFrame.insert(END, 'Blood Pressure:'+bloodPressure.get()+'\n')
    prescriptionFrame.insert(END, 'Patient Name:'+patientname.get()+'\t\t\t')
    prescriptionFrame.insert(END, 'DOB:'+DOB1.get()+'\n')
    prescriptionFrame.insert(END, 'Address:'+bloodPressure.get()+'\t\t\t')
    prescriptionFrame.insert(END, 'EXP date:'+ExpDate.get()+'\n')


def delete():
    con = mysql.connector.connect(
    host="localhost", username="root", password="asiyacse504@", database="pythondata")
    myCursor = con.cursor()

    myCursor.execute("truncate table patientdata")
    con.commit()
    messagebox.showinfo('Info','All the records have been deleted')
    # Close the cursor and the connection
    myCursor.close()
    con.close()


def clear():
    NamesofTablet.set("")
    patientId.set("")
    IssueDate.set("")
    Dose.set("")
    Tablets.set("")
    bloodPressure.set("")
    patientname.set("")
    DOB1.set("")
    Address1.set("")
    ExpDate.set("")

    
# buttons
prescriptionBtn = Button(buttonFrame,command=prescriptionDetails, text='Prescription', font=' bold 10', bg='green',
                         fg='white', width=18)
prescriptionBtn.grid(row=0, column=0, padx=10, pady=5)

prescriptionData = Button(buttonFrame,command=prescription, text='Prescription Data',
                          font='bold 10', bg='green', fg='white', width=18)
prescriptionData.grid(row=0, column=1, padx=10, pady=5)

deleteBtn = Button(buttonFrame, text='Delete',command=delete, font='bold 10',
                   bg='red', fg='white', width=18)
deleteBtn.grid(row=0, column=2, padx=10, pady=5)

updateBtn = Button(buttonFrame, text='update', command=update, font='bold 10', bg='red', fg='white', width=18)
updateBtn.grid(row = 0, column=3, padx=10, pady=5)

clearBtn = Button(buttonFrame,command=clear, text='Clear', font='bold 10',
                  bg='green', fg='white', width=18)
clearBtn.grid(row=0, column=4, padx=10, pady=5)

exitBtn = Button(buttonFrame, text='Exit', font='bold 10',
                 bg='green', fg='white', width=18, command=exit)
exitBtn.grid(row=0, column=5, padx=10, pady=5)

# details frame [table]..............................................///
scrollX = ttk.Scrollbar(detailsFrame, orient='horizontal')
scrollY = ttk.Scrollbar(detailsFrame, orient='vertical')
hmsTable = ttk.Treeview(detailsFrame, column=("NamesofTablet", "patientID", "IssueDate", "Dose", "Tablets",
                        "bloodPressure", "patientname", "DOB1", "Address1", "ExpDate"), xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
scrollX.pack(side='bottom', fill='x')
scrollY.pack(side='left', fill='y')

scrollX = ttk.Scrollbar(command=hmsTable.xview)
scrollY = ttk.Scrollbar(command=hmsTable.yview)

hmsTable.heading("NamesofTablet", text="NamesofTablet")
hmsTable.heading("patientID", text="patientID")
hmsTable.heading("IssueDate", text="IssueDate")
hmsTable.heading("Dose", text="Dose")
hmsTable.heading("Tablets", text="Tablets")
hmsTable.heading("bloodPressure", text="bloodPressure")
hmsTable.heading("patientname", text="patientname")
hmsTable.heading("DOB1", text="DOB1")
hmsTable.heading("Address1", text="Address1")
hmsTable.heading("ExpDate", text="ExpDate")

hmsTable["show"] = "headings"


hmsTable.column("NamesofTablet", width=100)
hmsTable.column("patientID", width=100)
hmsTable.column("IssueDate", width=100)
hmsTable.column("Dose", width=100)
hmsTable.column("Tablets", width=100)
hmsTable.column("bloodPressure", width=100)
hmsTable.column("patientname", width=100)
hmsTable.column("DOB1", width=100)
hmsTable.column("Address1", width=100)
hmsTable.column("ExpDate", width=100)
hmsTable.pack(fill='both', expand=1)
hmsTable.bind("<ButtonRelease-1>",getCursor)
fetchData()

window.mainloop()