import contact

print("Welcome")

print("1. Add Contact")
print("2. View Contact")
print("3. Search Contact")
print("4. Exit")

choice=int(input("Enter your Choice(1/2/3/4): "))

if choice==1:
    contact.add_contact()

elif choice==2:
    contact.view_contact()

elif choice==3:
    contact.search_contact()

elif choice==4:
    contact.exit()            

else:
    print("Invalid Choice")
