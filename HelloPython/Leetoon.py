#########   1.1
names = ['tom', 'jack', 'peter', 'tony']
print(names)

#########   1.2

for i in names:
    print("Hi, " + i.capitalize() + ", you are very good!")

#########   1.3
a = str(names)
b= a.replace("jack","marry")
print(b)


#########   2.1
name = input("请输入学生姓名：")
score = int(input("请输入期中考试平均分数(0~100)："))

if score < 0 or score > 100:
    print("您输入的分数无效，请重新输入")

#########   2.2
if score >= 90 and score <=100:
    print("学生姓名：" + name + "，期中考试平均成绩为" , score ,"分，考试评价为优秀")
if score >= 80 and score < 90:
    print("学生姓名：" + name + "，期中考试平均成绩为" , score ,"分，考试评价为良好")
if score >= 60 and score < 80:
    print("学生姓名：" + name + "，期中考试平均成绩为" , score ,"分，考试评价为及格")
if score >= 0 and score < 60:
    print("学生姓名：" + name + "，期中考试平均成绩为" , score ,"分，考试评价为不及格")


#########   3.1
学号 = [1, 2, 3]
print(学号)

#########   3.2
学号1 = {'学号': 1, '姓名': '张三', '语文': 95, '数学': 90, '英语': 93}
学号2 = {'学号': 2, '姓名': '李四', '语文': 80, '数学': 92, '英语': 82}
学号3 = {'学号': 3, '姓名': '王五', '语文': 75, '数学': 66, '英语': 78}
print(学号1, 学号2, 学号3)

#########   3.3
print("学号：" ,学号1['学号'], "，姓名：" + 学号1['姓名'] + "，语文成绩：",学号1['语文'],"分，数学成绩：",学号1['数学'] \
    , "分，英语成绩：", 学号1['英语'] ,"分")

