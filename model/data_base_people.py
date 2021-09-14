import mysql.connector
from datetime import date

#Create a connection object used to access to the database
def creationConnection():
    #Try to connect to the server
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            )   
    except Exception as e:
        print (e)
        connection.close()
        
    try:
            connection.connect(
            database='projetlogiciel'
            )
    except Exception as e:
            print (e)
    return connection

    
#Check if the Username is already used
def person_not_exists(Username):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT Username FROM people WHERE Username = %s"
            val = (Username,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
            
            if (len(results)==0):
                return 1
            else:
                return 0
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    
    return 0


# Insert a new member into the database
def insert_new_person(Name,Surname,Address,Balance,Username,Password,Admin,Picture):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "INSERT INTO `people` (`Name`, `Surname`, `Address`, `Balance`, `Username`, `Password`, `Admin`, `Picture`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (Name,Surname,Address,Balance,Username,Password,Admin,Picture,)
            connection_curseur.execute(sql, val)
            connection.commit()
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    
    return 0

# Modify a member who is into the database
def modify_person(Name,Surname,Address,Balance,Username,Password,Admin,Picture):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "UPDATE people SET Name=%s, Surname=%s, Address=%s, Balance=%s, Password=%s, Admin=%s, Picture=%s WHERE Username=%s"
            val = (Name,Surname,Address,Balance,Password,Admin,Picture,Username,)
            connection_curseur.execute(sql, val)
            connection.commit()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")

# Delete a member of the database
def delete_person(Username):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "DELETE FROM people WHERE Username=%s"
            val = (Username,)
            connection_curseur.execute(sql, val)
            connection.commit()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
   
#Select all the members     
def select_people():
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    L=list()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT Username FROM people ORDER BY Username"
            connection_curseur.execute(sql)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    #Create a list of all the members
    if len(results)!=0:
        for i in results:
            L.append(i[0])
    return L

#Get all the information about a member
def get_person_info(Username):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT * FROM people WHERE Username = %s"
            val = (Username,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
            
    return results[0]

#Add a new deposit into the database
def deposit(Username,Money):
    connection=creationConnection()
    

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "INSERT INTO `deposit` (`Username`, `Money`, `Date`) VALUES (%s,%s,%s)"
            val = (Username,Money,date.today(),)
            connection_curseur.execute(sql, val)
            connection.commit()
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    return

#Get all the inforamtions on all the deposits
def pdf_deposits():
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT * FROM deposit"
            connection_curseur.execute(sql)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
            
    return results

#Get the sum of all the deposits
def pdf_sum_deposits():
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT SUM(Money) FROM deposit"
            connection_curseur.execute(sql)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    return str(results[0][0])

# Check if the member is an admin
def admin(Username):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT Admin FROM people WHERE Username = %s"
            val = (Username,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    
    if str(results)!=0:
        return (results[0][0]) 
    else:
        return -1
            
#Check if a member is renting a plane
def not_flying(Username):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT Username FROM flying WHERE Username = %s"
            val = (Username,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
           
    return len(results)


#Check if the member is renting the plane
def user_using_this_plane(Username,plane):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT Username FROM flying WHERE Username = %s AND Plane= %s"
            val = (Username,plane,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
           
    return len(results)

# Pay the rental
def pay(Plane,Username,Price,time):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "INSERT INTO `flights` (`Plane`, `Username`, `Price`, `Time`, `Date`) VALUES (%s,%s,%s,%s,%s)"
            val = (Plane,Username,Price,time,date.today(),)
            connection_curseur.execute(sql, val)
            connection.commit()
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
        
    return


# Get the initial contribution of a member
def initial_contribution(Username):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT Balance FROM people WHERE Username = %s"
            val = (Username,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
            
    return str(results[0][0])


# Get all the deposits done by a member
def write_deposits_User(Username):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT * FROM deposit WHERE Username = %s"
            val = (Username,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
            
    return results


    #Delete the flights of the members
def delete_member_flights(Username):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "UPDATE flights SET Username='Delete' WHERE Username=%s"
            val = (Username,)
            connection_curseur.execute(sql, val)
            connection.commit()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    return

    #Delete the deposits of a member
def delete_member_deposits(Username):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "UPDATE deposit SET Username='Delete' WHERE Username=%s"
            val = (Username,)
            connection_curseur.execute(sql, val)
            connection.commit()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    return






