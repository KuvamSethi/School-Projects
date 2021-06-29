"""
? [1, 2, 3, 4, 4, 5, 6, 6]
"""
#! Ishant

# l = [1, 2, 3, 4, 4, 5, 6, 6]

# for i in l:
#     pass













#! Kuvam

# l = input("Enter string : ")

# m = l.split(' ')

# l = list(map(int, m))
# arr = []

# for i in l:
#     if i not in arr:
#         arr.append(i)

# arr.sort()
# print(l)
# print(arr[-2])



"""
? Aloo 25
? kuvam 10
? Viki 10
? ishant 0
? harshit -10

? [[harshit, -10], [kuvam, -10]]
"""

# _list = [x.split(" ") for x in input().split(",")]

# num = []
# name = []

# for [_, _num] in _list:
#     num.append(int(_num)) 

# _max = max(num)
# for x in num:
#     if _max in num:
#         num.remove(_max)

# for [_name , _num] in _list:
#     if int(_num) == max(num):
#         name.append(_name)

# print("\n".join(sorted(name)))



# import math

# def prime(m):
#     if m == 1:
#         return 0
    
#     for i in range(2, int(math.sqrt(m)+1)):
#         if m%i == 0:
#             return 0
#     return 1

# print(prime(111))


#? kuvam 80,harshit 60,ishant 70,nikki 50,vicky 70

# def once(p, v, a):
#     inf = p
#     cure = 0
#     t = 0
#     inf_once = 0
#     while inf_once < a:
#         inf+=inf
#         if t%5==0 and t!=0:
#             cure+=v
#             inf-=cure
#         inf_once = inf + cure
#         t+=1
#     return t


# N = int(input())
# for i in range(N):
#     p, v, a = input().split(" ")
#     print(once(int(p), int(v), int(a)))

# def book(x, y): 
#     books = [20*n**2 + 5*n + 1]
#     return books[0]
    
    



# N = int(input())
# for _ in range(N):
#     X, Y = input().split()
#     print(book(X, Y))

# def create(L,N):
#     for i in range(N):
#         L.append(20*(i+1)**2+5*(i+1)+1)

# def POP(L,P,T):
#     for i in range(P):
#         T.append(L.pop())
#     Sum=sum(T)
#     return Sum


# L=[]
# T=[]
# P=int(input("Enter the no. of Pickups : "))
# Pg=int(input("Enter the number of Pages :"))
# create(L,P+1)
# p1=POP(L,P,T)

# print(p1)

# free for all goods
# qwertyuiopasdfghjklzxcvbnm


def sen(st, abc):
    st = sorted(st, key = lambda word: [abc.index(c) for c in word])
    return " ".join(st)


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        st = input().split(" ")
        abc = input()
        print(sen(st, abc))