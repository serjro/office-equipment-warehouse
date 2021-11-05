class myclass(Exception):
    def __init__(self,str):
        self.str=str
        print("Введены некорректные данные - ",str)

def check(str2):
    try:
        strn=str(str2)
        if not strn.isdigit():
            raise myclass(strn)
        else: return int(strn)
    except myclass:
        return input("Введите числовое значение - ")

class sklad:
    description=[]
    id=-1
    def __init__(self):
        pass
    @classmethod
    def printall(self):
        print("Всего на складе:",self.id+1,"позиции \n")

class orgtech(sklad):
    department = []
    def  receiving(self,des,len,wid,mas,dep):
        sklad.description.append(des)
        sklad.id+=1
        self.len = check(len)
        self.wid = check(wid)
        self.mas = check(mas)
        orgtech.department.append(dep)
        print(f"Получено устройство {sklad.description[sklad.id]}")
    @classmethod
    def movementto(self,id,dep):
        orgtech.department.insert(id,dep)
        print(f"{sklad.description[id]} перемещен в отдел {dep}")

class printer(orgtech):
    def  receiving(self,des,color,len,wid,mas,dep):
        wid2="fdg"
        sklad.description.append(des)
        sklad.id+=1
        self.len = check(len)
        self.wid = check(wid)
        self.mas = check(mas)
        orgtech.department.append(dep)
        #self.department=12345
        self.color=color
        print(f"Добавлен принтер {sklad.description[sklad.id]}")
class scanner(orgtech):
    def  receiving(self,des,speed,len,wid,mas,dep):
        sklad.description.append(des)
        sklad.id+=1
        self.len = check(len)
        self.wid = check(wid)
        self.mas = check(mas)
        orgtech.department.append(dep)
        #self.department=12345
        self.speed=check(speed)
        print(f"Добавлен сканер {sklad.description[sklad.id]}")
class xerox(orgtech):
    def  receiving(self,mfu,des,len,wid,mas,dep):
        sklad.description.append(des)
        sklad.id+=1
        self.len = check(len)
        self.wid = check(wid)
        self.mas = check(mas)
        orgtech.department.append(dep)
        #self.department=12345
        self.mfu=mfu
        print(f"Добавлен ксерокс {sklad.description[sklad.id]}")


anyprinter=printer()
anyprinter.receiving("HP Enterprise 780 Color LaserJet","Monochrome and color",33,5,10,"otdel 1")
print("Отдел:",anyprinter.department[0])
anyprinter.movementto(0,3)
print("Новый отдел:",anyprinter.department[0],"\n")

anyscanner=scanner()
anyscanner.receiving("Epson Expression 10000",500,5,5,7,"otdel 2")
print("Проверка данных:",anyscanner.description[1],anyscanner.len,anyscanner.department[1])
orgtech.printall()

anyscanner2=scanner()
anyscanner2.receiving("HP ScanJet 500",500,5,5,2,"otdel 3")
orgtech.printall()
