a = input()
for i in range(len(a)):
    if type(a[i])==int:print('int : ',a[i])
    elif type(a[i])==str:print('str : ',a[i])
    elif type(a[i])==bool:print("bool : ", a[i])