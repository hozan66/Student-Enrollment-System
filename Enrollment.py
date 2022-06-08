# Our Project ==> Student Enrollment System

from tkinter import filedialog  # it will return the location
from PIL import ImageTk, Image
from tkinter import *
from datetime import date
from tkcalendar import *

from tkinter import ttk
import pyodbc
from tkinter import messagebox

def dashBoard():  # Registration Form
    root2.destroy()
    root.destroy()
    global regis_form_window
    regis_form_window = Tk()  # New Window
    regis_form_window.geometry("1325x675+20+0")
    regis_form_window.title("Registration Window")
    regis_form_window.config(bg="#56A2DD")
#     regis_form_window.resizable(False,False)
    regis_form_window.iconbitmap(r'student icon.ico')
    regis_form_window.focus_force()

    l_title = Label(regis_form_window, text="Registration Form Is Here", font=(
        'Century', 20, 'bold'), bg="#C1D9F9", fg="white")
    l_title.pack(pady=5, ipadx=5, ipady=5)

    regis_window = Frame(regis_form_window, bg="#C1D9F9")
    regis_window.pack(anchor=N)
    Label(regis_window, bg="#C1D9F9").grid(row=0, column=0)
    l_first_name = Label(regis_window, text="First Name: ", font=('Century', 16, 'bold'),
                         bg="#C1D9F9").grid(row=1, column=1, sticky=W)
    e_first_name = Entry(regis_window, font=(
        'Arial', 14), fg="#76787C", bg="#f0e99a", relief="groove", justify="center")
    e_first_name.grid(row=2, column=1)
    e_first_name.focus_force()
    # -----------------------------------------------------------------------------------
    Label(regis_window, bg="#C1D9F9").grid(row=0, column=2)

    l_last_name = Label(regis_window, text="Last Name: ", font=('Century', 16, 'bold'),
                        bg="#C1D9F9").grid(row=1, column=3)
    e_last_name = Entry(regis_window, font=(
        'Arial', 14), fg="#76787C", bg="#f0e99a", relief="groove", justify="center")
    e_last_name.grid(row=2, column=3)
    # -----------------------------------------------------------------------------------
    Label(regis_window, bg="#C1D9F9").grid(row=0, column=4)

    l_id = Label(regis_window, text="Student ID: ", font=('Century', 16, 'bold'),
                 bg="#C1D9F9").grid(row=1, column=5)
    e_id = Entry(regis_window, font=('Arial', 14), fg="#76787C",
                 bg="#f0e99a", relief="groove", justify="center")
    e_id.grid(row=2, column=5)
    # -----------------------------------------------------------------------------------
    Label(regis_window, bg="#C1D9F9").grid(row=0, column=6)

    l_gmail = Label(regis_window, text="Gmail: ", font=('Century', 16, 'bold'),
                    bg="#C1D9F9").grid(row=1, column=7)
    e_gmail = Entry(regis_window, font=('Arial', 14), fg="#76787C",
                    bg="#f0e99a", relief="groove", justify="center")
    e_gmail.grid(row=2, column=7)
    # -----------------------------------------------------------------------------------
    Label(regis_window, bg="#C1D9F9").grid(row=0, column=8)

    l_phone = Label(regis_window, text="Phone Number: ", font=('Century', 16, 'bold'),
                    bg="#C1D9F9").grid(row=1, column=9)
    e_phone = Entry(regis_window, font=('Arial', 14), fg="#76787C",
                    bg="#f0e99a", relief="groove", justify="center")
    e_phone.grid(row=2, column=9)
    # -----------------------------------------------------------------------------------
    Label(regis_window, bg="#C1D9F9").grid(row=3, column=0)  # space for row

    def open_file():
        regis_window.filename = filedialog.askopenfilename(initialdir="C:\\Users\\HOZAN\\Desktop", title="Select A File",
                                                           filetypes=(("png files", "*.png"), ("all files", "*.*")))
        v_image.set(regis_window.filename)

    b_upload = Button(regis_window, text="Upload Image Certificare: ", font=('Century', 10, 'bold'), cursor="hand2",
                      bg="#C69A9A", relief="ridge", command=open_file).grid(row=4, column=1, sticky=W)
    v_image = StringVar()
    v_image.set("")
    e_upload = Entry(regis_window, textvariable=v_image, font=(
        'Arial', 14), fg="#76787C", bg="#f0e99a", relief="groove")
    e_upload.grid(row=5, column=1)
    # -----------------------------------------------------------------------------------
    Label(regis_window, bg="#C1D9F9").grid(row=0, column=2)

    def get_date():       # global v_date
        v_date.set(cal.get_date())
        date_window.destroy()

    def grab_date():
        global date_window
        date_window = Toplevel(regis_window)
        date_window.title("Date Window")
        date_window.focus_force()

        global cal
        cal = Calendar(date_window, selectmode="day",
                       year=1999, month=11, day=9)
        cal.pack(pady=20)
        date_button = Button(date_window, text="Get Date", command=get_date)
        date_button.pack(pady=5)
        date_window.mainloop()
    v_date = StringVar()
    v_date.set("")
    b_Date = Button(regis_window, text="Date Of Birth: ", font=('Century', 10, 'bold'), cursor="hand2",
                    bg="#C69A9A", relief="ridge", command=grab_date).grid(row=4, column=3)
    e_Date = Entry(regis_window, textvariable=v_date, font=('Arial', 14),
                   fg="#76787C", bg="#f0e99a", relief="groove", justify="center")
    e_Date.grid(row=5, column=3)
    # -----------------------------------------------------------------------------------
    Label(regis_window, bg="#C1D9F9").grid(row=0, column=4)

    # Creating a list of Universities
    universities = [
        "Salahaddin",
        "Sulaimani",
        "Duhok"
    ]
    coll_of_sala = [
        "Science",
        "Engineering",
        "Language"
    ]
    coll_of_sulai = [
        "Medicine",
        "Engineering"
    ]
    # Creating a list of colleges
    colleges = [
        "Science",
        "Engineering",
        "Language",
        "Medicine"
    ]
    # Creating a list of departments of Science
    dep_of_science = [
        "CS & IT",
        "Math",
        "Physic",
        "Geology",
        "Biology",
        "chemic"
    ]
    # Creating a list of departments of Engineering
    dep_of_engineering = [
        "Software Engineering",
        "Mechanical & Mechatronics",
        "Architecture",
        "Civil",
        "Electrical"
    ]
    # Creating a list of departments of Language
    dep_of_language = [
        "Kurdish",
        "Arabic",
        "English",
        "French",
        "Germany",
        "Turkish"
    ]
    # Creating a list of departments of Medicine
    dep_of_Medicine = [
        "General Medicine",
        "Dentistry",
        "Pharmacy",
        "Ophthalmology"
    ]

    def pick_dep(e):
        if coll_combo.get() == "Science":
            dep_combo.config(value=dep_of_science)
