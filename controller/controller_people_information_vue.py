from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from tkinter import messagebox

from model import data_base_planes
from model import data_base_people

#Create the logbook of a member
def fill_pilot_logbook(pdf,Username):
    #Flights
    a=[21.5,0,0,0]
    
    #Change font
    pdf.setFont('Helvetica', 16)
    pdf.drawString(3*cm, 23*cm, u'Flights')
    
    #Get the flights of a member
    L=data_base_planes.get_flights(Username)
    
    #change font
    pdf.setFont('Helvetica', 12)
    #Write all the flights
    for i in L:
        String=str(i[4])+'   Plane: '+i[0]+'  for: '+str(int(i[3]/60))+'h '+str(i[3]%60)+'min  '+' costed: '+str(i[2])+' €'
        pdf.drawString(3*cm, a[0]*cm, u''+String+'')
        #Change line
        a[0]=a[0]-1.5
        
        a[1]+=1
        a[2]+=i[2]
        a[3]+=i[3]
        
        # Goto the next page if it is hte end of the current page
        if(a[0]<3):
            pdf.showPage()
            a[0]=25
    
    # Goto the next page if it is hte end of the current page
    if(a[0]<10):
        pdf.showPage()
        a[0]=25
    #draw a line
    pdf.line(3*cm,a[0]*cm,18*cm,a[0]*cm)
    #change line
    a[0]=a[0]-1.5
    
    #Write the total
    pdf.drawString(10*cm, a[0]*cm, u'Total: '+ str( round(a[1], 2) )+' flights  '+str(int(a[3]/60))+'h '+str(a[3]%60)+'min  '+str( round(a[2]) )+' €')
    return pdf

#Inform the user that the logbook has been created
def info_Logbook_created():
    messagebox.showinfo('Pilot logbook', 'Created')    
    return

#Inform the user that the Account balance_ has been created
def info_Balance_created():
    messagebox.showinfo('Account_balance_', 'Created')    
    return

#Creta the account balance of a member
def fill_account_balance(pdf,Username):
    # Write the Initial contribution
    pdf=initial_contribution(pdf,Username)
    #change page
    pdf.showPage()
    # Write the flights
    pdf=fill_pilot_logbook(pdf,Username)
    #change page
    pdf.showPage()
    # Write the deposits
    pdf=write_deposits_User(pdf,Username)
    #change page
    pdf.showPage()
    # Write the total
    pdf=total_balance(pdf,Username)    
    #Inform the user that the Account balance_ has been created
    info_Balance_created()
    
    return pdf


#Write the initial contribution
def initial_contribution(pdf,Username):
    
    #Initial contribution
    a=[21.5,0,0,0]
    #Get all the flights of a member
    L=data_base_people.initial_contribution(Username)
    #Change font
    pdf.setFont('Helvetica', 16)
    #Write contribution
    String='Initial contribution: '+str(L)
    pdf.drawString(3*cm, a[0]*cm, u''+String+'')
        
    return pdf

#Write the deposits of a member into the account balance
def write_deposits_User(pdf,Username):
    
    #Flights
    a=[21.5,0,0,0]
    #Change font
    pdf.setFont('Helvetica', 16)
    pdf.drawString(3*cm, 23*cm, u'Deposits')
    
    #Gets deposits of a member
    L=data_base_people.pdf_deposits()
    
    #Write deposits
    pdf.setFont('Helvetica', 12)
    for i in L:
        String=str(i[2])+' '+str(i[1])+'€'
        pdf.drawString(3*cm, a[0]*cm, u''+String+'')
        a[0]=a[0]-1.5
        # Goto the next page if it is hte end of the current page
        if(a[0]<3):
            pdf.showPage()
            a[0]=25
    
    
    pdf.line(3*cm,a[0]*cm,18*cm,a[0]*cm)
    a[0]=a[0]-1.5
    # Goto the next page if it is hte end of the current page
    if(a[0]<3):
        pdf.showPage()
        a[0]=25
    
    pdf.setFont('Helvetica', 16)
    L=data_base_people.pdf_sum_deposits()
    if(L=='None'):
        L=0
    a[1]=L    
    #Write the sum of the deposits
    pdf.drawString(10*cm, a[0]*cm, u'Sum of deposits: '+str(L)+' €')
    a[0]=a[0]-1.5
    # Goto the next page if it is hte end of the current page
    if(a[0]<3):
        pdf.showPage()
        a[0]=25
    #Draw line
    pdf.line(3*cm,a[0]*cm,18*cm,a[0]*cm)
    a[0]=a[0]-1.5
    # Goto the next page if it is hte end of the current page
    if(a[0]<3):
        pdf.showPage()
        a[0]=25
    
    return pdf


#Write the total balance
def total_balance(pdf,Username):
    #Get initial contribution
    initial_contribution=data_base_people.initial_contribution(Username)
    
    #get sum of deposits
    total_deposits=0.0
    deposits=data_base_people.pdf_deposits()
    for i in deposits:
        total_deposits=total_deposits+i[1]
    
    #get prize of all the flights
    total_flights=0.0
    flights=data_base_planes.get_flights(Username)
    for i in flights:
        total_flights=total_flights+i[2]
    
    #Write the total
    pdf.setFont('Helvetica', 18)
    pdf.drawString(10*cm, 23*cm, u'Total balance: '+str( round( float(initial_contribution) -total_flights+total_deposits, 2)) +' €')
    
    return pdf

