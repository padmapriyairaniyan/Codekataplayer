string=input("enter a sentecnce")
print(''.join(i for i in string.title() if not i.isspace()))
