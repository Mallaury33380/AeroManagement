from tkinter import messagebox
import  tkinter as tk 
from model import data_base_planes
from PIL import Image
from PIL import ImageTk
import os

#Controll the inputs
def controllEntries(Immatriculation,Model,Year,Hours,Price,Overhaul,Picture,Flying):
    if len(Immatriculation)==0 or len(Model)==0 or len(Picture)==0:
        messagebox.showinfo('New Plane', 'Incomplete')
        return
    if(data_base_planes.immatriculaton_not_exists(Immatriculation)==0):
        messagebox.showinfo('New Plane', 'This plane already exists')
        return
    Picture=transform_Picture(Immatriculation,Picture)
    data_base_planes.insert_new_plane(Immatriculation,Model,Year,Hours,Price,Overhaul,Picture,Flying)
    messagebox.showinfo('New Plane', 'The plane has been created')
    return

#Transform a picture into the corrects dimensions
def transform_Picture(Immatriculation,Picture):
    link='./res/planes/'+Immatriculation+'.png'
    
    x = 200 # largeur
    y = 200 # hauteur
    Image.img = Image.open(Picture, 'r').resize((x,y)).save(link)
    return link

#Modify a plane into the data base
def modifyPlane(Immatriculation,Model,Year,Hours,Price,Overhaul,Picture,Flying):
    if len(Immatriculation)==0 or len(Model)==0 or len(Picture)==0:
        messagebox.showinfo('New Plane', 'Incomplete')
        return
    if(data_base_planes.immatriculaton_not_exists(Immatriculation)==1):
        messagebox.showinfo('New Plane', 'This plane does not exist')
        return
    Picture=transform_Picture(Immatriculation,Picture)
    data_base_planes.modify_plane(Immatriculation,Model,Year,Hours,Price,Overhaul,Picture,Flying)
    messagebox.showinfo('New Plane', 'The plane has been modified')
    return    

#Delete a plane of the data base
def delete_plane(Immatriculation):
    if len(Immatriculation)==0:
        messagebox.showinfo('New Plane', 'Incomplete')
        return
    if(data_base_planes.immatriculaton_not_exists(Immatriculation)==1):
        messagebox.showinfo('New Plane', 'This plane does not exist')
        return
    data_base_planes.delete_plane(Immatriculation)
    delete_picture(Immatriculation)
    messagebox.showinfo('New Plane', 'The plane has been deleted')
    return

#delete a picture of the planes repository 
def delete_picture(Immatriculation):
    link='./res/planes/'+Immatriculation+'.png'
    
    if os.path.exists(link):
        os.remove(link)
    else:
        print("No picture")
    return

#buils the list of all the planes
def build_list():
    return data_base_planes.select_all_immatriculation()

#get information about a plane
def get_plane_info(plane):
    return data_base_planes.get_plane_info(plane)

