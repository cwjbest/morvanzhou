# text = "You look stupid!\nYou look so stupid!!\nYou look very stupid!!!"
# append_text = "\nYes,I agree with you "

# 后一个参数是打开方式。'w', 'r', 'a'追加
# my_file = open('my_file.txt', 'a')
# my_file.write(append_text)
# my_file.close()

file = open('my_file.txt', 'r')
# content = file.read()
# 读所有
# content = file.readline()
# 读一行
content = file.readlines()
# 以list形式读所有
print(content)
