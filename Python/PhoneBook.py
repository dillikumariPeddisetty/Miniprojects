class Contacts:
    def addContact(self):
        Name = input("Enter Contact Name : ")
        Number = input("Enter Contact Number : ")
        f = open("contact.txt","a")
        f.write(Name+" : "+Number+"\n")
        f.close()
    def SearchContact(self):
        Details = input("Enter Name or Number to Search : ")
        f = open("contact.txt","r")
        for data in f.readlines():
            if Details in data:
                print(data)
                break
        else:
            print("No contact Found")
            self.SearchContact()
        f.close()
    def DeleteContact(self):
        Details= input("Enter contact Name or NUmber to delete : ")
        f = open("contact.txt","r")
        res = f.readlines()
        for data in res:
            if Details in data:
               res.remove(data)
        f.close()
        f=open("contact.txt","w")
        f.writelines(res)
        f.close()
    def UpdateContact(self):
        u_con=input("Enter Either name or number:")
        f=open("contact.txt","r")
        lis=f.readlines()
        for data in range(len(lis)):
            if u_con in list[data]:
                new_name=input("Enter the name:")
                new_num=input("Enter the number:")
                list[data]=new_name+":" +new_num+"\n"
                break
                print("No Contact Found")
        f.close()
        f=open("contact.txt","w")
        f.writelines(lis)
        f.close()
#main code
Book=Contacts()
print("Press 1 to add contact \n Press 2 to search contact \n Press 3 to update contact \n press 4 to delete contact \n press 0 to exit \n press 5 to display all contacts")
X=True
while X:
   num=input("Press a number:")
   if num=='1':
      Book.addContact()
   if num=='2':
      Book.SearchContact()
   if num=='3':
      Book.UpdateContact()
   if num=='4':
      Book.DeleteContact()
   if num=='0':
      X=False
   else:
      print("INVALID OPTION")

   


