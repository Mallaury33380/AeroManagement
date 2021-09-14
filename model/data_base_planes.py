import mysql.connector

#Check if the database exists. If it does not exist it creates it.
def check_DB_exists():
    
    #Try to connect to the server
    try:
        connexion=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            )   
    except Exception as e:
        print (e)
        connexion.close()

    #Create a cursor
    connexion_curseur=connexion.cursor()
    
    #Looking for if the DB has already been created
    existante=False
    #If the connection is set
    if (connexion.is_connected()):
        #Looking for the DB
        connexion_curseur.execute("SHOW DATABASES")
        for x in connexion_curseur:
            if(x==('projetlogiciel',)):
                existante=True
    else:
        print("Connexion lost")
    
    #If the DB is not created
    if(existante==False):
        #If the connection is set
        if (connexion.is_connected()):
            #Create the DB
            try:
                connexion_curseur.execute("CREATE DATABASE projetLogiciel")
                connexion.connect(
                                    database='projetlogiciel'
                                    )       
            except Exception as e:
                print (e)
        else:
            print("Connexion lost")
    
        #Create tables
        if (connexion.is_connected()):
            try:
                connexion_curseur.execute("CREATE TABLE `projetlogiciel`.`people` ( `Name` VARCHAR(100) NOT NULL , `Surname` VARCHAR(100) NOT NULL , `Address` VARCHAR(100) NOT NULL , `Balance` FLOAT NOT NULL, `Username` VARCHAR(100), `Password` VARCHAR(100) , `Admin` BOOLEAN NOT NULL, `Picture` VARCHAR(100) NOT NULL)")
                connexion_curseur.execute("CREATE TABLE `projetlogiciel`.`planes` ( `Immatriculation` VARCHAR(100) NOT NULL , `Model` VARCHAR(100) NOT NULL , `Year` INT NOT NULL , `Hours` FLOAT NOT NULL ,`Price` INT NOT NULL,`Flying` BOOLEAN NOT NULL , `Overhaul` BOOLEAN NOT NULL , `Picture` VARCHAR(100) NOT NULL )")
                connexion_curseur.execute("CREATE TABLE `projetlogiciel`.`deposit` ( `Username` VARCHAR(100) NOT NULL , `Money` FLOAT NOT NULL,`Date` DATE NOT NULL)")
                connexion_curseur.execute("CREATE TABLE `projetlogiciel`.`Overhaul` ( `Plane` VARCHAR(100) NOT NULL , `Money` FLOAT NOT NULL)")
                connexion_curseur.execute("CREATE TABLE `projetlogiciel`.`Flights` ( `Plane` VARCHAR(100) NOT NULL ,`Username` VARCHAR(100) NOT NULL , `Price` FLOAT NOT NULL, `Time` INT NOT NULL, `Date` DATE NOT NULL)")
                connexion_curseur.execute("CREATE TABLE `projetlogiciel`.`Flying` ( `Plane` VARCHAR(100) NOT NULL ,`Username` VARCHAR(100) NOT NULL)")
                #Create first admin account
                connexion_curseur.execute("INSERT INTO `people` (`Name`, `Surname`, `Address`, `Balance`, `Username`, `Password`, `Admin`, `Picture`) VALUES ('Admin', 'Admin', 'Admin', '0', 'Login', 'Password', '1','./res/logo_wait_picture_person.png')")
                #Create account impossible to reach used as name for deleted members into the tables flights and deposits
                connexion_curseur.execute("INSERT INTO `people` (`Name`, `Surname`, `Address`, `Balance`, `Username`, `Password`, `Admin`, `Picture`) VALUES ('Admin', 'Admin', 'Admin', '0', 'Delete', '', '1','./res/logo_wait_picture_person.png')")
            except Exception as e:
                print (e)
        else:
            print("Connexion lost")
            
            
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

