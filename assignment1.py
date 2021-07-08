mylist =["riverdale", "friends", "lawschool", "jesuscode", "biohackers", "geteven", "bloodandwater"]
for i in mylist:
  print(i)
  
 --Q2-- 
  
mylist= ["riverdale", "friends", "lawschool", "jesuscode", "biohackers", "geteven", "bloodandwater"]
yourlist = input("your fav shows: ")
mylist.append(yourlist)
print(mylist)

--Q3--

print(tl[1::2])

--Q4--
a=[98,6,12,56,55]
i=0
sum= 0
while i<len(a):
    sum=sum+a[i]
    i+=1
print(sum)


--Q5--
no_of_rows =int(input("enter no of rows:"))
for i in range(no_of_rows):
    for j in range(i+1):
        print(j+1,end="")
   print()
    
    
    
