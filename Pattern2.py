'''
1
01
101
0101
'''

def PatternA():
    c=int(input('Enter number of lines'))#input from user
    for i in range(1,c+1):#outer loop - line numbers
        #start of each line
        for j in range(i,i+i):
            print(j%2,end="")
        #end of each line
        print()

'''
   *
  * *
 *   *
*******
'''

def PatternB():
    n=int(input('Enter the number of lines'))#input from user
    for i in range(n,1,-1):#outer loop - line numbers
        #start of each line
        for j in range(1,i):#first triangle of spaces
            print(" ",end = " ")
        if(i==n): #first star of a line
            print("*")
            continue
        else:
            print("*",end = " ")
        for k in range(2,2*(n-i)+1): # spaces between consecutive stars of the same line
            print(" ",end=" ")
        print("*")#second star and next line
    for l in range(1,2*n):#last line of stars
        print("*",end = " ")
    print()
    
'''
1
121
12321
1234321
12321
121
1
'''

def Pattern(n):
    for i in range(1,n+1):#first half of pattern with unrepeated lines
        for j in range(1,i+1):
            print(j,end="")
        for j in range(i-1,0,-1):
            print(j,end="")
        print()
    for i in range(n-1,0,-1):#second half of pattern of repeated lines
        for j in range(1,i+1):
            print(j,end="")
        for j in range(i-1,0,-1):
            print(j, end="")
        print()
def PatternC():
    n=int(input('Enter number of unrepeated lines'))#input from user
    Pattern(n) #func call 

'''
   4
  343
 23432
1234321
'''

def PatternF():
    n = int(input("Enter the number of lines"))#input from user
    ch = n
    for i in range(1,n+1):
        for j in range(n,i,-1):#loop to print spaces
            print(" ", end = " ")
        if i == 1:#loop to print first line
            print(ch)
            ch -= 1
        else:#loop for all lines except first one
            while 1:#loop to print first half of every line 
                print(ch,end=" ")
                ch += 1
                if ch == n:
                    break
            while ch>=(n-i+1):#loop to print last half of every line
                print(ch,end=" ")    
                ch -= 1
            print()

'''
   1
  333
 55555
7777777
 55555
  333
   1
'''
def PatternE(): 
    n = int(input("Enter the number of lines"))#input from user
    f=int(n/2)+1
    num = 1
    for i in range(1,f+1):#loop to print first half of the pattern
        ch = num
        for j in range(f,i,-1):#loop to print spaces in the first half of the pattern
            print(" ",end=" ")
        while ch > 0:#to print pattern of digits in the said line
                print(num,end=" ")
                ch -= 1
        print()
        num += 2
    num -= 4
    for i in range(1,f):#loop to print second half of the pattern
        ch = num
        for j in range(1,i+1):#loop to print spaces in the second half of the pattern
            print(" ",end=" ")
        while ch > 0:#to print the pattern of digits in the said line
                print(num,end=" ")
                ch -= 1
        print()
        num -= 2

while 1:
    ch = input("A-Pattern A\nB-Pattern B\nC-Pattern C\nE-Pattern E\nF-Pattern F\nX-Exit ") #choice for user
    if ch == "A":
        PatternA() #func call 
    elif ch == "B":
        PatternB() #func call 
    elif ch == "C":
        PatternC() #func call
    elif ch == "E":
        PatternE() #func call
    elif ch == "F":
        PatternF() #func call
    elif ch == "X":
        break #exit
    else:
        print("Invalid Input") 

'''
OUTPUT:

A-Pattern A
B-Pattern B
C-Pattern C
E-Pattern E
F-Pattern F
X-Exit A   
Enter number of lines4
1
01
101        
0101       
A-Pattern A
B-Pattern B
C-Pattern C
E-Pattern E
F-Pattern F
X-Exit B
Enter the number of lines4
      *
    *   *
  *       *
* * * * * * *
A-Pattern A
B-Pattern B
C-Pattern C
E-Pattern E
F-Pattern F
X-Exit C
Enter number of unrepeated lines4
1
121
12321
1234321
12321
121
1
A-Pattern A
B-Pattern B
C-Pattern C
E-Pattern E
F-Pattern F
X-Exit E   
Enter the number of lines7
      1       
    3 3 3     
  5 5 5 5 5   
7 7 7 7 7 7 7 
  5 5 5 5 5   
    3 3 3     
      1
A-Pattern A
B-Pattern B
C-Pattern C
E-Pattern E
F-Pattern F
X-Exit F
Enter the number of lines4
      4
    3 4 3
  2 3 4 3 2
1 2 3 4 3 2 1
A-Pattern A
B-Pattern B
C-Pattern C
E-Pattern E
F-Pattern F
X-Exit X
'''        