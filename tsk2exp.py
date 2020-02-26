from tkinter import *
import shelve
from tkinter import messagebox
from tkinter import ttk

EMPLOYEEDB = r"C:\Users\\Aykdk\Desktop\nortonpy\STW121COM\EmployeeDatabase\databseemployee"
DEPARTMENTDB = r"C:\Users\\Aykdk\Desktop\nortonpy\STW121COM\DepartmentDatabse\databasedepartment"
DEPARTMENTLIST = r"C:\Users\\Aykdk\Desktop\nortonpy\STW121COM\DEPARTMENTlist"
dbUser = r"C:\Users\\Aykdk\Desktop\nortonpy\STW121COM\UserDatabase\databaseUser"

listval = []

default_font = ('Futura',10,'bold')
title_font = ('Futura',16,'bold')
bg_color = '#393f4d'
fg_color = 'white'
db_path = r"C:\\Users\\Aykdk\\Desktop\nortonpy\\classexercise\\Register User\\user registration"

with shelve.open(DEPARTMENTLIST) as listadd:
    for n in listadd.values():
        print(n)
        listval.append(n) #to add into the list
print(listval)


class AddDepartmentwindow:
    def __init__(self):
        self.dep = Tk()
        self.dep.geometry('400x550')
        self.dep.title('Add Department')
        self.dep.configure(background='#393f4d')

        title_label2 = Label(self.dep,bg='#393f4d',fg='white',text='New Department Registration',font=('Futura',16,'bold'))
        title_label2.grid(row=0,column=0,padx=20,pady=20,columnspan=6)

        label_code = Label(self.dep,bg='#393f4d',fg='white',text='Department Code*',font=default_font)
        label_code.grid(row=1,column=0,padx=20,pady=20,sticky=E)

        self.entry_code = Entry(self.dep,bg=fg_color,fg=bg_color)
        self.entry_code.grid(row=1,column=1,padx=20,pady=20,sticky=E)

        label_name = Label(self.dep,bg='#393f4d',fg='white',text='Department Name',font=default_font)
        label_name.grid(row=2,column=0,padx=20,pady=20,sticky=E)

        self.entry_name = Entry(self.dep,bg=fg_color,fg=bg_color)
        self.entry_name.grid(row=2,column=1,padx=20,pady=20,sticky=E)

        register_btn = Button(self.dep,bg='#393f4d',width=15,fg='white',text='Register',command=self.register)
        register_btn.grid(row=4,column=1,padx=20,pady=10)

        reset_btn = Button(self.dep,bg='#393f4d',width=15,fg='white',text='Reset',command=self.resetbtn)
        reset_btn.grid(row=3,column=1,padx=20,pady=10)

        frane1 = LabelFrame(self.dep,bg='#393f4d')
        frane1.grid(row=5,column=0,padx=20,pady=20,columnspan=2)

        back1 = Button(frane1,bg='#393f4d',width=15,fg='white',text='Back',command=self.backbtn)
        back1.grid(row=0, column=0,padx=20,pady=20)

        self.dep.mainloop()



    def resetbtn(self):
        self.entry_code.delete(0,END)
        self.entry_name.delete(0,END)
    def backbtn(self):
        self.dep.destroy()

    def savedepat(self):
        with shelve.open(DEPARTMENTDB) as saveData:
            saveData[self.entry_code.get()] = {'Department Code':self.entry_code.get(),'Department Name':self.entry_name.get()}

        with shelve.open(DEPARTMENTLIST) as keylist:
            keylist[self.entry_name.get()] = self.entry_name.get()


    def chkdepat(self):
        with shelve.open(DEPARTMENTDB) as checkData:
            id_depart = checkData.get(self.entry_code.get(),None)
            return id_depart

    def register(self):
        if self.entry_code.get() == '':
            messagebox.showwarning('Empty entry','Please enter the department code')
        else:
            if self.chkdepat() is None:
                self.savedepat()
                messagebox.showinfo('Registration Successful','Department has been successfully Registered')
                self.dep.destroy()


            else:
                messagebox.showerror('Department Exists','The department already exists')

