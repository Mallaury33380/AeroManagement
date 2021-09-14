from tkinter  import messagebox
from model import data_base_planes
from model import data_base_people

#Check credentials inputed
def controllEntries(login,password):
    if len(login) == 0 or len(password) == 0:
        messagebox.showinfo('Credentials', 'Crdentials incorrects')
        return 0
    if data_base_planes.credentials_corrects(login, password) == 0:
        return 0
    return 1

#Check if the member is an admin
def admin(login):
    return data_base_people.admin(login)