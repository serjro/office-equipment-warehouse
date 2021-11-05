class Complex:

    def __init__(self,num):
        self.num=num
        if num.find('+')>0:
            self.a = int(num[0:num.find('+')])
            self.b = int(num[num.find('+')+1:num.find('i')])
        if num[1:99].find('-')>=0:
            self.a = int(num[0:num[1:99].find('-')+1])
            self.b = int(num[num[1:99].find('-')+1:num.find("i")])

    def __add__(self, other):
        add=f"{self.num}+{other.num}i"
        if self.b+other.b>0:return f"({self.num})+({other.num})={self.a+other.a}+{self.b+other.b}i"
        else:return f"({self.num})+({other.num})={self.a+other.a}{self.b+other.b}i"

    def __sub__(self, other):
        if self.b-other.b>0:return f"({self.num})-({other.num})={self.a-other.a}+{self.b-other.b}i"
        else:return f"({self.num})-({other.num})={self.a-other.a}{self.b-other.b}i"

    def __mul__(self, other):
        if self.b*other.a+self.a*other.b>0:return f"({self.num})*({other.num})={self.a*other.a-self.b*other.b}+{self.b*other.a+self.a*other.b}i"
        else:return f"({self.num})*({other.num})={self.a*other.a-self.b*other.b}{self.b*other.a+self.a*other.b}i"

    def __floordiv__(self, other):
        a1=self.a
        b1=self.b
        a2=other.a
        b2=other.b
        num1=float("{:.4f}".format((a1*a2+b1*b2)/(a2*a2+b2*b2)))
        num2=float("{:.4f}".format((b1*a2-a1*b2)/(a2*a2+b2*b2)))
        if num2>0:return f"({self.num})/({other.num})={num1}+{num2}i"
        else:return f"({self.num})/({other.num})={num1}{num2}i"


cnum1=Complex("-3-4i")
cnum2=Complex("5-6i")

print(cnum1+cnum2)
print(cnum1-cnum2)
print(cnum1*cnum2)
print(cnum1//cnum2)

