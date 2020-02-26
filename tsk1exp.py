import tkinter as tk
import shelve
from tkinter import messagebox
import tsk2exp

class DataBaseManagement:
    def storedata(self,Userid_entry,confirmpasswrd_entry):
        with shelve.open(r"C:\\Users\\Aykdk\\Desktop\nortonpy\\classexercise\\Register User\\user registration") as userdata:
            userdata[Userid_entry] = {'User Id':Userid_entry,
                                      'User Password':confirmpasswrd_entry} #using independent args

    def checkpassword(self,userpasswrd_entry,confirmpasswrd_entry):
        if userpasswrd_entry == confirmpasswrd_entry:
            return 1
        else:
            return None

    def checkdata(self,Userid_entry):
        with shelve.open(r"C:\\Users\\Aykdk\\Desktop\nortonpy\\classexercise\\Register User\\user registration") as read_data:
            shelve_key = read_data.get(Userid_entry,None)
            return shelve_key #returns the value of shelve key

    def registerbutton(self,Userid_entry,userpasswrd_entry,confirmpasswrd_entry ):
        if self.checkdata(Userid_entry) is None: #if the key value is Nonne execute this
            if self.checkpassword(userpasswrd_entry,confirmpasswrd_entry) is None:
                messagebox.showwarning('Password Unmatch','The password\'s do not match with each other.')
            else:
                print('password match')
            self.storedata(Userid_entry,confirmpasswrd_entry)
            print('User registered succesfully')
            messagebox.showinfo('Registration successful','Your account has beeen registered succesfully')
            print('Registration unsuccessful')
        else:
            messagebox.showwarning('Account exists','The user account already exists')


class DataBase2:
        def checklogin(self,Userid_entry1):
            with shelve.open(r"C:\\Users\\Aykdk\\Desktop\nortonpy\\classexercise\\Register User\\user registration") as login_data:
                data_log = login_data.get(Userid_entry1,None)
                return data_log

        def id_check(self,Userid_entry1,userpasswrd_entry1):
            with shelve.open(r"C:\\Users\\Aykdk\\Desktop\nortonpy\\classexercise\\Register User\\user registration") as idcheck:
                id_user = idcheck.get(Userid_entry1)
                if id_user['User Id'] == Userid_entry1 and id_user['User Password'] == userpasswrd_entry1:
                    print('login successful')
                    messagebox.showinfo('login successful','You\'ve been succesfully logged in')
                    tsk2exp.Openwindow()
                else:
                    print('You\'ve entered the wrong username or password')
                    messagebox.showerror('Wromg Entry','You\'ve entered wrong Username or password')

        def loginbttn(self,Userid_entry1,userpasswrd_entry1):
            if self.checklogin(Userid_entry1) is None:
                messagebox.showwarning('Incomplete','Please enter both username and Id')
            else:
                self.id_check(Userid_entry1,userpasswrd_entry1)
                print('successful')


class LoginWindow:

    def __init__(self):
        wn_login=tk.Tk()
        wn_login.geometry('400x550')
        wn_login.configure(background='#393f4d')
        wn_login.title('Login GUI')
        # root.iconbitmap(r'C:\Users\\Aykdk\Downloads\college.ico')
        title_label1 = tk.Label(wn_login,bg='#393f4d',fg='white',text='User Login Window',font=('Futura',20,'bold'))
        title_label1.grid(row=0,column=0,padx=20,pady=20,columnspan=6)
        User_id1 = tk.Label(wn_login,bg='#393f4d',fg='white',text='User Id:',font=('Futura',10,'bold'))
        User_id1.grid(row=1,column=0,padx=20,pady=20,sticky='w')

        self.Userid_entry1 = tk.Entry(wn_login,bg='white',fg='#393f4d',font=('italic',10))
        self.Userid_entry1.grid(row=1,column=1,padx=20,pady=20)

        User_password1 = tk.Label(wn_login,bg='#393f4d',fg='white',text='Password:',font=('Futura',10,'bold'))
        User_password1.grid(row=2,column=0,padx=20,pady=20,sticky='w')

        self.userpasswrd_entry1 = tk.Entry(wn_login,bg='white',fg='#393f4d',show='*')
        self.userpasswrd_entry1.grid(row=2,column=1,padx=20,pady=20)
        login_btn = tk.Button(wn_login,bg='#393f4d',fg='white',text='Log in',font=('Futura',10),command=lambda: DataBase2().loginbttn(self.Userid_entry1.get(),
                                                                                                                        self.userpasswrd_entry1.get()))
        login_btn.grid(row=3,column=1,padx=5,pady=5)

        backbt1 = tk.Button(wn_login,bg='#393f4d',width=10,fg='white',text='Back',command=lambda: wn_login.destroy())
        backbt1.grid(row=4, column=1,padx=10,pady=10)
        wn_login.mainloop()

class MainClass:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x550')
        self.root.configure(background='#393f4d')
        self.root.title('Register GUI')
        # self.root.iconbitmap(r'C:\Users\\Aykdk\Downloads\college.ico')


        title_label = tk.Label(bg='#393f4d',fg='white',text='User Register Window',font=('Futura',20,'bold'))
        title_label.grid(row=0,column=0,padx=20,pady=20,columnspan=6)

        User_id = tk.Label(bg='#393f4d',fg='white',text='User Id:',font=('Futura',10,'bold'))
        User_id.grid(row=1,column=0,padx=20,pady=20,sticky='w')

        Userid_entry = tk.Entry(bg='white',fg='#393f4d',font=('italic',10))
        Userid_entry.grid(row=1,column=1,padx=20,pady=20)

        User_password = tk.Label(bg='#393f4d',fg='white',text='Password:',font=('Futura',10,'bold'))
        User_password.grid(row=2,column=0,padx=20,pady=20,sticky='w')

        userpasswrd_entry = tk.Entry(bg='white',fg='#393f4d',show='*')
        userpasswrd_entry.grid(row=2,column=1,padx=20,pady=20)

        confirm_password = tk.Label(bg='#393f4d',fg='white',text='Confirm Password:',font=('Futura',10,'bold'))
        confirm_password.grid(row=3,column=0,padx=20,pady=20)

        confirmpasswrd_entry = tk.Entry(bg='white',fg='#393f4d',show='*')
        confirmpasswrd_entry.grid(row=3,column=1,padx=20,pady=20)

        register_button = tk.Button(bg='#393f4d',fg='white',text='Register',command=lambda: DataBaseManagement().registerbutton(Userid_entry.get(),
                                                                                                                            userpasswrd_entry.get(),
                                                                                                                            confirmpasswrd_entry.get()))
        register_button.grid(row=4,column=1,padx=20,pady=20)

        frame_label = tk.LabelFrame(bg='#393f4d',fg='white')
        frame_label.grid(row=5,column=0,padx=20,pady=20,columnspan=3)

        ask_label = tk.Label(frame_label,bg='#393f4d',fg='white',text='Have an account?',font=('Futura',10))
        ask_label.grid(row=0,column=0,padx=10,pady=10)

        login_btn = tk.Button(frame_label,bg='#393f4d',fg='white',text='Log in',font=('Futura',10),command=self.loginbtn)
        login_btn.grid(row=0,column=1,padx=5,pady=5)

    def loginbtn(self):
        LoginWindow()

window1 = MainClass()
window1.root.mainloop()
