#3 programm 
#print(max([int(s) for s in input().split()]))


# 2 programm
#
#n = int(input()) - 1
#res = 0
#a = ([0] * 8) + [1 for i in range(2)]
#for k in range (9, n): 
#    a.append(int(sum(a[k: k - 9 : -1])))
#print(int(a[n]))


#4_programm
#from itertools import groupby
#x = [int(s) for s in input().split()]
#data = sorted(x)
#new_data = [el for el, _ in groupby(data)]
#count = 0
#fin_mas = []
#for i in range(len(new_data) - 1): 
#    for j in range(len(data) - 1): 
#        if new_data[i] == data[j]:
#            count += 1
#    if count == 1:
#        fin_mas.append(new_data[i])
#print(data)
#print(new_data)
#print(fin_mas)
#data = input().split()
#answ = []
##        if data.count(i) == 1: answ.append(i)
#print(max(answ))
#------------------------
#def counting(arr):
#   if element in d:
#           d[element] += 1
#      else:
#           d[element] = 1
#   result = []
#   for key, value in d.items(): 
#        if value==1: 
#              result.append(key) 
#   return result
#x = [int(s) for s in input().split()]
#res = counting(x)
#print(max(res))

#5programm
#data = [str(i) for i in input().split()]
##for i in data: 
 #   if i in d:
 #       d[i]+=1
 #   else:
 #       d[i] = 1
#for keys in d:  
#    print(d[keys], keys) 
# прога не сортирует слова 
 
#lst = [str(line) for line in input().split()]
#print(*sorted(set(lst), key=lambda x: (-lst.count(x), x)),sep='\n')

a = input().split(" ")
d = list({i: a.count(i) for i in a}.items())
for i in sorted(d, key=lambda y: ((-1) * y[1], y[0])):
    print(f"{i[1]} {i[0]}")


    