#             dep_combo.current(0)
        elif coll_combo.get() == "Engineering":
            dep_combo.config(value=dep_of_engineering)
#             dep_combo.current(0)
        elif coll_combo.get() == "Language":
            dep_combo.config(value=dep_of_language)
#             dep_combo.current(0)
        elif coll_combo.get() == "Medicine":
            dep_combo.config(value=dep_of_Medicine)
#             dep_combo.current(0)

    def pick_coll(e):
        if univ_combo.get() == "Salahaddin":
            coll_combo.config(value=coll_of_sala)
            coll_combo.delete(0, END)
            dep_combo.delete(0, END)
        elif univ_combo.get() == "Sulaimani":
            coll_combo.config(value=coll_of_sulai)
            coll_combo.delete(0, END)
            dep_combo.delete(0, END)
        elif univ_combo.get() == "Duhok":
            coll_combo.config(value=colleges)
            coll_combo.delete(0, END)
            dep_combo.delete(0, END)

    l_univ = Label(regis_window, text="Choose University: ", font=('Century', 16, 'bold'),
                   bg="#C1D9F9").grid(row=4, column=5)
    # create a dropdown box
    univ_combo = ttk.Combobox(
        regis_window, value=universities, font=('Arial', 12))
#     univ_combo.current(0)
    univ_combo.grid(row=5, column=5)
    univ_combo.bind("<<ComboboxSelected>>", pick_coll)
    # -----------------------------------------------------------------------------------
    Label(regis_window, bg="#C1D9F9").grid(row=0, column=6)

    l_coll = Label(regis_window, text="Choose College: ", font=('Century', 16, 'bold'),
                   bg="#C1D9F9").grid(row=4, column=7)

    coll_combo = ttk.Combobox(regis_window, value=colleges, font=('Arial', 12))
