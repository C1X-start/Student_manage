# 1.学生个人信息的增删改查
# 2.登录学生的分数
# 3.依据分数做出排行榜，并分析平均
# 4.全部学生信息展示
# 5.手动退出系统
import re
import csv

def main():
    title()


def title():
    goal = int(input("请选择需求\n1.学生信息添加\n2.修改信息\n3.成绩排名\n")) #输入的是字符串类型 要转换
    match goal:
        case 1:
            information_add()
        case 2:
            adjust_stu()
        case 3:
            score_rank()
        case _:
            print("输入错误，请重新输入")


def information_add():
    while True:
        student = input("请输入学生的姓名、8位学号、性别和考试分数，中间用逗号隔开")
        matches = re.search(r"(.+),(\d{8}),(.+),(\d{1,3})",student)
        if matches:
            name,number,sex,score = matches.group(1),matches.group(2),matches.group(3),matches.group(4)
            print(name,number,sex,score)
            with open("student.csv","a",newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name,number,sex,score])
                print("添加成功")
                break

def adjust_stu():
    adjust1 = input("请输入需要修改的学生学号")


def score_rank():
    pass


main()