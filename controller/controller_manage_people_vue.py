from PIL import Image
from tkinter import messagebox
from model import data_base_people
import os

#Transform a picture into the corrects dimensions
def transform_Picture(Username,Picture):
    link='./res/people/'+Username+'.png'
    
    x = 200 # largeur
    y = 200 # hauteur
    Image.img = Image.open(Picture, 'r').resize((x,y)).save(link)
    
    return link

#Controll the inputs
def controllEntries(Name,Surname,Address,Balance,Username,Password,Admin,Picture):
    if len(Name)==0 or len(Surname)==0 or len(Address)==0 or len(Username)==0 or len(Password)==0 or len(Picture)==0:
        messagebox.showinfo('New Person', 'Incomplete')
        return
    if(data_base_people.person_not_exists(Username)==0):
        messagebox.showinfo('New Person', 'This Username already exists')
        return
    
    Picture=transform_Picture(Username,Picture)
    data_base_people.insert_new_person(Name,Surname,Address,Balance,Username,Password,Admin,Picture)
    messagebox.showinfo('New Person', 'The person has been created')
    return

#Modify a member into the data base
def modifyPerson(Name,Surname,Address,Balance,Username,Password,Admin,Picture):
    if len(Name)==0 or len(Surname)==0 or len(Address)==0 or len(Username)==0 or len(Password)==0 or len(Picture)==0:
        messagebox.showinfo('Modify Person', 'Incomplete')
        return
    if(data_base_people.person_not_exists(Username)==1):
        messagebox.showinfo('Modify Person', 'This Username does not exist')
        return
    Picture=transform_Picture(Username,Picture)
    data_base_people.modify_person(Name,Surname,Address,Balance,Username,Password,Admin,Picture)
    messagebox.showinfo('Modify Person', 'The username has been modified')
    return

#Delete a member of the data base
def delete_person(Username):
    if len(Username)==0:
        messagebox.showinfo('Delete Person', 'Incomplete')
        return
    if(data_base_people.person_not_exists(Username)==1):
        messagebox.showinfo('Delete Person', 'This person does not exist')
        return
    data_base_people.delete_person(Username)
    delete_picture(Username)
    
    #Delete the flights of the members
    data_base_people.delete_member_flights(Username)
    #Delete the deposits of a member
    data_base_people.delete_member_deposits(Username)
    
    messagebox.showinfo('Delete Person', 'The person has been deleted')
    return

#Delete a picture of the repository people
def delete_picture(Username):
    link='./res/people/'+Username+'.png'
    
    if os.path.exists(link):
        os.remove(link)
    else:
        print("No picture")
    return

#Create a list of all the members
def build_list():
    return data_base_people.select_people()

#Get all the information on a member
def get_person_info(Username):
    return data_base_people.get_person_info(Username)