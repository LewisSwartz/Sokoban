# This class is to load maps.
class Sokoban:
    # This method creates a empty list.
    def __init__(self):
        self.__list=[]
    # This method is to read maps.
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
    # This method is return get_list.
    def get_list(self):
        return self.__list