class RemoveDepartment:

    def __init__(self):

        self.remv = Tk()
        self.remv.geometry('400x550')
        self.remv.configure(background='#393f4d')
        self.remv.title('Remove Department')


        title_label3 = Label(self.remv,bg='#393f4d',fg='white',text='Remove Department',font=('Futura',16,'bold'))
        title_label3.grid(row=0,column=0,padx=20,pady=20,columnspan=6)

        label_code2 = Label(self.remv,bg='#393f4d',fg='white',text='Department Code*',font=default_font)
        label_code2.grid(row=1,column=0,padx=20,pady=20,sticky=E)

        self.entry_code2 = Entry(self.remv,bg=fg_color,fg=bg_color)
        self.entry_code2.grid(row=1,column=1,padx=20,pady=20,sticky=E)

        label_name2 = Label(self.remv,bg='#393f4d',fg='white',text='Department Name',font=default_font)
        label_name2.grid(row=2,column=0,padx=20,pady=20,sticky=E)

        entry_name2 = Entry(self.remv,bg=fg_color,fg=bg_color)
        entry_name2.grid(row=2,column=1,padx=20,pady=20,sticky=E)

        remove_btn = Button(self.remv,bg='#393f4d',width=15,fg='white',text='Remove',command=self.final_remove)
        remove_btn.grid(row=4,column=1,padx=20,pady=20)

        reset_btn2 = Button(self.remv,bg='#393f4d',width=15,fg='white',text='Reset')
        reset_btn2.grid(row=3,column=1,padx=20,pady=20)

        frane2 = LabelFrame(self.remv,bg='#393f4d')
        frane2.grid(row=5,column=0,padx=20,pady=20,columnspan=2)

        back2 = Button(frane2,bg='#393f4d',width=15,fg='white',text='Back',command=self.backbtn2)
        back2.grid(row=0, column=0,padx=20,pady=20)


        self.remv.mainloop()
    def checkdepart(self):
        with shelve.open(DEPARTMENTDB) as checkDepartment:
            idDepart = checkDepartment.get(self.entry_code2.get(),None)
            return idDepart
    def remove(self):
        with shelve.open(DEPARTMENTDB) as removeDepartment:
            popDepart = removeDepartment.pop(self.entry_code2.get())
            return popDepart
    def backbtn2(self):
        self.remv.destroy()

    def final_remove(self):
        if self.checkdepart() is None:
            messagebox.showerror('Department Error','No department found')
        else:
            self.remove()
            messagebox.showinfo('Done','Department Removed successfully')
            self.remv.destroy()



class ViewDepartment:
    def __init__(self):
        self.vie = Tk()
        self.vie.configure(background='#393f4d')
        self.vie.geometry('400x550')
        self.vie.title('View Department')

        labelDepartment = Label(self.vie,bg='#393f4d',fg='white',text='Department Code',font=default_font)
        labelDepartment.grid(row=0,column=0,padx=10,pady=10)

        labelDepartmentCode = Label(self.vie,bg='#393f4d',fg='white',text='Department Name',font=default_font)
        labelDepartmentCode.grid(row=0,column=1,padx=10,pady=10)
        self.readdict()

        self.vie.mainloop()

    def readdict(self):
        with shelve.open(DEPARTMENTDB) as dept:
            dept = dict(dept)
        ro = 1
        for row in dept.values():
            co = 0
            for col in row.values():
                Label(self.vie,bg='#393f4d',fg=fg_color,text=col).grid(row=ro,column=co,padx=10,pady=10)
                co = co + 1
            ro = ro + 1


