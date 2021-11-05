class Data:
    day=0
    month=0
    year=0
    def __init__(self, dmy):
        self.dmy = dmy

    @classmethod
    def toint(cls, param):  # Метод класса
        Data.day=int(param[:2])
        Data.month = int(param[3:5])
        Data.year = int(param[6:10])
        print(Data.day, Data.month, Data.year)

    @staticmethod
    def check():
        if 0<Data.day<32 and 0<Data.month<13 and 0<Data.year<9999:
            print("Проверка прошла успешно!")
        else:print("Значения не соответствуют дате")
Data.toint("09-05-1945")
Data.check()