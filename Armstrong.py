#Program to find if a number is an armstrong number
#Take input from the user
number = int(input("input your number: "))
#Calculate number of digits
digits = len(str(number))
#Initialize result variable
resultnumber = 0
#find the sum of a^digit of each digit
temp = number
while temp>0:
    digit = temp%10
    resultnumber += digit**digits
    temp//=10
#display the results
if number ==resultnumber:
    print(number,"is an armstrong number")
else:
    print(number,"is not an armstrong number")