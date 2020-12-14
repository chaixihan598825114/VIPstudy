'''
name = 'abcdef'
print(name[0])
print(name[1])
print(name[3])
# 序列[开始位置下标:结束位置下标:步长()]
name = 'abcdefg'
print(name[2:5:1])
print(name[2:5])
print(name[:5])
print(name[1:])
print(name[:])
print(name[::2])
print(name[:-1])
print(name[-4:-1])
print(name[::-1])

mystr = 'hello world and test and day2'
print(mystr.find('and',22,25))
# 用index报错后会终止代码，所以常用find
# print(mystr.index('and',22,20))
print(mystr.count('and'))
print(mystr.count('ands'))
print(mystr.count('and',21,25))
# replace 替换字符串 不会改变原来的字符串
print(mystr.replace('and','or',0))
# split分割字符串
print(mystr.split('and'))
# join 多字符串连接
list1 = ['1','2','3','4','5']
print(' '.join(list1))




mystr = "   hello world and superctest and chaoge and Python   "
print(mystr)

print(mystr.capitalize())

print(mystr.lower())

print(mystr.title())

print(mystr.upper())
# ljust(长度，填充字符):返回⼀个原字符串左对⻬,并使用指定字符(默认空格)填充至对应长度的新字符串，rjust(右侧对齐)。
print(mystr.ljust(55,'.'))
# center(长度，填充字符):返回⼀个原字符串居中对齐,并使⽤指定字符(默认空格)填充至对应长度的新字符串，语法和ljust()相同。
print(mystr.center(80))
# strip():删除字符串两侧空⽩字符,(lstrip(删除左侧空白字符，rstrip(删除字符串右侧空白字符))
print(mystr.strip())
'''


# 判断 直接返回 True或False
mystr = "hello world and supertest and chaoge and Python "
# starswith(子串，开始位置下标，结束位置下标)，endwwith用法一样(子串，结束位置下标，结束位置下标)
print(mystr.startswith('hello'))
print(mystr.startswith('hello',5,20))
#isalpha():如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False。
mystr1 = 'hello'
mystr2 = 'hello12345'
print(mystr1.isalpha())
print(mystr2.isalpha())
# isdigit():如果字符串只包含数字则返回 True 否则返回 False。
mystr1 = 'aaa12345'
mystr2 = '12345'
print(mystr1.isdigit())
print(mystr2.isdigit())
# isalnum():如果字符串⾄至少有⼀个字符并且所有字符都是字母或数字则返回True,否则返回False。
mystr1 = 'aaa12345'
mystr2 = '12345-'
print(mystr1.isalnum())
print(mystr2.isalnum())
# isspace():如果字符串中只包含空白，则返回True，否则返回False。
mystr1 = '1 2 3 4 5'
mystr2 = ' '
print(mystr1.isspace())
print(mystr2.isspace())