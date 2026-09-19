#Project-1
import pickle
import os

'''Project_Topic_Name'''

print('*'*107)

for i in range(107):
    if i%2==0:
        print('*',end='')
    else:
        print(' ',end='')
print()


print('*',end='')        
print(' '*40,end='')
print("STUDENT MANAGEMENT SYSTEM",end='')
print(' '*40,end='')
print('*')
    
for i in range(107):
    if i%2==0:
        print('*',end='')
    else:
        print(' ',end='')
print()


print('*'*107)


#admin_functions

def add_record():
    
    F=open("sturec.dat","ab")
    
    try:
        while True:
            admno=int(input('Enter admno'))
            rno=int(input('Enter rollno'))
            fname=input('Enter first name')
            lname=input('Enter last name')
            gen=input('Enter gender')
            dob=input('Enter dob')
            cl=int(input('Enter class'))
            sec=input('Enter section')
            stm=input('Enter stream')

            #for_convenient_printing
            if stm.lower()=="science":        
                stm=stm+" "
            elif stm.lower()=="arts":
                stm=stm+"    "
                
            mks=float(input("Enter marks"))
            grd=input('Enter grade')
            
            rec=[admno,rno,fname,lname,gen,dob,cl,sec,stm,mks,grd]
            pickle.dump(rec,F)

            print("\nRecord Added Successfully...\n")
            ch=input("Enter y/n to continue:")
            if ch in "nN":
                break

    except Exception:
        print("An Error occured while adding Student Record...\n")
    
    F.close()


def display_record():

    #Display_rec_on_the_basis_of_rno_entered_by_end_user
    
    F=open("sturec.dat","rb")                             

    try:
        r=int(input("Enter Roll no. to be displayed"))
    except ValueError:
        print("Invalid Input\n")
        
    try:
        while True:
            rec=pickle.load(F)
            if rec[1]==r:
                print("Record of Student: rno",r,'\n')
                print("Admiss.No\tR.No.\tF.Name\tL.Name\tGen\tDateOfBirth\tCl\tSec\tStream\t\tMks\tGrd")
                print (rec[0], rec[1], rec[2], rec[3], rec[4], rec[5],  rec[6],     
               rec[7], rec[8], rec[9], rec[10], sep="\t")
                break
    except Exception:
        print("Record not found...\n")
        
    F.close()


def display_all_records():
    
    F=open("sturec.dat","rb")
    print('All Student Records:\n')
    print("Admiss.No\tR.No.\tF.Name\tL.Name\tGen\tDateOfBirth\tCl\tSec\tStream\t\tMks\tGrd")
    
    try:
        while True:
            rec=pickle.load(F)
            print(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],
            rec[8],rec[9],rec[10],sep='\t')
    except Exception:
        pass
    
    F.close()


def search_record():

    F=open("sturec.dat","rb")
    
    print("1.Searching by Rno")
    print("2.Searching by Section")
    print("3.Searching by Stream")
    print("4.Searching by Grade")

    ch=0

    try:
        ch=int(input("Enter Your Choice"))
    except ValueError:
        print("Invalid Input\n")
    
    if ch==1:                                               #search_by_rno     
        r=int(input("\nEnter Student Rno to be Searched"))

        try:
            while True:
                rec=pickle.load(F)
                if rec[1]==r:
                    print("Record Found:\n")
                    print("Admiss.No\tR.No.\tF.Name\tL.Name\tGen\tDateOfBirth\tCl\tSec\tStream\t\tMks\tGrd")
                    print(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],
                    rec[6],rec[7],rec[8],rec[9],rec[10],sep="\t")
                    break
        
        except Exception:
            print("Record not found...\n")
            
        
 
    elif ch==2:                                            #search_by_section                                
        s=input("\nEnter Section to be searched")
        found=False
        
        try:
            while True:
                rec=pickle.load(F)
                if rec[7]==s:
                    print("\nAdmiss.No\tR.No.\tF.Name\tL.Name\tGen\tDateOfBirth\tCl\tSec\tStream\t\tMks\tGrd")
                    print(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],
                    rec[6],rec[7],rec[8],rec[9],rec[10],sep="\t")
                    found=True
                    
        except Exception:
            if found==False:
                print("Records not found...\n")
                
        
    elif ch==3:                                            #search_by_stream       
        stm=input("\nEnter Stream to be Searched")
        found=False
        
        try:
            while True:
                rec=pickle.load(F)
                
                if rec[8].strip().lower()==stm.lower():
                    print("\nAdmiss.No\tR.No.\tF.Name\tL.Name\tGen\tDateOfBirth\tCl\tSec\tStream\t\tMks\tGrd")
                    print(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],
                    rec[7],rec[8],rec[9],rec[10],sep="\t")
                    found=True
                
        except Exception:
            if found==False:
                print("Records not found...\n")
                

    elif ch==4:                                             #search_by_grade
        gd=input("\nEnter Grade to be Searched")
        found=False
        
        try:
            while True:
                rec=pickle.load(F)
                if rec[10]==gd:
                    print("\nAdmiss.No\tR.No.\tF.Name\tL.Name\tGen\tDateOfBirth\tCl\tSec\tStream\t\tMks\tGrd")
                    print(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],
                    rec[7],rec[8],rec[9],rec[10],sep="\t")
                    found=True
                    
        except Exception:
            if found==False:
                print("Records not found...\n")
        
    
    F.close()


