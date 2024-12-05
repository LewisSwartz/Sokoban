from tkinter import *
from sokoban_move import *
from store import *
class Login:
    def __init__(self):
        self.__window=Tk()
        self.__new_obj=Save()
        self.__new_obj.read()
        self.__list12=self.__new_obj.get_main_list()
        self.__frame1=Frame(self.__window)
        self.__frame2=Frame(self.__window)
        self.__frame3=Frame(self.__window)
        self.__lbl_name=Label(self.__frame1,text="User Name")
        self.__lbl_pass=Label(self.__frame2,text="Password  ")
        self.__ent_name=Entry(self.__frame1,width=20)
        self.__ent_pass=Entry(self.__frame2,width=20)
        self.__btn_ok=Button(self.__frame3,text="OK",command=self.convert)
        self.__frame1.pack()
        self.__frame2.pack()
        self.__frame3.pack()
        self.__lbl_name.pack(side="left")
        self.__lbl_pass.pack(side="left")
        self.__ent_name.pack(side="left")
        self.__ent_pass.pack(side="left")
        self.__btn_ok.pack(side="top")
        self.__window.mainloop()     

    def convert(self):
        self.__window.withdraw()
        obj2=self.__new_obj.search(self.__ent_name.get(),self.__ent_pass.get())
        Isobj(self.__window,obj2,self.__list12)
        


Login()