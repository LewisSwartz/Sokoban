import pygame
from sokoban import *
from tkinter import *
from obj_on_board import *
from store import *
from tkinter.messagebox import *
from pickle import *
class Isobj:
    def __init__(self,parent,obj,list12):
        pygame.init()
        self.__parent=parent
        self.__window=Toplevel(parent)
        self.__obj5=obj
        self.__list12=list12
        self.__d=0
        self.__count=0
        self.__name=self.__obj5.get_name()
        self.__pass=self.__obj5.get_pass()
        self.__n=self.__obj5.get_lvl()
        self.__playerx=0
        self.__playery=0
        person=PhotoImage(file="D:\\Python programs\\sokoban\\worker.png")
        box=PhotoImage(file="D:\\Python programs\\sokoban\\box.png")
        floor=PhotoImage(file="D:\\Python programs\\sokoban\\floor.png")
        wall=PhotoImage(file="D:\\Python programs\\sokoban\\wall.png")
        destination=PhotoImage(file="D:\\Python programs\\sokoban\\dock.png")
        box_on_destination=PhotoImage(file="D:\\Python programs\\sokoban\\box_docked.png")
        obj2=Sokoban()
        obj2.load_map(self.__n)
        dlist=obj2.get_list()
        self.__list_lbl=[]
        self.__list_obj=[]
        for i in range(len(dlist)):
            self.__list_b=[]
            self.__list_a=[]
            for j in range(len(dlist[i])):
                if dlist[i][j]=="f":
                    dlist[i][j]=Label(self.__window,image=floor)
                    self.__list_a.append(Floor())
                elif dlist[i][j]=="w":
                    dlist[i][j]=Label(self.__window,image=wall)
                    self.__list_a.append(Wall())
                elif dlist[i][j]=="b":
                    dlist[i][j]=Label(self.__window,image=box)
                    self.__list_a.append(Box())
                elif dlist[i][j]=="p":
                    dlist[i][j]=Label(self.__window,image=person)
                    self.__list_a.append(Person())
                    self.__playery=i
                    self.__playerx=j
                elif dlist[i][j]=="d":
                    dlist[i][j]=Label(self.__window,image=destination)
                    self.__list_a.append(Destination())
                    self.__d+=1
                self.__list_b.append(dlist[i][j])
            self.__list_lbl.append(self.__list_b)
            self.__list_obj.append(self.__list_a)
            self.__list_a=[]
            self.__list_b=[]
        for i in range (len(self.__list_lbl)):
            for j in range (len(self.__list_lbl[i])):
                self.__list_lbl[i][j].grid(row=i,column=j)
                
        self.__window.bind("<Key-Left>",self.move_left)
        self.__window.bind("<Key-Right>",self.move_right)
        self.__window.bind("<Key-Up>",self.move_up)
        self.__window.bind("<Key-Down>",self.move_down)
        # self.show()
        self.__window.protocol("WM_DELETE_WINDOW",self.ok_cancel)
        self.__window.mainloop()
    
    def get_obj(self):
        return self.__list_obj()
    
    def ok_cancel(self):
        option=askokcancel(message="Are you sure you want to exit?")
        if option:
            self.write()
            self.__window.destroy()
            self.__parent.destroy()
            
    def show(self):
        for i in range(len(self.__list_obj)):
            for j in range(len(self.__list_obj[i])):
                print(self.__list_obj[i][j],end=" ")
            print()
        print()

    def move_left(self,event):
        x=self.__playerx
        y=self.__playery
        a=self.__list_obj[y][x].get_is_under()
        obj2=self.__list_obj[y][x-1]
        b=obj2.get_is_under()
        obj3=self.__list_obj[y][x-2]
        if self.__list_obj[y][x-1].get_is_obstacle()==False:
            self.__list_obj[y][x-1]=self.__list_obj[y][x]
            self.__list_obj[y][x]=a
            self.__list_obj[y][x-1].set_is_under(obj2)
            img1=PhotoImage(file=self.__list_obj[y][x-1].get_path())
            self.__list_lbl[y][x-1].image=img1
            self.__list_lbl[y][x-1].configure(image=img1)
            img2=PhotoImage(file=self.__list_obj[y][x].get_path())
            self.__list_lbl[y][x].image=img2
            self.__list_lbl[y][x].configure(image=img2)
            self.__playerx-=1

        elif self.__list_obj[y][x-1].get_is_pushable()==True:
            if self.__list_obj[y][x-2].get_is_obstacle()==False:
                self.__list_obj[y][x-2]=self.__list_obj[y][x-1]
                self.__list_obj[y][x-2].set_is_under(obj3)
                self.__list_obj[y][x-1]=self.__list_obj[y][x]
                self.__list_obj[y][x-1].set_is_under(b)
                self.__list_obj[y][x]=a
                if self.__list_obj[y][x-1].get_is_under().get_is_destination()==True:
                    self.__count-=1
                if self.__list_obj[y][x-2].get_is_under().get_is_destination()==True:
                    obj4=BoxOnDestination()
                    self.__list_obj[y][x-2]=obj4
                    self.__list_obj[y][x-2].set_is_under(obj3)
                    img3=PhotoImage(file=obj4.get_path())
                    self.__list_lbl[y][x-2].image=img3
                    self.__list_lbl[y][x-2].configure(image=img3)
                    self.__count+=1
                else:
                    obj5=Box()
                    self.__list_obj[y][x-2]=obj5
                    self.__list_obj[y][x-2].set_is_under(obj3)
                    img3=PhotoImage(file=obj5.get_path())
                    self.__list_lbl[y][x-2].image=img3
                    self.__list_lbl[y][x-2].configure(image=img3)
                img1=PhotoImage(file=self.__list_obj[y][x-1].get_path())
                self.__list_lbl[y][x-1].image=img1
                self.__list_lbl[y][x-1].configure(image=img1)
                img2=PhotoImage(file=self.__list_obj[y][x].get_path())
                self.__list_lbl[y][x].image=img2
                self.__list_lbl[y][x].configure(image=img2)    
                self.__playerx-=1
        self.check()
        # self.show()
    
    def move_right(self,event):
        x=self.__playerx
        y=self.__playery
        a=self.__list_obj[y][x].get_is_under()
        obj2=self.__list_obj[y][x+1]
        b=obj2.get_is_under()
        obj3=self.__list_obj[y][x+2]
        if self.__list_obj[y][x+1].get_is_obstacle()==False:
            self.__list_obj[y][x+1]=self.__list_obj[y][x]
            self.__list_obj[y][x]=a
            self.__list_obj[y][x+1].set_is_under(obj2)
            img1=PhotoImage(file=self.__list_obj[y][x+1].get_path())
            self.__list_lbl[y][x+1].image=img1
            self.__list_lbl[y][x+1].configure(image=img1)
            img2=PhotoImage(file=self.__list_obj[y][x].get_path())
            self.__list_lbl[y][x].image=img2
            self.__list_lbl[y][x].configure(image=img2)
            self.__playerx+=1
        elif self.__list_obj[y][x+1].get_is_pushable()==True:
            if self.__list_obj[y][x+2].get_is_obstacle()==False:
                self.__list_obj[y][x+2]=self.__list_obj[y][x+1]
                self.__list_obj[y][x+2].set_is_under(obj3)
                self.__list_obj[y][x+1]=self.__list_obj[y][x]
                self.__list_obj[y][x+1].set_is_under(b)
                self.__list_obj[y][x]=a
                if self.__list_obj[y][x+1].get_is_under().get_is_destination()==True:
                    self.__count-=1
                if self.__list_obj[y][x+2].get_is_under().get_is_destination()==True:
                    obj4=BoxOnDestination()
                    self.__list_obj[y][x+2]=obj4
                    self.__list_obj[y][x+2].set_is_under(obj3)
                    img3=PhotoImage(file=obj4.get_path())
                    self.__list_lbl[y][x+2].image=img3
                    self.__list_lbl[y][x+2].configure(image=img3)
                    self.__count+=1
                else:
                    obj5=Box()
                    self.__list_obj[y][x+2]=obj5
                    self.__list_obj[y][x+2].set_is_under(obj3)
                    img3=PhotoImage(file=obj5.get_path())
                    self.__list_lbl[y][x+2].image=img3
                    self.__list_lbl[y][x+2].configure(image=img3)
                img1=PhotoImage(file=self.__list_obj[y][x+1].get_path())
                self.__list_lbl[y][x+1].image=img1
                self.__list_lbl[y][x+1].configure(image=img1)
                img2=PhotoImage(file=self.__list_obj[y][x].get_path())
                self.__list_lbl[y][x].image=img2
                self.__list_lbl[y][x].configure(image=img2)               
                self.__playerx+=1
        self.check()
        # self.show()

    def move_up(self,event):
        x=self.__playerx
        y=self.__playery
        a=self.__list_obj[y][x].get_is_under()
        obj2=self.__list_obj[y-1][x]
        b=obj2.get_is_under()
        obj3=self.__list_obj[y-2][x]
        if self.__list_obj[y-1][x].get_is_obstacle()==False:
            self.__list_obj[y-1][x]=self.__list_obj[y][x]
            self.__list_obj[y][x]=a
            self.__list_obj[y-1][x].set_is_under(obj2)
            img1=PhotoImage(file=self.__list_obj[y-1][x].get_path())
            self.__list_lbl[y-1][x].image=img1
            self.__list_lbl[y-1][x].configure(image=img1)
            img2=PhotoImage(file=self.__list_obj[y][x].get_path())
            self.__list_lbl[y][x].image=img2
            self.__list_lbl[y][x].configure(image=img2)
            self.__playery-=1
        elif self.__list_obj[y-1][x].get_is_pushable()==True:
            if self.__list_obj[y-2][x].get_is_obstacle()==False:
                self.__list_obj[y-2][x]=self.__list_obj[y-1][x]
                self.__list_obj[y-2][x].set_is_under(obj3)
                self.__list_obj[y-1][x]=self.__list_obj[y][x]
                self.__list_obj[y-1][x].set_is_under(b)
                self.__list_obj[y][x]=a
                if self.__list_obj[y-1][x].get_is_under().get_is_destination()==True:
                    self.__count-=1
                if self.__list_obj[y-2][x].get_is_under().get_is_destination()==True:
                    obj4=BoxOnDestination()
                    self.__list_obj[y-2][x]=obj4
                    self.__list_obj[y-2][x].set_is_under(obj3)
                    img3=PhotoImage(file=obj4.get_path())
                    self.__list_lbl[y-2][x].image=img3
                    self.__list_lbl[y-2][x].configure(image=img3)
                    self.__count+=1
                else:
                    obj5=Box()
                    self.__list_obj[y-2][x]=obj5
                    self.__list_obj[y-2][x].set_is_under(obj3)
                    img3=PhotoImage(file=obj5.get_path())
                    self.__list_lbl[y-2][x].image=img3
                    self.__list_lbl[y-2][x].configure(image=img3)
                img1=PhotoImage(file=self.__list_obj[y-1][x].get_path())
                self.__list_lbl[y-1][x].image=img1
                self.__list_lbl[y-1][x].configure(image=img1)
                img2=PhotoImage(file=self.__list_obj[y][x].get_path())
                self.__list_lbl[y][x].image=img2
                self.__list_lbl[y][x].configure(image=img2)
                self.__playery-=1
        self.check()    
        # self.show()
        
    
    def move_down(self,event):
        x=self.__playerx
        y=self.__playery
        a=self.__list_obj[y][x].get_is_under()
        obj2=self.__list_obj[y+1][x]
        b=obj2.get_is_under()
        obj3=self.__list_obj[y+2][x]
        if self.__list_obj[y+1][x].get_is_obstacle()==False:
            self.__list_obj[y+1][x]=self.__list_obj[y][x]
            self.__list_obj[y][x]=a
            self.__list_obj[y+1][x].set_is_under(obj2)
            img1=PhotoImage(file=self.__list_obj[y+1][x].get_path())
            self.__list_lbl[y+1][x].image=img1
            self.__list_lbl[y+1][x].configure(image=img1)
            img2=PhotoImage(file=self.__list_obj[y][x].get_path())
            self.__list_lbl[y][x].image=img2
            self.__list_lbl[y][x].configure(image=img2)
            self.__playery+=1
        elif self.__list_obj[y+1][x].get_is_pushable()==True:
            if self.__list_obj[y+2][x].get_is_obstacle()==False:
                self.__list_obj[y+2][x]=self.__list_obj[y+1][x]
                self.__list_obj[y+2][x].set_is_under(obj3)
                self.__list_obj[y+1][x]=self.__list_obj[y][x]
                self.__list_obj[y+1][x].set_is_under(b)
                self.__list_obj[y][x]=a
                if self.__list_obj[y+1][x].get_is_under().get_is_destination()==True:
                    self.__count-=1
                if self.__list_obj[y+2][x].get_is_under().get_is_destination()==True:
                    obj4=BoxOnDestination()
                    self.__list_obj[y+2][x]=obj4
                    self.__list_obj[y+2][x].set_is_under(obj3)
                    img3=PhotoImage(file=obj4.get_path())
                    self.__list_lbl[y+2][x].image=img3
                    self.__list_lbl[y+2][x].configure(image=img3)
                    self.__count+=1
                else:
                    obj5=Box()
                    self.__list_obj[y+2][x]=obj5
                    self.__list_obj[y+2][x].set_is_under(obj3)
                    img3=PhotoImage(file=obj5.get_path())
                    self.__list_lbl[y+2][x].image=img3
                    self.__list_lbl[y+2][x].configure(image=img3)
                img1=PhotoImage(file=self.__list_obj[y+1][x].get_path())
                self.__list_lbl[y+1][x].image=img1
                self.__list_lbl[y+1][x].configure(image=img1)
                img2=PhotoImage(file=self.__list_obj[y][x].get_path())
                self.__list_lbl[y][x].image=img2
                self.__list_lbl[y][x].configure(image=img2)
                self.__playery+=1
        
        self.check()    
        # self.show()
        
    def check(self):
        if self.__count==self.__d:
            if self.__n==5:
                showinfo("Sokoban","Congratulation! You completed all levels.")
                pygame.mixer.music.load("D:\\Python programs\\sokoban\\Win.mp3")
                pygame.mixer.music.play()
                self.write()
                self.__window.destroy()
                self.__parent.destroy()
            else:
                showinfo("Sokoban","Congratulation!")
                pygame.mixer.music.load("D:\\Python programs\\sokoban\\Win.mp3")
                pygame.mixer.music.play()
                self.__n+=1
                self.__obj5.set_lvl(self.__n)
                self.__window.withdraw()
                Isobj(self.__window,self.__obj5,self.__list12)
    
    def write(self):
        for i in range(len(self.__list12)):
            if self.__name==self.__list12[i].get_name() and self.__pass==self.__list12[i].get_pass():
                self.__list12[i].set_lvl(self.__n)
        file_obj=open("user_info.obj","wb")
        dump(self.__list12,file_obj)
        file_obj.close()