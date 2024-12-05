class Sokoban:
    def __init__(self):
        self.__list=[]
    def load_map(self,n):
        obj=open("map"+str(n)+".txt","r")
        string=obj.readline().rstrip()
        list1=[]
        while string!="":
            for i in string:
                list1.append(i)
            self.__list.append(list1)
            string=obj.readline().rstrip()
            list1=[]
        obj.close()
    def get_list(self):
        return self.__list
