b = int(input())
with open ("salom.txt","r") as falle:
    a = falle.readlines()
    print(a[b])