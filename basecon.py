
class Base_converter:
    def __init__(self,number,base):
        self.number=number
        self.base= base 
        self.decimal_value = self.convert_to_decimal()
    
    def convert_to_decimal(self):
        self.deci_num = int(str(self.number),self.base)
        return self.deci_num
    
    def decimal_to_exess3(self):
        self.exess = self.deci_num +3 
        return bin(self.exess)[2:]

    def to_decimal(self):
        return self.decimal_value
    

    def to_binary(self):
        return bin(self.decimal_value)[2:]
    
    
    def to_octal(self):
        return oct(self.decimal_value)[2:]
    
    def to_hexadecimal(self):
        return hex(self.decimal_value)[2:].upper()
    
    def to_gray(self):
        #binary = (input("enter your binary code"))
        if not all(bit in '01' for bit in self.number):
            raise ValueError("Invalid binary input. Only 0 and 1 are allowed.")

        gray = self.number[0]
        for i in range(1,len(self.number)):
            gray += str(int(self.number[i])^int(self.number[i-1]))

        return gray    

    def convert_to_specific_base(self,target_base):
        if target_base==2:
            return self.to_binary()
        elif target_base == 8:
            return self.to_octal()
        elif target_base == 10:
            return self.to_decimal()
        elif target_base == 16:
            return self.to_hexadecimal()
        elif target_base == 3:
            return self.decimal_to_exess3()
        elif target_base == "Gray":
            return self.to_gray()
        else:
            return "suported bases are 2,8,10 $ 16 only"
        
class Binary_calculator:
    def __init__(self, number1 ,base1,number2,base2):
        self.num1 = Base_converter(number1,base1)
        self.num2 = Base_converter(number2,base2)
    
    def __add__(self):
        add = self.num1.to_decimal() + self.num2.to_decimal()
        return add
    
    def __sub__(self):
        sub = self.num1.to_decimal() - self.num2.to_decimal()
        return sub
    
    def __mul__(self):
        mul = self.num1.to_decimal() * self.num2.to_decimal()
        return mul
    
    def __truediv__(self):
        div = self.num1.to_decimal() //  self.num2.to_decimal()
        return div
    
# calc = Binary_calculator("048",16,"840",10)
# print(calc.__add__())

