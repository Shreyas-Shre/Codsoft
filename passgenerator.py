import random
n=int(input('Enter the length of the password: '))
c=input('Enter the complexity of the password(Easy,Medium,Hard): ')
com={
     'easy':0,
     'medium':1,
     'hard':2
     }
if c not in com.keys():
    hi = print("Invalid complexity")
    quit()
result=''
for i in range(n):
    a=random.randint(0, com[c.lower()])
    if a==0:
        result+=chr(random.randrange(97, 122))
    elif a==1:
        result+=chr(random.randrange(65,90))
    else:
        result+=str(random.randrange(9))
print(result)
