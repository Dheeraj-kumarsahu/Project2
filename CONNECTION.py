#purpose :To Build a simple data entry system
#input:Data 
#output:To store records
#Author:'dheerajkumarsahu827@gmail.com'
# contact:- '7389580688' 
from datetime import datetime
now = datetime.now()
import mysql.connector as c
def structure():
    try:
        mydb=c.connect(host="localhost",user="root",password="dheeraj@19",database="cuet")
        print('Connected to Mysql server')
        cur=mydb.cursor() 
        print('Cursor created ')
        query='''DESC STUDENT'''
        cur.execute(query)
        for row in cur.fetchall():
            print(row)
    except Exception as p:
        print(p)
    finally:
        mydb.close()
def admin():
    try:
        Enter_password=(input("Enter password  to login:-  "))
        if Enter_password == '1234': 
            print("WELCOME ADMIN")
            def inP():
                    try:
                        Enter_password=int(input("Enter password :-  "))
                        if Enter_password == 0000: 
                            mydb=c.connect(host="localhost",user="root",password="dheeraj@19",database="cuet")
                            print('Connected to Mysql server')
                            cur=mydb.cursor()
                            query='''SELECT * FROM STUDENT '''
                            cur.execute(query)
                            for i in cur.fetchall():
                                print(i)
                            print(' ****Enter Details of the Student**** ')
                            Roll=int(input("Enter Roll_number :- "))
                            Name=input("Enter Name of the student :- ")
                            Course=input("Enter Course :- ")
                            Gender=(input("Enter Gender(M/F) Only :- "))
                            Date=int(input("Enter joining year  :- "))
                            Age=int(input("Enter  Age (Minimum age = '17') :- "))
                            Addmission_no=int(input("Enter Admission Number :- "))
                            if Age >16:
                                query='''INSERT INTO STUDENT (Roll_no,Name,Course,Gender,DOJ,AGE,Admission_no) VALUES(%s,%s,%s,%s,%s,%s,%s)'''
                                val=(Roll,Name,Course,Gender,Date,Age,Addmission_no)
                                cur.execute(query,val)
                                mydb.commit()
                                query='''SELECT * FROM STUDENT '''
                                cur.execute(query)
                                for i in cur.fetchall():
                                    print(i)
                            else:
                                print("MINIMUM AGE MUST BE 17, AGE BELOW 17 IS NOT ALLOWED")
                    except Exception as p:
                        print(p)
                    finally:
                        mydb.close()
            def update():
                    try:
                        Enter_password=int(input("Enter password :-  "))
                        if Enter_password == 0000: 
                                mydb=c.connect(host="localhost",user="root",password="dheeraj@19",database="cuet")
                                print('Connected to Mysql server')
                                cur=mydb.cursor()
                                query='''SELECT * FROM STUDENT '''
                                cur.execute(query)
                                for i in cur.fetchall():
                                    print(i)
                                Roll=int(input('Enter ROLL NUMBER OF THE STUDENT WHOSE DATA NEED TO BE UPDATED :-  '))
                                Name=input("Enter Name of the student :- ")
                                Course=input("Enter Course :- ")
                                Gender=(input("Enter Gender(M/F) Only :- "))
                                Date=int(input("Enter joining year  :- "))
                                Age=int(input("Enter  Age(Min age is 17) :- "))
                                Admission_no=int(input("Enter Admission Number :- "))
                                if Age > 16:
                                    query='''UPDATE STUDENT SET name=%s,course=%s,gender=%s,doj=%s,age=%s,admission_no=%s where Roll_no=%s '''
                                    value=(Name,Course,Gender,Date,Age,Admission_no,Roll)
                                    cur.execute(query,value)
                                    mydb.commit()
                                    print("Data after Update")
                                    query='''SELECT * FROM STUDENT '''
                                    cur.execute(query)
                                    for i in cur.fetchall():
                                        print(i)
                                else:
                                    print("MINIMUM AGE MUST BE '17'")
                    except Exception as e:
                        print(e)
                    finally:
                        mydb.close()
            def structure():
                    try:
                        mydb=c.connect(host="localhost",user="root",password="dheeraj@19",database="cuet")
                        print('Connected to Mysql server')
                        cur=mydb.cursor() 
                        print('Cursor created ')
                        query='''DESC STUDENT'''
                        cur.execute(query)
                        for row in cur.fetchall():
                            print(row)
                    except Exception as p:
                        print(p)
                    finally:
                        mydb.close()
            def delete():
                    Enter_password=int(input("Enter password :-  "))
                    if Enter_password == 0000: 
                        try:
                            mydb=c.connect(host="localhost",user="root",password="dheeraj@19",database="cuet")
                            print('Connected to Mysql server')
                            cur=mydb.cursor()
                            query='''SELECT * FROM STUDENT '''
                            cur.execute(query)
                            for i in cur.fetchall():
                                print(i)
                            Roll_number=int(input("Enter Roll number to delete the data :- "))
                            query='''DELETE FROM STUDENT WHERE Roll_no = %s'''
                            val=(Roll_number,)
                            cur.execute(query,val)
                            mydb.commit()
                            query='''SELECT * FROM STUDENT '''
                            cur.execute(query)
                            print(f'RECORDS AFTER REMOVAL OF {Roll_number}')
                            for i in cur.fetchall():
                                print(i)
                        except Exception as e:
                            print(e)
                        finally:
                            mydb.close()            
            def reg():
                    try:
                        mydb=c.connect(host="localhost",user="root",password="dheeraj@19",database="cuet")
                        print('Connected to Mysql server')
                        cur=mydb.cursor()
                        query='''SELECT * FROM STUDENT '''
                        cur.execute(query)
                        for i in cur.fetchall():
                            print(i)
                    except  Exception as e:
                        print(e)
                    finally:
                        mydb.close()
            def feedback():
                    try:
                        file=open('C:\\Users\\User\\OneDrive\\Desktop\\Python program\\Project\\Studentdatamanagement\\Feedback.txt','r')
                        x=file.read()
                        print(x)
                    except Exception as e:
                        print(e)
                    finally:
                        file.close()
            def NOTICE():
                    X=input('Enter Notice :- ')
                    file=open('C:\\Users\\User\\OneDrive\\Desktop\\Python program\\Project\\Studentdatamanagement\\Notice.txt','a')
                    file.write(f'\n{X},The Notice is issued on :- {now} ')
                    file.close()
                    print('Notice added successfully')
            def acad():
                    def viewcourse():
                        CON=c.connect(host="localhost",user="root",password="dheeraj@19",database="cuet")
                        cur=CON.cursor()
                        print('Following Are the courses Except Student:-\n')
                        query='''SHOW TABLES'''
                        cur.execute(query)
                        for i in cur.fetchall():
                            print(i)
                    def addcourse():
                        print('Current courses available:')
                        viewcourse()
                        CON=c.connect(host="localhost",user="root",password="dheeraj@19",database="cuet")
                        cur=CON.cursor()
                        course=input('Enter Course name:-')
                        duration=int(input("Enter Number of semesters :-  "))
                        query=f'''CREATE TABLE {course} (Roll_no int(10),Sem_1 float(8),FOREIGN KEY (Roll_no) REFERENCES STUDENT(Roll_no) ON DELETE CASCADE ON UPDATE CASCADE)'''
                        cur.execute(query)
                        CON.commit()
                        for i in range(2,duration+1):
                            query1=f'''alter table {course} add column sem_{i} float(8)'''
                            cur.execute(query1)
                            CON.commit()
                            print(f'Course {course} added successfully with {duration} semesters')  
                    def addresult():
                        CON=c.connect(host="localhost",user="root",password="dheeraj@19",database="cuet")
                        cur=CON.cursor()
                        query1='''SELECT Roll_no,Name,Course FROM STUDENT'''
                        cur.execute(query1)
                        for i in cur.fetchall():
                            print(i)
                        course=input('Enter Course name :- ')
                        Roll_no=int(input("Enter Roll number to add result :- "))
                        sem=int(input("Enter Number of semester to add result from above list :- "))
                        if course == 'LLB' and sem == 6:
                            print(f'List of regristered students in {course}:')
                            query='''SELECT * FROM  STUDENT WHERE Course = 'LLB' '''
                            cur.execute(query)
                            for i in cur.fetchall():
                                print(i)
                            sem_1=float(input("Enter marks of sem_1 :- "))
                            sem_2=float(input("Enter marks of sem_2 :- "))
                            sem_3=float(input("Enter marks of sem_3 :- "))
                            sem_4=float(input("Enter marks of sem_4 :- "))
                            sem_5=float(input("Enter marks of sem_5 :- "))
                            sem_6=float(input("Enter marks of sem_6 :- "))    
                            query1=f'''INSERT INTO LLB (Roll_no,sem_1, sem_2, sem_3, sem_4, sem_5, sem_6) VALUES ({Roll_no},{sem_1}, {sem_2}, {sem_3}, {sem_4}, {sem_5}, {sem_6})'''
                            cur.execute(query1)
                            CON.commit()
                        elif course == 'B.SC' and sem == 6:
                            print(f'List of regristered students in {course}:')
                            query='''SELECT * FROM STUDENT WHERE Course = 'B.SC' '''
                            cur.execute(query)
                            for i in cur.fetchall():
                                print(i)
                            sem_1=float(input("Enter marks of sem_1 :- "))
                            sem_2=float(input("Enter marks of sem_2 :- "))
                            sem_3=float(input("Enter marks of sem_3 :- "))
                            sem_4=float(input("Enter marks of sem_4 :- "))
                            sem_5=float(input("Enter marks of sem_5 :- "))
                            sem_6=float(input("Enter marks of sem_6 :- "))    
                            query=f'''INSERT INTO BSC (Roll_no,sem_1, sem_2, sem_3, sem_4, sem_5, sem_6) VALUES ({Roll_no},{sem_1}, {sem_2}, {sem_3}, {sem_4}, {sem_5}, {sem_6})'''
                            cur.execute(query)
                            CON.commit()
                        elif course == 'B.TECH' and sem == 8:
                            print(f'List of regristered students in {course}:')
                            query='''SELECT * FROM  STUDENT WHERE Course = 'B.TECH' '''
                            cur.execute(query)
                            for i in cur.fetchall():
                                print(i)
                            sem_1=float(input("Enter marks of sem_1 :- "))
                            sem_2=float(input("Enter marks of sem_2 :- "))
                            sem_3=float(input("Enter marks of sem_3 :- "))
                            sem_4=float(input("Enter marks of sem_4 :- "))
                            sem_5=float(input("Enter marks of sem_5 :- "))
                            sem_6=float(input("Enter marks of sem_6 :- "))
                            sem_7=float(input("Enter marks of sem_7 :- "))
                            sem_8=float(input("Enter marks of sem_8 :- "))    
                            query1=f'''INSERT INTO BTECH (Roll_no,sem_1, sem_2, sem_3, sem_4, sem_5, sem_6, sem_7, sem_8) VALUES ({Roll_no},{sem_1}, {sem_2}, {sem_3}, {sem_4}, {sem_5}, {sem_6}, {sem_7}, {sem_8})'''
                            cur.execute(query1)
                            CON.commit()
                        elif course == 'M.TECH' and sem == 4:
                            print(f'List of regristered students in {course}:')
                            query='''SELECT * FROM  STUDENT WHERE COURSE = 'M.TECH' '''
                            cur.execute(query)
                            for i in cur.fetchall():
                                print(i)
                            sem_1=float(input("Enter marks of sem_1 :- "))
                            sem_2=float(input("Enter marks of sem_2 :- "))
                            sem_3=float(input("Enter marks of sem_3 :- "))
                            sem_4=float(input("Enter marks of sem_4 :- "))    
                            query1=f'''INSERT INTO MTECH (Roll_no,sem_1, sem_2, sem_3, sem_4) VALUES ({Roll_no},{sem_1}, {sem_2}, {sem_3}, {sem_4}) '''
                            cur.execute(query1)
                            CON.commit()                            
                        else:
                            if sem==4:
                                print(f'List of regristered students in {course}:')
                                query=f'''SELECT * FROM  STUDENT WHERE COURSE = '{course}' '''
                                cur.execute(query)
                                for i in cur.fetchall():
                                    print(i)
                                sem_1=float(input("Enter marks of sem_1 :- "))
                                sem_2=float(input("Enter marks of sem_2 :- "))
                                sem_3=float(input("Enter marks of sem_3 :- "))
                                sem_4=float(input("Enter marks of sem_4 :- "))    
                                query=f'''INSERT INTO {course} VALUES({Roll_no}, {sem_1},{sem_2},{sem_3},{sem_4})'''
                                cur.execute(query)
                                CON.commit()
                            elif sem==6:
                                print(f'List of regristered students in {course}:')
                                query=f'''SELECT * FROM  STUDENT WHERE COURSE = '{course}' '''
                                cur.execute(query)
                                for i in cur.fetchall():
                                    print(i)
                                sem_1=float(input("Enter marks of sem_1 :- "))
                                sem_2=float(input("Enter marks of sem_2 :- "))
                                sem_3=float(input("Enter marks of sem_3 :- "))
                                sem_4=float(input("Enter marks of sem_4 :- "))
                                sem_5=float(input("Enter marks of sem_5 :- "))
                                sem_6=float(input("Enter marks of sem_6 :- "))
                                query=f'''INSERT INTO {course} VALUES({Roll_no}, {sem_1},{sem_2},{sem_3},{sem_4},{sem_5},{sem_6})'''
                                cur.execute(query)
                                CON.commit()
                            elif sem==8:
                                print(f'List of regristered students in {course}:')
                                query=f'''SELECT * FROM  STUDENT WHERE COURSE = '{course}' '''
                                cur.execute(query)
                                for i in cur.fetchall():
                                    print(i)
                                sem_1=float(input("Enter marks of sem_1 :- "))
                                sem_2=float(input("Enter marks of sem_2 :- "))
                                sem_3=float(input("Enter marks of sem_3 :- "))
                                sem_4=float(input("Enter marks of sem_4 :- "))
                                sem_5=float(input("Enter marks of sem_5 :- "))
                                sem_6=float(input("Enter marks of sem_6 :- "))
                                sem_7=float(input("Enter marks of sem_7 :- "))
                                sem_8=float(input("Enter marks of sem_8 :- "))
                                query=f'''INSERT INTO {course} VALUES({Roll_no}, {sem_1},{sem_2},{sem_3},{sem_4},{sem_5},{sem_6},{sem_7},{sem_8})'''
                                cur.execute(query)
                                CON.commit()
                            else:
                                print("PLEASE UPDATE THE BACKEND WITH PROPER NUMBER OF SEMESTERS ")
                    def Menu():
                        while True:
                            print("\n========== ACADEMIC MENU ===========")
                            print("1. View Course")
                            print("2. Add Course")
                            print("3. Add Result")
                            print('4. EXIT' )  
                            choice = input("Enter choice: ")       
                            if choice == '1':
                                viewcourse()
                            elif choice == '2':
                                addcourse()
                            elif choice == '3':
                                addresult()
                            elif choice == '4':
                                print("👋 Exiting...")
                                break
                            else:
                                print("❌ Invalid choice! Try again.")
                    Menu()
            def Menu():
                while True:
                    print("\n========== Admin MENU ===========")
                    print("1. Structure ")
                    print("2. List of Regitered Student")
                    print("3. ADD data")
                    print("4. UPDATE DATA")
                    print("5. DELETE DATA")
                    print("6. Feedback")
                    print("7. Academics(Results)")
                    print('8. ADD NOTICE')
                    print('9. EXIT' )  

                    choice = input("Enter choice: ")       
                    if choice == '1':
                        structure()
                    elif choice == '2':
                        reg()
                    elif choice == '3':
                        inP()
                    elif choice == '4':
                        update()
                    elif choice == '5':
                        delete()
                    elif choice == '6':
                        feedback()
                    elif choice == '7':
                        acad()
                    elif choice == '8':
                        NOTICE()
                    elif choice == '9':
                        print("👋 Exiting...")
                        break
                    else:
                        print("❌ Invalid choice! Try again.")
            Menu()
        
        else:
            print("❌ Incorrect password! Access denied.")
    except Exception as e1:
        print(e1)  