#     coll_combo.current(0)
    coll_combo.grid(row=5, column=7)
    coll_combo.bind("<<ComboboxSelected>>", pick_dep)
    # -----------------------------------------------------------------------------------
    Label(regis_window, bg="#C1D9F9").grid(row=0, column=8)

    l_dep = Label(regis_window, text="Choose Department: ", font=('Century', 16, 'bold'),
                  bg="#C1D9F9").grid(row=4, column=9)

    # Department combo box
    dep_combo = ttk.Combobox(regis_window, value=[" "], font=('Arial', 12))
    dep_combo.current(0)
    dep_combo.grid(row=5, column=9)
    # -----------------------------------------------------------------------------------
    Label(regis_window, bg="#C1D9F9").grid(row=6, column=0)  # space for row

    l_gender = Label(regis_window, text="Choose Gender: ", font=('Century', 16, 'bold'),
                     bg="#C1D9F9").grid(row=7, column=1)
    va = StringVar()
    va.set(" ")
    Radiobutton(regis_window, text="Male", variable=va, value="Male",
                font=('Arial', 10), bg="#C1D9F9").grid(row=7, column=3, sticky=W)
    Radiobutton(regis_window, text="Female", variable=va, value="Female",
                font=('Arial', 10), bg="#C1D9F9").grid(row=7, column=3, sticky=E)
    # -----------------------------------------------------------------------------------
    Label(regis_window, bg="#C1D9F9").grid(row=8, column=0)  # space for row

    l_grade = Label(regis_window, text="Your Grade: ", font=('Century', 16, 'bold'),
                    bg="#C1D9F9").grid(row=7, column=5)
    e_grade = Entry(regis_window, font=('Arial', 14), fg="#76787C",
                    bg="#f0e99a", relief="groove", justify="center")
    e_grade.grid(row=7, column=7)

    # _________________________________________________________________________________________________________________________

    show_window = Frame(regis_form_window, bg="#C1D9F9")
    show_window.pack(pady=5)
    # Add Some Style
    style = ttk.Style()
    # Pick a theme
    style.theme_use("default")  # default,clam,alt
    # Configre our treeview colors
    style.configure("Treeview",
                    background="white",
                    forground="black",
                    rowheight=25,
                    fieldbackground="white")
    # Change Selected Color
    style.map("Treeview",
              background=[('selected', 'blue')])
    # Create treeview Frame
    tree_frame = Frame(show_window, bg="yellow")
    tree_frame.pack(pady=10)
    # Treeview Scrollbar
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side="right", fill=Y)
    # Create Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
    # pack to the screen
    my_tree.pack()
    # Configure the scrollbar
    tree_scroll.config(command=my_tree.yview)
    # Define Our Columns
    my_tree['columns'] = ("First Name", "Last Name",
                          "Student ID", "Gmail",
                          "Image Certificare", "DOB",
                          "Gender", "Grade",
                          "Phone Number", "University",
                          "College", "Department")
    # Format Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("First Name", anchor=CENTER, width=100)
    my_tree.column("Last Name", anchor=CENTER, width=100)
    my_tree.column("Student ID", anchor=CENTER, width=100)
    my_tree.column("Gmail", anchor=CENTER, width=130)
    my_tree.column("Image Certificare", anchor=CENTER, width=120)
    my_tree.column("DOB", anchor=CENTER, width=100)
    my_tree.column("Gender", anchor=CENTER, width=100)
    my_tree.column("Grade", anchor=CENTER, width=100)
    my_tree.column("Phone Number", anchor=CENTER, width=120)
    my_tree.column("University", anchor=CENTER, width=100)
    my_tree.column("College", anchor=CENTER, width=100)
    my_tree.column("Department", anchor=CENTER, width=120)

    # Create Headings
    my_tree.heading("#0", text="", anchor=CENTER)
    my_tree.heading("First Name", text="First Name", anchor=CENTER)
    my_tree.heading("Last Name", text="Last Name", anchor=CENTER)
    my_tree.heading("Student ID", text="Student ID", anchor=CENTER)
    my_tree.heading("Gmail", text="Gmail", anchor=CENTER)
    my_tree.heading("Image Certificare",
                    text="Image Certificare", anchor=CENTER)
    my_tree.heading("DOB", text="DOB", anchor=CENTER)
    my_tree.heading("Gender", text="Gender", anchor=CENTER)
    my_tree.heading("Grade", text="Grade", anchor=CENTER)
    my_tree.heading("Phone Number", text="Phone Number", anchor=CENTER)
    my_tree.heading("University", text="University", anchor=CENTER)
    my_tree.heading("College", text="College", anchor=CENTER)
    my_tree.heading("Department", text="Department", anchor=CENTER)

    # Add Data
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=HOZANPC;'
                                'Database=userDB2;'
                                'Trusted_Connection=yes;')
    cursorObject = connection.cursor()
    global data
    data = cursorObject.execute('''select * from userDB2.dbo.University u
    join College c
    on u.Univ_ID=c.Univ_ID
    join Department d
    on c.College_ID=d.College_ID
    join Enrollment e
    on d.Dep_ID=e.Dep_ID
    join Student s
    on e.Student_ID=s.Student_ID;''')
    # Create striped row tags
    my_tree.tag_configure('oddRow', background="white")
    my_tree.tag_configure('evenRow', background="lightblue")
    global count
    count = 0
    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text="",
                           values=(record[18], record[19], record[17],
                                   record[22], record[14], record[21],
                                   record[20], record[13], record[23],
                                   record[1], record[4], record[8]),
                           tags=('evenRow'))
        else:
            my_tree.insert(parent='', index='end', iid=count, text="",
                           values=(record[18], record[19], record[17],
                                   record[22], record[14], record[21],
                                   record[20], record[13], record[23],
                                   record[1], record[4], record[8]),
                           tags=('oddRow'))
        count += 1

    update_ID = ''
    update_mark = ''
    global row_to_list
    # Add Record

    def add_record():  # put values of Entry in variables for using it in database
        fname = e_first_name.get()
        lname = e_last_name.get()
        global st_ID
        st_ID = e_id.get()
        gmail = e_gmail.get()
        phone_num = e_phone.get()
        image = v_image.get()
        DOB = v_date.get()
        gender = va.get()
        mark = e_grade.get()
        univ = univ_combo.get()
        coll = coll_combo.get()
        dep = dep_combo.get()

        # new connection with database
        connection = pyodbc.connect('Driver={SQL Server};'
                                    'Server=HOZANPC;'
                                    'Database=userDB2;'
                                    'Trusted_Connection=yes;')
        cursorObject = connection.cursor()
        query = cursorObject.execute("select * from userDB2.dbo.Student where Student_ID=(?) or Email=(?) or Phone_Number=(?)",
                                     (st_ID, gmail, phone_num))
        if(fname == '' or lname == '' or st_ID == '' or gmail == '' or phone_num == '' or image == '' or DOB == '' or
           gender == ' ' or mark == '' or univ == '' or coll == '' or dep == ''):
            messagebox.showwarning(
                "Registration", "The Entries Must Not Be Empty All Of It Required", parent=regis_form_window)
        elif(query.fetchall()):
            messagebox.showwarning(
                "Registration", "This Student ID or Gmail or Phone Number Is Already Exist", parent=regis_form_window)
            e_first_name.delete(0, END)
            e_last_name.delete(0, END)
            e_id.delete(0, END)
            e_gmail.delete(0, END)
            e_phone.delete(0, END)
            v_image.set("")
            v_date.set("")
            va.set(" ")
            e_grade.delete(0, END)
            univ_combo.delete(0, END)
            coll_combo.delete(0, END)
            dep_combo.delete(0, END)
        else:
            messagebox.showinfo(
                "Registration", "New Student Added Successfully", parent=regis_form_window)
            st_ID = int(e_id.get())
            enroll_ID = st_ID+10
            mark = float(e_grade.get())
            data2 = cursorObject.execute('''select e.Dep_ID, d.Dep_ID from University u
            join College c
            on u.Univ_ID=c.Univ_ID
            join Department d
            on c.College_ID=d.College_ID
            join Enrollment e
            on d.Dep_ID=e.Dep_ID
            join Student s
            on e.Student_ID=s.Student_ID
            where u.Univ_Name=(?) and c.College_Name=(?) and d.Dep_Name=(?); ''', (univ, coll, dep))

            global row_to_list
            row_to_list = [123]
            print(row_to_list)

            for row in data2:
                row_to_list = [elem for elem in row]
            print(row_to_list)
            dep_ID = row_to_list[0]

            sql_command_stud = (
                '''insert into userDB2.dbo.Student values(?,?,?,?,?,?,?)''')
            sql_command_enroll = ('''insert into userDB2.dbo.Enrollment (Enrol_ID,Enrollment_Date,
            Grade,Image_Certificate,Student_ID,Dep_ID)
            values(?,?,?,?,?,?)''')

            cursorObject.execute(sql_command_stud,
                                 (st_ID, fname, lname, gender, DOB, gmail, phone_num))
            Enroll_date = str(date.today())
            cursorObject.execute(
                sql_command_enroll, (enroll_ID, Enroll_date, mark, image, st_ID, dep_ID))
            connection.commit()
            connection.close()

            my_tree.tag_configure('oddRow', background="white")
            my_tree.tag_configure('evenRow', background="lightblue")
            global count
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text="",
                               values=(e_first_name.get(), e_last_name.get(), e_id.get(),
                                       e_gmail.get(), v_image.get(), v_date.get(),
                                       va.get(), e_grade.get(), e_phone.get(),
                                       univ_combo.get(), coll_combo.get(), dep_combo.get()),
                               tags=('evenRow'))
            else:
                my_tree.insert(parent='', index='end', iid=count, text="",
                               values=(e_first_name.get(), e_last_name.get(), e_id.get(),
                                       e_gmail.get(), v_image.get(), v_date.get(),
                                       va.get(), e_grade.get(), e_phone.get(),
                                       univ_combo.get(), coll_combo.get(), dep_combo.get()),
                               tags=('oddRow'))
            count += 1

            # Cleare Entry Boxes
            e_first_name.delete(0, END)
            e_last_name.delete(0, END)
            e_id.delete(0, END)
            e_gmail.delete(0, END)
            e_phone.delete(0, END)
            v_image.set("")
            v_date.set("")
            va.set(" ")
            e_grade.delete(0, END)
            univ_combo.delete(0, END)
            coll_combo.delete(0, END)
            dep_combo.delete(0, END)

    def remove_one():  # Remove the selected one
        selected = my_tree.focus()
        if selected == '':
            messagebox.showerror(
                "Registration", "You Should To Select First", parent=regis_form_window)
            return

        messagebox.showinfo(
            "Registration", "The Record Has Been Successfully Deleted", parent=regis_form_window)
        # my_tree.selection()[0] for select one item only
        x = my_tree.selection()[0]
        values = my_tree.item(selected, 'values')  # Getting the whole row
        my_tree.delete(x)
        # new connection with database
        connection = pyodbc.connect('Driver={SQL Server};'
                                    'Server=HOZANPC;'
                                    'Database=userDB2;'
                                    'Trusted_Connection=yes;')
        cursorObject = connection.cursor()
        stu_id = int(values[2])
        grade = float(values[7])
        cursorObject.execute(
            "delete from userDB2.dbo.Enrollment where Student_ID=(?) and Grade=(?)", (stu_id, grade))
        cursorObject.execute(
            "delete from userDB2.dbo.Student where Student_ID=(?)", stu_id)
        connection.commit()
        connection.close()

    def select_record():  # Select Record
        # Cleare Entry Boxes
        e_first_name.delete(0, END)
        e_last_name.delete(0, END)
        e_id.delete(0, END)
        e_gmail.delete(0, END)
        e_phone.delete(0, END)
        v_image.set("")
        v_date.set("")
        va.set(" ")
        e_grade.delete(0, END)
        univ_combo.delete(0, END)
        coll_combo.delete(0, END)
        dep_combo.delete(0, END)

        # grab record number
        selected = my_tree.focus()
        if selected == '':
            messagebox.showerror(
                "Registration", "You Should To Select First", parent=regis_form_window)
            return
        # grab record values
        global values
        values = my_tree.item(selected, 'values')
