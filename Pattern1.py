'''
ABCDEFGFEDCBA
ABCDEF FEDCBA
ABCDE   EDCBA
ABCD     DCBA
ABC       CBA
AB         BA
A           A
'''

def pattern1(): #func definition starts here
    n = int(input("Enter the number of lines"))
    
    for i in range(n,0,-1): #outer loop - line numbers
        #start of each line
        ch = 'A'
        for j in range(1,i+1): #first triangle
            print(ch,end=" ")
            m=ord(ch) #ASCII of ch
            m += 1 #increase ASCII to get the NEXT ALPHABET
            ch = chr(m) #converting ASCII to corresponding char'''

        for k in range(0,2*(n-i)-1): #second triangle (of spaces)
            print(" ",end=" ")
        m=ord(ch) #ASCII of ch
        m -= 1 #increase ASCII to get the NEXT ALPHABET
        ch = chr(m) #converting ASCII to corresponding char'''

        if i == (n): #to repeat first line segment as it is simlar to the second line segment
            m=ord(ch) #ASCII of ch
            m -= 1 #increase ASCII to get the NEXT ALPHABET
            ch = chr(m) #converting ASCII to corresponding char'''

            for x in range(0,n-1): #third right angled triangle
                print(ch,end=" ")
                m=ord(ch) #ASCII of ch
                m -= 1 #increase ASCII to get the NEXT ALPHABET
                ch = chr(m) #converting ASCII to corresponding char'''
        else:
            for l in range(1,i+1):
                print(ch,end=" ")
                m=ord(ch) #ASCII of ch
                m -= 1 #increase ASCII to get the NEXT ALPHABET
                ch = chr(m) #converting ASCII to corresponding char'''
        #end of each line
        print()

'''
Z
ZY
ZYX
.......
ZYX..........A
YX..........A
......
CBA
BA
A
'''

def pattern2(): #func definition starts here
    n = int(input("Enter the number of lines"))
    f = int(n/2)+1 #half of the requested number of lines
    for i in range(1,f+1): #first half of the pattern
        ch = "Z"
        for j in range(1,i+1): #pattern to add one letter to the end after every iteration
            print(ch,end=" ")
            m=ord(ch) #ASCII of ch
            m -= 1 #increase ASCII to get the NEXT ALPHABET
            ch = chr(m) #converting ASCII to corresponding char'''
        print()

    for i in range(f-1,0,-1): #second half of the pattern
        ch = "Y"
        for k in range(f,i+1,-1):# to remove (n-f) letters from the front (n being the number of lines outputted )
            m=ord(ch) #ASCII of ch
            m -= 1 #increase ASCII to get the NEXT ALPHABET
            ch = chr(m) #converting ASCII to corresponding char'''
        for j in range(1,i+1): 
            print(ch,end=" ")
            m=ord(ch) #ASCII of ch
            m -= 1 #increase ASCII to get the NEXT ALPHABET
            ch = chr(m) #converting ASCII to corresponding char'''
        print()
while 1:
    ch = int(input("1-Pattern 1     2-Pattern 2     0-Exit ")) #choice for user
    if ch == 1:
        pattern1() #func call 
    elif ch == 2:
        pattern2() #func call 
    elif ch == 0:
        break #exit
    else:
        print("Invalid Input") 

'''
OUTPUT:

1-Pattern 1     2-Pattern 2     0-Exit 1
Enter the number of lines7
A B C D E F G F E D C B A 
A B C D E F   F E D C B A 
A B C D E       E D C B A 
A B C D           D C B A 
A B C               C B A 
A B                   B A 
A                       A 
1-Pattern 1     2-Pattern 2     0-Exit 2
Enter the number of lines51
Z   
Z Y 
Z Y X
Z Y X W
Z Y X W V
Z Y X W V U
Z Y X W V U T
Z Y X W V U T S
Z Y X W V U T S R
Z Y X W V U T S R Q
Z Y X W V U T S R Q P
Z Y X W V U T S R Q P O
Z Y X W V U T S R Q P O N
Z Y X W V U T S R Q P O N M
Z Y X W V U T S R Q P O N M L
Z Y X W V U T S R Q P O N M L K
Z Y X W V U T S R Q P O N M L K J
Z Y X W V U T S R Q P O N M L K J I
Z Y X W V U T S R Q P O N M L K J I H
Z Y X W V U T S R Q P O N M L K J I H G
Z Y X W V U T S R Q P O N M L K J I H G F
Z Y X W V U T S R Q P O N M L K J I H G F E
Z Y X W V U T S R Q P O N M L K J I H G F E D
Z Y X W V U T S R Q P O N M L K J I H G F E D C
Z Y X W V U T S R Q P O N M L K J I H G F E D C B
Z Y X W V U T S R Q P O N M L K J I H G F E D C B A
Y X W V U T S R Q P O N M L K J I H G F E D C B A
X W V U T S R Q P O N M L K J I H G F E D C B A
W V U T S R Q P O N M L K J I H G F E D C B A
V U T S R Q P O N M L K J I H G F E D C B A
U T S R Q P O N M L K J I H G F E D C B A
T S R Q P O N M L K J I H G F E D C B A
S R Q P O N M L K J I H G F E D C B A
R Q P O N M L K J I H G F E D C B A
Q P O N M L K J I H G F E D C B A
P O N M L K J I H G F E D C B A
O N M L K J I H G F E D C B A
N M L K J I H G F E D C B A
M L K J I H G F E D C B A
L K J I H G F E D C B A
K J I H G F E D C B A
J I H G F E D C B A
I H G F E D C B A
H G F E D C B A
G F E D C B A
F E D C B A
E D C B A
D C B A
C B A
B A
A
1-Pattern 1     2-Pattern 2     0-Exit 0
'''