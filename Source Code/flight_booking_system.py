from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re  # for email pattern
from reportlab.pdfgen import canvas
import os
import random
from tkcalendar import DateEntry

class FlightBookingSystem:
    def __init__(self, root):
        # main window 
        self.root = root
        self.root.title("FLIGHT BOOKING")
        self.root.geometry("1920x1080")
        self.root.configure(bg="#fff")
        
        # background image for main window
        self.img = PhotoImage(file="front.png")
        label = Label(self.root, image=self.img, bg="white")
        label.place(x=0, y=0)
        
        # self.username_var = StringVar()
        # self.password_var = StringVar()

        # VIIT AIRLINES Lable
        airline_heading=Label(self.root,text="VIIT AIRLINES",fg="#0D4AA3",bg="#AED3FF",font=("Montserrat Black Italic",55))
        airline_heading.place(x=845,y=55,anchor=CENTER)

        # frame of main window
        self.frame = Frame(self.root, width=550, height=550, bg="White")
        self.frame.place(x=1100, y=310)

        # Signin heading
        heading = Label(self.frame, text="Sign in", fg="#57a1f8", bg="White",font=("Montserrat SemiBold Italic", 35))
        heading.grid(row=0, column=1, padx=0, pady=0, ipadx=0, ipady=0)
        
        #user buttom for user window
        button_user =Button(self.frame, text="User",fg="white",width=8,height=1,border=0,bg="#4682B4",font=("Montserrat SemiBold Italic",18),command=self.user_window)
        button_user.grid(row=1,column=0,padx=0,pady=70,ipadx=0,ipady=1)

        # admin botton for admin window
        button_admin =Button(self.frame, text="Admin",fg="white", width=8,height=1,border=0,bg="#4682B4",font=("Montserrat SemiBold Italic",18),command=self.admin_window)
        button_admin.grid(row=1,column=2,padx=0,pady=70,ipadx=0,ipady=1)    
            
    # function to create user window and Signin User
    def user_window(self):
        
        #destroy Main window
        self.root.withdraw()
        
        # create User window
        self.user_window1 = Toplevel()
        self.user_window1.title("User Window")
        self.user_window1.geometry("1920x1080")
        self.user_window1.configure(bg ="#fff")
        
        # background image for user window
        self.img2 = PhotoImage(file="Signin2.png")
        label3 = Label(self.user_window1, image=self.img2, bg="white")
        label3.place(x=0, y=0)
        
      
        #frame of user window
        self.frame_user=Frame(self.user_window1,width=550,height=550,bg="white")
        self.frame_user.place(x=1215,y=170)

        # Sign in heading
        heading=Label(self.frame_user,text="Sign in",fg="#57a1f8",bg="white",font=("Montserrat SemiBold Italic",35))
        heading.grid(row=0,column=0,padx=0,pady=0,ipadx=0,ipady=30)
        
        #Username Signin
        self.username=Entry(self.frame_user,width=21,fg="black",border=0,bg="white",font=("Montserrat SemiBold Italic",14))
        self.username.grid(row=1,column=0,padx=0,pady=0,ipadx=0,ipady=0)
        self.username.insert(0,"Username")
        self.username.bind("<FocusIn>",self.username_on_enter) #funtion is given below for this
        self.username.bind("<FocusOut>",self.username_on_leave) #funtion is given below for this
        
        Frame(self.frame_user,width=295,height=2,bg="black").grid(row=2,column=0,padx=0,pady=10,ipadx=0,ipady=0)
            
        #Password Signin
        self.password=Entry(self.frame_user,width=21,fg="black",border=0,bg="white",font=("Montserrat SemiBold Italic",14))
        self.password.grid(row=3,column=0,padx=0,pady=10,ipadx=0,ipady=0)
        self.password.insert(0,"Password")
        self.password.bind("<FocusIn>",self.password_on_enter) #funtion is given below for this
        self.password.bind("<FocusOut>",self.password_on_leave) #funtion is given below fpassword
        Frame(self.frame_user,width=295,height=2,bg="black").grid(row=4,column=0,padx=0,pady=0,ipadx=0,ipady=0)    

        #User Signin button
        button_signin=Button(self.frame_user,width=15,height=2,text="Sign in",fg="white",font=("Montserrat SemiBold Italic",14),bg="#57a1f8",border=0,command=self.signin)
        button_signin.grid(row=5,column=0,padx=0,pady=25,ipadx=0,ipady=0)
    
        # Don't have and account lable
        label_signup=Label(self.frame_user,text="Don't have an account?",fg="black",bg="white",font=("Montserrat SemiBold",12))
        label_signup.grid(row=6,column=0,padx=0,pady=0,ipadx=0,ipady=0)
        
        #User Signup button
        button_signup=Button(self.frame_user,width=6,text="Sign up",font=("Montserrat SemiBold",12),border=0,bg="white",fg="#57a1f8",command=self.signup)
        button_signup.grid(row=7,column=0,padx=0,pady=0,ipadx=0,ipady=0)
        
        #Back to user root window
        back_button_userwindow =Button(self.user_window1, text="🔙",fg="#0D4AA3", width=4,height=0,border=0,bg="#bedff6",font=("Montserrat SemiBold",20),command=self.back_to_root_window_from_user_window)
        back_button_userwindow.place(x=2,y=3)
        
    def signup(self):
    
        #destroy user window
        self.user_window1.withdraw()
        # create user signup window
        self.user_signup = Toplevel()
        self.user_signup.title("Signup Window")
        self.user_signup.geometry("1920x1080")
        self.user_signup.configure(bg ="#fff")
        
        # background image for signup window
        self.img5 = PhotoImage(file="User signup.png")
        label5 = Label(self.user_signup, image=self.img5, bg="white")
        label5.place(x=0, y=0)
        
        # frame of user window
        self.frame_signin=Frame(self.user_signup,width=550,height=550,bg="white")
        self.frame_signin.place(x=210,y=170)

        # signup lable
        heading=Label(self.frame_signin,text="Signup",fg="#57a1f8",bg="white",font=("Montserrat SemiBold Italic",35))
        heading.grid(row=0,column=0,padx=0,pady=0,ipadx=0,ipady=30)
        
        #Username Signin entry
        self.signup_username=Entry(self.frame_signin,width=20,fg="black",border=0,bg="white",font=("Montserrat SemiBold Italic",14))
        self.signup_username.grid(row=1,column=0,padx=0,pady=0,ipadx=0,ipady=0)
        self.signup_username.insert(0,"Username")
        self.signup_username.bind("<FocusIn>",self.signup_username_on_enter) #funtion is given below for this
        self.signup_username.bind("<FocusOut>",self.signup_username_on_leave) #funtion is given below fpassword
        
        Frame(self.frame_signin,width=295,height=2,bg="black").grid(row=2,column=0,padx=0,pady=10,ipadx=0,ipady=0)
        
        #Password Signin entry
        self.signup_password=Entry(self.frame_signin,width=20,fg="black",border=0,bg="white",font=("Montserrat SemiBold Italic",14))
        self.signup_password.grid(row=3,column=0,padx=0,pady=10,ipadx=0,ipady=0)
        self.signup_password.insert(0,"Password")
        self.signup_password.bind("<FocusIn>",self.signup_password_on_enter) #funtion is given below for this
        self.signup_password.bind("<FocusOut>",self.signup_password_on_leave) #funtion is given below fpassword

        
        Frame(self.frame_signin,width=295,height=2,bg="black").grid(row=4,column=0,padx=0,pady=0,ipadx=0,ipady=0)
        
        #User Signup entry
        self.confirm_signup_password=Entry(self.frame_signin,width=20,fg="black",border=0,bg="white",font=("Montserrat SemiBold Italic",14))
        self.confirm_signup_password.grid(row=5,column=0,padx=0,pady=10,ipadx=0,ipady=0)
        self.confirm_signup_password.insert(0,"Confirm password")
        self.confirm_signup_password.bind("<FocusIn>",self.confirm_signup_password_on_enter) #funtion is given below for this
        self.confirm_signup_password.bind("<FocusOut>",self.confirm_signup_password_on_leave) #funtion is given below fpassword

        
        Frame(self.frame_signin,width=295,height=2,bg="black").grid(row=6,column=0,padx=0,pady=0,ipadx=0,ipady=0)
        
        # User email entry
        self.signup_email=Entry(self.frame_signin,width=20,fg="black",border=0,bg="white",font=("Montserrat SemiBold Italic",14))
        self.signup_email.grid(row=7,column=0,padx=0,pady=10,ipadx=0,ipady=0)
        self.signup_email.insert(0,"Email")
        self.signup_email.bind("<FocusIn>",self.signup_email_on_enter) #funtion is given below for this
        self.signup_email.bind("<FocusOut>",self.signup_email_on_leave) #funtion is given below fpassword

        
        Frame(self.frame_signin,width=295,height=2,bg="black").grid(row=8,column=0,padx=0,pady=0,ipadx=0,ipady=0)
            

        #User Register button
        button_register=Button(self.frame_signin,width=15,height=2,text="Register",fg="white",font=("Montserrat SemiBold Italic",14),bg="#57a1f8",border=0,command=self.register)
        button_register.grid(row=9,column=0,padx=0,pady=25,ipadx=0,ipady=0)
        
        # Back button
        back_button_signup_to_user =Button(self.user_signup, text="🔙",fg="#081d4b", width=5,height=0,border=0,bg="#2482f1",font=("Montserrat SemiBold",20),command=self.back_to_sign_window)
        back_button_signup_to_user.place(x=3,y=3)
        
   
    #User SignIn Mysql function   
    def signin(self):
    
        username_var=self.username.get()
        password_var=self.password.get()
       
        #connecting mysql
        import mysql.connector as con
        connection = con.connect(host="localhost",user="root",password="starboy22*",database="flight")      
        cursor = connection.cursor()

        #show error if all fields are not entered
        if (username_var =="" or password_var==""):
            messagebox.showerror("Error","All fields are required")
            return
        
        cursor.execute("select count(*) from login_data")  
        afetch = cursor.fetchone()
        bfetch = afetch[0] #it has the number of rows
        
        cursor.execute('select username,password from login_data where username=username and password=password')
        row=cursor.fetchall()

        counter=0
        for i in range(0,bfetch):
        
            if(row[i][0]==username_var and row[i][1]==password_var ):
                counter=1 
            
        if (counter==1):
            messagebox.showinfo("Found","Logging In")
            self.flight_list_user()
        
        else:
            messagebox.showinfo("Not found","password and username does not exsist")

        connection.close()            


    # User Registration Values insert in table mysql
    def register(self):    
       
        # email format
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        #if any entry is empty
        if (self.signup_username.get()==""or self.signup_password.get()==""or self.confirm_signup_password.get()==""or self.signup_email.get()==""):

            messagebox.showerror("Error","All Fields Are Required")
            
        #Confirming Password
        elif self.signup_password.get()!=self.confirm_signup_password.get():
            messagebox.showerror("Error","Password and Confirm Password Should Be Same")
        
        #Email Pattern
            
        elif not re.match(email_pattern, self.signup_email.get()):
            messagebox.showerror("Error", "Please enter a valid email address")
        
        #variables to store values    
        else:
            printuser=self.signup_username.get()
            printpass=self.signup_password.get()
            printemail=self.signup_email.get()
        
            


        #Mysql connection
        import mysql.connector as con
        connection = con.connect(host="localhost", user="root", password="starboy22*", database="flight")

        cursor = connection.cursor()

        #Mysql Query
        cursor.execute("INSERT INTO login_data (username,password,email) VALUES (%s, %s , %s)", (printuser, printpass, printemail))
        connection.commit()     # connnection.commit()
    
        connection.close() #closing connection

        messagebox.showinfo("Success", "Register Succesful")
        
        messagebox.showinfo("Redirect to login","Please Login to continue" )
        self.user_window()
        self.user_signup.destroy()

    # Admin window
    def admin_window(self):
        
        #destroy Main window
        self.root.withdraw()
        # create second window
        self.admin_window1 = Toplevel()
        self.admin_window1.title("Admin Window")
        self.admin_window1.geometry("1920x1080")
        self.admin_window1.configure(bg ="#fff")
        
        # background image for admin window
        self.img4 = PhotoImage(file="Admin signin.png")
        label4 = Label(self.admin_window1, image=self.img4)
        label4.place(x=0, y=0)
        
        #frame of admin login window
        self.frame_admin=Frame(self.admin_window1,width=200,height=550,bg="White")
        self.frame_admin.place(x=680,y=220)

        # Sign in heading
        heading=Label(self.frame_admin,text="Sign in",fg="#57a1f8",bg="White",font=("Montserrat SemiBold Italic",35))
        heading.grid(row=0,column=0,padx=100,pady=0,ipadx=0,ipady=30)
        
        #Username Signin
        self.admin_username=Entry(self.frame_admin,width=20,fg="black",border=0,bg="white",font=("Montserrat SemiBold Italic",14))
        self.admin_username.grid(row=1,column=0,padx=0,pady=0,ipadx=0,ipady=0)
        self.admin_username.insert(0,"Username")
        self.admin_username.bind("<FocusIn>",self.admin_username_on_enter) #funtion is given below for this
        self.admin_username.bind("<FocusOut>",self.admin_username_on_leave) #funtion is given below fpassword
        
        Frame(self.frame_admin,width=295,height=2,bg="black").grid(row=2,column=0,padx=0,pady=10,ipadx=0,ipady=0)
        
        #Password Signin
        self.admin_password=Entry(self.frame_admin,width=20,fg="black",border=0,bg="white",font=("Montserrat SemiBold Italic",14))
        self.admin_password.grid(row=3,column=0,padx=0,pady=10,ipadx=0,ipady=0)
        self.admin_password.insert(0,"Password")
        self.admin_password.bind("<FocusIn>",self.admin_password_on_enter) #funtion is given below for this
        self.admin_password.bind("<FocusOut>",self.admin_password_on_leave) #funtion is given below fpassword

        
        Frame(self.frame_admin,width=295,height=2,bg="black").grid(row=4,column=0,padx=0,pady=0,ipadx=0,ipady=0)
        
        #Admin Signin button
        button_signin=Button(self.frame_admin,width=15,height=2,text="Sign in",fg="white",font=("Montserrat SemiBold Italic",14),bg="#57a1f8",border=0,command=self.admin_signin)
        button_signin.grid(row=5,column=0,padx=0,pady=25,ipadx=0,ipady=0)
        
        #Back to user root window
        back_button_adminwindow =Button(self.admin_window1, text="🔙",fg="#081d4b", width=5,height=0,border=0,bg="#468dcb",font=("Montserrat SemiBold",20),command=self.back_to_root_window)
        back_button_adminwindow.place(x=3,y=3)
        

    # Admin Mysql signin function
    def admin_signin(self):

        #connecting mysql
        import mysql.connector as con
        connection = con.connect(host="localhost",user="root",password="starboy22*",database="flight")
        
        cursor = connection.cursor()

        #show error if all fields are not entered
        if (self.admin_username.get() =="" or self.admin_password.get()==""):
            messagebox.showerror("Error","All fields are required")
            return
        
        
        cursor.execute("select count(*) from admin_data")  
        afetch = cursor.fetchone()
        bfetch = afetch[0] #it has the number of rows
        
        cursor.execute('select username,password from admin_data where username=username and password=password')
        row=cursor.fetchall()
        
        counter=0
        for i in range(0,bfetch):
        
            if(row[i][0]==self.admin_username.get() and row[i][1]==self.admin_password.get() ):
                counter=1 
            
        if (counter==1):
            messagebox.showinfo("Found","Logging In")
            self.admin_system_setting_window()
            
        else:
            messagebox.showinfo("Not found","password and username does not exsist")

        connection.close()
        self.admin_treeview_insert_data()        

    # back to Main Window from user window
    def back_to_root_window_from_user_window(self):
        
        # back to root window   
        self.root.deiconify()
        # destroying user window
        self.user_window1.destroy()
        

    # back to Main Window from admin window
    def back_to_root_window(self):
        
        # back to Main/root window
        self.root.deiconify()
        # destroying admin window
        self.admin_window1.destroy()


    # back button to user window
    def back_to_user_window(self):
        
        # back to User signin window
        self.user_window()
        # destroying flight list window
        self.flight_list_window.destroy()
        
        
    # back button to Sigin window
    def back_to_sign_window(self):

        # back to user and admin window 
        self.user_window()
        # destroying signup window
        self.user_signup.destroy()
        
    # home button from systemsetting
    def home_from_ss(self):

        # back to user and admin window 
        self.root.deiconify()
        # destroying signup window
        self.system_setting_window.destroy() 
           
    # home button from systemsetting
    def flight_list_logout(self):

        # back to user and admin window 
        self.root.deiconify()
        # destroying signup window
        self.flight_list_window.destroy()    

    #flight list window show flights
    def flight_list_user(self):
        #destroy user_window window
        self.user_window1.destroy()
        # create flight list window
        self.flight_list_window = Toplevel()
        self.flight_list_window.title("Flight_List Window")
        self.flight_list_window.geometry("1920x1080")
        self.flight_list_window.configure(bg ="#fff")
        
        # background image
        self.img1 = PhotoImage(file="Booking.png")
        label2 = Label(self.flight_list_window, image=self.img1)
        label2.place(x=0,y=0)
        
        # back button
        back_button_flight_userwindow =Button(self.flight_list_window, text="🔙",fg="#08314f", width=5,height=0,border=0,bg="#bedef5",font=("Montserrat SemiBold",20),command=self.back_to_user_window)
        back_button_flight_userwindow.place(x=2,y=2)
        
        #frame of flight_list_user window
        self.flight_list_user_frame=Frame(self.flight_list_window,width=550,height=300,bg="white")
        self.flight_list_user_frame.place(x=830,y=110) 
        
        # combo box from
        self.from_box=ttk.Combobox(self.flight_list_user_frame,width=15,justify="center")
        self.from_box["values"] = self.destination_from()
        self.from_box.config(font=("Roboto",15))
        self.from_box.grid(row=2,column=0)

        # combo box To
        self.to_box=ttk.Combobox(self.flight_list_user_frame,width=15,justify="center")
        self.to_box["values"] = self.destination_to()  
        self.to_box.bind("<<ComboboxSelected>>", self.to_box.set(self.to_box.get()))
        self.to_box.config(font=("Roboto",15))
        self.to_box.grid(row=2,column=2)
        
        # #Book your ticket label
        book_label=Label(self.flight_list_user_frame,text="Book Your Ticket",fg="white",bg="#08314f",font=("Montserrat SemiBold",25))
        book_label.grid(row=0,column=1,padx=0,pady=15)
        
        # source Label
        self.source_label=Label(self.flight_list_user_frame,text="Source",fg="black",bg="white",font=("Montserrat SemiBold",20))
        self.source_label.grid(row=1,column=0,padx=0,pady=0,ipadx=0,ipady=0)
        
        # destination Label
        self.destination_label=Label(self.flight_list_user_frame,text="Destination",fg="black",bg="white",font=("Montserrat SemiBold",20))
        self.destination_label.grid(row=1,column=2,padx=0,pady=0,ipadx=0,ipady=0)
        
        # blank spaces in grid
        blank_label=Label(self.flight_list_user_frame,text="",fg="black",bg="white",font=("Roboto",20))
        blank_label.grid(row=4,column=1,padx=0,pady=0,ipadx=0,ipady=0)
            
        # arrow between from and to
        arrow_label=Label(self.flight_list_user_frame,text="  ⇆  ",fg="black",bg="white",font=("Montserrat SemiBold",20))
        arrow_label.grid(row=2,column=1,padx=0,pady=0,ipadx=0,ipady=0)
        
        # search button
        search_button=Button(self.flight_list_user_frame,text="Search",fg="white",width=10,height=1,border=0,bg="#0A314F",font=("Montserrat SemiBold",14),command=self.search)
        search_button.grid(row=5,column=1,padx=0,pady=0,ipadx=0,ipady=0)
        
        # treebox frame
        self.frame_for_treebox=Frame(self.flight_list_window,width=750,height=400,bg="white")
        self.frame_for_treebox.place(x=700,y=400) 
        
        # Enter your name lable
        name_user_label=Label(self.flight_list_window,text="Enter Your Name",fg="White",bg="#08314f",font=("Montserrat SemiBold",25))
        name_user_label.place(x=230,y=130)
        
        # Entry for name
        self.name_user=Entry(self.flight_list_window,width=25,fg="black",border=0,bg="white",font=("Montserrat SemiBold",14))
        self.name_user.place(x=215,y=200)
        
        # cancel ticket button
        self.cancel_ticket_button =Button(self.flight_list_window, text="Cancel Ticket",fg="white", width=11,height=0,border=0,bg="#08314f",font=("Montserrat SemiBold",15),command=self.cancel_ticket)
        self.cancel_ticket_button.place(x=1248,y=18)
        
        # logout button
        self.logout_button =Button(self.flight_list_window, text="Logout",fg="white", width=10,height=0,border=0,bg="#08314f",font=("Montserrat SemiBold",15),command=self.flight_list_logout)
        self.logout_button.place(x=1450,y=18)
       
        
    # display the destination_from values in combo box
    def destination_from(self):  

        import mysql.connector as con
        connection = con.connect(host="localhost",user="root",password="starboy22*",database="flight")
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT destination_from FROM flight_list")
        
        result1 = cursor.fetchall()
        
        cursor.close()
        connection.close()
        return [row[0] for row in result1] 
    
    # display the destination_to values in combo box
    def destination_to(self):  

        import mysql.connector as con
        connection = con.connect(host="localhost",user="root",password="starboy22*",database="flight")
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT destination_to FROM flight_list")
        
        result2 = cursor.fetchall()
  
        cursor.close()
        connection.close()
        return [row[0] for row in result2]


    # Search flights and show in treeview
    def search(self):

        # variables for selected destinations 
        self.from_var = self.from_box.get()
        self.to_var = self.to_box.get()

        # show error if all fields are not entered
        if (self.from_var == "" or self.to_var == ""):
            messagebox.showerror("Error", "Enter Destinations")
            return
        
        if (self.from_var == self.to_var ):
            messagebox.showerror("Error", "Source and Destination must not be same")
            return  

        # connecting mysql
        import mysql.connector as con
        connection = con.connect(host="localhost", user="root", password="starboy22*", database="flight")
        cursor = connection.cursor()

        # mysql query for showing flights in treeview
        cursor.execute('select * from flight_list where destination_from = (%s) and destination_to = (%s)', (self.from_var, self.to_var))
        
        rows = cursor.fetchall()
        
        if (cursor.rowcount == 0):
            
            messagebox.showinfo("Error","Flight is not available.")

        # destroy the old tree object
        for child in self.frame_for_treebox.winfo_children():
            child.destroy()
           
            
        # # create new tree object
        # style = ttk.Style()

        # # Set the border width
        # style.configure('tree', borderwidth=15)
        

        # creating treeview
        self.tree = ttk.Treeview(self.frame_for_treebox)
        self.tree.config(height=15)
        self.tree["show"]="headings"

        self.tree["columns"] = ("ID", "destination_from", "destination_to", "departure_date", "departure_time", "arrival_date", "arrival_time", "price", "seats")
        self.tree.column("ID", width=50, minwidth=50, anchor=CENTER)
        self.tree.column("destination_from", width=100, minwidth=100, anchor=CENTER)
        self.tree.column("destination_to", width=100, minwidth=100, anchor=CENTER)
        self.tree.column("departure_date", width=130, minwidth=130, anchor=CENTER)
        self.tree.column("departure_time", width=130, minwidth=130, anchor=CENTER)
        self.tree.column("arrival_date", width=130, minwidth=130, anchor=CENTER)
        self.tree.column("arrival_time", width=130, minwidth=130, anchor=CENTER)
        self.tree.column("price", width=100, minwidth=50, anchor=CENTER)
        self.tree.column("seats", width=50, minwidth=50, anchor=CENTER)

        self.tree.heading("ID", text="ID", anchor=CENTER)
        self.tree.heading("destination_from", text="From", anchor=CENTER)
        self.tree.heading("destination_to", text="To", anchor=CENTER)
        self.tree.heading("departure_date", text="Departure Date", anchor=CENTER)
        self.tree.heading("departure_time", text="Departure Time", anchor=CENTER)
        self.tree.heading("arrival_date", text="Arrival Date", anchor=CENTER)
        self.tree.heading("arrival_time", text="Arrival Time", anchor=CENTER)
        self.tree.heading("price", text="Price", anchor=CENTER)
        self.tree.heading("seats", text="Seats", anchor=CENTER)
        
        # insert rows into the tree object
        for row in rows:
            self.tree.insert("", "end", values=row[0:])

        # pack the tree object
        self.tree.grid(row=0,column=0)
        
        # book button
        book_button=Button(self.frame_for_treebox,text="Book",fg="white",width=10,height=1,border=0,bg="#0A314F",font=("MADE Okine Sans",14),command=self.booked_flight)
        book_button.grid(row=1,column=0)
    
    # mysql query for booked_flight table  
    def booked_flight(self):
        # get the selected item from the Treeview widget
        selected_item = self.tree.selection()
        
        #variable for User Name 
        printname=self.name_user.get()
        
        # for generating transaction
        transaction_id = random.randint(100000, 999999)
        
        if not selected_item:
            # display an error message if no item is selected
            messagebox.showerror("Error", "Please select flight.")
            return
        
        elif (self.name_user.get()==""):
            messagebox.showerror("Error", "Please Enter Your Name.")
            return
        
       
            
        # retrieve the ID of the selected item for query
        id = self.tree.item(selected_item, "values")[0]
                
        # delete the corresponding record from the database
        import mysql.connector as con
        connection = con.connect(host="localhost", user="root", password="starboy22*", database="flight")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO booked_flight (destination_from, destination_to, departure_date, departure_time, arrival_date, arrival_time, price, name, transaction_id) SELECT destination_from, destination_to, departure_date, departure_time, arrival_date, arrival_time, price, %s, %s FROM flight_list WHERE ID= %s", (printname,transaction_id,id))
        connection.commit()
        messagebox.showinfo("Booked","Flight Succefully Booked")
        
        self.ticket_book_window()

        connection.close()  
    
    # ticket generating
    def ticket_book_window(self):

        self.seat_no = random.randint(1, 100)
        
        # get the last inserted record from the booked_flight table
        import mysql.connector as con
        connection = con.connect(host="localhost", user="root", password="starboy22*", database="flight")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM booked_flight ORDER BY ticket_id DESC LIMIT 1")
        record = cursor.fetchone()
        
        # create a new PDF canvas
        self.ticket = canvas.Canvas("ticket.pdf")
        
        # set font size and type
        self.ticket.setFont("Helvetica-Bold", 20)
        
        # draw the title
        self.ticket.drawCentredString(300, 780, "VIIT Airlines")
        self.ticket.drawCentredString(300, 750, "Flight Ticket")
        
        
        # set font size and type
        self.ticket.setFont("Helvetica-Bold", 14)
        
        # display the flight details
        
        self.ticket.drawString(50, 680, "Ticket ID: {}".format(record[0]))
        self.ticket.drawString(50, 650, "From: {}".format(record[1]))
        self.ticket.drawString(50, 620, "To: {}".format(record[2]))
        self.ticket.drawString(50, 590, "Departure Date: {}".format(record[3]))
        self.ticket.drawString(50, 560, "Departure Time: {}".format(record[4]))
        self.ticket.drawString(50, 530, "Arrival Date: {}".format(record[5]))
        self.ticket.drawString(50, 500, "Arrival Time: {}".format(record[6]))
        self.ticket.drawString(50, 470, "Price: {}".format(record[7])+" Rs")
        
        # display the passenger details
        self.ticket.setFont("Helvetica-Bold", 16)
        self.ticket.drawString(50, 420, "Passenger Details")
        self.ticket.setFont("Helvetica-Bold", 14)
        self.ticket.drawString(50, 380, "Name: {}".format(record[8]))
        self.ticket.drawString(50, 350, "Seat no: {}".format(self.seat_no))
        self.ticket.drawString(50, 320, "Transaction ID: {}".format(record[9]))
        
        # save the PDF canvas
        self.ticket.save()
        
        # open the generated PDF file
        
        os.startfile("ticket.pdf")  
    
    # cancel ticket window
    def cancel_ticket(self):
        
        # create cancel ticket window
        self.cancel_ticket_window = Toplevel()
        self.cancel_ticket_window.title("Cancel Ticket Window")
        self.cancel_ticket_window.geometry("540x540")
        self.cancel_ticket_window.configure(bg ="#fff")
        
        # background image for cancel ticket window
        self.img7=PhotoImage(file="cancel ticket.png")
        self.label7=Label(self.cancel_ticket_window,image=self.img7)
        self.label7.place(x=0,y=0)
        
        # frame for cancel ticket
        self.cancel_ticket_frame=Frame(self.cancel_ticket_window,width=300,height=300,bg="white")
        self.cancel_ticket_frame.place(x=160,y=120) 
        
        # Enter Ticket ID label
        self.cancel_label=Label(self.cancel_ticket_frame,text="Enter Ticket ID",fg="#081d4b",bg="White",font=("Montserrat SemiBold Italic",18))
        self.cancel_label.grid(row=0,column=0,padx=20,pady=0,ipadx=0,ipady=30)
        
        # Entry for ticket id
        self.cancel_entry=Entry(self.cancel_ticket_frame,width=10,fg="black",border=0,bg="white",font=("Montserrat SemiBold Italic",16))
        self.cancel_entry.grid(row=1,column=0,padx=20,pady=0,ipadx=0,ipady=1)
        Frame(self.cancel_ticket_frame,width=150,height=2,bg="black").grid(row=2,column=0,padx=0,pady=5,ipadx=0,ipady=0)
        
        # cancel button
        self.cancel_button=Button(self.cancel_ticket_frame,text="Submit",fg="white",width=10,height=2,border=0,bg="#4682B4",font=("Montserrat SemiBold",12),command=self.cancel_ticket_sql)
        self.cancel_button.grid(row=4,column=0,padx=5,pady=20,ipadx=0,ipady=0)
        
    # cancel ticket mysql 
    def cancel_ticket_sql(self):
        
        #connecting mysql
        import mysql.connector as con
        connection = con.connect(host="localhost",user="root",password="starboy22*",database="flight")
        
        cursor = connection.cursor()

        #show error if all fields are not entered
        if (self.cancel_entry.get() ==""):
            messagebox.showerror("Error","Please Enter Ticket ID.")
            return
            
        cursor.execute("DELETE FROM booked_flight WHERE ticket_id = %s", (self.cancel_entry.get(),))
        
        if cursor.rowcount > 0:
            connection.commit()
            messagebox.showinfo("Canceled","Ticket Successfully Canceled")
            self.cancel_ticket_window.destroy()
        else:
            messagebox.showinfo("Not found","Ticket ID does not exist")

        connection.close()   

        
    # Admin System setting window
    def admin_system_setting_window(self):

        #destroy admin_window window
        self.admin_window1.destroy()
        # create window
        self.system_setting_window = Toplevel()
        self.system_setting_window.title("System Window")
        self.system_setting_window.geometry("1920x1080")
        self.system_setting_window.configure(bg ="#fff")
        
        # background image for system setting window
        self.img6= PhotoImage(file="System setting.png")
        self.img6_label=Label(self.system_setting_window,image=self.img6)
        self.img6_label.place(x=0,y=0)
        
        # label system setting
        heading=Label(self.system_setting_window,text="System Setting",fg="white",bg="#081d4b",font=("Montserrat SemiBold Italic",28))
        heading.place(x=710,y=30)
        
        # frame for system setting
        self.frame_system_setting=Frame(self.system_setting_window,width=600,height=200,bg="white")
        self.frame_system_setting.place(x=60,y=180)
        
        #Source label and entry
        self.source_label=Label(self.frame_system_setting,text="Source",fg="#081d4b",bg="White",font=("Made Okine Sans Light",14))
        self.source_label.grid(row=0,column=0,padx=0,pady=5,ipadx=0,ipady=0)
        self.source=Entry(self.frame_system_setting,width=20,fg="black",border=0,bg="white",font=("Made Okine Sans Light",14))
        self.source.grid(row=1,column=0,padx=15,pady=0,ipadx=0,ipady=0)

        Frame(self.frame_system_setting,width=240,height=2,bg="black").grid(row=2,column=0,padx=40,pady=10,ipadx=0,ipady=0)
        
        # Calender for departure date
        def departure_date():
            def date_get():
                date = cal.get_date().strftime("%Y-%m-%d")
                self.departure_date.delete(0, END)
                self.departure_date.insert(0, date)
                top.destroy()
            
            # calender window
            top = Toplevel()
            top.geometry('200x200+580+300')
            
            cal = DateEntry(top, width=12, background='#081d4b', foreground='white', borderwidth=2)
            cal.pack(pady=10)
            
            ok_button = Button(top, text="OK", command=date_get)
            ok_button.pack()

        # Departure date label and entry
        self.ddate_label=Label(self.frame_system_setting,text="Departure Date",fg="#081d4b",bg="White",font=("MADE Okine Sans light",14))
        self.ddate_label.grid(row=3,column=0,padx=0,pady=5,ipadx=0,ipady=0)    
        self.departure_date=Entry(self.frame_system_setting,width=20,fg="black",border=0,bg="white",font=("MADE Okine Sans light",14))
        self.departure_date.grid(row=4,column=0,padx=0,pady=0,ipadx=0,ipady=0)

        Frame(self.frame_system_setting,width=240,height=2,bg="black").grid(row=5,column=0,padx=0,pady=10,ipadx=0,ipady=0)
        button = Button(self.frame_system_setting, text="Select Date", command=departure_date) # select button for departure date
        button.grid(row=6,column=0,padx=0,pady=10,ipadx=0,ipady=0)
        
        # Departure time label and entry
        self.dtime_label=Label(self.frame_system_setting,text="Departure Time",fg="#081d4b",bg="White",font=("MADE Okine Sans light",14))
        self.dtime_label.grid(row=7,column=0,padx=0,pady=5,ipadx=0,ipady=0)
        self.departure_time=Entry(self.frame_system_setting,width=20,fg="black",border=0,bg="white",font=("MADE Okine Sans light",14))
        self.departure_time.grid(row=8,column=0,padx=0,pady=0,ipadx=0,ipady=0)
        
        Frame(self.frame_system_setting,width=240,height=2,bg="black").grid(row=9,column=0,padx=0,pady=10,ipadx=0,ipady=0)
        
        # Destination label and entry
        self.destination_label=Label(self.frame_system_setting,text="Destination",fg="#081d4b",bg="White",font=("MADE Okine Sans light",14))
        self.destination_label.grid(row=0,column=1,padx=0,pady=5,ipadx=0,ipady=0)
        self.destination=Entry(self.frame_system_setting,width=20,fg="black",border=0,bg="white",font=("MADE Okine Sans light",14))
        self.destination.grid(row=1,column=1,padx=0,pady=10,ipadx=0,ipady=0)

        Frame(self.frame_system_setting,width=240,height=2,bg="black").grid(row=2,column=1,padx=0,pady=0,ipadx=0,ipady=0)
        
        # Calender for Arrival date
        def arrival_date():
            def date_get():
                date = cal.get_date().strftime('%Y-%m-%d')
                self.arrival_date.delete(0, END)
                self.arrival_date.insert(0, date)
                top.destroy()
            
            # calender new window    
            top = Toplevel()
            top.geometry('200x200+580+300')
            
            cal = DateEntry(top, width=12, background='#081d4b', foreground='white', borderwidth=2)
            cal.pack(pady=10)
            
            ok_button = Button(top, text="OK", command=date_get)
            ok_button.pack()
        
        # Arrival date label and entry
        self.adate_label=Label(self.frame_system_setting,text="Arrival Date",fg="#081d4b",bg="White",font=("MADE Okine Sans light",14))
        self.adate_label.grid(row=3,column=1,padx=0,pady=5,ipadx=0,ipady=0)    
        self.arrival_date=Entry(self.frame_system_setting,width=20,fg="black",border=0,bg="white",font=("MADE Okine Sans light",14))
        self.arrival_date.grid(row=4,column=1,padx=0,pady=0,ipadx=0,ipady=0)
        
        Frame(self.frame_system_setting,width=240,height=2,bg="black").grid(row=5,column=1,padx=0,pady=0,ipadx=0,ipady=0)  
        button = Button(self.frame_system_setting, text="Select Date", command=arrival_date)# select button for departure date
        button.grid(row=6,column=1,padx=0,pady=10,ipadx=0,ipady=0)

        # Arrival time label and entry
        self.atime_label=Label(self.frame_system_setting,text="Arrival Time",fg="#081d4b",bg="White",font=("MADE Okine Sans light",14))
        self.atime_label.grid(row=7,column=1,padx=0,pady=5,ipadx=0,ipady=0) 
        self.arrival_time=Entry(self.frame_system_setting,width=20,fg="black",border=0,bg="white",font=("MADE Okine Sans light",14))
        self.arrival_time.grid(row=8,column=1,padx=0,pady=10,ipadx=0,ipady=0)

        Frame(self.frame_system_setting,width=240,height=2,bg="black").grid(row=9,column=1,padx=0,pady=0,ipadx=0,ipady=0)
        
        
        # Price label and entry
        self.price_label=Label(self.frame_system_setting,text="Price",fg="#081d4b",bg="White",font=("MADE Okine Sans light",14))
        self.price_label.grid(row=10,column=0,padx=0,pady=5,ipadx=0,ipady=0) 
        self.price=Entry(self.frame_system_setting,width=20,fg="black",border=0,bg="white",font=("MADE Okine Sans light",14))
        self.price.grid(row=11,column=0,padx=0,pady=10,ipadx=0,ipady=0)
    
        Frame(self.frame_system_setting,width=240,height=2,bg="black").grid(row=12,column=0,padx=0,pady=0,ipadx=0,ipady=0)
        
        # Seats label and entry
        self.seats_label=Label(self.frame_system_setting,text="Seats",fg="#081d4b",bg="White",font=("MADE Okine Sans light",14))
        self.seats_label.grid(row=10,column=1,padx=0,pady=5,ipadx=0,ipady=0) 
        self.seats=Entry(self.frame_system_setting,width=20,fg="black",border=0,bg="white",font=("MADE Okine Sans light",14))
        self.seats.grid(row=11,column=1,padx=0,pady=10,ipadx=0,ipady=0)

        Frame(self.frame_system_setting,width=240,height=2,bg="black").grid(row=12,column=1,padx=0,pady=0,ipadx=0,ipady=0)
        
        # frame for system setting treeview
        self.frame_treeview_system_setting=Frame(self.system_setting_window,width=650,height=300,bg="white")
        self.frame_treeview_system_setting.place(x=720,y=200)
        
        # Back button
        home_button=Button(self.system_setting_window, text="🏠",fg="#081d4b", width=3,height=0,border=0,bg="#c7e5ff",font=("MADE Okine Sans",25),command=self.home_from_ss)
        home_button.place(x=5,y=5)
        
        # frame for treeview buttons
        self.frame_treeview_button=Frame(self.system_setting_window,width=650,height=500,bg="white")
        self.frame_treeview_button.place(x=140,y=650)
        
        # update button
        update_button =Button(self.frame_treeview_button, text="Update",fg="white", width=10,height=2,border=0,bg="#081d4b",font=("MADE Okine Sans",14),command=self.system_setting_insert)
        update_button.grid(row=0,column=0,padx=15,pady=20,ipadx=0,ipady=0) 
        
        # refresh button
        refresh_button=Button(self.frame_treeview_button,text="Refresh",fg="white",width=10,height=2,border=0,bg="#081d4b",font=("MADE Okine Sans",14),command=self.admin_treeview_insert_data)
        refresh_button.grid(row=0,column=1,padx=15,pady=20,ipadx=0,ipady=0)
        
        # delete button
        delete_button=Button(self.frame_treeview_button,text="Delete",fg="white",width=10,height=2,border=0,bg="#081d4b",font=("MADE Okine Sans",14),command=self.admin_treeview_delete_data)
        delete_button.grid(row=0,column=2,padx=15,pady=20,ipadx=0,ipady=0)
        
    
    # Admin treeview insert 
    def admin_treeview_insert_data(self):

        # connecting mysql
        import mysql.connector as con
        connection = con.connect(host="localhost", user="root", password="starboy22*", database="flight")
        cursor = connection.cursor()

        cursor.execute('select * from flight_list')
        rows = cursor.fetchall()

        # destroy the old tree object
        for child in self.frame_treeview_system_setting.winfo_children():
            child.destroy()

        # creating Treeview for system setting
        self.tree = ttk.Treeview(self.frame_treeview_system_setting)
        self.tree.config(height=15)
        self.tree["show"]="headings"

        # creating treeview columns
        self.tree["columns"] = ("ID", "destination_from", "destination_to", "departure_date", "departure_time", "arrival_date", "arrival_time", "price", "seats")
        self.tree.column("ID", width=50, minwidth=50, anchor=CENTER)
        self.tree.column("destination_from", width=100, minwidth=100, anchor=CENTER)
        self.tree.column("destination_to", width=100, minwidth=100, anchor=CENTER)
        self.tree.column("departure_date", width=130, minwidth=130, anchor=CENTER)
        self.tree.column("departure_time", width=130, minwidth=130, anchor=CENTER)
        self.tree.column("arrival_date", width=130, minwidth=130, anchor=CENTER)
        self.tree.column("arrival_time", width=130, minwidth=130, anchor=CENTER)
        self.tree.column("price", width=100, minwidth=50, anchor=CENTER)
        self.tree.column("seats", width=50, minwidth=50, anchor=CENTER)

        # giving names to columns
        self.tree.heading("ID", text="ID", anchor=CENTER)
        self.tree.heading("destination_from", text="From", anchor=CENTER)
        self.tree.heading("destination_to", text="To", anchor=CENTER)
        self.tree.heading("departure_date", text="Departure Date", anchor=CENTER)
        self.tree.heading("departure_time", text="Departure Time", anchor=CENTER)
        self.tree.heading("arrival_date", text="Arrival Date", anchor=CENTER)
        self.tree.heading("arrival_time", text="Arrival Time", anchor=CENTER)
        self.tree.heading("price", text="Price (Rs)", anchor=CENTER)
        self.tree.heading("seats", text="Seats", anchor=CENTER)

        # insert rows into the tree object
        for row in rows:
            self.tree.insert("", "end", values=row[0:])

        # pack the tree object
        self.tree.grid(row=0,column=0)
    
    # treeview delete 
    def admin_treeview_delete_data(self):
        # get the selected item from the Treeview widget
        selected_item = self.tree.selection()
        
        if not selected_item:
            # display an error message if no item is selected
            messagebox.showerror("Error", "Please select an item to delete.")
            return
        
        # retrieve the ID of the selected item
        id = self.tree.item(selected_item, "values")[0]
        
        # delete the selected item from the Treeview widget
        self.tree.delete(selected_item)
        
        # delete the corresponding record from the database
        import mysql.connector as con
        connection = con.connect(host="localhost", user="root", password="starboy22*", database="flight")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM flight_list WHERE ID = %s", (id,))
        connection.commit()
        messagebox.showinfo("Deleted","Entry Successfully Deleted")
        connection.close()
            
    # treeview insert        
    def system_setting_insert(self):
           
        # Regular expression to match time in the format "hh:mm:ss"
        time_pattern = r'^([0-1]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
            
        #if any entry is empty
        if (self.source.get() == "" or self.departure_date.get() == "" or self.departure_time.get() == "" or 
            self.destination.get() == "" or self.arrival_date.get() == "" or self.arrival_time.get() == "" or 
            self.price.get() == "" or self.seats.get() == ""):
            
            messagebox.showerror("Error", "All Fields Are Required")
            return
            
            
        elif len(self.departure_date.get()) != 10 or self.departure_date.get()[4] != '-' or self.departure_date.get()[7] != '-':
                
            messagebox.showerror("Error", "Invalid date format. Date format must be (YYYY-MM-DD)")
            return   
            
        elif len(self.arrival_date.get()) != 10 or self.arrival_date.get()[4] != '-' or self.arrival_date.get()[7] != '-':
                
            messagebox.showerror("Error", "Invalid date format. Date format must be (YYYY-MM-DD)")
            return 
            
        elif not re.match(time_pattern, self.departure_time.get()):
            messagebox.showerror("Error", "Invalid deaparture time format. Time format must be (HH:MM:SS)")
            return
            
        elif not re.match(time_pattern, self.arrival_time.get()):
            messagebox.showerror("Error", "Invalid arrival time format. Time format must be (HH:MM:SS)")
            return
            
        elif (self.departure_date.get() > self.arrival_date.get()):
            messagebox.showerror("Error", "Arrival Date must not be less than Departure Date")
            return
            
        elif (self.departure_date.get() == self.arrival_date.get()):
            
            if self.arrival_time.get() == self.departure_time.get() or self.arrival_time.get() < self.departure_time.get():
                messagebox.showerror("Error", "Arrival Time must greater than Departure Time")
                return
                
        printsource = self.source.get()
        printdestination = self.destination.get()
        printDdate = self.departure_date.get()
        printDtime = self.departure_time.get()
        printAdate = self.arrival_date.get()
        printAtime = self.arrival_time.get()
        printprice = self.price.get()
        printseats = self.seats.get()    
            
        #Mysql connection
        import mysql.connector as con
        connection = con.connect(host="localhost", user="root", password="starboy22*", database="flight")

        cursor = connection.cursor()

        #Mysql Query
        cursor.execute("INSERT INTO flight_list (destination_from,destination_to,departure_date,departure_time,arrival_date,arrival_time,price,seats) VALUES (%s, %s , %s, %s, %s , %s, %s, %s)", 
                    (printsource, printdestination, printDdate, printDtime,printAdate,printAtime,printprice,printseats))
        connection.commit()     # connnection.commit()
        
        connection.close() #closing connection

        messagebox.showinfo("Success", "Register Succesful")    
        
            
    # Binding all Entry
    # Binding User Signin Entry 
    # for User name
    def username_on_enter(self,event):
       
        self.username.delete(0,"end")

    def username_on_leave(self,event):
    
        if (self.username.get()==""):
            self.username.insert(0,"Username")   
    # for Password
    def password_on_enter(self,event):
        
        self.password.delete(0,"end")

    def password_on_leave(self,event):

        if (self.password.get()==""):
            self.password.insert(0,"Password") 
            
    # Binding User Signup Entry 
    # User
    # for user name
    def signup_username_on_enter(self,event):
 
        self.signup_username.delete(0,"end")

    def signup_username_on_leave(self,event):
        
        if (self.signup_username.get()==""):
            self.signup_username.insert(0,"Username")   
    # for Password
    def signup_password_on_enter(self,event):
       
        self.signup_password.delete(0,"end")

    def signup_password_on_leave(self,event):
      
        if (self.signup_password.get()==""):
            self.signup_password.insert(0,"Password")  
    # for confirm password
    def confirm_signup_password_on_enter(self,event):
      
        self.confirm_signup_password.delete(0,"end")

    def confirm_signup_password_on_leave(self,event):
    
        if (self.confirm_signup_password.get()==""):
            self.confirm_signup_password.insert(0,"Confirm Password")   
    # for email
    def signup_email_on_enter(self,event):
       
        self.signup_email.delete(0,"end")

    def signup_email_on_leave(self,event):
      
        if (self.signup_email.get()==""):
            self.signup_email.insert(0,"Email")       
            
    # Admin
    
    # for User name
    def admin_username_on_enter(self,event):
     
        self.admin_username.delete(0,"end")

    def admin_username_on_leave(self,event):

        if (self.admin_username.get()==""):
            self.admin_username.insert(0,"Username")   
    # for Password
    def admin_password_on_enter(self,event):

        self.admin_password.delete(0,"end")

    def admin_password_on_leave(self,event):
       
        if (self.admin_password.get()==""):
            self.admin_password.insert(0,"Password")  
 
     
if __name__ == "__main__":
    root = Tk()
    app = FlightBookingSystem(root)
    root.mainloop()

