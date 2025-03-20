import sqlite3
import  pandas as pd

class Universty():

    def __init__(self,name,country):
        self.name = name
        self.country = country
        self.status = True
        self.Connection()
        self.CreateAtable()

    def menu(self):
        print(self.name," ",self.country)
        print("***********")
        print("1-> Add student\n2-> Show student\n3-> Remove student\n4-> Search student\n5-> Update student\n6-> Exit")

    def run(self):
        self.menu()
        while(self.status):
            choice = self.Selection()
            if choice == 1:
                self.StudentAdd()
            elif choice == 2:
                self.show()
            elif choice == 3:
                self.removeStudent()
            elif choice == 4:
                self.SearchStudent()
            elif choice == 5:
                self.updateStudent()
            elif choice == 6:
                print("Exiting the program...")
                self.status = False

    def Selection(self):
        while(True):
            try:
                selection = int(input("Make your choice: "))
                if(selection < 0 or selection > 6):
                    print("your choice must be (1,2,3,4,5,6).")
                    continue
                break
            except ValueError:
                print("your choice must be number value.")
        return  selection

    def StudentAdd(self):
        self.name = input("Please enter your name: ").lower().capitalize()
        self.surname = input("Please enter your surname: ").lower().capitalize()
        while(True):
            try:
                self.studentID = int(input("Please enter your studentID: "))
                if(self.studentID >= 10000 or self.studentID < 1000):
                    print("Please entered your studentID wrong.")
                    continue
                break
            except ValueError:
                print("your studentID must be number value.")
        self.department = input("Please enter your department: ")
        while(True):
            try:
                self.typeOfEducation = int(input("Please enter your type of education: "))
                if(self.typeOfEducation > 2 or self.typeOfEducation <= 0 ):
                    print("Type of education must be 1 or 2")
                    continue
                break
            except ValueError:
                print("your type of education must be number value.")

        while(True):
            self.situation = input("Enter the student's status(Active/Graduate): ")
            if self.situation == "Active" or self.situation == "Graduate":
                break
            else:
                print("Student's status must be Active or Graduate")
        self.cursor.execute("Insert into StudentInfo Values(?,?,?,?,?,?)",(self.name, self.surname , self.studentID, self.department, self.typeOfEducation, self.situation))
        self.con.commit()
        print("student successfully added")

    def show(self):
        print("1-> All student information\n2-> Name information\n3-> Surname information\n4-> Student ID information\n5-> Department information\n6-> Type of education information\n7-> Situation information")
        while(True):
            try:
                self.select = int(input("Enter your must be (1,2,3,4,5,6,7): "))
                if(self.select > 7 or self.select < 1):
                    print("please choose one of 1,2,3,4,5,6,7 numbers ")
                    continue
                break
            except ValueError:
                print("Please enter your must be number value.")
        if(self.select == 1):
            self.cursor.execute("Select * From StudentInfo")
            self.list = self.cursor.fetchall()
            strlist = lambda x : [str(y) for y in x]
            print("*****Student information****")
            if not self.list:
                print("No students found.")
            else:
                for i,j in enumerate(self.list,1):
                    print("{}.) {}".format(i," ".join(strlist(j))))
        if(self.select == 2):
            self.cursor.execute("Select Name From StudentInfo")
            self.list2 = list(enumerate(list(set(self.cursor.fetchall())),1))
            if not self.list2:
                print("No students found.")
            else:
                print("****Student name information***")
                for i,j in self.list2:
                    print("{}.) {}".format(i, j[0]))
            while(True):
                try:
                    select = int(input("Select: "))
                    break
                except ValueError:
                    print("Must be enter integer")
            self.cursor.execute("Select * From StudentInfo where Name = '{}'".format(self.list2[select-1][1][0]))
            alllist = self.cursor.fetchall()
            alllist_str = lambda x : [str(y) for y in x]
            for i,j in enumerate(alllist,1):
                print("{}.) {}".format(i, " ".join(alllist_str(j))))

        if (self.select == 3):
            self.cursor.execute("Select Surname From StudentInfo")
            self.list3 = list(enumerate(list(set(self.cursor.fetchall())),1))
            if not self.list3:
                print("No students found.")
            else:
                print("****Student surname information***")
                for i, j in self.list3:
                    print("{}.) {}".format(i, j[0]))
            while(True):
                try:
                    selectt = int(input("Select: "))
                    break
                except ValueError:
                    print("Enter the must be integer.")
            self.cursor.execute("Select * From StudentInfo where Surname = '{}'".format(self.list3[selectt-1][1][0]))
            allstudent = self.cursor.fetchall()
            allstudent_str = lambda x : [str(y) for y in x]
            for i,j in enumerate(allstudent, 1):
                print("{}.) {}".format(i , " ".join(allstudent_str(j))))
        if (self.select == 4):
            self.cursor.execute("Select StudentID From StudentInfo")
            self.list4 = list(enumerate(list(set(self.cursor.fetchall())),1))
            if not self.list4:
                print("No students found.")
            else:
                print("****Student ID information***")
                strID = lambda x: [str(y) for y in x]
                for i, j in self.list4:
                    print("{}.) Student ID: {}".format(i, " ".join(strID(j))))
            while(True):
                try:
                    s = int(input("Select: "))
                    break
                except ValueError:
                    print("Select must be integer.")
            self.cursor.execute("Select * From StudentInfo where StudentID = {}".format(self.list4[s - 1][1][0]))
            sall = self.cursor.fetchall()
            sall_str = lambda x : [str(y) for y in x]
            for i, j in enumerate(sall, 1):
                print("{}.) {}".format(i, " ".join(sall_str(j))))
        if (self.select == 5):
            self.cursor.execute("Select Department From StudentInfo")
            self.list5 = list(enumerate(list(set(self.cursor.fetchall())),1))
            if not self.list5:
                print("No students found.")
            else:
                print("****Student department information***")
                for i, j in self.list5:
                    print("{}.) {}".format(i,j[0]))
            while(True):
                try:
                    select = int(input("select: "))
                    break
                except ValueError:
                    print("Enter type must be integer.")
            self.cursor.execute("Select * From StudentInfo where Department = '{}'".format(self.list5[select - 1][1][0]))
            alls = self.cursor.fetchall()
            a = lambda x: [str(y) for y in x]
            for i,j in enumerate(alls,1):
                print("{}.) {}".format(i," ".join(a(j))))
        if (self.select == 6):
            self.cursor.execute("Select TypEducation From StudentInfo")
            self.list6 = list(enumerate(list(set(self.cursor.fetchall())), 1))
            if not self.list6:
                print("No students found.")
            else:
                print("****Student Typ education information***")
                strTyp = lambda x: [str(y) for y in x]
                for i, j in self.list6:
                    print("{}.) Student typ education {}".format(i, " ".join(strTyp(j))))
            while (True):
                try:
                    sellect = int(input("Select: "))
                    break
                except ValueError:
                    print("Select must be integer.")
            studentall = self.cursor.execute("Select * From StudentInfo where TypEducation = {}".format(self.list6[sellect - 1][1][0]))
            studentall_str = lambda x : [str(y) for y in x]
            for i, j in enumerate(studentall, 1):
                print("{}.) {}".format(i, " ".join(studentall_str(j))))
        if (self.select == 7):
            self.cursor.execute("Select Situation From StudentInfo")
            self.list7 = list(enumerate(list(set(self.cursor.fetchall())),1))
            if not self.list7:
                print("No students found.")
            else:
                print("****Student situation information***")
                for i, j in self.list7:
                    print("{}.) {}".format(i, j[0]))
                while(True):
                    try:
                        Select1 = int(input("Select: "))
                        break
                    except ValueError:
                        print("please enter the integer")
                self.cursor.execute("Select * From StudentInfo where Situation = '{}'".format(self.list7[Select1 - 1][1][0]))
                allstudent = self.cursor.fetchall()
                allstudent_str = lambda x: [str(y) for y in x]
                for i, j in enumerate(allstudent, 1):
                    print("{}.) {}".format(i, " ".join(allstudent_str(j))))

    def removeStudent(self):
        self.cursor.execute("Select * From StudentInfo")
        self.list = self.cursor.fetchall()
        strlist = lambda x: [str(y) for y in x]
        for i, j in enumerate(self.list, 1):
            print("{}.) {}".format(i, " ".join(strlist(j))))
        while(True):
            try:
                delete = int(input("Enter the number of the student you want to delete: "))
                break
            except ValueError:
                print("Please must be enter number value")
        if(self.cursor.execute("Delete From StudentInfo where rowid = {}".format(delete))):
            print("student successfully removed")
            self.con.commit()

    def SearchStudent(self):
        name = input("Enter the name of the student you want to call: ").lower().capitalize()
        surname = input("Enter the surname of the student you want to call: ").lower().capitalize()
        studentID = input("Enter the student ID the student you want to call: ")
        self.cursor.execute("Select * From StudentInfo where Name = ? and Surname = ? and StudentID = ?",(name, surname, studentID,))
        liste = self.cursor.fetchall()
        strliste = lambda x : [str(y) for y in x]
        if not liste:
            print("Student not found")
        else:
            print("**Student found**")
            for i in liste:
                print(" ".join(strliste(i)))

    def updateStudent(self):
        print("1-> All a student update\n2-> Name update\n3-> Surname update\n4-> Student ID update\n5-> Department update\n6-> Type of education update\n7-> Situation update")
        def choice():
            while(True):
                try:
                    choice = int(input("Please make a choice, must be (1,2,3,4,5,6,7): "))
                    if(choice > 7 or choice < 1):
                        print("Plwase enter the must be (1,2,3,4,5,6,7")
                        continue
                    break
                except ValueError:
                    print("Please enter the must be valued number")
            return choice
        keep = choice()
        if keep == 1:
            oldname1 = input("Please enter old name: ")
            newname1 = input("Please enter new name: ")
            self.cursor.execute("Update StudentInfo set Name = ? where Name = ?", (newname1, oldname1))
            self.con.commit()
            oldsur1 = input("Please enter old surname: ")
            newsur1 = input("Please enter new surname: ")
            self.cursor.execute("Update StudentInfo set Surname = ? where Surname = ?", (newsur1, oldsur1))
            self.con.commit()
            while (True):
                try:
                    oldID1 = int(input("Please enter old student ID: "))
                    if oldID1 < 1000 or oldID1 > 10000:
                        print("Old student mustn't be less than 1000 and greater than 10000 ")
                        continue
                    break
                except ValueError:
                    print("Enter must be INT")
            while (True):
                try:
                    newID1 = int(input("Please enter new student ID: "))
                    if (newID1 < 1000 or newID1 >= 10000):
                        print("Enter the mustn't be greater than 10000 and less than 1000")
                        continue
                    break
                except ValueError:
                    print("Enter must be INT")
            self.cursor.execute("Update StudentInfo set StudentID = ? where StudentID = ?", (newID1, oldID1))
            self.con.commit()
            oldDepartment1 = input("Please enter old Department: ")
            newDepartment1 = input("Please enter new Department: ")
            self.cursor.execute("Update StudentInfo set Department = ? where Department = ?", (newDepartment1, oldDepartment1))
            self.con.commit()
            while (True):
                try:
                    oldTypEducation1 = int(input("Please enter old Typ education: "))
                    break
                except ValueError:
                    print("Please must the enter value number")
            while (True):
                try:
                    newTypEducation1 = int(input("Please enter new Typ education: "))
                    if (newTypEducation1 > 2 or newTypEducation1 < 1):
                        print("Enter the value less than 1 and greater than 2")
                        continue
                    break
                except ValueError:
                    print("Enter the value must be 1 or 2")
            self.cursor.execute("Update StudentInfo set TypEducation = ? where TypEducation = ?", (newTypEducation1, oldTypEducation1))
            self.con.commit()
            while(True):
                oldSituation1 = input("Please enter old Situation: ").lower().capitalize()
                if(oldSituation1 == "Active" or oldSituation1 == "Graduate"):
                    break
                else:
                    print("Enter the must be Active or Graduate")
            while(True):
                newSituation1 = input("Please enter new Situation: ").lower().capitalize()
                if (newSituation1 == "Active" or newSituation1 == "Graduate"):
                    break
                else:
                    print("Enter the must be Active or Graduate")
            self.cursor.execute("Update StudentInfo set Situation = ? where Situation = ?",(newSituation1, oldSituation1))
            self.con.commit()
            print("Student successfully renewed")

        elif(keep == 2):
            oldname = input("Please enter old name: ")
            newname = input("Please enter new name: ")
            self.cursor.execute("Update StudentInfo set Name = ? where Name = ?",(newname, oldname))
            self.con.commit()
            print("Name changed successfully")

        elif(keep == 3):
            oldsur = input("Please enter old surname: ")
            newsur = input("Please enter new surname: ")
            self.cursor.execute("Update StudentInfo set Surname = ? where Surname = ?", (newsur, oldsur))
            self.con.commit()
            print("Surname changed successfully")
        elif(keep == 4):
            while(True):
                try:
                    oldID = int(input("Please enter old student ID: "))
                    break
                except ValueError:
                    print("Enter must be INT")
            while(True):
                try:
                    newID = int(input("Please enter new student ID: "))
                    if(newID < 1000 or newID >= 10000):
                        print("Enter the must be greater than 1000 and less than 10000")
                        continue
                    break
                except ValueError:
                    print("Enter must be INT")
            self.cursor.execute("Update StudentInfo set StudentID = ? where StudentID = ?", (newID, oldID))
            self.con.commit()
            print("Student ID changed successfully")
        elif(keep == 5):
            oldDepartment = input("Please enter old Department: ")
            newDepartment = input("Please enter new Department: ")
            self.cursor.execute("Update StudentInfo set Department = ? where Department = ?", (newDepartment, oldDepartment))
            self.con.commit()
            print("Department changed successfully")
        elif keep == 6:
            while(True):
                try:
                    oldTypEducation = int(input("Please enter old Typ education: "))
                    break
                except ValueError:
                    print("Please must the enter value number")
            while(True):
                try:
                    newTypEducation = int(input("Please enter new Typ education: "))
                    if(newTypEducation > 2 or newTypEducation < 1):
                        print("Enter the value less than 1 and greater than 2")
                        continue
                    break
                except ValueError:
                    print("Enter the value must be 1 or 2")
            self.cursor.execute("Update StudentInfo set TypEducation = ? where TypEducation = ?", (newTypEducation, oldTypEducation))
            self.con.commit()
            print("Typ education changed successfully")
        elif keep == 7:
            oldSituation = input("Please enter old Situation: ").lower().capitalize()
            newSituation = input("Please enter new Situation: ").lower().capitalize()
            if(newSituation == "Active" or newSituation == "Graduate"):
                self.cursor.execute("Update StudentInfo set Situation = ? where Situation = ?", (newSituation, oldSituation))
                self.con.commit()
                print("Department changed successfully")
            else:
                print("Enter must be Graduate or Active")

    def Connection(self):
        self.con = sqlite3.connect("StudentInfo.db")
        self.cursor = self.con.cursor()
        self.CreateAtable()

    def CreateAtable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS StudentInfo (Name TEXT, Surname TEXT, StudentID INT, Department TEXT, TypEducation INT, Situation TEXT)")
        self.con.commit()

class DataStudent():
    def file_path(self):
        db_file = "C:/Users/Ayhan/PycharmProjects/pythonProject1/StudentInfo.db"
        return db_file
    def sqlConnect(self):
        conn = sqlite3.connect(self.file_path())
        query = "Select * From StudentInfo"
        df = pd.read_sql_query(query, conn)
        print(df.info())
        conn.close()


universty = Universty("ZBEU","Turkey")
#universty.run()
dataPandas = DataStudent()
dataPandas.sqlConnect()