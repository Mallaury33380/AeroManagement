from tkinter import messagebox

from model import data_base_planes
from model import data_base_people

#Ceck if the member can rent a plane
def is_possible(Username,Plane):
    if Plane=='':
        messagebox.showinfo('Rent a plane', 'Choose a plane')
        return 0
        
    if data_base_planes.not_flying(Plane)==0:
        if data_base_people.not_flying(Username)==0:
            return 1
        else:
            messagebox.showinfo('Rent a plane', Username+' has already a rental')
            return 0
    else:
        messagebox.showinfo('Rent a plane', Plane+' is already flying')
        return 0

#The member rent a plane
def rent_plane(Username,plane):
    data_base_planes.rent_plane(Username,plane)
    messagebox.showinfo('Rent a plane', 'You are renting '+plane)
    return

#Calculate the prize of the rental
def calculatePrice(Plane,time):
    if Plane=='':
        messagebox.showinfo('Return a plane', 'Select a plane')
        return 0
    
    if time>0 and time< 1000000:
        var_Price=data_base_planes.plane_price(Plane)*time/60
        return "%.2f" %var_Price
    
    return 0
    
#Check if the member is renting this plane
def user_using_this_plane(Username,plane):
    if data_base_people.user_using_this_plane(Username,plane):
        return 1
    messagebox.showinfo('Return a plane', 'You didn''t rent this plane')
    return 0

#Return a plane and calcualte the price of the rental
def return_plane(Username,Plane,time):
    #Insert in flights
    data_base_people.pay(Plane,Username,calculatePrice(Plane,time),time)
    
    #Change the flight time of the aircraft
    change_Flight_time(Plane,time)
    
    #return plane
    data_base_planes.return_plane(Plane,Username)
    
    messagebox.showinfo('Return a plane', 'You have returned '+Plane)
    
    return

# Change the flight time of a plane
def change_Flight_time(Plane,time):
    data_base_planes.change_Flight_time(Plane,time/60 + (data_base_planes.get_Fligt_time(Plane)) )
    return