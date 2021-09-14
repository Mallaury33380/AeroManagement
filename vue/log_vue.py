import  tkinter as tk 
from PIL import ImageTk,Image

from vue import manage_planes_vue
from vue import take_plane_vue
from controller import controller_log_vue
from model import data_base_planes
    

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('AeroManagement')
        self.iconbitmap("./res/logo.ico")
        self._frame = None
        self.switch_frame(log_vue)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class log_vue(tk.Frame):
        
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        Frame1 = tk.Frame(self, borderwidth=2, relief=tk.GROOVE)
        Frame1.pack()
        
        #title
        tk.Label(Frame1, text="AeroManagement", font=('Helvetica', 30, "bold")).pack()
        
        #image
        my_img=ImageTk.PhotoImage(Image.open("./res/fond_log.png"))
        my_label= tk.Label(Frame1,image=my_img)
        my_label.image = my_img
        my_label.pack()
        
        # login
        valueLogin = tk.StringVar() 
        valueLogin.set("Login")
        self.entreeLogin = tk.Entry(Frame1, textvariable=valueLogin, width=30)
        self.entreeLogin.pack()
        
        # Password
        valuePassword = tk.StringVar() 
        valuePassword.set("Password")
        self.entreePassword = tk.Entry(Frame1, textvariable=valuePassword, width=30)
        self.entreePassword.pack()
        
        B = tk.Button(Frame1, text ="Log In", command=lambda: self.controllData(master))
        B.pack()
        
    def controllData(self,master):
        #Check if dat base exist
        data_base_planes.check_DB_exists()
        #check Credentials
        if controller_log_vue.controllEntries(self.entreeLogin.get(), self.entreePassword.get()):
            
            temp=controller_log_vue.admin(self.entreeLogin.get())
            if(temp):
                master.switch_frame(manage_planes_vue.manage_planes_vue)
            elif temp==0:
                take_plane_vue.Username=self.entreeLogin.get()
                master.switch_frame( take_plane_vue.take_plane_vue);
            
                
                

        