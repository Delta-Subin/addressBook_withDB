
import mysql.connector

# Establishing a connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="******",
    database="delta")


# Creating a cursor to execute SQL queries
mycursor = mydb.cursor()

# Creating a table for the address book if it doesn't exist
mycursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), email VARCHAR(255), phone VARCHAR(20))")





#making an address book with name, emailid and conatct number


class AddressBook:
    def __init__(self):
      self.ContactName = ""
      self.emailID = ""
      self.ContactNo = ""
      
#Adding new conatct details 

    def NewcontactDetails(self):
     self.ContactName = input("Enter Your Name: " )
     self.emailID = input("Enter Emailid: ")
     self.ContactNo = int(input("Enter you Ph No: "))   
     
    # Inserting the new contact into the MySQL database
     sql = "INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)"
     val = (self.ContactName, self.emailID, self.ContactNo)
     mycursor.execute(sql, val)
     mydb.commit()    


#Display Conatct Number
    def Displayaddress(self):
        print("Conatct Name: ", self.ContactName)
        print("Email ID: ", self.emailID)
        print("Conatct No: ", self.ContactNo)
        
  
  #tuple because i want the data to be unchanged      
Contact_DB = list([])

# selection option

select = "Yes" 

#for continuse looping 
while select == "Yes":
    print("1. Add New contact Details" "\n"
      "2. Show Contacts")
     
    response = int(input("Enter Your Choice: "))
 
#contact as same as class
#new contact adding 
    if(response== 1):
         Contact = AddressBook()
         Contact.NewcontactDetails()
         Contact_DB.append(Contact)

#displaying the saved data       
    elif (response== 2):
        for x in Contact_DB:
            x.Displayaddress()

#for wrong input         
    else:
       print("Please Check your response")
    
       select = input("press Yes to continue")       
         
# Closing the MySQL connection

mycursor.close()
mydb.close()