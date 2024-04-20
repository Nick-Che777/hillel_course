x=input("Type 5 digit number:")
x=int(x)
d_1=x//10000
d_2=x//1000%10
d_3=x//100%10
d_4=x//10%10
d_5=x%10
inverse_digit=d_5*10000+d_4*1000+d_3*100+d_2*10+d_1
print(inverse_digit)
