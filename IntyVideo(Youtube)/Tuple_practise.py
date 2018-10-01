my_tuple = (1,2,3,4,5)
# print(type(my_tuple))

my_list = [1,2,3,4,5]
# print(my_list)

# print(dir(my_tuple))
#
# print('...................')
#
# print(dir(my_list))

#list is mutable,属性、功能多，
# 数据量很大的时候运行慢；
#tuple is inmutable，属性、功能少，
# 确定存储的数据不需要变动的时候进行设定；

my_tuple.remove(2)
print(my_tuple)

my_list.remove(2)
print(my_list)

