def keyExs(key,kwDic):
    if key in kwDic:
        return True
    return False

dic = {}

word = "word"

arr = [1,2,3,4]

dic[word]=arr
print(dic)

dic[word].append(2)
print(dic)
print(keyExs("namık",dic))