def update_record():
    F=open("sturec.dat","rb")
    F2=open("new.dat","wb")
    
    print("1.Update Admission no.")
    print("2.Update Name")
    print("3.Update DOB")
    print("4.Update Gender")
    print("5.Update Section")
    print("6.Update Stream")
    print("7.Update Marks and Grade")

    ch=0

    try:
        ch=int(input("Enter Your Choice"))
        r=int(input("\nEnter Student Rno whose record is to be Updated"))
    except Exception:
        print("Invalid Input\n")

    
    
        
    found=False

    if ch==1:                           #update_admno
        try:
            while True:
                rec=pickle.load(F)
                if rec[1]==r:
                    rec[0]=int(input("Enter new Admission no."))
                    found=True
                pickle.dump(rec,F2)
                    
        except Exception:
            if found==True:
                print("Record Updated Successfully…\n")
            else:
                print("Record Not Found…\n")


    elif ch==2:                          #update_name
        try:
            while True:
                rec=pickle.load(F)
                if rec[1]==r:
                    rec[2]=input("Enter new First name")
                    rec[3]=input("Enter new Last name")
                    found=True
                pickle.dump(rec,F2)
                    
        except Exception:
            if found==True:
                print("Record Updated Successfully…\n")
            else:
                print("Record Not Found…\n")


        
    elif ch==3:                         #update_dob
        
        try:
            while True:
                rec=pickle.load(F)
                if rec[1]==r:
                    rec[5]=input("Enter new DOB(dd-mm-yy)")
                    found=True
                pickle.dump(rec,F2)
                    
        except Exception:
            if found==True:
                print("Record Updated Successfully…\n")
            else:
                print("Record Not Found…\n")
        
    
    elif ch==4:                         #update_gender
        try:
            while True:
                rec=pickle.load(F)
                if rec[1]==r:
                    rec[4]=input("Enter new Gender")
                    found=True
                pickle.dump(rec,F2)
                    
        except Exception:
            if found==True:
                print("Record Updated Successfully…\n")
            else:
                print("Record Not Found…\n")      
    
    elif ch==5:                          #update_section
        try:
            while True:
                rec=pickle.load(F)
                if rec[1]==r:
                    rec[7]=input("Enter new Section")
                    found=True
                pickle.dump(rec,F2)
                    
        except Exception:
            if found==True:
                print("Record Updated Successfully…\n")
            else:
                print("Record Not Found…\n")
        
    elif ch==6:                          #update_stream
        try:
            while True:
                rec=pickle.load(F)
                if rec[1]==r:
                    rec[8]=input("Enter new Stream")

                    #for_convenient_printing
                    if rec[8].lower()=="science":        
                        rec[8]=rec[8]+" "
                    elif rec[8].lower()=="arts":
                        rec[8]=rec[8]+"    "

                    found=True
                pickle.dump(rec,F2)
                    
                    
        except Exception:
            if found==True:
                print("Record Updated Successfully…\n")
            else:
                print("Record Not Found…\n")
            
    elif ch==7:                          #update_marks&grade
        try:
            while True:
                rec=pickle.load(F)
                if rec[1]==r:
                    rec[9]=float(input("Enter new Marks"))
                    rec[10]=input("Enter new Grade")
                    found=True
                pickle.dump(rec,F2)
                    
        except Exception:
            if found==True:
                print("Record Updated Successfully…\n")
            else:
                print("Record Not Found…\n")

    else:
        try:
            while True:
                rec=pickle.load(F)
                pickle.dump(rec,F2)

        except Exception:
            pass
    
    F.close()
    F2.close()
    os.remove("sturec.dat")
    os.rename("new.dat","sturec.dat")

    
        
