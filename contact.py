print("Welcome to your Contact Book")

def add_contact():
    f=open(r"C:\Users\kastu\OneDrive\Desktop\python\Contact Book\contact.txt","a")
    Name=input("Your Name:")
    Age=input("Your Age:")
    Number=input("Your Number:")
    Address=input("Your Address:")
    f.write(Name+","+Age+","+Number+","+Address+"\n")
    f.close()

def view_contact():
     f = open(r"C:\Users\kastu\OneDrive\Desktop\python\Contact Book\contact.txt", "r")
     print("The Reserved Contact")
     print("........................")
     print("Name  Age  Number  Address")

     empty=True
     for line in f:
         print(line)
         empty=False

     if empty:
         print("Contact is not listed")

     f.close()     

         
def search_contact():
    Name=input("Enter name to search:")
    f=open(r"C:\Users\kastu\OneDrive\Desktop\python\Contact Book\contact.txt","r")
    found=False

    for line in f:
        if Name in line:
           print("Contact Found")
           print("Name Age Number Address")
           print(line)
           found=True
           break

    if not found:
       print("Contact Not listed")

    f.close()

def exit():
    print("Thanyou For Using Our Contact Book!")

     

    
