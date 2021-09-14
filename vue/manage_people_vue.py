import  tkinter as tk 
from tkinter.filedialog import *
from PIL import ImageTk,Image
from tkinter.ttk	import *
from vue import manage_planes_vue
from vue import manage_balance_vue
from controller import controller_manage_people_vue
from vue import log_vue

class manage_people_vue(tk.Frame):

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
        Button_person=tk.Button(FrameOptions, text = 'Click Me !', image = img_person)
        Button_person.image = img_person
        Button_person.grid(sticky=tk.NW+tk.S)
        
        # Button bilan
        Button_bilan=tk.Button(FrameOptions, text = 'Click Me !', image = img_bilan,command=lambda: master.switch_frame(manage_balance_vue.manage_balance_vue))
        Button_bilan.image = img_bilan
        Button_bilan.grid(sticky=tk.NW+tk.S)
        
        # Button exit
        Button_exit=tk.Button(FrameOptions, text = 'Click Me !', image = img_exit,command=lambda: master.switch_frame(log_vue.log_vue))
        Button_exit.image = img_exit
        Button_exit.grid(sticky=tk.NW+tk.S)
        
        
        
        
        #Main Frame
        FramePrincipal = tk.Frame(self, borderwidth=2, relief=tk.GROOVE)
        FramePrincipal.grid(column=1, row=0,  sticky=tk.NE)


        #New person
        NewPerson = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)

        self.valueName = tk.StringVar() 
        self.valueName.set("Name")
        self.entryName = tk.Entry(NewPerson, textvariable=self.valueName, width=20)
        
        self.valueSurname = tk.StringVar() 
        self.valueSurname.set("Surname")
        self.entrySurname = tk.Entry(NewPerson, textvariable=self.valueSurname, width=20)
        
        self.valueAddress = tk.StringVar() 
        self.valueAddress.set("Address")
        self.entryAddress = tk.Entry(NewPerson, textvariable=self.valueAddress, width=20)
        
        self.valueBalance = tk.IntVar()
        self.entryBalance = tk.Spinbox(NewPerson, from_=0,to=10000, width=10,textvariable=self.valueBalance)
        
        self.valueUsername = tk.StringVar() 
        self.valueUsername.set("Username")
        self.entryUsername = tk.Entry(NewPerson, textvariable=self.valueUsername, width=20)
        
        self.valuePassword = tk.StringVar() 
        self.valuePassword.set("Password")
        self.entryPassword = tk.Entry(NewPerson, textvariable=self.valuePassword, width=20)
        
        self.varAdmin = tk.IntVar()
        self.entryAdmin = tk.Checkbutton(NewPerson, text="Admin?", variable=self.varAdmin)
        
        self.filepath = ''
        
        Button_Picture=tk.Button(NewPerson, text = 'Choose picture', command=self.get_Picture)
        
        Button_Validate=tk.Button(NewPerson, text = 'Validate', command=self.validate_new_person)

        NewPerson.add(tk.Label(NewPerson, text='New person:',  anchor=tk.CENTER, width=20))
        NewPerson.add(self.entryName)
        NewPerson.add(self.entrySurname)
        NewPerson.add(self.entryAddress)
        NewPerson.add(tk.Label(NewPerson, text='Contribution:',  anchor=tk.CENTER))
        NewPerson.add(self.entryBalance)
        NewPerson.add(self.entryUsername)
        NewPerson.add(self.entryPassword)
        NewPerson.add(self.entryAdmin)
        NewPerson.add(Button_Picture)
        NewPerson.add(Button_Validate)
        NewPerson.pack()
        
        #Modify person
        ModifyPerson = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)

        self.valueModifyName = tk.StringVar() 
        self.valueModifyName.set("Name")
        self.entryModifyName = tk.Entry(ModifyPerson, textvariable=self.valueModifyName, width=20)
        
        self.valueModifySurname = tk.StringVar() 
        self.valueModifySurname.set("Surname")
        self.entryModifySurname = tk.Entry(ModifyPerson, textvariable=self.valueModifySurname, width=20)
        
        self.valueModifyAddress = tk.StringVar() 
        self.valueModifyAddress.set("Address")
        self.entryModifyAddress = tk.Entry(ModifyPerson, textvariable=self.valueModifyAddress, width=20)
        
        self.valueModifyBalance = tk.IntVar()
        self.entryModifyBalance = tk.Spinbox(ModifyPerson, from_=0,to=10000, width=10,textvariable=self.valueModifyBalance)
        
        self.valueModifyUsername = tk.StringVar() 
        self.valueModifyUsername.set("Username")
        self.entryModifyUsername = tk.Entry(ModifyPerson, textvariable=self.valueModifyUsername, width=20)
        
        self.valueModifyPassword = tk.StringVar() 
        self.valueModifyPassword.set("Password")
        self.entryModifyPassword = tk.Entry(ModifyPerson, textvariable=self.valueModifyPassword, width=20)
        
        self.varModifyAdmin = tk.IntVar()
        self.entryModifyAdmin = tk.Checkbutton(ModifyPerson, text="Admin?", variable=self.varModifyAdmin)
        
        self.filepath = ''
        
        Button_ModifyPicture=tk.Button(ModifyPerson, text = 'Choose picture', command=self.get_Picture)
        
        Button_ModifyValidate=tk.Button(ModifyPerson, text = 'Modify', command=self.modify_person)

        ModifyPerson.add(tk.Label(ModifyPerson, text='Modify person:',  anchor=tk.CENTER, width=20))
        ModifyPerson.add(self.entryModifyName)
        ModifyPerson.add(self.entryModifySurname)
        ModifyPerson.add(self.entryModifyAddress)
        ModifyPerson.add(tk.Label(ModifyPerson, text='Contribution:',  anchor=tk.CENTER))
        ModifyPerson.add(self.entryModifyBalance)
        ModifyPerson.add(self.entryModifyUsername)
        ModifyPerson.add(self.entryModifyPassword)
        ModifyPerson.add(self.entryModifyAdmin)
        ModifyPerson.add(Button_ModifyPicture)
        ModifyPerson.add(Button_ModifyValidate)
        ModifyPerson.pack()

        
        #Delete person
        DeletePerson = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)

        
        self.valueDeleteUsername = tk.StringVar() 
        self.valueDeleteUsername.set("Username")
        self.entryDeleteUsername = tk.Entry(DeletePerson, textvariable=self.valueDeleteUsername, width=20)
        
        Button_DeleteValidate=tk.Button(DeletePerson, text = 'Delete', command=self.delete_person)

        DeletePerson.add(tk.Label(DeletePerson, text='Delete person:',  anchor=tk.CENTER, width=20))
        DeletePerson.add(self.entryDeleteUsername)
        DeletePerson.add(Button_DeleteValidate)
        DeletePerson.pack()

        #Canvas for picture
        self.my_img=ImageTk.PhotoImage(Image.open("./res/logo_wait_picture_person.png"))
        self.my_label= tk.Label(FramePrincipal,image=self.my_img, borderwidth=2, relief="solid",height=200,width=200)
        self.my_label.image = self.my_img
        self.my_label.pack()




        #Show people
        ShowPeople = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)
        
        self.personSelect= tk.StringVar()
        self.allPeople=self.build_list_people()
        self.listPeople= Combobox(ShowPeople,textvariable=self.personSelect, values=self.allPeople, state='readonly')
        
        self.person_string_info= tk.StringVar()
        self.person_string_info=""
        self.person_info = tk.Label(ShowPeople, text=self.person_string_info,borderwidth=2, relief="solid",width=100,anchor=tk.W )
        
        Button_Select=tk.Button(ShowPeople, text = 'See', command=self.select_person)
        
        
        ShowPeople.add(tk.Label(ShowPeople, text='See a member:',  anchor=tk.CENTER, width=20))
        ShowPeople.add(self.listPeople)
        ShowPeople.add(Button_Select)
        ShowPeople.add(self.person_info)
        ShowPeople.pack(anchor=tk.W)
        
        self.person_img=ImageTk.PhotoImage(Image.open("./res/logo_wait_picture_person.png"))
        self.person_label= tk.Label(FramePrincipal,image=self.person_img, borderwidth=2, relief="solid",height=200,width=200)
        self.person_label.image = self.person_img
        self.person_label.pack(anchor=tk.CENTER)





    #Pick a picture for a new member
    def get_Picture(self):
        #ask the path of the picture 
        self.filepath=askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
        
        #save the picture
        if self.filepath!='':
            self.my_img2=ImageTk.PhotoImage(Image.open(controller_manage_people_vue.transform_Picture("temp/tempory_picture",self.filepath)))
            self.my_label.configure(image=self.my_img2)
            self.my_label.image=self.my_img2
        
    #create a new member        
    def validate_new_person(self):
        controller_manage_people_vue.controllEntries(self.valueName.get(),self.valueSurname.get(),self.valueAddress.get(),self.valueBalance.get(),self.valueUsername.get(),self.valuePassword.get(),self.varAdmin.get(),self.filepath)
        self.allPeople=self.build_list_people()
        self.listPeople.configure(values=self.allPeople)
        return
    
    #modify a member
    def modify_person(self):
        controller_manage_people_vue.modifyPerson(self.valueModifyName.get(),self.valueModifySurname.get(),self.valueModifyAddress.get(),self.valueModifyBalance.get(),self.valueModifyUsername.get(),self.valueModifyPassword.get(),self.varModifyAdmin.get(),self.filepath)
        self.allPeople=self.build_list_people()
        self.listPeople.configure(values=self.allPeople)
        return
    
    #delete a member
    def delete_person(self):
        controller_manage_people_vue.delete_person(self.valueModifyUsername.get())
        self.allPeople=self.build_list_people()
        self.listPeople.configure(values=self.allPeople)
        return

    #build list of all member
    def build_list_people(self):
        return controller_manage_people_vue.build_list()

    #select a member to display in the canva
    def select_person(self):
        if self.personSelect.get()!='':
            L=controller_manage_people_vue.get_person_info(self.personSelect.get())
            
            self.person_string_info=''
            self.person_string_info="Name:"+L[0]+" Surname:"+L[1]+" Address:"+L[2]+" Password:"+L[5]+" Admin:"
            if L[6]==1:
                self.person_string_info=self.person_string_info+"Yes"
            else:
                self.person_string_info=self.person_string_info+"No"
                
            self.person_info.configure(text=self.person_string_info)
            
            self.person_img=ImageTk.PhotoImage(Image.open(L[7]))
            self.person_label.configure(image=self.person_img)
            self.person_label.image=self.person_img
        return




