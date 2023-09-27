print(".......TEMPERATURE CONVERTER........\n")
print("enter the choice:\n")
print("1- celsius-fahrenheit 2-celsius to kelvin  3-fahrenheit-celsius 4-fahrenheit-kelvin 5-kelvin-celsius 6-kelvin-farenheit")
ch=int(input("enter your choice:"))
if(ch==1):
   c=int(input("enter temperature in celsius:"))
   f=(9/5)*(c)+32
   print("temperature in farenheit:",f)
elif(ch==2):
    c=int(input("enter temperature in celsius:"))
    k=c+273
    print("temperature in kelvin:",k)
elif(ch==3):
    f=int(input("enter temperature in fahrenheit:"))
    c=(5/9)*(f-32)
    print("temperature in celsius:",c)
elif(ch==4):
    f=int(input("enter temperature in fahrenheit:"))
    k=(f-32)/(1.8)+273.15
    print("temperature in kelvin:",k)
elif(ch==5):
    k=int(input("enter temperature in kelvin:"))
    c=k-273
    print("temperature in celsius:",c)
elif(ch==6):
    k=int(input("enter temperature in kelvin:"))
    f=(1.8)*(k-273.15)+32
    print("temperature in fahrenheit:",f)
else:
    print("enter valid choice\n")