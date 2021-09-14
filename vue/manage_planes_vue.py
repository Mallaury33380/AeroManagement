import  tkinter as tk 
from tkinter.filedialog import *
from PIL import ImageTk,Image
from tkinter.ttk	import *

from controller import controller_manage_planes_vue
from vue import manage_people_vue
from vue import manage_balance_vue
from vue import log_vue
    

class manage_planes_vue(tk.Frame):

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
        Button_plane=tk.Button(FrameOptions, text = 'Click Me !', image = img_plane)
        Button_plane.image = img_plane
        Button_plane.grid(sticky=tk.NW+tk.S)
        
        # Button person
        Button_person=tk.Button(FrameOptions, text = 'Click Me !', image = img_person,command=lambda: master.switch_frame(manage_people_vue.manage_people_vue))
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
        
        
        
        #New plane
        NewPlane = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)
        
        self.valueNewMatricule = tk.StringVar() 
        self.valueNewMatricule.set("Immatriculation")
        self.entryMatricule = tk.Entry(NewPlane, textvariable=self.valueNewMatricule, width=20)
        
        self.valueNewModel = tk.StringVar() 
        self.valueNewModel.set("Model")
        self.entryModel = tk.Entry(NewPlane, textvariable=self.valueNewModel, width=20)
        
        self.valueNewYear = tk.IntVar()
        self.entryYear = tk.Spinbox(NewPlane, from_=1900,to=3000, width=10,textvariable=self.valueNewYear)
        
        self.valueNewHours = tk.IntVar()
        self.entryHours = tk.Spinbox(NewPlane, from_=0,to=100000, width=10,textvariable=self.valueNewHours)
        
        self.valueNewPrice = tk.IntVar()
        self.entryPrice = tk.Spinbox(NewPlane, from_=0,to=10000, width=10,textvariable=self.valueNewPrice)
        
        self.varEntryOverhaul = tk.IntVar()
        self.entryOverhaul = tk.Checkbutton(NewPlane, text="Overhaul?", variable=self.varEntryOverhaul)
        
        self.varEntryFlying = tk.IntVar()
        self.entryFlying = tk.Checkbutton(NewPlane, text="Flying?", variable=self.varEntryFlying)
        
        self.filepath = ''
        
        Button_Picture=tk.Button(NewPlane, text = 'Choose picture', command=self.get_Picture)
        
        Button_Validate=tk.Button(NewPlane, text = 'Validate', command=self.validate_new_plane)
        
        NewPlane.add(tk.Label(NewPlane, text='New plane:',  anchor=tk.CENTER, width=20))
        NewPlane.add(self.entryMatricule)
        NewPlane.add(self.entryModel)
        NewPlane.add(tk.Label(NewPlane, text='Year:',  anchor=tk.CENTER))
        NewPlane.add(self.entryYear)
        NewPlane.add(tk.Label(NewPlane, text='Hours:',  anchor=tk.CENTER))
        NewPlane.add(self.entryHours)
        NewPlane.add(tk.Label(NewPlane, text='Price:',  anchor=tk.CENTER))
        NewPlane.add(self.entryPrice)
        NewPlane.add(self.entryOverhaul)
        NewPlane.add(self.entryFlying)
        NewPlane.add(Button_Picture)
        NewPlane.add(Button_Validate)
        NewPlane.pack()
        
        
        
        #Modify plane
        ModifyPlane = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)
        
        self.valueMatricule = tk.StringVar() 
        self.valueMatricule.set("Immatriculation")
        self.entryMatricule = tk.Entry(ModifyPlane, textvariable=self.valueMatricule, width=20)
        
        self.valueModel = tk.StringVar() 
        self.valueModel.set("Model")
        self.entryModel = tk.Entry(ModifyPlane, textvariable=self.valueModel, width=20)
        
        self.entryYear = tk.Spinbox(ModifyPlane, from_=1900,to=3000, width=10)
        
        self.entryHours = tk.Spinbox(ModifyPlane, from_=0,to=100000, width=10)
        
        self.entryPrice = tk.Spinbox(ModifyPlane, from_=0,to=10000, width=10)
        
        self.varEntryOverhaul = tk.IntVar()
        self.entryOverhaul = tk.Checkbutton(ModifyPlane, text="Overhaul?", variable=self.varEntryOverhaul)
        
        self.varEntryFlying = tk.IntVar()
        self.entryFlying = tk.Checkbutton(ModifyPlane, text="Flying?", variable=self.varEntryFlying)
        
        
        Button_Picture=tk.Button(ModifyPlane, text = 'Choose picture', command=self.get_Picture)
        
        Button_Validate=tk.Button(ModifyPlane, text = 'Modify', command=self.modify_plane)
        
        
        ModifyPlane.add(tk.Label(ModifyPlane, text='Modify plane:',  anchor=tk.CENTER, width=20))
        ModifyPlane.add(self.entryMatricule)
        ModifyPlane.add(self.entryModel)
        ModifyPlane.add(tk.Label(ModifyPlane, text='Year:',  anchor=tk.CENTER))
        ModifyPlane.add(self.entryYear)
        ModifyPlane.add(tk.Label(ModifyPlane, text='Hours:',  anchor=tk.CENTER))
        ModifyPlane.add(self.entryHours)
        ModifyPlane.add(tk.Label(ModifyPlane, text='Price:',  anchor=tk.CENTER))
        ModifyPlane.add(self.entryPrice)
        ModifyPlane.add(self.entryOverhaul)
        ModifyPlane.add(self.entryFlying)
        ModifyPlane.add(Button_Picture)
        ModifyPlane.add(Button_Validate)
        ModifyPlane.pack()
        
        
        #Delete plane
        DeletePlane = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)
        
        self.valueDeleteMatricule = tk.StringVar() 
        self.valueDeleteMatricule.set("Immatriculation")
        self.entryDeleteMatricule = tk.Entry(DeletePlane, textvariable=self.valueDeleteMatricule, width=20)
        
        
        Button_Delete=tk.Button(DeletePlane, text = 'Delete', command=self.delete_plane)
        
        
        DeletePlane.add(tk.Label(DeletePlane, text='Delete plane:',  anchor=tk.CENTER, width=20))
        DeletePlane.add(self.entryDeleteMatricule)
        DeletePlane.add(Button_Delete)
        DeletePlane.pack(anchor=tk.W)
        
        #Canvas for picture
        self.my_img=ImageTk.PhotoImage(Image.open("./res/logo_wait_picture_plane.png"))
        self.my_label= tk.Label(FramePrincipal,image=self.my_img, borderwidth=2, relief="solid",height=200,width=200)
        self.my_label.image = self.my_img
        self.my_label.pack()
        
        
        
        #Show plane
        ShowPlane = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)
        
        self.planeSelect= tk.StringVar()
        self.allPlanes=self.build_list_plane()
        self.listPlanes= Combobox(ShowPlane,textvariable=self.planeSelect, values=self.allPlanes, state='readonly')
        #self.listPlanes.current(0)
        
        self.plane_string_info= tk.StringVar()
        self.plane_string_info=""
        self.plane_info = tk.Label(ShowPlane, text=self.plane_string_info,borderwidth=2, relief="solid",width=80,anchor=tk.W )
        
        Button_Select=tk.Button(ShowPlane, text = 'See', command=self.select_plane)
        
        
        ShowPlane.add(tk.Label(ShowPlane, text='See a plane:',  anchor=tk.CENTER, width=20))
        ShowPlane.add(self.listPlanes)
        ShowPlane.add(Button_Select)
        ShowPlane.add(self.plane_info)
        ShowPlane.pack(anchor=tk.W)
        
        self.plane_img=ImageTk.PhotoImage(Image.open("./res/logo_wait_picture_plane.png"))
        self.plane_label= tk.Label(FramePrincipal,image=self.plane_img, borderwidth=2, relief="solid",height=200,width=200)
        self.plane_label.image = self.plane_img
        self.plane_label.pack(anchor=tk.CENTER)
        
        
        
        
    #Get a picture for a new plane
    def get_Picture(self):
        #ask path of the picture
        self.filepath=askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
        #save it and display it in the canva
        if self.filepath!='':
            self.my_img2=ImageTk.PhotoImage(Image.open(controller_manage_planes_vue.transform_Picture("temp/tempory_picture",self.filepath)))
            self.my_label.configure(image=self.my_img2)
            self.my_label.image=self.my_img2
        
    #create a new plane
    def validate_new_plane(self):
        controller_manage_planes_vue.controllEntries(self.valueNewMatricule.get(),self.valueNewModel.get(),self.valueNewYear.get(),self.valueNewHours.get(),self.valueNewPrice.get(),self.varEntryOverhaul.get(),self.filepath,self.varEntryFlying.get())
        self.allPlanes=self.build_list_plane()
        self.listPlanes.configure(values=self.allPlanes)
        
    #Modify a plane
    def modify_plane(self):
        controller_manage_planes_vue.modifyPlane(self.valueMatricule.get(),self.valueModel.get(),self.entryYear.get(),self.entryHours.get(),self.entryPrice.get(),self.varEntryOverhaul.get(),self.filepath,self.varEntryFlying.get())
        self.allPlanes=self.build_list_plane()
        self.listPlanes.configure(values=self.allPlanes)
      
    #delete a plane
    def delete_plane(self):
        controller_manage_planes_vue.delete_plane(self.valueDeleteMatricule.get())
        self.allPlanes=self.build_list_plane()
        self.listPlanes.configure(values=self.allPlanes)
     
    #Build the list of all the plane
    def build_list_plane(self):
        return controller_manage_planes_vue.build_list()
    
    #Choose a plane to display
    def select_plane(self):
        if self.planeSelect.get()!='':
            L=controller_manage_planes_vue.get_plane_info(self.planeSelect.get())
            self.plane_string_info=""
        
            self.plane_string_info="Model: "+L[1]+"  Year:"+str(L[2])+"  Hours:"+str(L[3])+"h  Price:"+str(L[4])+"€  "
        
            self.plane_info.configure(text=self.plane_string_info)
        
            self.plane_img=ImageTk.PhotoImage(Image.open(L[7]))
            self.plane_label.configure(image=self.plane_img)
            self.plane_label.image=self.plane_img
        
        return
        
        
        
    