# Finding the greatest number

a,b,c,d,e = 60,70,80,90,100

if (a>=b) and (a>=c) and (a>=d) and (a>=e):
    print(a, "is the greatest")

elif (b>=a) and (b>=c) and (b>=d) and (b>=e):
    print(b, "is the greatest")

elif (c>=a) and (c>=b) and (c>=d) and (c>=e):
    print(c, "is the greatest")

elif (d>=a) and (d>=b) and (d>=c) and (d>=e):
    print(d, "is the greatest")

elif (e>=a) and (e>=b) and (e>=c) and (e>=d):
    print(e, "is the greatest")

else:
    print("Invalid number")
