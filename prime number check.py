
#https://www.youtube.com/watch?v=iOV-4xICZH8&list=PLUDwpEzHYYLv0iZsTx4dm-v-icoVXRqrz&index=2

num = int(input("Enter the number : "))
count = 0

if num>1:
    for i in range (1,num+1):
        if (num%i) == 0:
            count = count +1
    if count==2:
        print("Number is primary ",num)
    else:
        print("number is not primary",num)