#         print(values)
        # temp_label.config(text=values[0])  #Return Tuple

        # Output to entry boxes
        e_first_name.insert(0, values[0])
        e_last_name.insert(0, values[1])
        global update_ID
        update_ID = values[2]
        e_id.insert(0, values[2])
        e_gmail.insert(0, values[3])
        v_image.set(values[4])
        v_date.set(values[5])
        va.set(values[6])
        global update_mark
        update_mark = values[7]
        e_grade.insert(0, values[7])
        e_phone.insert(0, values[8])
        univ_combo.insert(0, values[9])
        coll_combo.insert(0, values[10])
        dep_combo.insert(0, values[11])

    def update_record():  # Save Update Record
        global update_ID
        global update_mark
        # grab record number
        selected = my_tree.focus()
        if selected == '':
            messagebox.showerror(
                "Registration", "You Should To Select First", parent=regis_form_window)
            return
        # put values of Entry in variables for using it in database
        fname = e_first_name.get()
        lname = e_last_name.get()
        global st_ID
        st_ID = e_id.get()
        gmail = e_gmail.get()
        phone_num = e_phone.get()
        image = v_image.get()
        DOB = v_date.get()
        gender = va.get()
        mark = e_grade.get()
        univ = univ_combo.get()
        coll = coll_combo.get()
        dep = dep_combo.get()

        # new connection with database
        connection = pyodbc.connect('Driver={SQL Server};'
                                    'Server=HOZANPC;'
                                    'Database=userDB2;'
                                    'Trusted_Connection=yes;')
        cursorObject = connection.cursor()
        # Delete Record
        cursorObject.execute("delete from userDB2.dbo.Enrollment where Student_ID=(?) and Grade=(?)",
                             (update_ID, update_mark))
        cursorObject.execute(
            "delete from userDB2.dbo.Student where Student_ID=(?)", update_ID)

        query = cursorObject.execute("select * from userDB2.dbo.Student where Student_ID=(?) or Email=(?) or Phone_Number=(?)",
                                     (st_ID, gmail, phone_num))
        if(fname == '' or lname == '' or st_ID == '' or gmail == '' or phone_num == '' or image == '' or DOB == '' or
           gender == ' ' or mark == '' or univ == '' or coll == '' or dep == ''):
            messagebox.showwarning(
                "Registration", "The Entries Must Not Be Empty All Of It Required", parent=regis_form_window)
        elif(query.fetchall()):
            messagebox.showwarning(
                "Registration", "This Student ID or Gmail or Phone Number Is Already Exist", parent=regis_form_window)
            e_first_name.delete(0, END)
            e_last_name.delete(0, END)
            e_id.delete(0, END)
            e_gmail.delete(0, END)
            e_phone.delete(0, END)
            v_image.set("")
            v_date.set("")
            va.set(" ")
            e_grade.delete(0, END)
            univ_combo.delete(0, END)
            coll_combo.delete(0, END)
            dep_combo.delete(0, END)
        else:
            messagebox.showinfo(
                "Registration", "The Student Updated Successfully", parent=regis_form_window)
            st_ID = int(e_id.get())
            enroll_ID = st_ID+10
            mark = float(e_grade.get())
            data2 = cursorObject.execute('''select e.Dep_ID, d.Dep_ID from University u
            join College c
            on u.Univ_ID=c.Univ_ID
            join Department d
            on c.College_ID=d.College_ID
            join Enrollment e
            on d.Dep_ID=e.Dep_ID
            join Student s
            on e.Student_ID=s.Student_ID
            where u.Univ_Name=(?) and c.College_Name=(?) and d.Dep_Name=(?); ''', (univ, coll, dep))

            global row_to_list
            row_to_list = [123]

            for row in data2:
                row_to_list = [elem for elem in row]
            print(row_to_list)
            dep_ID = row_to_list[0]

            # ADD Record
            sql_command_stud = (
                '''insert into userDB2.dbo.Student values(?,?,?,?,?,?,?)''')
            sql_command_enroll = ('''insert into userDB2.dbo.Enrollment (Enrol_ID,Enrollment_Date,
            Grade,Image_Certificate,Student_ID,Dep_ID)
            values(?,?,?,?,?,?)''')

            cursorObject.execute(sql_command_stud,
                                 (st_ID, fname, lname, gender, DOB, gmail, phone_num))
            Enroll_date = str(date.today())
            cursorObject.execute(
                sql_command_enroll, (enroll_ID, Enroll_date, mark, image, st_ID, dep_ID))
            connection.commit()
            connection.close()
            # save new data
            my_tree.item(selected, text="",
                         values=(e_first_name.get(), e_last_name.get(), e_id.get(),
                                 e_gmail.get(), v_image.get(), v_date.get(),
                                 va.get(), e_grade.get(), e_phone.get(),
                                 univ_combo.get(), coll_combo.get(), dep_combo.get(),))
            # Clear Entry Boxes
            e_first_name.delete(0, END)
            e_last_name.delete(0, END)
            e_id.delete(0, END)
            e_gmail.delete(0, END)
            e_phone.delete(0, END)
            v_image.set("")
            v_date.set("")
            va.set(" ")
            e_grade.delete(0, END)
            univ_combo.delete(0, END)
            coll_combo.delete(0, END)
            dep_combo.delete(0, END)

    def reset_record():
        # Clear Entry Boxes
        e_first_name.delete(0, END)
        e_last_name.delete(0, END)
        e_id.delete(0, END)
        e_gmail.delete(0, END)
        e_phone.delete(0, END)
        v_image.set("")
        v_date.set("")
        va.set(" ")
        e_grade.delete(0, END)
        univ_combo.delete(0, END)
        coll_combo.delete(0, END)
        dep_combo.delete(0, END)

    # Buttons
    reset_button = Button(show_window, text="Reset Record", cursor="hand2",
                          bg="#33AD6A", fg="white", font=('Century', 12), relief="flat", overrelief="ridge", command=reset_record)
    reset_button.pack(side="left", padx=80)

    select_button = Button(show_window, text="Select Record", cursor="hand2",
                           bg="#33AD6A", fg="white", font=('Century', 12), relief="flat", overrelief="ridge", command=select_record)
    select_button.pack(side="left", padx=60)

    update_button = Button(show_window, text="Save Record", cursor="hand2",
                           bg="#33AD6A", fg="white", font=('Century', 12), relief="flat", overrelief="ridge", command=update_record)
    update_button.pack(side="left", padx=60)

    add_records = Button(show_window, text="Add Record", cursor="hand2",
                         bg="#33AD6A", fg="white", font=('Century', 12), relief="flat", overrelief="ridge", command=add_record)
    add_records.pack(side="left", padx=60)

    # Remove the selected one
    remove_one = Button(show_window, text="Delete One Selected", cursor="hand2",
                        bg="#33AD6A", fg="white", font=('Century', 12), relief="flat", overrelief="ridge", command=remove_one)
    remove_one.pack(side="left", padx=80, pady=10)
    connection.commit()
    connection.close()
    regis_form_window.mainloop()