def reg():
    try:
        mydb=c.connect(host="localhost",user="root",password="dheeraj@19",database="cuet")
        print('Connected to Mysql server')
        cur=mydb.cursor()
        query='''SELECT * FROM STUDENT '''
        cur.execute(query)
        for i in cur.fetchall():
            print(i)
    except  Exception as e:
        print(e)
    finally:
        mydb.close()
def aca():
    try:    
        Roll_no=int(input("Enter Roll number to see Result :- "))
        mydb=c.connect(host="localhost",user="root",password="dheeraj@19",database="cuet")
        con=mydb.cursor()
        query='''SELECT Roll_no from student  WHERE Roll_no = %s'''
        val=(Roll_no,)
        con.execute(query,val)
        for i in con.fetchall():
            if i[0]==Roll_no:
                con.execute('''SELECT DISTINCT COURSE FROM STUDENT''')
                for i in con.fetchall():
                    print(i)    
                course=input("Enter Course name to check the result :- ")
                adm=int(input("Enter Admission_no to see the result :- "))
                query1='''SELECT Admission_no from student WHERE Roll_no = %s'''
                val=(Roll_no,)
                con.execute(query1,val)
                for i in con.fetchall():
                   if adm==i[0] :
                      print('Roll number and Admission number matched')
                      if course == 'LLB':
                          query='''SELECT * FROM LLB AS B INNER JOIN  STUDENT AS A ON B.Roll_no = A.Roll_no WHERE A.Roll_no = %s'''
                          val=(Roll_no,)
                          con.execute(query,val)
                          for i in con.fetchall():
                                print("**************RESULT**************")
                                print("ROLL_NO: ",i[0])
                                print("NAME : ",i[8])
                                print("SEM-1: ",i[1])
                                print("SEM-2: ",i[2])
                                print("SEM-3: ",i[3])
                                print("SEM-4: ",i[4])
                                print("SEM-5: ",i[5])
                                print("SEM-6: ",i[6])
                                print(f"TOTAL CGPA:{(i[1]+i[2]+i[3]+i[4]+i[5]+i[6])/6} ")
                      elif course == 'B.SC':
                           query1='''SELECT * FROM BSC AS B INNER JOIN  STUDENT AS A ON B.Roll_no = A.Roll_no WHERE A.Roll_no = %s'''
                           val=(Roll_no,)
                           con.execute(query1,val)
                           for k in con.fetchall():
                                print("**************RESULT**************")
                                print("ROLL_NO: ",k[0])
                                print("NAME : ",k[8])
                                print("SEM-1: ",k[1])
                                print("SEM-2: ",k[2])
                                print("SEM-3: ",k[3])
                                print("SEM-4: ",k[4])
                                print("SEM-5: ",k[5])
                                print("SEM-6: ",k[6])
                                print(f"TOTAL CGPA:{(k[1]+k[2]+k[3]+k[4]+k[5]+k[6])/6}")
                      elif course == 'B.TECH':
                          query='''SELECT * FROM BTECH AS B INNER JOIN  STUDENT AS A ON B.Roll_no = A.Roll_no WHERE A.Roll_no = %s'''
                          val=(Roll_no,)
                          con.execute(query,val)
                          for l in con.fetchall():
                            print("**************RESULT**************")
                            print("ROLL_NO: ",l[0])
                            print("NAME : ",l[10])
                            print("SEM-1: ",l[1])
                            print("SEM-2: ",l[2])
                            print("SEM-3: ",l[3])
                            print("SEM-4: ",l[4])
                            print("SEM-5: ",l[5])
                            print("SEM-6: ",l[6])
                            print("SEM-7: ",l[7])
                            print("SEM-8: ",l[8])
                            print(f"TOTAL CGPA:{(l[1]+l[2]+l[3]+l[4]+l[5]+l[6]+l[7]+l[8])/8} ")
                      elif course == 'M.TECH':
                          query='''SELECT * FROM MTECH AS B INNER JOIN  STUDENT AS A ON B.Roll_no = A.Roll_no WHERE A.Roll_no = %s'''
                          val=(Roll_no,)
                          con.execute(query,val)        
                          for m in con.fetchall():
                            print("**************RESULT**************")
                            print("ROLL_NO: ",m[0])
                            print("NAME : ",m[6])
                            print("SEM-1: ",m[1])
                            print("SEM-2: ",m[2])
                            print("SEM-3: ",m[3])
                            print("SEM-4: ",m[4])
                            print(f"TOTAL CGPA:{(m[1]+m[2]+m[3]+m[4])/4} ")
                      else:
                           query=f'''SELECT * FROM {course} AS B INNER JOIN  STUDENT AS A ON B.Roll_no = A.Roll_no WHERE A.Roll_no = {Roll_no}'''
                           con.execute(query)
                           for n in con.fetchall():
                             print("**************RESULT**************")
                             print("ROLL_NO: ",n[0])
                             print("NAME : ",n[-1])
                             for i in range(1,len(n)-1):
                                 print(f"SEM-{i} : ",n[i])
                                 print(f"TOTAL CGPA:{sum(n[1:-1])/len(n[1:-1])} ")
                   else:
                    print('IF RESULT NOT FOUND, Check lIST OF COURSES,\n Please contact to admin to add the course and result')
            else:
               print('Roll Number not found')
    except Exception as e:
        print(e)
