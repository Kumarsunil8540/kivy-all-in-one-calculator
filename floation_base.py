
# # from floating import Floating_calculator
# # class Floating_Base:
# #     def __init__(self,binary,base):
# #         self.binary=binary
# #         self.base = base

# #     def split_binary(self):
# #         binary=str(self.binary)
# #         if'.'in binary:
# #             integer_part, fractional_part=self.binary.split('.')
# #         else:
# #             integer_part=binary 
# #             fractional_part=''

# #         self.decimal_integer=int(integer_part,self.base)

# #         self.decimal_fractional = 0

# #         for i, bit in enumerate(fractional_part):
# #             self.decimal_fractional += int(bit)*(self.base**-(i+1))

# #         self.decimal_value = self.decimal_integer+self.decimal_fractional
            
# #         return  self.decimal_integer+self.decimal_fractional
    
# #     def to_hexa(self):
# #         hexa_deci = hex(str(self.decimal_integer))[2:]

# #         binary_fractional = ''

# #         while self.decimal_fractional and len(binary_fractional)<10:

# #             self.decimal_fractional *= 16
# #             bit = int(self.decimal_fractional)
# #             binary_fractional += str (bit)
# #             self.decimal_fractional -= bit
# #         return f"{hexa_deci}.{binary_fractional}"
    
# # num = Floating_Base("001.0101",2)

# # print(num.to_hexa())


# class FloatingBaseConverter:
#     def __init__(self, number, source_base):
#         self.number = str(number)
#         self.source_base = source_base
#         self.decimal_value = self.convert_to_decimal()

#     def convert_to_decimal(self):
#         # फ्लोटिंग वैल्यू को बेस 10 में बदलें
#         if '.' in self.number:
#             integer_part, fractional_part = self.number.split('.')
#         else:
#             integer_part = self.number
#             fractional_part = ''

#         # integer पार्ट को decimal में बदलें
#         decimal_integer = int(integer_part, self.source_base)

#         # fractional पार्ट को decimal में बदलें
#         decimal_fractional = 0
#         for i, digit in enumerate(fractional_part):
#             decimal_fractional += int(digit, self.source_base) * (self.source_base ** -(i + 1))

#         return decimal_integer + decimal_fractional

#     def from_decimal(self, target_base):
#         # integer पार्ट को target base में बदलना
#         integer_part = int(self.decimal_value)
#         fractional_part = self.decimal_value - integer_part

#         # integer पार्ट
#         target_integer = ''
#         while integer_part > 0:
#             target_integer = str(integer_part % target_base) + target_integer
#             integer_part //= target_base

#         # fractional पार्ट
#         target_fractional = ''
#         count = 0
#         while fractional_part > 0 and count < 10:  # 10 तक के अंकों की सीमा
#             fractional_part *= target_base
#             digit = int(fractional_part)
#             target_fractional += str(digit)
#             fractional_part -= digit
#             count += 1

#         if not target_integer:
#             target_integer = '0'

#         return f"{target_integer}.{target_fractional}" if target_fractional else target_integer

#     def convert_to_base(self, target_base):
#         if target_base < 2 or target_base > 16:
#             raise ValueError("Supported bases are from 2 to 16 only.")
#         return self.from_decimal(target_base)


# # उपयोग का उदाहरण
# number = "-101101"  # फ्लोटिंग वैल्यू
# source_base = 8  # स्रोत बेस
# target_base = 2  # लक्ष्य बेस

# converter = FloatingBaseConverter(number, source_base)
# result = converter.convert_to_base(target_base)

# print(f"{number} in base {source_base} is {result} in base {target_base}")



class FloatingBaseConverter:
    def __init__(self, number, source_base):
        self.number = str(number)
        self.source_base = source_base
        self.decimal_value = self.convert_to_decimal()

    def convert_to_decimal(self):
        
        is_negative = self.number.startswith('-')
        if is_negative:
            self.number = self.number[1:]  

       
        if '.' in self.number:
            integer_part, fractional_part = self.number.split('.')
        else:
            integer_part = self.number
            fractional_part = ''

        
        decimal_integer = int(integer_part, self.source_base)

        
        decimal_fractional = 0
        for i, digit in enumerate(fractional_part):
            decimal_fractional += int(digit, self.source_base) * (self.source_base ** -(i + 1))

        decimal_value = decimal_integer + decimal_fractional
        return -decimal_value if is_negative else decimal_value

    def from_decimal(self, target_base):
        
        is_negative = self.decimal_value < 0
        decimal_value = abs(self.decimal_value)

        
        integer_part = int(decimal_value)
        fractional_part = decimal_value - integer_part

        
        target_integer = ''
        while integer_part > 0:
            target_integer = str(integer_part % target_base) + target_integer
            integer_part //= target_base

        
        target_fractional = ''
        count = 0
        while fractional_part > 0 and count < 10: 
            fractional_part *= target_base
            digit = int(fractional_part)
            target_fractional += str(digit)
            fractional_part -= digit
            count += 1

        if not target_integer:
            target_integer = '0'

        result = f"{target_integer}.{target_fractional}" if target_fractional else target_integer
        return f"-{result}" if is_negative else result

    def convert_to_base(self, target_base):
        if target_base < 2 or target_base > 16:
            raise ValueError("Supported bases are from 2 to 16 only.")
        return self.from_decimal(target_base)


# 
# number = "-101.101"  
# source_base = 2  
# target_base = 10  

# converter = FloatingBaseConverter(number, source_base)
# result = converter.convert_to_base(target_base)

# print(f"{number} in base {source_base} is {result} in base {target_base}")
