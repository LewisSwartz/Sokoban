from pickle import *
from tkinter.messagebox import *

class User:
    def __init__(self):
        self.__name=""
        self.__password=""
        self.__lvl=1
    
    def set_name(self,name):
        self.__name=name
    
    def set_pass(self,password):
        self.__password=password
    
    def set_lvl(self,level):
        self.__lvl=level

    def get_name(self):
        return self.__name
    
    def get_pass(self):
        return self.__password
    
    def get_lvl(self):
        return self.__lvl

class Save:
    def __init__(self):
        self.__main_list=[]
    
    def add_obj(self,name,password):
        user_obj=User()
        user_obj.set_name(name)
        user_obj.set_pass(password)
        self.__main_list.append(user_obj)
        return user_obj

    def read(self):
        try:
            file_obj=open("user_info.obj","rb")
            self.__main_list=load(file_obj)
            file_obj.close()
        except FileNotFoundError:
            print("File not found and new file has been created!!")
    
    def get_main_list(self):
        return self.__main_list
    
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