list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
  if i==1:
    print("Number 1 is neither prime nor composite")
    continue
  try:
    for j in range(2,i):
        if i%j==0:
            raise Exception("Composite Number")
            
  except:
    print (f"Number {i} is not a Prime number")
  else:
    print(f"Number {i} is a Prime number")