def submit2():
    user = e1.get()
    password = e2.get()
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=HOZANPC;'
                                'Database=userDB2;'
                                'Trusted_Connection=yes;')
    cursorObject = connection.cursor()
    query = cursorObject.execute(
        "select * from userDB2.dbo.users where userName=(?) and password=(?)", (user, password))
    if(query.fetchall()):
        messagebox.showinfo("Login", "Login Successfully", parent=root2)
        dashBoard()
    elif user == '' or password == '':
        messagebox.showwarning(
            "Login", "The Entry Must Not Be Empty", parent=root2)
    else:
        messagebox.showerror(
            "Login", "Wrong Username or Password", parent=root2)
        e1.delete(0, END)
        e2.delete(0, END)
    connection.commit()
    connection.close()


def login():
    global e1, e2, root2
    root2 = Toplevel(root)
    root2.title('Login Window')
    root2.focus_force()
    root2.resizable(False, False)
    root2.geometry('+250+10')
    root2.iconbitmap(r'student icon.ico')
    root2.config(bg='white')

    f1 = Frame(root2, bg="white")
    f1.pack(side='top')

    f2 = Frame(root2, bg="white")
    f2.pack(side='top', pady=16)

    f3 = Frame(root2, bg="white")
    f3.pack(side='left', pady=16)

    Label(f1, text='Student Enrollment System', font=(
        'Century', 20, 'bold'), bg="white").pack(pady=26)
    p1 = PhotoImage(file='login Enrollment.png')
    Label(f1, image=p1, bg="white").pack()

    Label(f1, text='Login Form', font=(
        'Century', 20, 'bold'), bg="white").pack(pady=16)

    Label(f1, text='User Name: ', font=('Century', 18, 'bold'),
          bg="white").pack(side='left', padx=30)
    e1 = Entry(f1, font=('Arial', 16, 'bold'), fg="#76787C", bg='#ccc')
    e1.pack(side='left')
    e1.focus_force()

    Label(f2, text='Password: ', font=('Century', 18, 'bold'),
          bg="white").pack(side='left', padx=14)
    e2 = Entry(f2, font=('Arial', 16, 'bold'),
               fg="#76787C", bg='#ccc', show='*')
    e2.pack(side='left')

    cb = PhotoImage(file="cancelB2.png")
    sb = PhotoImage(file="checked2.png")
    Button(f3, image=cb, bg="white", relief=FLAT, takefocus=1, command=lambda: root2.destroy(),
           cursor="hand2", overrelief='ridge').pack(side='left', padx=160)
    Button(f3, image=sb, bg="white", relief=FLAT, takefocus=2, command=submit2,
           cursor="hand2", overrelief='ridge').pack(side='left')

    root2.mainloop()