class AddEmployee:

    def __init__(self):
        self.employ = Tk()
        self.employ.geometry('400x550')
        self.employ.configure(background='#393f4d')
        self.employ.iconbitmap(r'C:\Users\\Aykdk\Downloads\project2.ico')
        self.employ.title('self.Employee Register Form')

        self.lable_title = Label(self.employ,bg='#393f4d',fg='white',text='Employee Register Form',font={'Futura',30})
        self.lable_title.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.lable_empty = Label(self.employ,bg='#393f4d',text='')
        self.lable_empty.grid(row=1,column=0,padx=10,pady=10,)
        self.label_id = Label(self.employ,bg='#393f4d',fg='white',text='ID:',font={'Futura',25})
        self.label_id.grid(row=2,column=0,padx=10,pady=10,sticky=E)

        self.lable_name = Label(self.employ,bg='#393f4d',fg='white',text='Name:',font={'Futura',25})
        self.lable_name.grid(row=3,column=0,padx=10,pady=10,sticky=E)

        self.lable_age = Label(self.employ,bg='#393f4d',fg='white',text='Age:',font={'Futura',25})
        self.lable_age.grid(row=4,column=0,padx=10,pady=10,sticky=E)

        self.lable_gender = Label(self.employ,bg='#393f4d',fg='white',text='Gender:',font={'Futura',25})
        self.lable_gender.grid(row=5,column=0,padx=10,pady=10,sticky=E)

        self.label_address = Label(self.employ,bg='#393f4d',fg='white',text='Address:',font={'Futura',25})
        self.label_address.grid(row=6,column=0,padx=10,pady=10,sticky=E)

        label_contact = Label(self.employ,bg='#393f4d',fg='white',text='Contact:',font={'Futura',25})
        label_contact.grid(row=7,column=0,padx=10,pady=10,sticky=E)

        label_department = Label(self.employ,bg='#393f4d',fg='white',text='Department',font={'Futura',25})
        label_department.grid(row=8,column=0,padx=10,pady=10,sticky=E)

        self.entry_id = Entry(self.employ,bg='white',fg='#393f4d',width=10,borderwidth=2)
        self.entry_id.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        self.entry_name = Entry(self.employ,bg='white',fg='#393f4d',width=30,borderwidth=2)
        self.entry_name.grid(row=3,column=1,padx=10,pady=10,columnspan=2)

        self.entry_age = Entry(self.employ,bg='white',fg='#393f4d',width=10,borderwidth=2)
        self.entry_age.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        # dropdown_gender = OptionMenu(self.employ,gender_variable,*gender_options) #to show option button
        # dropdown_gender.grid(row=5,column=1,padx=10,pady=10,sticky=W)

        self.gender_combobox = ttk.Combobox(self.employ,values=['Male','Female','Other'],width=10)
        self.gender_combobox.grid(row=5,column=1,padx=10,pady=10,sticky=W)

        self.entry_address = Entry(self.employ,bg='white',fg='#393f4d',width=30,borderwidth=2)
        self.entry_address.grid(row=6,column=1,padx=10,pady=10)

        self.entry_contact = Entry(self.employ,bg='white',fg='#393f4d',width=30,borderwidth=2)
        self.entry_contact.grid(row=7,column=1,padx=10,pady=10)

        self.combobox_department = ttk.Combobox(self.employ,values=listval)
        self.combobox_department.grid(row=8,column=1,padx=10,pady=10)


        self.button_register = Button(self.employ,bg='#393f4d',fg='white',padx=30,text='Submit',command=self.registerbutton)
        self.button_register.grid(row=9,column=1,padx=10,pady=10)

        self.button_reset = Button(self.employ,bg='#393f4d',fg='white',padx=30,text='Reset',command=self.reset)
        self.button_reset.grid(row=9,column=0,padx=10,pady=10)

        self.frane3 = LabelFrame(self.employ,bg='#393f4d')
        self.frane3.grid(row=10,column=0,padx=20,pady=20,columnspan=2)

        self.back3 = Button(self.frane3,bg='#393f4d',width=15,fg='white',text='Back',command=lambda: self.employ.destroy())
        self.back3.grid(row=0, column=0,padx=20,pady=20)


        self.employ.mainloop()

    def registerdata(self):
        with shelve.open(EMPLOYEEDB) as fileWriter:
            fileWriter[self.entry_id.get()] = {
                                            'User Id':self.entry_id.get(),
                                            'Name':self.entry_name.get(),
                                            'Age':self.entry_age.get(),
                                            'Gender': self.gender_combobox.get(),
                                            'Address':self.entry_address.get(),
                                            'Contact':self.entry_contact.get(),
                                            'Department':self.combobox_department.get()}

    def readingdata(self):
        with shelve.open(EMPLOYEEDB) as filereader:
            idvalue = filereader.get(self.entry_id.get(),None)
            return idvalue

    def checkage(self):
        ageentry = self.entry_age.get()
        try:
            if int(ageentry) < 18:
                messagebox.showwarning('Age error','You\'re not old enough')

            else:
                print('You\'re old enough')
        except ValueError as lol:
            messagebox.showerror('Entry error','Enter a number')

    def checkcontact(self):
        contactentry = self.entry_contact.get()
        try:
            if int(contactentry) and len(contactentry) == 10:
                print('contact is okay')
            else:
                messagebox.showwarning('Enter vaild','No more than 10 digits should be entered')
        except ValueError:
            messagebox.showwarning('Entry error','Enter number in the contact entry box')

    def registerbutton(self):
        if self.readingdata() is None:
            self.checkage()
            self.checkcontact()
            self.registerdata()
            messagebox.showinfo('Registration Successful','Your data has been successfully registered')
            self.employ.destroy()

        else:
            messagebox.showerror('Account exists','The account already exists')
            print('Registration unsuccessful')
    def reset():
        self.entry_id.delete(0,END)
        self.entry_name.delete(0,END)
        self.entry_age.delete(0,END)
        self.gender_combobox.delete(0,END)
        self.entry_address.delete(0,END)
        self.entry_contact.delete(0,END)
        self.combobox_department.delete(0,END)

