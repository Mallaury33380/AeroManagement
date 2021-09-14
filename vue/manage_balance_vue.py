import  tkinter as tk 
from tkinter.filedialog import *
from PIL import ImageTk,Image

from vue import manage_planes_vue
from vue import manage_people_vue
from controller import controller_manage_balance_vue
from vue import log_vue

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import datetime

class manage_balance_vue(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        
        #Menu Options admin
        FrameOptions = tk.Frame(self, borderwidth=2, relief=tk.GROOVE)
        FrameOptions.grid(column=0, row=0, sticky=tk.NW+tk.S)
                
        # Creating a photoimage object to use image 
        img_plane=ImageTk.PhotoImage(Image.open("./res/logo_plane.png"))
        img_person=ImageTk.PhotoImage(Image.open("./res/logo_person.png"))
        img_bilan=ImageTk.PhotoImage(Image.open("./res/logo_bilan.png"))
        img_exit=ImageTk.PhotoImage(Image.open("./res/logo_exit.png"))
                                      
        # Button plane
        Button_plane=tk.Button(FrameOptions, text = 'Click Me !', image = img_plane,command=lambda: master.switch_frame(manage_planes_vue.manage_planes_vue))
        Button_plane.image = img_plane
        Button_plane.grid(sticky=tk.NW+tk.S)
        
        # Button person
        Button_person=tk.Button(FrameOptions, text = 'Click Me !', image = img_person,command=lambda: master.switch_frame(manage_people_vue.manage_people_vue))
        Button_person.image = img_person
        Button_person.grid(sticky=tk.NW+tk.S)
        
        # Button bilan
        Button_bilan=tk.Button(FrameOptions, text = 'Click Me !', image = img_bilan)
        Button_bilan.image = img_bilan
        Button_bilan.grid(sticky=tk.NW+tk.S)
        
        # Button exit
        Button_exit=tk.Button(FrameOptions, text = 'Click Me !', image = img_exit,command=lambda: master.switch_frame(log_vue.log_vue))
        Button_exit.image = img_exit
        Button_exit.grid(sticky=tk.NW+tk.S)
        
        
        
        #Main Frame
        FramePrincipal = tk.Frame(self, borderwidth=2, relief=tk.GROOVE)
        FramePrincipal.grid(column=1, row=0,  sticky=tk.NE)
        
        
        #Give money
        MoneyPerson = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)

        self.valueMoneyUsername = tk.StringVar() 
        self.valueMoneyUsername.set("Username")
        self.entryMoneyUsername = tk.Entry(MoneyPerson, textvariable=self.valueMoneyUsername, width=20)
        
        self.valueBalance = tk.IntVar()
        self.entryBalance = tk.Spinbox(MoneyPerson, from_=-10000,to=10000, width=10,textvariable=self.valueBalance)
        
        Button_MoneyValidate=tk.Button(MoneyPerson, text = 'Add money', command=self.money_person)

        MoneyPerson.add(tk.Label(MoneyPerson, text='Add money:',  anchor=tk.CENTER, width=20))
        MoneyPerson.add(self.entryMoneyUsername)
        MoneyPerson.add(self.entryBalance)
        MoneyPerson.add(Button_MoneyValidate)
        MoneyPerson.pack()
        
        
        #Money Overhaul
        MoneyOverhaul = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL, )

        self.valueMoneyPlane = tk.StringVar() 
        self.valueMoneyPlane.set("Immatriculation")
        self.entryMoneyPlane = tk.Entry(MoneyOverhaul, textvariable=self.valueMoneyPlane, width=20)
        
        self.valueMoneyOverhaul = tk.IntVar()
        self.entryMoneyOverhaul = tk.Spinbox(MoneyOverhaul, from_=-10000,to=10000, width=10,textvariable=self.valueMoneyOverhaul)
        
        Button_OverhaulValidate=tk.Button(MoneyOverhaul, text = 'Add money', command=self.money_overhaul)

        MoneyOverhaul.add(tk.Label(MoneyOverhaul, text='Money Overhaul:',  anchor=tk.CENTER, width=20))
        MoneyOverhaul.add(self.entryMoneyPlane)
        MoneyOverhaul.add(self.entryMoneyOverhaul)
        MoneyOverhaul.add(Button_OverhaulValidate)
        MoneyOverhaul.pack()
        
        #Financial statement
        Financial_statement = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)
        
        
        Button_filepath=tk.Button(Financial_statement, text = 'Choose directory', command=self.get_Path, width=20)
        
        self.string_filepath= tk.StringVar()
        self.string_filepath=""
        self.label_filepath = tk.Label(Financial_statement, text=self.string_filepath,borderwidth=2, relief="solid",width=50,anchor=tk.W )
        
        Button_Create=tk.Button(Financial_statement, text = 'Create financial statement', command=self.create_financial_statement)
        
        Financial_statement.add(tk.Label(Financial_statement, text='Financial statement:',  anchor=tk.CENTER, width=20))
        Financial_statement.add(Button_filepath)
        Financial_statement.add(self.label_filepath)
        Financial_statement.add(Button_Create)
        Financial_statement.pack()
        
    #Create a deposit for a member
    def money_person(self):
        controller_manage_balance_vue.money_person(self.valueMoneyUsername.get(),self.valueBalance.get())
        return
    
    #Create a overhaul for a plane
    def money_overhaul(self):
        controller_manage_balance_vue.money_overhaul(self.valueMoneyPlane.get(),self.valueMoneyOverhaul.get())
        return
      
    #ask path to save the financial statement
    def get_Path(self):
        self.string_filepath=askdirectory()
        self.label_filepath.configure(text=self.string_filepath)
        return
        
    #Create the financial statement
    def create_financial_statement(self):
        if(self.string_filepath!=''):
            today = datetime.date.today()
            d1 = today.strftime("%d_%m_%Y")
            link=self.string_filepath+"/Financial_Report_"+d1+".pdf"
            
            pdf = canvas.Canvas(link)
            pdf=controller_manage_balance_vue.fill_pdf(pdf)
            pdf.save()
            
        return
        
        
        
        