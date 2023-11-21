#triange
"""def triangle1(n):
    for i in range(0,n):
        print("*",end="")
triangle1(5)"""

def triangle1(n):
    x =0
    for i in range(0,n):
      for j in range(0,x):
         print("",end="")
      x=x+1
      for k in range(0,n):
        print("*",end="")
      n=n-1
      print("\r")
triangle1(5)


#side pattern
def triangle1(n):
    x =0
    for i in range(0,n):
      for j in range(0,x):
         print(" ",end=" ")
      x=x+1
      for k in range(0,n):
        print("*",end=" ")
      n=n-1
      print("\r")
triangle1(5)


#side pattern
def triangle1(n):
    for i in range(0,n):
      for j in range(0,i):
         print(" * ",end="")
      print("\r")
triangle1(6)

#side pattern
def triangle1(n):
    x =0
    for i in range(0,n):
      for j in range(0,x):
         print(" ",end="")
      x=x+1
      for k in range(0,n):
        print("*",end=" ")
      n-=1
      print("\r")
triangle1(5)

#side triangle
def triangle1(n):
    x =n-1
    for i in range(1,n):
      for j in range(0,x):
         print(" ",end="")
      x=x-1
      for k in range(0,i):
        print("*",end=" ")

      print("\r")
triangle1(6)

#side triangle
def triangle1(n):
    x =n-1
    for i in range(1,n):
      for j in range(0,x):
         print(" ",end=" ")
      x=x-1
      for k in range(0,i):
        print("*",end=" ")
      print("\r")
triangle1(6)

#fibnoic series
def fibnoic(n):
    x = 0
    for i in range(0,n):
        lst = [0, 1, 1, 2, 3,5]
        for j in range(0 , x):
            print("",end="")
        x+=1
        for k in range(0 , n):
            print(lst[k],end="")
        n=n-1
print("\r")