def delete_record():
    F=open("sturec.dat","rb")
    F1=open("rec.dat","wb")

    try:
        r=int(input("Enter Rno of student Whose record is to be deleted"))
    except ValueError:
        print("Invalid Input\n")
        
    c=0
    
    try:
        while True:
            rec=pickle.load(F)
            if rec[1]!=r:
                pickle.dump(rec,F1)
                c+=1
    except Exception:
        if c==0:
            print("Failed to delete Student Record\n")
        else:
            print("Record Deleted Successfully\n")
                
    F.close()
    F1.close()
    os.remove("sturec.dat")
    os.rename("rec.dat","sturec.dat")


#user_functions
    
def search_details():
    
    F=open("sturec.dat","rb")
   
        
    #Search_Student_Details_on_the_basis_of_rno_entered
    #by_end_user
    try:
        while True:
            rec=pickle.load(F)
            stat=None
            if ((rec[9])/500)>=(0.45):
                stat="Passed"
            else:
                stat="Failed"
            if rec[1]==r:
                print("Here are your details:")
                print("Admiss.No\tR.No.\tF.Name\tL.Name\tGen\tDateOfBirth\tCl\tSec\tStream\t\tStatus")
                print(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],
                rec[7],rec[8],stat,sep="\t")
                break
    except Exception:
        print("Student Details not found...\n")

    F.close()

def show_marks():
    F=open("sturec.dat","rb")

        
    #Show_Student_Marks_on_the_basis_of_rno_entered_ 
    #by_end_user
    per=0.0
    try:
        while True:
            rec=pickle.load(F)
            if rec[1]==r:
                print("Total Marks out of 500:",rec[9])
                per=(rec[9])*0.2 
                print("Percentage:",per)
                break
    except Exception:
        print("Student Details not found\n")

    F.close()


#admin_Interface
def admin():
    
    print('*'*38,end='')
    print(" WELCOME TO STUDENT MANAGEMENT ",end='')
    print('*'*38)

    print("_"*107)

    print(" "*45,end='')
    print("(Admin Interface)",end='')
    print(" "*45)

    while True:
        print("     ADMIN MENU")
        print("     -----------")
        print("1.Add student record")
        print("2.View student details")
        print("3.Show all Student Records")
        print("4.Search Student Record")
        print("5.Update student details")
        print("6.Delete student details")
        print("7.Exit")
        
        ch=0

        try:
            ch=int(input("Enter Your Choice..."))
        except ValueError:
            print("Invalid Input...\n")
        
        
        if ch==1:
            add_record()
            print('_'*107,'\n')

        elif ch==2:
            display_record()
            print('_'*107,'\n')

        elif ch==3:
            display_all_records()
            print('_'*107,'\n')

        elif ch==4:
            search_record()
            print('_'*107,'\n')

        elif ch==5:
            update_record()
            print('_'*107,'\n')

        elif ch==6:
            delete_record()
            print('_'*107,'\n')

        elif ch==7:
            print(' '*49,end='')
            print("EXITTING...",end='')
            print(' '*45,'\n')
            break


#student(user)_Interface
def user():
    print('*'*38,end='')
    print(" WELCOME TO STUDENT MANAGEMENT ",end='')
    print('*'*38)

    print("_"*107)

    print(" "*42,end='')
    print("(Student Interface)",end='')
    print(" "*42)

    
    while True:                                     #for_correct_input
        try:
            global r
            r=int(input("\nEnter Your Roll No."))
            if type(r)==int:
                pass
                
            rol=int(input("Confirm Student Roll No."))
            if rol==r:
                break
            else:
                print("\nRoll No. did not match\n")
        except ValueError:
            print("Invalid Input...\n")
            

    
    while True:
        print("\n      USER MENU")
        print("      ---------")
        print("1.Search your details")
        print("2.View your Marks and Percentage")
        print("3.Exit\n")

        ch=0

        try:
            ch=int(input("Enter Your Choice..."))
        except ValueError:
            print("Invalid Input...\n")
            
        if ch==1:
            search_details()
            print('_'*107,"\n")
            
        elif ch==2:
            show_marks()
            print('_'*107,"\n")
            
        elif ch==3:
            print(' '*49,end='')
            print("EXITTING...",end='')
            print(' '*45,"\n")
            break


def endmsg():
    print('*'*49,end='')
    print("THANK YOU",end='')
    print('*'*49)

    print('*'*107)

#asking-end-user-(admin-or-user)
print("ENTER End User:")
print("--------------")
print("1.Admin")
print("2.User\n")
choice=int(input("Enter Your Choice"))

if choice==1:
    admin()
    endmsg()
elif choice==2:
    user()
    endmsg()
else:
    print("Invalid Input")
#end_of_project
