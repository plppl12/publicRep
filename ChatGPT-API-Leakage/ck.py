import pickle
import json

# 读取JSON文件中的Cookies
with open('cookies.json', 'r') as file:
    cookies = json.load(file)

# 将Cookies保存为Pickle文件
with open('cookies.pkl', 'wb') as file:
    pickle.dump(cookies, file)

print("Cookies已保存到cookies.pkl文件")


