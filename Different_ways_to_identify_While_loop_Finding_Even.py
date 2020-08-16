# Finding even numbers from the list
"""
list_var = [1, 2, 4, 5, 6, 7, 6, 8, 65, 64, 34, 45]
i = 0
while i < len(list_var):
    if list_var[i] % 2 == 0:
        print(list_var[i])
    i += 1
"""

# another way of finding even number between 1 to 30
"""
i=2

while i<=30:
    print(i)

    i+=2
"""

# finding odd number between 1 to 30
"""
i=1
while i<=30:
    print(i)

    i+=2
"""
# finding even number reverse order between 1 to 30
"""
i = 30
while i >= 2:
    print(i)

    i -= 2
"""
# Finding Odd numbers from the list
"""
my_var = [2,3,90,99,97,98,75,79,45,54]

i = 0
while i<len(my_var):
    if my_var[i]%2!=0:
        print(my_var[i])
    i+=1
"""

# Finding even and odd using while loop in range function

x = range(0,101)

i = 1
while i<=len(x) -1:
    if x[i]%2 == 0:
        print(x[i], "is even")
    else:
        print (x[i], "is odd")

    i += 1
