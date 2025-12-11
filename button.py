binary = (input("enter your binary code"))
# if not all(bit in '01' for bit in binary):
#     raise ValueError("Invalid binary input. Only 0 and 1 are allowed.")


# gray = binary[0]

# for i in range(1,len(binary)):
#     gray += str(int(binary[i])^int(binary[i-1]))

# print(gray)


for bit in binary:
    if int(bit)>1:
        print("Invalid binary input. Only 0 and 1 are allowed.")

    else :
        sunil = binary

print(sunil)