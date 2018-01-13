import re
pattern1 = 'cat'
pattern2 = 'bird'
string = "dog runs to cat"

# 最简单的匹配
print(pattern1 in string)
print(pattern2 in string)

# 正则
print(re.search(pattern1, string))
print(re.search(pattern2, string))

# 字符串前加r说明这就是一个表达式了，[]代表多种可能，a/u都可以匹配
ptn = r"r[au]n"
print(re.search(ptn, "dog ran to cat"))

# 范围
print("范围匹配")
print(re.search(r"r[A-Z]n", string))
print(re.search(r"r[a-z]n", string))
print(re.search(r"r[0-9]n", string))
print(re.search(r"r[0-9 a-z]n", string))

# \d:匹配所有数字
print(re.search(r"r\dn", "run r4n"))
# \D:匹配所有字母
print(re.search(r"r\Dn", "run r4n"))

# \s匹配各种空白符
print(re.search(r"r\sn", "r\nn r4n"))
# \S匹配各种非空白符
print(re.search(r"r\Sn", "r\nn r4n"))

# 还有很多，需要的时候再查吧


