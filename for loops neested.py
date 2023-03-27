#create L from x using for loop
items =[2,2,2,2,7,7]
for y in items:
    outputs =''
    for b in range(y):
        outputs+='x'
    print(outputs)

names = ['Lukas', 'Jan', 'Maciek', 'Marta']
print(names[0])


#Find greatest number
list=[2,1,3,4,9]
max=list[0]
for c in list:
    if c>max:
        max=c
print(max)

#2 dimension list
matrix=[
    [1,2,3],
    [3,4,5],
    [6,7,8]
]
matrix[0][1]=20
print(matrix[0][1])

for x in matrix:
    for c in x:
        print(c)