n= int(input())
for i in range(0,n):
    binary_string = input()
    ones_list=binary_string.split('0')
    number_list=[]
    for item in ones_list:
        number_list.append(len(item))
    number_list.sort(reverse=True)
    loop= len(number_list)
    tom=0
    for j in range(0,loop):
        if(j%2 == 0):
            tom = tom+ number_list[j]
    print(tom)
