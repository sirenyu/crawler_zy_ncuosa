# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#ch03
grade=76
height=175.5
weight=75.5
print("成绩="+str(grade))
print("身高="+str(height))
print("体重="+str(weight))
x,y=1,2
print("X=",x,"Y=",y)
#print遇到，就是分别看待，字串用+则表示连接，数字要加str()
print(str(1)+"a"+"b")
#数值形态
a=1
print(type(a)) #integers整数
b=7.11
print(type(b)) #float浮点数
c=2+3j
print(type(c)) #complex number复数
#字串形态string
str1="学习python程式"
print(type(str1))
#布林形态boolean
x=True
print(type(x))
y=False
print(type(y))

#ch04
#整数除法“//"
a=13//3
print(a)
#余数除法“%"
a=9%2
print(a)
#指数“**"
a=2**3
print(a)

var1=int(input("10"))
var2=int(input("8"))
var3=var1*var2
print("相乘结果="+str(var3))
var4=var1/var2
print("相除结果="+str(var4))

a=60 #00111100
b=15 #00001111
print("a="+str(a))
print("b="+str(b))
r=a&b       #and运算
print("a&b="+str(r))
c=3  #00000011
print("c="+str(c))
r=a|c       #or运算
print("a|c="+str(r))
d=120  #00111100
print("d="+str(d))
r=a^d      #xor运算
print("a^b="+str(r))
e=5     #00000101
print("e="+str(e))
r=~e      #not运算
print("~e="+str(r))
r=~r       #not运算
print("~r="+str(r))

var1=int(input())
if var1>=10:
    print("condition is true")
print("var1="+str(var1))

s=int(input("请输入成绩:"))
if s>=60:
    print("成绩及格!")
else:
    print("成绩不及格！")

var1=int(input("please enter an interger=>"))
var1=20
for i in range(1,11):
    print("i="+str(i))
print("var1="+str(var1))
#ex:
target,guess=38,1
while True:
    guess=int(input("请输入猜测数字(1-100):"))
    if target==guess:
        print("猜测数字=",target)
        break
    elif guess>target:
        print("数字太大!")
    else:
        print("数字太小!")
#ex:
def print_msg():
    print("欢迎学习python程式设计")

def sum_to_ten():
    s=0
    for i in range(1,11):
        s+=i
    print("从1加到10="+str(s))
print_msg()
sum_to_ten()

def sum_to_n(star,stop):
    s=0
    for i in range(star,stop+1):
        s+=i
    print("从n加到n=" + str(s))

m=5
sum_to_n(1,5)
sum_to_n(2,m+2)

#ex:
def print_age(age):
    if age<=18:
        print("年龄太小")
        return
    print("年龄="+str(age))

def is_valid_num(no):
    if no>=0 and no<=200.0:
        return True
    else:
        return False

def convert_to_f(c):
    f=(9.0*c)/5.0+32.0
    return f

c=100.00
print_age(15)
print_age(22)

#ex:
def is_valid_num(no):
    if no>=0 and no<=200.0:
        return True
    else:
        return False

def convert_to_f(c):
    f=(9.0*c)/5.0+32.0
    return f

c=100.00
print_age(15)
print_age(22)

#ex:
def volume(length,width=2,height=3):
    return length*width*height

l,w,h=10,5,15
print("盒子体积：",volume(1,w,h))
print("盒子体积：",volume(1,w))
print("盒子体积：",volume(1))


def sum(a,b,c):
    return a+b+c

r1=sum(1,2,3)
r2=sum(b=2,c=3,a=1)
r3=sum(1,c=3,b=2)
r4=sum(1,2,c=3)
print("总和="+str(r1))
print("总和="+str(r2))
print("总和="+str(r3))
print("总和="+str(r4))


t=1
def increment():
    global t
    t+=1
    print("increment中:t=",t)

def global_var():
    global x
    x=100
    print("global_var中:x=",x)

print("全域变数初值:t=",t)
increment()
print("呼叫increment后:t=",t)
global_var()
print("呼叫global_var后:x=",x)

def sum(a,b):
    return a+b

square=lambda x:x*x

total=sum
r=square(10)
print("square(10)=",r)
r=sum(10,5)
print("sum(10,5)=",r)
r=total(10,5)
print("total(10,5)=",r)

class Student:
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade
    def displayStudent(self):
        print("姓名:",self.name)
        print("成绩:", self.grade)
    def whoami(self):
        return self.name
s1=Student("陈会安",90)
s1.displayStudent()
print("s1.whoami():",s1.whoami())
print("s1.name:",s1.name)
print("s1.grade:",s1.grade)




import pickle
fp =open("note.dat","wb")
pickle.dump(11,fp)
pickle.dump("陈会安",fp)
pickle.dump([1,2,3,4],fp)
fp.close()

import pickle
fp = open("note.dat","rd")
num = pickle.load(fp)
print(num)

import math
print(math.e)
print(math.sqrt(3))
import random
r1=random.randint(1,6)
r2=random.randint(1,6)
print(r1+r2)

lst1=list(range(11))
print(lst1)
r3=random.choice(lst1)
print(r3)

fp=open("note.txt", "w")
if fp != None:
    print("档案开启成功!")



from selenium import webdriver

def crawl():
    chorme_options = webdriver.ChromeOptions()
    # chorme_options.add_argument("--headless")
    chorme_options.add_experimental_option( "excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=chorme_options)
    driver.get("https://www.dcard.tw/f")

    title = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[3]/article/h2/a/span")
    print(title.text)

    link= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[3]/article/h2/a")
    print(link.get_attribute("href"))

    emoji_amount = driver.find_element_by_xpath( "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[3]/article/div[3]/div[1]/div/div[2]")
    print(emoji_amount.text)

    reply_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[3]/article/div[3]/div[2]/div/span" )
    print(reply_amount.text)

    driver.quit()

if __name__ == "__main__":
    crawl()