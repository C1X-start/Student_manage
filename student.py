# 1.学生个人信息的增删改查
# 2.登录学生的分数
# 3.依据分数做出排行榜，并分析平均
# 4.全部学生信息展示
# 5.手动退出系统
import re
import csv
import statistics


def main():
    title()


def load_stu():
    try:
        with open("student.csv","r",encoding="gbk") as file:
            reader = csv.reader(file)
            students=list(reader)
            return students
    except FileNotFoundError:
        return []

def save_stu(students):
    with open("student.csv","w",encoding="gbk") as file:
        writer = csv.writer(file)
        writer.writerows(students)

def title():
    goal = int(input("请选择需求\n1.学生信息添加\n2.修改信息\n3.成绩排名\n4.查看全部学生\n")) #输入的是字符串类型 要转换
    match goal:
        case 1:
            information_add()
        case 2:
            adjust_stu()
        case 3:
            score_rank()
        case 4:
            view_stu()
        case _:
            print("输入错误，请重新输入")


def information_add():
    while True:
        student = input("请输入学生的姓名、8位学号、性别和考试分数，中间用逗号隔开")
        matches = re.search(r"(.+),(\d{8}),(.+),(\d{1,3})",student)
        if matches:
            name,number,sex,score = matches.group(1),matches.group(2),matches.group(3),matches.group(4)
            print(name,number,sex,score)
            with open("student.csv","a",newline="",encoding="gbk") as file:
                writer = csv.writer(file)
                writer.writerow([name,number,sex,score])
                print("添加成功")
                break

def adjust_stu():
    students = []
    adjust1 = input("请输入需要修改的学生学号")

    with open("student.csv","r",encoding="gbk") as file:
        for line in file:
            name,number,sex,score = line.rstrip().split(",")
            if number == adjust1:
                student = input("请输入学生的姓名、8位学号、性别和考试分数，中间用逗号隔开")
                matches = re.search(r"(.+),(\d{8}),(.+),(\d{1,3})",student)
                if matches:
                    name,number,sex,score = matches.group(1),matches.group(2),matches.group(3),matches.group(4)
                    with open("student.csv","a",newline="",encoding="gbk") as file:
                        writer = csv.writer(file)
                        writer.writerow([name,number,sex,score])
                        print("修改成功成功")
                                    

    

def score_rank():
    all_score = []
    
    result = sorted(load_stu(),key= lambda student: int(student[3]),reverse=True)
    for stu in result:
        all_score.append(int(stu[3]))
        
        print(f"{stu[0]}:{stu[3]}")
    max_score = max(all_score)
    min_score = min(all_score)
    avg_score = statistics.mean(all_score)
    print(f"最高分为{max_score},最低分为{min_score},平均分为{avg_score}")


def view_stu():
    for student in load_stu():
        print(student)

main()