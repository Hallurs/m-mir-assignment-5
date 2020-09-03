#ég bý til while lykkju
#ég bý til lista svo ég geti náð í og leitað eftir hæðsta integer

listi = []
while num_int >= 0:
    listi.append(num_int)
    num_int = int(input("Input a number: "))
max_int = max(listi)
print("The maximum is", max_int)
