import  tkinter as tk 
from tkinter.filedialog import *
from PIL import ImageTk,Image
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from datetime import date

from vue import take_plane_vue
from vue import log_vue
from controller import controller_people_information_vue

#Username of the user
Username=''
        
class people_information_vue(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        
        #def Username next page
        people_information_vue.Username=Username
        
        #Menu Options admin
        FrameOptions = tk.Frame(self, borderwidth=2, relief=tk.GROOVE)
        FrameOptions.grid(column=0, row=0, sticky=tk.NW+tk.S)
                
        # Creating a photoimage object to use image 
        img_take_plane=ImageTk.PhotoImage(Image.open("./res/take_plane.png"))
        img_information=ImageTk.PhotoImage(Image.open("./res/information.png"))
        img_exit=ImageTk.PhotoImage(Image.open("./res/logo_exit.png"))
                                                                 
        # Button take plane
        Button_plane=tk.Button(FrameOptions, text = 'Click Me !', image = img_take_plane,command=lambda: master.switch_frame(take_plane_vue.take_plane_vue))
        Button_plane.image = img_take_plane
        Button_plane.grid(sticky=tk.NW+tk.S)
        
        # Button account information
        Button_person=tk.Button(FrameOptions, text = 'Click Me !', image = img_information)
        Button_person.image = img_information
        Button_person.grid(sticky=tk.NW+tk.S)
        
        
        # Button exit
        Button_exit=tk.Button(FrameOptions, text = 'Click Me !', image = img_exit,command=lambda: master.switch_frame(log_vue.log_vue))
        Button_exit.image = img_exit
        Button_exit.grid(sticky=tk.NW+tk.S)
        
        
        
        #Main Frame
        FramePrincipal = tk.Frame(self, borderwidth=2, relief=tk.GROOVE)
        FramePrincipal.grid(column=1, row=0,  sticky=tk.NE)
        
        
        
        #Pilot logbook
        Pilot_Logbook = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)
        
        Button_filepath=tk.Button(Pilot_Logbook, text = 'Choose directory', command=lambda: self.get_Path(0), width=20)
        
        self.string_filepath= tk.StringVar()
        self.string_filepath=""
        self.label_filepath = tk.Label(Pilot_Logbook, text=self.string_filepath,borderwidth=2, relief="solid",width=50,anchor=tk.W )
        
        Button_Logbook=tk.Button(Pilot_Logbook, text = 'Pilot logbook', command=self.create_pilot_logbook)
        
        Pilot_Logbook.add(tk.Label(Pilot_Logbook, text='Create pilot logbook:',  anchor=tk.CENTER, width=20))
        Pilot_Logbook.add(Button_filepath)
        Pilot_Logbook.add(self.label_filepath)
        Pilot_Logbook.add(Button_Logbook)
        Pilot_Logbook.pack()
        
        
        
        #Account_balance
        Account_balance = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)
        
        Button_filepath2=tk.Button(Account_balance, text = 'Choose directory', command=lambda: self.get_Path(1), width=20)
        
        self.string_filepath2= tk.StringVar()
        self.string_filepath2=""
        self.label_filepath2 = tk.Label(Account_balance, text=self.string_filepath2,borderwidth=2, relief="solid",width=50,anchor=tk.W )
        
        Button_Balance=tk.Button(Account_balance, text = 'Account balance', command=self.create_account_balance)
        
        Account_balance.add(tk.Label(Account_balance, text='Create account balance:',  anchor=tk.CENTER, width=22))
        Account_balance.add(Button_filepath2)
        Account_balance.add(self.label_filepath2)
        Account_balance.add(Button_Balance)
        Account_balance.pack()
    
    
    #Create the logbook of the user
    def create_pilot_logbook(self):
        if(self.string_filepath!=''):
            today = date.today()
            d1 = today.strftime("%d_%m_%Y")
            link=self.string_filepath+"/Pilot_Logbook_"+d1+".pdf"
            
            pdf = canvas.Canvas(link)
            
            pdf.setFont('Helvetica', 20)
            pdf.drawString(5*cm, 25*cm, u'Pilot logbook: '+Username)
            pdf.line(3*cm,24.5*cm,18*cm,24.5*cm)
            
            pdf=controller_people_information_vue.fill_pilot_logbook(pdf,Username)
            controller_people_information_vue.info_Logbook_created()
            pdf.save()
        
        return
    
    #Create the account balance of a user
    def create_account_balance(self):
        if(self.string_filepath2!=''):
            today = date.today()
            d1 = today.strftime("%d_%m_%Y")
            link=self.string_filepath2+"/Account_balance_"+d1+".pdf"
            
            pdf = canvas.Canvas(link)
            
            pdf.setFont('Helvetica', 20)
            pdf.drawString(5*cm, 25*cm, u'Account balance: '+Username)
            pdf.line(3*cm,24.5*cm,18*cm,24.5*cm)
            
            pdf=controller_people_information_vue.fill_account_balance(pdf,Username)
            pdf.save()
        return
    
    #ask path to save the pdf
    def get_Path(self,number):
        if number==0:
            self.string_filepath=askdirectory()
            self.label_filepath.configure(text=self.string_filepath)
        elif number==1:
            self.string_filepath2=askdirectory()
            self.label_filepath2.configure(text=self.string_filepath2)
        
        return