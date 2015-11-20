import time


limit = input("which fibinachi number do you want?  :")
A = 0
B = 1
#print A
#print B
for i in range(limit):
    C = A + B
    A = B
    B = C
print C
