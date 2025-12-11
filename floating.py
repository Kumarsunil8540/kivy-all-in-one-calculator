
# class Floating_calculator:
#     def __init__(self,binary,base):
#         self.binary=binary
#         self.base = base


#     def split_binary(self):
#         binary=str(self.binary)
#         if'.'in binary:
#             integer_part, fractional_part=self.binary.split('.')
#         else:
#             integer_part=binary 
#             fractional_part=''

#         decimal_integer=int(integer_part,self.base)

#         decimal_fractional = 0

#         for i, bit in enumerate(fractional_part):
#             decimal_fractional += int(bit)*(self.base**-(i+1))
            
#         return decimal_integer+decimal_fractional
    
#     def to_binary(self,decimal_value):
#         if decimal_value < 0:
#             sign = "-"
#             decimal_value = -decimal_value
#         else:
#             sign = "" 

#         integer_part = int(decimal_value)
#         fractional_part=decimal_value-integer_part

#         binary_integer = bin ( integer_part)[2:]

#         binary_fractional = ''

#         while fractional_part and len(binary_fractional)<10:

#             fractional_part *= 2
#             bit = int(fractional_part)
#             binary_fractional += str (bit)
#             fractional_part -= bit

#         return f"{sign}{binary_integer}.{binary_fractional}" if binary_fractional else binary_integer
    
#     # def to_octal(self,decimal_value):
#     #     if decimal_value < 0:
#     #         sign = "-"
#     #         decimal_value = -decimal_value
#     #     else:
#     #         sign = "" 

#     #     integer_part = int(decimal_value)
#     #     fractional_part=decimal_value-integer_part

#     #     binary_integer = oct ( integer_part)[2:]

#     #     binary_fractional = ''

#     #     while fractional_part and len(binary_fractional)<10:

#     #         fractional_part *= 8
#     #         bit = int(fractional_part)
#     #         binary_fractional += str (bit)
#     #         fractional_part -= bit

#     #     return f"{sign}{binary_integer}.{binary_fractional}" if binary_fractional else binary_integer
    
#     # def to_decimal(self,decimal_value):
#     #     if decimal_value < 0:
#     #         sign = "-"
#     #         decimal_value = -decimal_value
#     #     else:
#     #         sign = ""

#     #     result = decimal_value

#     #     return f"{sign}{result} "
    
#     def __add__(self,binary2):
#         add=self.split_binary() + binary2.split_binary() 

#         return self.to_binary(add)#,self.to_octal(add),self.to_decimal(add)
    
#     def __sub__(self,binary2):
#         sub = self.split_binary() - binary2.split_binary()

#         return self.to_binary(sub)#,self.to_octal(sub),self.to_decimal(sub)
    
#     def __mul__(self,binary2):
#         mul = self.split_binary() * binary2.split_binary()

#         return self.to_binary(mul)#,self.to_octal(mul),self.to_decimal(mul)
    
#     def __truediv__(self,binary2):
#         div = self.split_binary() / binary2.split_binary()

#         return self.to_binary(div)#,self.to_octal(div),self.to_decimal(div)
    
    
    
# binary1="-10101.01010"
# binary2="0101010.010"
# num1 = Floating_calculator(binary1,8)
# num2 = Floating_calculator(binary2,8)
# sum = num1+ num2
# sub = num1-num2
# mul = num1*num2
# div = num1/num2
# print(sum)
# print(sub)
# print(mul)
# print(div)


class Floating_calculator:
    def __init__(self, binary, base):
        self.binary = binary
        self.base = base

    def split_binary(self):
        binary = str(self.binary)
        if '.' in binary:
            integer_part, fractional_part = binary.split('.')
        else:
            integer_part = binary
            fractional_part = ''

        decimal_integer = int(integer_part, self.base)
        decimal_fractional = 0

        for i, bit in enumerate(fractional_part):
            decimal_fractional += int(bit) * (self.base ** -(i + 1))

        return decimal_integer + decimal_fractional

    def to_binary(self, decimal_value):
        if decimal_value < 0:
            sign = "-"
            decimal_value = -decimal_value
        else:
            sign = ""

        integer_part = int(decimal_value)
        fractional_part = decimal_value - integer_part

        binary_integer = bin(integer_part)[2:]
        binary_fractional = ''

        while fractional_part > 0 and len(binary_fractional) < 10:
            fractional_part *= 2
            bit = int(fractional_part)
            binary_fractional += str(bit)
            fractional_part -= bit

        return f"{sign}{binary_integer}.{binary_fractional}" if binary_fractional else f"{sign}{binary_integer}"

    def __add__(self, binary2):
        add = self.split_binary() + binary2.split_binary()
        return self.to_binary(add)

    def __sub__(self, binary2):
        sub = self.split_binary() - binary2.split_binary()
        return self.to_binary(sub)

    def __mul__(self, binary2):
        mul = self.split_binary() * binary2.split_binary()
        return self.to_binary(mul)

    def __truediv__(self, binary2):
        div = self.split_binary() / binary2.split_binary()
        return self.to_binary(div)


# binary1 = "-10101.01010"
# binary2 = "101010.010"
# num1 = Floating_calculator(binary1, 2)
# num2 = Floating_calculator(binary2, 2)

# sum_result = num1 + num2
# sub_result = num1 - num2
# mul_result = num1 * num2
# div_result = num1 / num2

# print("Sum:", sum_result)
# print("Subtraction:", sub_result)
# print("Multiplication:", mul_result)
# print("Division:", div_result)