class ViewEmployee:
    def __init__(self):
        self.vieW = Tk()
        self.vieW.configure(background=bg_color)
        self.vieW.geometry('650x500')
        self.vieW.title('self.View Employee')

        label_empid = Label(self.vieW,bg=bg_color,fg=fg_color,text='Employee Id',font=default_font)
        label_empid.grid(row=0,column=0,padx=5,pady=2)

        label_empname = Label(self.vieW,bg=bg_color,fg=fg_color,text='Name',font=default_font)
        label_empname.grid(row=0,column=1,padx=5,pady=2)

        label_empage = Label(self.vieW,bg=bg_color,fg=fg_color,text='Age',font=default_font)
        label_empage.grid(row=0,column=2,padx=5,pady=2)

        label_empgender =Label(self.vieW,bg=bg_color,fg=fg_color,text='Age',font=default_font)
        label_empgender.grid(row=0,column=3,padx=5,pady=2)

        label_empaddress=Label(self.vieW,bg=bg_color,fg=fg_color,text='Address',font=default_font)
        label_empaddress.grid(row=0,column=4,padx=5,pady=2)

        label_empcontact=Label(self.vieW,bg=bg_color,fg=fg_color,text='Contact no.',font=default_font)
        label_empcontact.grid(row=0,column=5,padx=5,pady=2)

        label_empdepartment = Label(self.vieW,bg=bg_color,fg=fg_color,text='Department',font=default_font)
        label_empdepartment.grid(row=0,column=6,padx=5,pady=2)

        self.viewing_employee()
        self.vieW.mainloop()

    def viewing_employee(self):
        with shelve.open(EMPLOYEEDB) as emp:
            emp = dict(emp)
        ron = 1
        for ran in emp.values():
            con = 0
            for coln in ran.values():
                Label(self.vieW,bg=bg_color,fg=fg_color,text=coln).grid(row=ron,column=con,padx=5,pady=2)
                con= con + 1
            ron = ron + 1


