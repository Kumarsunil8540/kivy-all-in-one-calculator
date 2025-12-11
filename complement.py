# class complement:
#     def __init__(self,number,base):
#         self.number = number 
#         self.base = base 


# # binary = (input("enter your binary code  :"))
# # if not all(bit in '01' for bit in binary):
# #     raise ValueError("Invalid binary input. Only 0 and 1 are allowed.")
#     def decimal_complement(self):
#         self.n = self.base-1
# # n = base-1
#         self.gray = ""

#         for i in range(0,len(self.number)):
#             self.gray += str(int(self.n)-int(self.number[i]))

#         return self.gray

        
#         # r = self.gray[:len(self.number)-1]
#     def r_complement(self):    
#         self.r = self.gray[:len(self.number)-1]
#         for i in range((len(self.gray)-1),len(self.gray)):
#             self.r += str(int(self.gray[i])+1)

# # print(r)
#         return self.r
# num = complement("858",9)
# print(num.decimal_complement())
# print(num.r_complement())


# # num= "67565658822"
# # nu= num[len(num)-1:len(num)]
# # print(nu)



# class Complement:
#     def __init__(self, number, base):
#         if not all(0 <= int(digit) < base for digit in number):
#             raise ValueError(f"Invalid number for base {base}.")
#         self.number = number  # Input number as a string
#         self.base = base      # Base of the number

#     def decimal_complement(self):
#         """Calculate (r-1)'s complement."""
#         r_minus_1 = self.base - 1
#         complement = ""

#         for digit in self.number:
#             complement += str(r_minus_1 - int(digit))  # Calculate (r-1)-complement for each digit
        
#         return complement

#     def r_complement(self):
#         """Calculate r's complement."""
#         r_minus_1_complement = self.decimal_complement()
#         r_complement = list(r_minus_1_complement)  # Convert to list for manipulation

#         # Add 1 to the last digit, handling carry if necessary
#         carry = 1
#         for i in range(len(r_complement) - 1, -1, -1):
#             new_value = int(r_complement[i]) + carry
#             if new_value < self.base:
#                 r_complement[i] = str(new_value)
#                 carry = 0
#                 break
#             else:
#                 r_complement[i] = '0'
#                 carry = 1

#         # If there's still a carry, prepend it
#         if carry:
#             r_complement.insert(0, '1')

#         return ''.join(r_complement)

# # Example usage
# num = Complement("858", 16)
# print("Decimal Complement (r-1's):", num.decimal_complement())
# print("R's Complement:", num.r_complement())

# num2 = Complement("101", 2)
# print("\nDecimal Complement (r-1's):", num2.decimal_complement())
# print("R's Complement:", num2.r_complement())


class Complement:
    def __init__(self, number, base):
        # Validate the input number for the given base
        if not all(0 <= int(digit, base) < base for digit in number.upper()):
            raise ValueError(f"Invalid number for base {base}.")
        self.number = number.upper()  # Ensure consistency for hexadecimal
        self.base = base

    def decimal_complement(self):
        """Calculate (r-1)'s complement."""
        r_minus_1 = self.base - 1
        complement = ""

        for digit in self.number:
            value = int(digit, self.base)  # Convert to decimal
            complement += format(r_minus_1 - value, 'X')  # Convert back to base and format as a string
        
        return complement

    def r_complement(self):
        """Calculate r's complement."""
        r_minus_1_complement = self.decimal_complement()
        r_complement = list(r_minus_1_complement)  # Convert to list for manipulation

        # Add 1 to the last digit, handling carry if necessary
        carry = 1
        for i in range(len(r_complement) - 1, -1, -1):
            new_value = int(r_complement[i], 16) + carry
            if new_value < self.base:
                r_complement[i] = format(new_value, 'X')
                carry = 0
                break
            else:
                r_complement[i] = '0'
                carry = 1

        # If there's still a carry, prepend it
        if carry:
            r_complement.insert(0, '1')

        return ''.join(r_complement)

# Example usage for the number "236" in base 16
num = Complement("236", 16)
decimal_complement = num.decimal_complement()
r_complement = num.r_complement()

print(f"(r-1)'s complement: {decimal_complement}")
print(f"r's complement: {r_complement}")