def submit():
    new_user = v1.get()
    new_password = v2.get()
    conf = v3.get()
    if new_user == '' or new_password == '' or conf == '':
        messagebox.showwarning(
            "Login", "The Entry Must Not Be Empty", parent=sign_up_window)
        return

    if conf == '123456':  # verifacation code
        connection = pyodbc.connect('Driver={SQL Server};'
                                    'Server=HOZANPC;'
                                    'Database=userDB2;'
                                    'Trusted_Connection=yes;')
        cursorObject = connection.cursor()
        query = cursorObject.execute("select * from userDB2.dbo.users where userName=(?) and password=(?)",
                                     (new_user, new_password))
        if(query.fetchall()):
            messagebox.showwarning(
                "Sign UP", "User Name Exist", parent=sign_up_window)
            v1.set('')
            v2.set('')
            v3.set('')
        else:
            query = cursorObject.execute("INSERT INTO userDB2.dbo.users(userName,password) values(?,?)",
                                         (new_user, new_password))
            messagebox.showinfo(
                "Add New User", "New User Added Successfully", parent=sign_up_window)
            v1.set('')
            v2.set('')
            v3.set('')
        sign_up_window.destroy()
        connection.commit()
        connection.close()
    else:
        messagebox.showerror(
            "Wrong Sign Up", "You are not allowed to create admin account", parent=sign_up_window)
        v1.set('')
        v2.set('')
        v3.set('')


