# set跟java差不多，不能重复
char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']
print(set(char_list))

unique_char = set(char_list)
unique_char.add('e')
print(unique_char)

unique_char.remove('e')
print(unique_char)

# 清空
unique_char.clear()
print(unique_char)