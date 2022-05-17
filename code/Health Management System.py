#!/usr/bin/env python
# coding: utf-8

# # Health Management System

# In[ ]:


# type your name here


# In[ ]:


## type your id


# In[ ]:


###type your section etc also


# **Display all Patient Record**

# In[277]:


import re
#This method will displays all the Patients’ information recorded
def getAllPatientRecord(): 
    try:# try catch for any exception like file does not exit
        print("==========================================================================================================")
        file=open("C:\\Users\\Ahmad\\Desktop\\patient_record.txt","r") #open file given path with read mode
        list=file.readlines()#read data from the file and assign into the list which is actually list data sturture 
        file.close()#close file
        dic={}#create empyty dictionary 
        c=0 # for count
        for x in list:#x takes line1,line2 ,line2 ...etc from input file as loop progresses
            y=re.split(r'\s{2,}', x)# to break down a bigger string into several smaller strings
            dic[c]=y# after splict assign into dictionary
            c+=1 # here incress value 1 by 1 with loop
        for k, i in dic.items():# print in tabular form
            pid, pname, weight,aweight,visit = i
            print ("{:<20} {:<25} {:<20} {:<20} {:<20}".format( pid, pname, weight,aweight,visit))
            
        temp=input("Press Enter key to continue...")#AS per project requrment can't start before pressing any key  
        print("==========================================================================================================")
   
    except IOError:
                 print("\nFile Not Found\n") #if have any exception then print 


# **Display the Record of a particular Patient**

# In[278]:


'''This methid will searches PatientID in the text-file. If the Patient is
found then show all information about person otherwise will 
show appropriate error message is displayed'''
import re
def getPatient(patientID):
      
    try: # try catch for any exception like file does not exit
        print("==========================================================================================================")
        file=open("C:\\Users\\Ahmad\\Desktop\\patient_record.txt","r") #open file given path with read mode
        list=file.readlines()#read data from the file and assign into the list which is actually list data sturture 
        file.close()#close file
        fc=-1
        dic={}#create empyty dictionary 
        for x in list: #x takes line1,line2 ,line2 ...etc from input file as loop progresses
            if x!=list[0]:#check x not equal to list zero index
                z=re.split(r'\s{2,}', list[0]) # to break down a bigger string into several smaller strings
                y=re.split(r'\s{2,}', x) # to break down a bigger string into several smaller strings
                if int(y[0])==patientID: # here match id one by one
                    #print(y[0])
                    #print(y)
                    dic[1]=z # after splict assign into dictionary
                    dic[2]=y # here also after splict assign into dictionary
                    #print(y)
                    for k, i in dic.items():# print in tabular form
                        pid, pname, weight,aweight,visit = i
                        print ("{:<20} {:<25} {:<20} {:<20} {:<20}".format( pid, pname, weight,aweight,visit)) # for display
                        print(dic[2])
                        fc=1
                        break
                    if fc==-1:
                        print("\nError: Invalid Patient\n") # if patient is not found
        
        
        
        temp=input("Press Enter key to continue...")#AS per project requrment can't start before pressing any key  
        print("==========================================================================================================")
    except IOError:  #if have any exception then print 
                        print("\nFile Not Found\n")
            


   


# **Display all Patient Weight**

# In[279]:


'''This method will be prompts and reads a maximum weight from the user. Then it displays all patients with weight less
than or equal to the given weight.'''
import re
def  getWeight(weight):
   
    try:   # try catch for any exception like file does not exit
      print("==========================================================================================================")
      file=open("C:\\Users\\Ahmad\\Desktop\\patient_record.txt","r") #open file given path with read mode
      list1=file.readlines()#read data from the file and assign into the list1 which is actually list data sturture 
      file.close()#close file
      dic={}#create empyty dictionary 
      c=1 #create varibale with iniliztion value is for create keys for dictionary 
      list2=re.split(r'\s{2,}', list1[0])#list2 which contains column data form line 1 of input file 
      list2.insert(4,"P(%)")  # insert 5 th column
      dic[0]=list2 #element in dictionary which contains the headings to print
      for x in list1: #x takes line1,line2 ,line2 ...etc from input file as loop progresses
          if x!=list1[0]: #to skip line1 as it only contains headings
              y=re.split(r'\s{2,}', x)#y is also contains data from input file
              if float(y[2])<=float(weight):
                  p=((float(y[2])-float(y[3]))/float(y[3]))*100  ##P = (weight – average weight) / (average weight) x 100 
                  m=y #copy data into y
                  m.insert(4,p) # insert 5 column value
                  dic[c]=m  #element in dictionary for output
                  c+=1
      for k, i in dic.items():# print in tabular form
                      pid, pname, weight,aweight,pw,visit = i
                      print ("{:<20} {:<25} {:<20} {:<20}{:<15}{:<30}".format( pid, pname, weight,aweight,pw,visit))
            
     
      temp=input("Press Enter key to continue...")#AS per project requrment can't start before pressing any key  
      print("==========================================================================================================")
                    
    except IOError:  #if have any exception then print 
                      print("\nFile Not Found\n")
            


# **Update Patient**

# In[280]:


