import pickle
# pickle python的持久化模块
a_dict = {'a', 111, '2', 222}
file = open('pickle_example.pickle', 'wb')
pickle.dump(a_dict, file)
file.close()

openFile = open('pickle_example.pickle', 'rb')
b_dict = pickle.load(openFile)
print(b_dict)