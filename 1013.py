import math

valor = input().split(" ")

a, b, c = valor

fml = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
re = (int(fml) + int(c) + abs(int(fml) - int(c)))/2

print("%d eh o maior" %re)
