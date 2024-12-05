from pickle import *
from tkinter.messagebox import *

# This class is to create user information.
class User:
    # This init method is to create name, password and lvl.
    def __init__(self):
        self.__name=""
        self.__password=""
        self.__lvl=1
    
    # This method is to set_name.
    def set_name(self,name):
        self.__name=name
    
    # This method is to set_pass.
    def set_pass(self,password):
        self.__password=password
    
    # This method is to set_lvl.
    def set_lvl(self,level):
        self.__lvl=level
    
    # This method is to return name.
    def get_name(self):
        return self.__name
    
    # This method is to return password.
    def get_pass(self):
        return self.__password
    
    # This method is to return lvl.
    def get_lvl(self):
        return self.__lvl

# This class is to create add_obj, read, get_main_list, search method.
class Save:
    # This method is to create a empty list.
    def __init__(self):
        self.__main_list=[]
    
    # This method is to add name and password to a empty list.
    def add_obj(self,name,password):
        user_obj=User()
        user_obj.set_name(name)
        user_obj.set_pass(password)
        self.__main_list.append(user_obj)
        return user_obj

    # This method is to read the obj from the saved file.
    def read(self):
        try:
            file_obj=open("user_info.obj","rb")
            self.__main_list=load(file_obj)
            file_obj.close()
        except FileNotFoundError:
            print("File not found and new file has been created!!")
    
    # This method is to return main_list.
    def get_main_list(self):
        return self.__main_list
    
    # This method is to search the user in the object to know the old user or not.
    def search(self,name,password):
        try:
            user_obj1=User()
            user_obj1.set_name(name)
            user_obj1.set_pass(password)
            a=False
            for i in range (len(self.__main_list)):
                if name==self.__main_list[i].get_name() and password==self.__main_list[i].get_pass():
                    a=True
                    user_obj1=self.__main_list[i]       
            if a:
                showinfo("!!!","User has been found!!")
            else:
                showinfo("!!!","User doesn't exist!!. And new user has been created!!")
                user_obj1=self.add_obj(name,password)
            return user_obj1
        except EOFError:      
            pass