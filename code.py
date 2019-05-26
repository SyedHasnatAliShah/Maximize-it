g=globals()
total_list=input().split()
num_list=total_list[0]
#print(total_list)
#print(num_list)
maxum=[]
for i in range(int(num_list)):
    g['lst_{0}'.format(i)]=[]
    create_list=input().split()
    lst=set(create_list)
    #print(create_list)
    lst2=list(lst)
    lst2=list(map(int,lst2))
    a=max(lst2)
    #print(a)
    maxum.append(a)
    #g['lst_{0}'.format(i)]=create_list

print(maxum)
ad=0
for i in maxum:
    ad+=int(i)**2
    print(ad)
#print(ad)
div_max=total_list[1]
print(ad%int(div_max))
