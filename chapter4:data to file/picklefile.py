import os
import pickle

print("path " + os.path.abspath('.'))

os.getcwd()

os.chdir('../files')

os.getcwd()

with open ('mydata.pickle', 'wb') as mysavedata:
    pickle.dump([1, 2,'three'], mysavedata)


with open ('mydata.pickle', 'rb') as myrestoredata:
   alist = pickle.load(myrestoredata)

print(alist)

'''

pickle提供的是data save interface

对于使用者而言,它保存的是具象的数据,
对于实际的实现而言,保存的是存储效率最高的形式.

通过dump保存数据,通过load加载数据

'''




