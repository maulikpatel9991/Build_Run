# a = "2"
# b = "3"
# print(a+b)

# x = "Hello"
# print(x[1:3])

# z = "xyz"
# j = "j"
# for j in z:
#     print(j, end=" ")

# x = ["XX","YY"]
# for i in a:
#     i.lower()
# print(a)


# t = "maulik"
# print(t[5:5])
# ------------------------------------------------------------------------------------------------------------------
# Good THink
def fun1(name,age=20):
    print(name)
    print(age)
fun1("demo",None)
# ------------------------------------------------------------------------------------------------------------------
print((type(int)))
# ------------------------------------------------------------------------------------------------------------------
mytuple = (1,2,3)
mytuple2 = mytuple * 2
print(mytuple2)

# ------------------------------------------------------------------------------------------------------------------
x = "Maulikpatel"
print(x[-1:-4:-1])

# ------------------------------------------------------------------------------------------------------------------
print(True * False)
print(True ** False)
print(True ** False / True)

# ------------------------------------------------------------------------------------------------------------------
# Error Tuple Hase not Attribute sort
# i = (3,5,2,1,0)
# i.sort()
# print(i)


# ------------------------------------------------------------------------------------------------------------------
w = '12'
print(w * 2)
print(w * 0)
print(w * -2)

# ------------------------------------------------------------------------------------------------------------------
#  Good Python Questions
i = 2,10
j = 3,5
add = i + j
print(add)

# ------------------------------------------------------------------------------------------------------------------
t = [1,2,3,4,5]
t.insert(10,4)
print(t)

# ------------------------------------------------------------------------------------------------------------------
o = {1,2,3,4}
print(o.remove(2))
print(o)

# ------------------------------------------------------------------------------------------------------------------
k,j = 12,12.0
if(k+j == 24):
    print("HIII")

Name = ["dfg","dgth"]
print(Name[1][-1])

# ------------------------------------------------------------------------------------------------------------------
s1 = {1,2,3,4}
s2 = {5,6,3,4}
print(s2-s1)

# ------------------------------------------------------------------------------------------------------------------
w1 = [1,2,3,4]
w1.append([5,6])
print(w1)
print(w1 *2)


# ------------------------------------------------------------------------------------------------------------------
l = [None] * 10
print(len(l))
print(l)

# ------------------------------------------------------------------------------------------------------------------
z = set('fhd$dj')
print('f' in z)