try:
    file = open("cwj.txt", 'r+')
except Exception as e:
    print(e)
    response = input("do you want to create a new file ?")
    if response == 'y':
        file = open("cwj.txt", 'w')
    else:
        pass
# 这个else是如果没有出现这种异常怎么做
else:
    file.write("This file is open successful !")
file.close()