class RemoveEmployee:
    def __init__(self):
        self.remE = Tk()
        self.remE.configure(background='#393f4d')
        self.remE.geometry('400x550')
        self.remE.title('removeEmployee')

        title_label3 = Label(self.remE,bg='#393f4d',fg='white',text='New Department Registration',font=('Futura',16,'bold'))
        title_label3.grid(row=0,column=0,padx=20,pady=20,columnspan=6)

        label_id2 = Label(self.remE,bg='#393f4d',fg='white',text='Employee Id *',font=default_font)
        label_id2.grid(row=1,column=0,padx=20,pady=20,sticky=E)

        self.entry_id2 = Entry(self.remE,bg=fg_color,fg=bg_color)
        self.entry_id2.grid(row=1,column=1,padx=20,pady=20,sticky=E)

        label_name3 = Label(self.remE,bg='#393f4d',fg='white',text='Employee Name',font=default_font)
        label_name3.grid(row=2,column=0,padx=20,pady=20,sticky=E)

        self.entry_name3 = Entry(self.remE,bg=fg_color,fg=bg_color)
        self.entry_name3.grid(row=2,column=1,padx=20,pady=20,sticky=E)

        remove_emp_btn = Button(self.remE,bg='#393f4d',width=15,fg='white',text='Remove',command=self.final_removeEmp)
        remove_emp_btn.grid(row=4,column=1,padx=20,pady=20)

        reset_btn3 = Button(self.remE,bg='#393f4d',width=15,fg='white',text='Reset',command=self.resetEmp)
        reset_btn3.grid(row=3,column=1,padx=20,pady=20)

        frane4 = LabelFrame(self.remE,bg='#393f4d')
        frane4.grid(row=10,column=0,padx=20,pady=20,columnspan=2)

        back4 = Button(frane4,bg='#393f4d',width=15,fg='white',text='Back',command=lambda: self.remE.destroy())
        back4.grid(row=0, column=0,padx=20,pady=20)
        self.remE.mainloop()

    def checkEmployee(self):
        with shelve.open(EMPLOYEEDB) as check_Employee:
            idEmploye = check_Employee.get(self.entry_id2.get(),None)
            return idEmploye
    def removeE(self):
        with shelve.open(EMPLOYEEDB) as remEmpl:
            popEmployee = remEmpl.pop(self.entry_id2.get())
            return popEmployee
    def final_removeEmp(self):
        if self.entry_id2.get() == '':
            messagebox.showwarning('Unfulfilled Requirement','Please enter the Employee Id')
        else:
            if self.checkEmployee() is None:
                messagebox.showerror('Department Error','No Employee found')
            else:
                self.removeE()
                messagebox.showinfo('Done','Employee data Removed successfully')
                self.remE.destroy()
    def resetEmp(self):
        self.entry_id2.delete(0,END)
        self.entry_name3.delete(0,END)


class Openwindow:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x550')
        self.root.configure(background='#393f4d')
        self.root.title('Login GUI')
        self.root.iconbitmap(r'C:\Users\\Aykdk\Downloads\college.ico')

        title_label = Label(self.root,bg='#393f4d',fg='white',text='Employee Management System',font=('Futura',16,'bold'))
        title_label.grid(row=0,column=0,padx=20,pady=20,columnspan=6)

        department_frame = LabelFrame(self.root,bg='#393f4d',fg='white',text='Department')
        department_frame.grid(row=1,column=1,padx=40,pady=40)

        button_add1 = Button(department_frame,bg='#393f4d',fg='white',width=20,text='Add Department',font=('Futura',10),command=AddDepartmentwindow)
        button_add1.grid(row=0,column=0,padx=5,pady=2)


        button_view1 = Button(department_frame,bg='#393f4d',fg='white',width=20,text='View Department',font=('Futura',10),command=ViewDepartment)

        button_view1.grid(row=1,column=0,padx=5,pady=2)

        button_remove1 = Button(department_frame,bg='#393f4d',fg='white',width=20,text='Remove Department',font=('Futura',10),command=RemoveDepartment)
        button_remove1.grid(row=2,column=0,padx=5,pady=2)

        employee_frame = LabelFrame(self.root,bg='#393f4d',fg='white',text='Employee')
        employee_frame.grid(row=2,column=1,padx=40,pady=40)

        button_add2 = Button(employee_frame,bg='#393f4d',fg='white',width=20,text='Add Employee',font=('Futura',10),command=AddEmployee)
        button_add2.grid(row=0,column=0,padx=5,pady=2)

        button_view2 = Button(employee_frame,bg='#393f4d',fg='white',width=20,text='View Employee',font=('Futura',10),command=ViewEmployee)
        button_view2.grid(row=1,column=0,padx=5,pady=2)

        button_remove2 = Button(employee_frame,bg='#393f4d',fg='white',width=20,text='Remove Employee',font=('Futura',10),command=RemoveEmployee)
        button_remove2.grid(row=2,column=0,padx=5,pady=2)
        self.root.mainloop()


if __name__ == '__main__':
    Openwindow()



