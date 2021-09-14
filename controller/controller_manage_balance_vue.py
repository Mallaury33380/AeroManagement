from tkinter import messagebox
from model import data_base_people
from model import data_base_planes

from reportlab.lib.units import cm

# Check values of inputs and credit the accout of the member
def money_person(Username,Money):
    if len(Username)==0 or Money==0:
        messagebox.showinfo('Add money', 'Incomplete')
        return
    if(data_base_people.person_not_exists(Username)==1):
        messagebox.showinfo('Add money', 'This Username does not exist')
        return
    data_base_people.deposit(Username,Money)
    messagebox.showinfo('Add money', 'Deposit done')
    return

# Check values of inputs and create a overhaul for a plane
def money_overhaul(Plane,Money):
    if len(Plane)==0 or Money==0:
        messagebox.showinfo('Add overhaul', 'Incomplete')
        return
    if(data_base_planes.immatriculaton_not_exists(Plane)==1):
        messagebox.showinfo('Add overhaul', 'This plane does not exist')
        return
    data_base_planes.overhaul(Plane,Money)
    messagebox.showinfo('Add overhaul', 'Overhaul added')
    return

# Create the financial report in pdf
def fill_pdf(pdf):
    #Change the font, write the tithe and a line
    pdf.setFont('Helvetica', 20)
    pdf.drawString(5*cm, 25*cm, u'Financial report')
    pdf.line(3*cm,24.5*cm,18*cm,24.5*cm)
    
    #Variable to store the differents sums
    a=[21.5,0,0,0]
    
    #deposits
    pdf=fill_pdf_deposits(pdf,a)
    #Flights
    pdf=fill_pdf_flights(pdf,a)
    #overhauls
    pdf=fill_pdf_overhauls(pdf,a)
    #total
    pdf=fill_pdf_total(pdf,a)
    #End message
    messagebox.showinfo('Financial report', 'Created')
    return pdf

# fill the financial report with the deposits part
def fill_pdf_deposits(pdf,a):
    #Change the font, write the tithe
    pdf.setFont('Helvetica', 16)
    pdf.drawString(3*cm, 23*cm, u'Deposits')
    
    #Get all the information on deposits
    L=data_base_people.pdf_deposits()
    
    #Change the font and write all the deposits
    pdf.setFont('Helvetica', 12)
    for i in L:
        String='M/Mmme: '+i[0]+' '+str(i[1])+'€'
        pdf.drawString(3*cm, a[0]*cm, u''+String+'')
        #go on the next line
        a[0]=a[0]-1.5
        
        #If it is the end of the page, change the page
        if(a[0]<3):
            pdf.showPage()
            a[0]=25
    
    #Write a line
    pdf.line(3*cm,a[0]*cm,18*cm,a[0]*cm)
    a[0]=a[0]-1.5
    
    #If it is the end of the page, change the page
    if(a[0]<3):
        pdf.showPage()
        a[0]=25
    
    #Change the font 
    pdf.setFont('Helvetica', 16)
    #get the sum of the deposits
    L=data_base_people.pdf_sum_deposits()
    if(L=='None'):
        L=0
    a[1]=L    
    #Write the sum of deposits
    pdf.drawString(10*cm, a[0]*cm, u'Sum of deposits: '+str( round(float(L), 2) )+' €')
    a[0]=a[0]-1.5
    
    #If it is the end of the page, change the page
    if(a[0]<3):
        pdf.showPage()
        a[0]=25
    #Write a line
    pdf.line(3*cm,a[0]*cm,18*cm,a[0]*cm)
    a[0]=a[0]-1.5
    #If it is the end of the page, change the page
    if(a[0]<3):
        pdf.showPage()
        a[0]=25
    
    return pdf

# fill the financial report with the flights part
def fill_pdf_flights(pdf,a):
    #Change the font, write the tithe
    pdf.showPage()
    pdf.setFont('Helvetica', 16)
    pdf.drawString(3*cm, 23*cm, u'Flights')
    a[0]=21.5
    
    #Get all the information on flights
    L=data_base_planes.pdf_flights()
    
    #Change the font and write all the flights
    pdf.setFont('Helvetica', 12)
    for i in L:
        String='M/Mmme: '+i[1]+' '+str(i[2])+'€'+' Plane: '+i[0]
        pdf.drawString(3*cm, a[0]*cm, u''+String+'')
        #go on the next line
        a[0]=a[0]-1.5
        #If it is the end of the page, change the page
        if(a[0]<3):
            pdf.showPage()
            a[0]=25
    
    #Write a line
    pdf.line(3*cm,a[0]*cm,18*cm,a[0]*cm)
    a[0]=a[0]-1.5
    #If it is the end of the page, change the page
    if(a[0]<3):
        pdf.showPage()
        a[0]=25
    #Change the font
    pdf.setFont('Helvetica', 16)
    L=data_base_planes.pdf_sum_flights()
    if(L=='None'):
        L=0
    a[2]=L    
    pdf.drawString(10*cm, a[0]*cm, u'Sum of flights: '+str( round(float(L), 2) )+' €')
    a[0]=a[0]-1.5

    if(a[0]<3):
        pdf.showPage()
        a[0]=25
    
    pdf.line(3*cm,a[0]*cm,18*cm,a[0]*cm)
    a[0]=a[0]-1.5
    
    if(a[0]<3):
        pdf.showPage()
        a[0]=25
    
    return pdf

# fill the financial report with the overhauls part
def fill_pdf_overhauls(pdf,a):
    #Change the font, write the title
    pdf.showPage()
    pdf.setFont('Helvetica', 16)
    pdf.drawString(3*cm, 23*cm, u'Overhauls')
    a[0]=21.5
    
    L=data_base_planes.pdf_overhauls()
    
    pdf.setFont('Helvetica', 12)
    for i in L:
        String='Plane: '+i[0]+' '+str(i[1])+'€'
        pdf.drawString(3*cm, a[0]*cm, u''+String+'')
        #go on the next line
        a[0]=a[0]-1.5

        if(a[0]<3):
            pdf.showPage()
            a[0]=25
    
    
    pdf.line(3*cm,a[0]*cm,18*cm,a[0]*cm)
    a[0]=a[0]-1.5
    
    if(a[0]<3):
        pdf.showPage()
        a[0]=25
    
    pdf.setFont('Helvetica', 16)
    L=data_base_planes.pdf_sum_overhauls()
    if(L=='None'):
        L=0
    a[3]=L    
    pdf.drawString(10*cm, a[0]*cm, u'Sum of overhauls: '+str( round((float(L)), 2) )+' €')
    a[0]=a[0]-1.5

    if(a[0]<3):
        pdf.showPage()
        a[0]=25
    
    pdf.line(3*cm,a[0]*cm,18*cm,a[0]*cm)
    a[0]=a[0]-1.5
    
    if(a[0]<3):
        pdf.showPage()
        a[0]=25
    
    return pdf


# fill the financial report with the final part:total sum
def fill_pdf_total(pdf,a):
    String=str( round(float(a[1])-float(a[2])-float(a[3]), 2) )
    pdf.drawString(12*cm, a[0]*cm, u'Total:'+String+' €')
    return pdf