#this function update take two perameter from user(patientID, weight) and update recorde of patient
def update(patientID,weight):
     print("==========================================================================================================")
     weight=float(input("Please Enter average weight(Kg):"))# here print on promate for user
     number=int(input("Please Enter the patients number of visits:"))# here also print on promate for user
     aweight=(weight+weight*number)/(number+1) # calculation as per requrment Avg. weight = (weight + avg. weight * visit) / (visit + 1)
     visits=number+1
     if weight>0:
         try:# try catch for any exception like file does not exit
             file=open("C:\\Users\\Ahmad\\Desktop\\patient_record.txt","r+") #open file given path with write mode
             list=file.readlines()#read data from the file and assign into the list1 which is actually list data sturture
             c=-1
             for i in range(1,len(list)): #loop
                 x=re.split(r'\s{2,}', list[i])
                 #print(x) # for testing perpose 
                 if int(x[0])==patientID: # here match id one by one
                     new=x[0]+"\t"+x[1]+"\t"+str(weight)+"\t"+str(aweight)+"\t"+str(visits)+"\n"
                     c=i
                 else:
                     print("Error : Invalid Patient ID")
                     temp=input("Press Enter key to continue...")
                     print("==========================================================================================================")
                     break
                 if c!=-1:
                     list[i]=new
                     file.writelines(list) #in write in flie 
                     file.close()
                     print("Patient's informaion has been updated...")
                     temp=input("Press Enter key to continue...")
                     print("==========================================================================================================")

         except IOError: #if have any exception then print 
                         print("\nFile Not Found\n")
                


# **Add New Patient**

# In[281]:


# this method will append the new record by serch patient id if Already exit then this method show error massage 
def addPatient(Name,patientID):
    try:
        print("==========================================================================================================")
        file=open("C:\\Users\\Ahmad\\Desktop\\patient_record.txt","w+") #open file given path with write mode
        list=file.readlines()#read data from the file and assign into the list1 which is actually list data sturture
        c=-1
        for i in range(1,len(list)):#loop
            x=re.split(r'\s{2,}', list[i]) # to break down a bigger string into several smaller strings
            if int(x[0])==patientID:# here match id one by one
                c=0
                break
        if c==-1:
                list.append(str(patientID)+"\t"+Name+"\n") # append person data
                file.writelines(list) # write in file
                print("successfully added new Patient")
                temp=input("Press Enter key to continue...")
                print("==========================================================================================================")
        else:
                print("Error, Patient Already exists") 
                file.close()             
                temp=input("Press Enter key to continue...")
                print("==========================================================================================================")
    except IOError:
            print("\nFile Not Found\n")


# **Delete Patient**

# In[282]:


# this search  method will match the PatientID  from text-file  the and deleted the patient if not serch then show error msg
def deletePatient(patientID):
    try:
        print("==========================================================================================================")
        file=open("C:\\Users\\Ahmad\\Desktop\\patient_record.txt","r+") #open file given path with write mode
        list=file.readlines()#read data from the file and assign into the list1 which is actually list data sturture
        c=-1
        for i in range(1,len(list)): #loop 
            x=re.split(r'\s{2,}', list[i])  # to break down a bigger string into several smaller strings
            if int(x[0])==patientID:# here match id one by one
                c=i
                break
        if c!=-1:
                list.remove(list[i])#remove 
                file.writelines(list)
                print("successfully remove Patient") 
                temp=input("Press Enter key to continue...")#AS per project requrment can't start before pressing any key  
                print("==========================================================================================================")
        else:
                print("Error, Patient does not exists")
                file.close()
                temp=input("Press Enter key to continue...")#AS per project requrment can't start before pressing any key  
                print("==========================================================================================================")
    except IOError:
                print("\nFile Not Found\n")
    

   


#  **Main Menu**

# In[283]:


#here is the main function in this function call all above function with loop 
def main():
    while True:
        print("1.Display all Patient Record")
        print("2.Display the Record of chose particular Patient")
        print("3.Display all Patient weight")
        print("4.Update Patient")
        print("5.Add New Patient")
        print("6.Delete Patient ")
        print("0.Exit")
        chose=int(input("Please select your choice :"))
        if chose==0:
            break
        elif chose==1:
            getAllPatientRecord() #call method getAllPatientRecord
        elif chose==2:
            pid=int(input("Please Enter Patient ID:"))
            getPatient(pid)#call method getPatient
        elif chose==3:
            w=int(input("Please enter max. weight(Kg):"))
            if w>0:
             getWeight(w)#call method getWeight
            else:
                print("Error: Invalid weight")
        elif chose==4:
            pid=float(input("Please Enter Patient ID:"))
            weg=float(input("Please Enter current weight(Kg):"))
            if weg>0:
                update(pid,weg)#call method update
            else:
                print("Error: Invalid weight")
        elif chose==5:
            n=input("Please Enter Name:")
            p=int(input("Please Enter Patient ID:"))
            addPatient(n,p)#call method addPatient
        elif chose==6:
            pid1=int(input("Please Enter PatientID:"))
            deletePatient(pid1)#call method deletePatient
        else:
         print("\nPlease Enter valid option\n")


# **Drive code**

# In[284]:


#Driver Code
main()


# In[ ]:





# In[ ]:




