"""university={'IT':54,'economy':6,'medicine':87}
university['IT']=55
university['lingustik']=556
university.pop('medicine')
total = sum(university.values())
print(total)


dict_={1:'a',2:'b',3:'c'}
new_dict={}
for key, value in dict_.items():
    new_dict.update({value: key})
print(new_dict)                          
count=int(input("how many guests"))
guests={}
for i in range(1,count+1):
    names=input()
    guests[i]=names
print(guests)"""

#my_list=[{'alma':44},
#         {'meat':33},
#         {'potato':9},
#        {'asdroid':2},
#         {'pizza':67}]
#while my_list:
 #   products_to_remove=input()
 #   for products in my_list:
 #       if products_to_remove in products:
 #           del products[products_to_remove]
 #           print(my_list)
  #  if not any(my_list):
  #      break
#print('it"s time to pay')

nigga=int(input('enter one number:'))
try:
    if nigga!=993:
        raise Exception
except:
    print('you are gay')
else:
    print(nigga)
finally:
    print('brrr skibidi bop')


num=1000
while num>0:
    num-=7
    print(num)

    