def sign_up():
    global v1
    global v2
    global v3
    global sign_up_window
    sign_up_window = Toplevel(root)
    sign_up_window.geometry("650x700+500+0")
    sign_up_window.title("Sign Up")
    sign_up_window.iconbitmap(r'student icon.ico')
    sign_up_window.focus_force()
    sign_up_window.config(bg="white")
    sign_up_window.resizable(False, False)

    Label(sign_up_window, text="Sign Up", font=('Century', 40, 'bold'),
          bg="white").pack(anchor=N, padx=10, pady=20)
    Label(sign_up_window, image=top_pic, bg="white").pack(pady=20)

    l_creat_username = Label(sign_up_window, text="Create User Name:   ", font=(
        'Century', 20, 'bold'), bg="white").place(x=20, y=460)
    v1 = StringVar('')
    e_username = Entry(sign_up_window, textvariable=v1, font=(
        'Arial', 20), fg="#76787C", bg="#f0e99a")
    e_username.place(x=300, y=460)
    e_username.focus_force()

    l_password = Label(sign_up_window, text="Create Password:   ", font=(
        'Century', 20, 'bold'), bg="white").place(x=20, y=520)
    v2 = StringVar('')
    e_password = Entry(sign_up_window, textvariable=v2, font=(
        'Arial', 20), fg="#76787C", bg="#f0e99a", show="*").place(x=300, y=520)

    l_ver = Label(sign_up_window, text="verification PW:   ", font=(
        'Century', 20, 'bold'), bg="white").place(x=20, y=580)
    v3 = StringVar('')
    e_ver = Entry(sign_up_window, textvariable=v3, font=(
        'Arial', 20), fg="#76787C", bg="#f0e99a", show="*").place(x=300, y=580)

    sub_button = Button(sign_up_window, text="Sign Up", font=('Century', 20, 'bold'),
                        command=submit,  bg="#f0e99a", relief="flat", overrelief="ridge", width=20).place(x=135, y=635)


root = Tk()
root.geometry("+600+0")
root.title("Enrolment Window ")
root.config(bg="white")
root.resizable(False, False)
root.iconbitmap(r'student icon.ico')
root.focus_force()
# =======frame
top_frame = Frame(root).pack(side=TOP)
mid_frame = Frame(root).pack(side=BOTTOM)
bootom_frsme = Frame(root)
lab1 = Label(top_frame, text="Student Enrollment System", font=(
    'Century', 40, 'bold'), bg="white").pack(anchor=N, padx=10, pady=20)
top_pic = PhotoImage(file="university enroll.png")
label_pic = Label(top_frame, image=top_pic, bg="white").pack(anchor=CENTER)
# ====================middle
signup_button = Button(mid_frame, text="Sign up", width="20", bg="#f0e99a", command=sign_up,
                       font=('Century', 20, 'italic', 'bold'), relief="flat", overrelief="ridge")
signup_button.pack(padx=30, pady=30, ipadx=10, ipady=10)
login_button = Button(mid_frame, text="login", width="20", bg="#f0e99a",
                      font=('Century', 20, 'italic', 'bold'), relief="flat", overrelief="ridge", command=login)
login_button.pack(padx=30, pady=30, ipadx=10, ipady=10)

root.mainloop()
