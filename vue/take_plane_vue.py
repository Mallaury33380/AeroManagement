import  tkinter as tk 
from tkinter.filedialog import *
from PIL import ImageTk,Image
from tkinter.ttk	import *



from vue import people_information_vue
from vue import log_vue
from controller import controller_manage_planes_vue
from controller import controller_take_plane_vue


#Username of the user
Username=''
        
class take_plane_vue(tk.Frame):

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
        Button_plane=tk.Button(FrameOptions, text = 'Click Me !', image = img_take_plane)
        Button_plane.image = img_take_plane
        Button_plane.grid(sticky=tk.NW+tk.S)
        
        # Button account information
        Button_person=tk.Button(FrameOptions, text = 'Click Me !', image = img_information,command=lambda: master.switch_frame(people_information_vue.people_information_vue))
        Button_person.image = img_information
        Button_person.grid(sticky=tk.NW+tk.S)
        
        
        # Button exit
        Button_exit=tk.Button(FrameOptions, text = 'Click Me !', image = img_exit,command=lambda: master.switch_frame(log_vue.log_vue))
        Button_exit.image = img_exit
        Button_exit.grid(sticky=tk.NW+tk.S)
        
        
        
        
        
        #Main Frame
        FramePrincipal = tk.Frame(self, borderwidth=2, relief=tk.GROOVE)
        FramePrincipal.grid(column=1, row=0,  sticky=tk.NE)
        
        
        
        
        
        #Rent a  plane
        RentPlane = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)
        
        self.planeSelect= tk.StringVar()
        self.allPlanes=self.build_list_plane()
        self.listPlanes= Combobox(RentPlane,textvariable=self.planeSelect, values=self.allPlanes, state='readonly')
        
        self.plane_string_info= tk.StringVar()
        self.plane_string_info=""
        self.plane_info = tk.Label(RentPlane, text=self.plane_string_info,borderwidth=2, relief="solid",width=80,anchor=tk.W )
        
        Button_Select=tk.Button(RentPlane, text = 'See information about the plane', command=self.select_plane)
        Button_Take=tk.Button(RentPlane, text = 'Rent this plane', command=self.take_plane)
        
        
        RentPlane.add(tk.Label(RentPlane, text='Rent a plane:',  anchor=tk.CENTER, width=20))
        RentPlane.add(self.listPlanes)
        RentPlane.add(self.plane_info)
        RentPlane.add(Button_Select)
        RentPlane.add(Button_Take)
        RentPlane.pack(anchor=tk.W)
        
        
        #Return a  plane
        ReturnPlane = tk.PanedWindow(FramePrincipal, orient=tk.HORIZONTAL)
        
        self.planeSelect2= tk.StringVar()
        self.allPlanes2=self.build_list_plane()
        self.listPlanes2= Combobox(ReturnPlane,textvariable=self.planeSelect2, values=self.allPlanes2, state='readonly')
        
        self.valueMinutes = tk.IntVar()
        self.entryMinutes = tk.Spinbox(ReturnPlane, from_=0,to=100000, width=10,textvariable=self.valueMinutes)
        
        self.plane_string_info2= tk.StringVar()
        self.plane_string_info2="0€"
        self.plane_info2 = tk.Label(ReturnPlane, text=self.plane_string_info2,borderwidth=2, relief="solid",width=66,anchor=tk.E )
        
        Button_Select2=tk.Button(ReturnPlane, text = 'Calculate the prize', command=self.calculatePrice)
        Button_Return=tk.Button(ReturnPlane, text = 'Pay the rental', command=self.pay_plane)
        
        
        ReturnPlane.add(tk.Label(ReturnPlane, text='Return a plane:',  anchor=tk.CENTER, width=20))
        ReturnPlane.add(self.listPlanes2)
        ReturnPlane.add(self.entryMinutes)
        ReturnPlane.add(self.plane_info2)
        ReturnPlane.add(Button_Select2)
        ReturnPlane.add(Button_Return)
        ReturnPlane.pack(anchor=tk.W)
        
        
        self.plane_img=ImageTk.PhotoImage(Image.open("./res/logo_wait_picture_plane.png"))
        self.plane_label= tk.Label(FramePrincipal,image=self.plane_img, borderwidth=2, relief="solid",height=200,width=200)
        self.plane_label.image = self.plane_img
        self.plane_label.pack(anchor=tk.CENTER)
        
        
    #Build the list of all planes in the data base
    def build_list_plane(self):
        return controller_manage_planes_vue.build_list()
    
    #Rent a plane
    def take_plane(self):            
        if controller_take_plane_vue.is_possible(Username,self.planeSelect.get()):
            controller_take_plane_vue.rent_plane(Username,self.planeSelect.get())
        return
    
    #Display information on a plane
    def select_plane(self):
        if self.planeSelect.get()!='':
            L=controller_manage_planes_vue.get_plane_info(self.planeSelect.get())
            self.plane_string_info=""
        
            self.plane_string_info="Model: "+L[1]+"  Year:"+str(L[2])+"  Hours:"+str( int(round(L[3], 0)) )+"h"+str( int((L[3]%1)*60) )+"  Price:"+str(L[4])+"€  "
        
            self.plane_info.configure(text=self.plane_string_info)
            
            self.plane_img=ImageTk.PhotoImage(Image.open(L[7]))
            self.plane_label.configure(image=self.plane_img)
            self.plane_label.image=self.plane_img
        
        return
    
    #Calculate prize of a flight
    def calculatePrice(self):
        
        self.plane_string_info2=str(controller_take_plane_vue.calculatePrice(self.planeSelect2.get(),self.valueMinutes.get())) + '€'
        
        self.plane_info2.configure(text=self.plane_string_info2)
        return
    
    #Pay a flight
    def pay_plane(self):
        if controller_take_plane_vue.user_using_this_plane(Username,self.planeSelect2.get()):
            controller_take_plane_vue.return_plane(Username,self.planeSelect2.get(),self.valueMinutes.get())
        return