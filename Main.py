from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Student:
    def __init__(self,root):
        #***Form***
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.root.state("zoomed")
        self.root.minsize(1366,720)
        self.root.maxsize(1366,720)


        #***Title***
        Title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("time new roman",40,"bold"),bg="#985EFF",fg="#DBB2FF")
        Title.pack(side=TOP,fill=X)


        #***All Variables***
        self.Roll_No_Var=StringVar()
        self.name_Var=StringVar()
        self.email_Var=StringVar()
        self.gender_Var=StringVar()
        self.contact_Var=StringVar()
        self.dob_Var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()


        #***Manage frame***
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#985EFF")
        Manage_Frame.place(x=20,y=100,width=450,height=600)

        #Manage title
        m_title=Label(Manage_Frame,text="Manage Students",bg="#985EFF",fg="white",font=("time new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        #Roll no lbl
        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="#985EFF",fg="white",font=("time new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        #Roll no input
        txt_roll=Entry(Manage_Frame,textvariable=self.Roll_No_Var,font=("time new roman",15,"bold"),bd=1,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        #Name lbl
        lbl_name=Label(Manage_Frame,text="Name",bg="#985EFF",fg="white",font=("time new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        #Name input
        txt_name=Entry(Manage_Frame,textvariable=self.name_Var,font=("time new roman",15,"bold"),bd=1,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        #Email lbl
        lbl_email=Label(Manage_Frame,text="Email",bg="#985EFF",fg="white",font=("time new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        #Email input
        txt_email=Entry(Manage_Frame,textvariable=self.email_Var,font=("time new roman",15,"bold"),bd=1,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        #Gender lbl
        lbl_gender=Label(Manage_Frame,text="Gender",bg="#985EFF",fg="white",font=("time new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        #Gender combobox
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_Var,font=("time new roman",16,"normal"),width="17",state="readonly")
        combo_gender['values']=("male","female","other")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        #Contact lbl
        lbl_contact=Label(Manage_Frame,text="Contact",bg="#985EFF",fg="white",font=("time new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        #Contact input
        txt_contact=Entry(Manage_Frame,textvariable=self.contact_Var,font=("time new roman",15,"bold"),bd=1,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        #D.O.B lbl
        lbl_dob=Label(Manage_Frame,text="D.O.B",bg="#985EFF",fg="white",font=("time new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        #D.O.B input
        txt_dob=Entry(Manage_Frame,textvariable=self.dob_Var,font=("time new roman",15,"bold"),bd=1,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        #Adress lbl
        lbl_adress=Label(Manage_Frame,text="Adress",bg="#985EFF",fg="white",font=("time new roman",20,"bold"))
        lbl_adress.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        #Adress input
        self.txt_adress=Text(Manage_Frame,font=("time new roman",14,"bold"),width=20,height=3)
        self.txt_adress.grid(row=7,column=1,pady=10,padx=20,sticky="w")


        #***btn Frame***
        btn_Frame=Frame(Manage_Frame,bd=2,relief=RIDGE,bg="#985EFF")
        btn_Frame.place(x=18,y=535,width=405)

        #Add btn
        add_btn=Button(btn_Frame,activebackground='#BB86FC',font=("time new roman",9,"bold"),text="Add",width=10,command=self.add_students)
        add_btn.grid(row=0,column=0,padx=10,pady=10)

        #Update btn
        update_btn=Button(btn_Frame,activebackground='#BB86FC',font=("time new roman",9,"bold"),text="Update",width=10,command=self.update_data)
        update_btn.grid(row=0,column=1,padx=10,pady=10)

        #Delete btn
        delete_btn=Button(btn_Frame,activebackground='#BB86FC',font=("time new roman",9,"bold"),text="Delete",width=10,command=self.delete_data)
        delete_btn.grid(row=0,column=2,padx=10,pady=10)

        #Clear btn
        clear_btn=Button(btn_Frame,activebackground='#BB86FC',font=("time new roman",9,"bold"),text="Clear",width=10,command=self.Clear)
        clear_btn.grid(row=0,column=3,padx=10,pady=10)    

        
        #***Detail frame***
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#985EFF")
        Detail_Frame.place(x=500,y=100,width=845,height=600)

        #Search lbl
        lbl_search=Label(Detail_Frame,text="Search By",bg="#985EFF",fg="white",font=("time new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        #Search combobox
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,font=("time new roman",16,"normal"),width="10",state="readonly")
        combo_search['values']=("Roll_No","Name","Contact")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")

        #Search input
        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,font=("time new roman",15,"bold"),bd=1,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        #Search btn
        search_btn=Button(Detail_Frame,activebackground='#BB86FC',font=("time new roman",9,"bold"),text="Search",width=10,command=self.search_data)
        search_btn.grid(row=0,column=3,padx=10,pady=10)

        #Show all btn
        showall_btn=Button(Detail_Frame,activebackground='#BB86FC',font=("time new roman",9,"bold"),text="Show All",width=10,command=self.fetch_data)
        showall_btn.grid(row=0,column=4,padx=10,pady=10)

        #Table frame
        table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#985EFF")
        table_Frame.place(x=10,y=70,width=815,height=500)

        #Treeview
        scroll_x=Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_Frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_Frame,columns=("Roll","Name","Email","Gender","Contact","Dob","Adress"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Roll",text="Roll No.")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Contact",text="Contact")
        self.student_table.heading("Dob",text="D.O.B")
        self.student_table.heading("Adress",text="Adress")

        self.student_table['show']='headings'
   
        self.student_table.column("Roll",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Contact",width=100)
        self.student_table.column("Dob",width=100)
        self.student_table.column("Adress",width=100)
    
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)


        #***Show All Tables***
        self.fetch_data()


    #***Add New Student***
    def add_students(self):
        if self.Roll_No_Var.get()=="" or self.name_Var.get()=="":
            messagebox.showerror("Error","Roll_No And Name Are Required!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",
            (
                self.Roll_No_Var.get(),
                self.name_Var.get(),
                self.email_Var.get(),
                self.gender_Var.get(),
                self.contact_Var.get(),
                self.dob_Var.get(),
                self.txt_adress.get('1.0',END)
            ))
            con.commit()
            self.fetch_data()
            self.Clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")


    #***Show All Students***
    def fetch_data(self):
        self.Clear()
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()


    #***Clear inputs***
    def Clear(self):
        self.Roll_No_Var.set("")
        self.name_Var.set("")
        self.email_Var.set("")
        self.contact_Var.set("")
        self.dob_Var.set("")
        self.txt_adress.delete("1.0",END)


    #***get inputs***
    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_Var.set(row[0])
        self.name_Var.set(row[1])
        self.email_Var.set(row[2])
        self.gender_Var.set(row[3])
        self.contact_Var.set(row[4])
        self.dob_Var.set(row[5])
        self.txt_adress.delete("1.0",END)
        self.txt_adress.insert(END,row[6])


    #***Update Student***
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",
        (
            self.name_Var.get(),
            self.email_Var.get(),
            self.gender_Var.get(),
            self.contact_Var.get(),
            self.dob_Var.get(),
            self.txt_adress.get('1.0',END),
            self.Roll_No_Var.get()
        ))
        con.commit()
        self.fetch_data()
        self.Clear()
        con.close()


    #***Delete Students***
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_Var.get())
        con.commit()
        self.fetch_data()
        self.Clear()
        con.close()


    #***Search Students***
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()


#***Main***
root=Tk()
ob=Student(root)
root.mainloop()