def feedback():
    try: 
      Roll_no=int(input("Enter Roll number to give feedback :- "))
      mydb=c.connect(host="localhost",user="root",password="dheeraj@19",database="cuet")
      cur=mydb.cursor()
      query='''SELECT Roll_no from student  WHERE Roll_no = %s'''
      val=(Roll_no,)
      cur.execute(query,val)
      for i in cur.fetchall():
        if i[0]==Roll_no:
            feedback=input("Enter your feedback here :- ")
            File=open('C:\\Users\\User\\OneDrive\\Desktop\\Python program\\Project\\Studentdatamanagement\\Feedback.txt','a')
            File.write(f'Roll number{Roll_no}  has Submmitted an feedback :- {feedback},on {now}\n')
            print("Feedback submitted successfully")
            File.close()
            mydb.close()
        else:
         print('Roll Number not found')
    except Exception as e:
        print(e)
def notice():
    try:
        file=open('C:\\Users\\User\\OneDrive\\Desktop\\Python program\\Project\\Studentdatamanagement\\Notice.txt','r')
        x=file.read()
        print(f'The Notice is : {x}')
    except Exception as e:
        print(e)
    finally:
        file.close()
def Menu():
    while True:
        print("\n========== STUDENT MANAGEMENT MENU ===========")
        print("1. Structure ")
        print("2. List of Regitered Student")
        print("3. Academics(Results)")
        print("4. Admin login")
        print('5. Feedback')
        print('6. NOTICE')
        print('7. EXIT' )  

        choice = input("Enter choice: ")       
        if choice == '1':
            structure()
        elif choice == '2':
            reg()
        elif choice == '3':
            aca()
        elif choice == '4':
            admin()
        elif choice == '5':
            feedback()
        elif choice == '6':
            notice()
        elif choice == '7':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice! Try again.")
Menu()