#Verify if the credentials are correct
def credentials_corrects(login,password):
    connection=creationConnection()

    #Creation a cursor
    connection_curseur=connection.cursor()
    
    #Get the password of the account
    if (connection.is_connected()):
        try:
            sql = "SELECT Password FROM people WHERE Username = %s"
            val = (login,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
            
            #if len=0 the account does not exist
            if (len(results)==0):
                return 0
            else:
                #if it exists, it tests the equality between the two passwords
                if password==results[0][0]:
                    return 1
                else:
                    return 0
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    
    return 0
    
#Check if a plane has already this name
def immatriculaton_not_exists(Immatriculation):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT Immatriculation FROM planes WHERE Immatriculation = %s"
            val = (Immatriculation,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
            
            #if len=0 no plane has this name
            if (len(results)==0):
                return 1
            else:
                return 0
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    
    return 0

#Insert a new plane into the data base
def insert_new_plane(Immatriculation,Model,Year,Hours,Price,Overhaul,Picture,Flying):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "INSERT INTO `planes` (`Immatriculation`, `Model`, `Year`, `Hours`, `Price`, `Flying`, `Overhaul`, `Picture`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (Immatriculation,Model,Year,Hours,Price,Flying,Overhaul,Picture)
            connection_curseur.execute(sql, val)
            connection.commit()
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    
    return 0

#Modify a plane which is in the data base
def modify_plane(Immatriculation,Model,Year,Hours,Price,Overhaul,Picture,Flying):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "UPDATE planes SET Model=%s, Year=%s, Hours=%s, Price=%s, Flying=%s, Overhaul=%s WHERE Immatriculation=%s"
            val = (Model,Year,Hours,Price,Flying,Overhaul,Immatriculation)
            connection_curseur.execute(sql, val)
            connection.commit()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    
    return

#Delete a plane which is in the data base
def delete_plane(Immatriculation):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "DELETE FROM planes WHERE Immatriculation=%s"
            val = (Immatriculation,)
            connection_curseur.execute(sql, val)
            connection.commit()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    
#Get the name of all planes
def select_all_immatriculation():
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    L=list()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT Immatriculation FROM planes ORDER BY Immatriculation"
            connection_curseur.execute(sql)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    #create a list of all the names
    if len(results)!=0:
        for i in results:
            L.append(i[0])
    return L

#Get all the information about a plane
def get_plane_info(plane):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT * FROM planes WHERE Immatriculation = %s"
            val = (plane,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
            
    return results[0]


#Create a overhaul for a plane
def overhaul(Plane,Money):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "INSERT INTO `overhaul` (`Plane`, `Money`) VALUES (%s,%s)"
            val = (Plane,Money,)
            connection_curseur.execute(sql, val)
            connection.commit()
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    return


#get all the informations on flights done by members
def pdf_flights():
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT * FROM flights"
            connection_curseur.execute(sql)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
            
    return results

#get the sum of all the flights
def pdf_sum_flights():
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT SUM(Price) FROM flights"
            connection_curseur.execute(sql)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
            
    return str(results[0][0])

#get all the informations on overhauls
def pdf_overhauls():
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT * FROM overhaul"
            connection_curseur.execute(sql)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
            
    return results

#get the sum of all the overhauls
def pdf_sum_overhauls():
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT SUM(Money) FROM overhaul"
            connection_curseur.execute(sql)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
            
    return str(results[0][0])

#Check if a plane is flying
def not_flying(Plane):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT Plane FROM flying WHERE Plane = %s"
            val = (Plane,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
           
    return len(results)


#Add the name of a the member who wants to use a plane
def rent_plane(Username,plane):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "INSERT INTO `flying` (`Plane`, `Username`) VALUES (%s,%s)"
            val = (plane,Username,)
            connection_curseur.execute(sql, val)
            connection.commit()
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    
    return 


# Get the hourly price of a plane
def plane_price(Plane):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT Price FROM planes WHERE Immatriculation = %s"
            val = (Plane,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    
    return results[0][0]

# Return a plane after a flight
def return_plane(Plane,Username):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "DELETE FROM flying WHERE Plane=%s AND Username=%s"
            val = (Plane,Username,)
            connection_curseur.execute(sql, val)
            connection.commit()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    return

# Get all the flights of a member
def get_flights(Username):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT * FROM flights WHERE Username = %s ORDER BY Date"
            val = (Username,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    return results

# Get the flight time of a plane
def get_Fligt_time(Plane):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "SELECT Hours FROM planes WHERE Immatriculation = %s"
            val = (Plane,)
            connection_curseur.execute(sql, val)
            results=connection_curseur.fetchall()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    
    return results[0][0]

# Change the flight time of a plane
def change_Flight_time(Plane,time):
    connection=creationConnection()

    #Creation cursor
    connection_curseur=connection.cursor()
    
    if (connection.is_connected()):
        try:
            sql = "UPDATE planes SET Hours=%s WHERE Immatriculation=%s"
            val = (time,Plane,)
            connection_curseur.execute(sql, val)
            connection.commit()
                    
        except Exception as e:
            print (e)
    else:
        print("Connection lost")
    
    return