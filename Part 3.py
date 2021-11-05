class myclass(Exception):
    def __init__(self,str):
        self.str=str
        if str.isdigit():lst.append(int(str))
lst=[]
a=""
while a!="stop":
    try:
        a=input("Введите новый элемент - ")
        if a!="" and a!="stop":
            raise myclass(a)
    except myclass:
        pass
print(lst)