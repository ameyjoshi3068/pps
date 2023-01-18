# string="lettersGoRoundAndGound"
# #Roteting by 45 degree anticlockwise
# count=len(string)
# for i in string:
#     print(" "*count+i)
#     count-=1
# print()

# #Rotating bt 90 degree anticlockwise
# for i in string:
#     print(i)

# #Rotating bt 135 degree anticlockwise

# for i in string:
#     print(" "*count+i)
#     count+=1
# print()

# #Rotating bt 180 degree anticlockwise
# print(string[::-1])
# print()

# #Roteting by 225 degree anticlockwise
# count=len(string)
# string=string[::-1]
# for i in string:
#     print(" "*count+i)
#     count-=1
# print()

# #Rotating bt 270 degree anticlockwise
# string=string[::-1]
# for i in string:
#     print(i)

# #Rotating bt 315 degree anticlockwise
# string=string[::-1]
# for i in string:
#     print(" "*count+i)
#     count+=1
# print()

# #Rotating bt 360 degree anticlockwise
# print(string)
# print()

string="letters"
times=int(input("How many times do you want to rotate?"))
for _ in range(times):
    for i in [0,90,180,270]:
        if i==0:
            count=len(string)+1
            counter=lambda x:x-1
            angles=[16,8,4,2,1]
            print(string)
        if i==90:
            count=1
            counter=lambda x:x+1
            angles=[1,2,4,8,16]
            string=string[::-1]
            for k in string:
                print(k)
        if i==180:
            count=len(string)+1
            counter=lambda x:x-1
            angles=[16,8,4,2,1]
            print(string[::-1])
        if i==270:
            count=1
            counter=lambda x:x+1
            angles=[1,2,4,8,16]
            string="letters"
            for k in string:
                print(k)
        for multiplier in angles: 
            for j in string:
                print(" "*count*multiplier+j)
                count=counter(count)
            print()
