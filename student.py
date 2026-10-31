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
    students = []
    try:
        with open("student.csv", "r", encoding="gbk") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    print(f"发现错误数据{row}请及时修改")
                    continue
                else:
                    students.append(row)
                    continue
            return students
    except FileNotFoundError:
        return []


def save_stu(students):
    with open("student.csv", "w", encoding="gbk", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)


def title():
    while True:
        #当要改变数据类型时一定要警惕数据错误
        try:
            goal = int(
                input(
                "请选择需求\n1.学生信息添加\n2.学生信息删除\n3.修改学生信息\n4.查看全部学生\n5.成绩排名\n6.退出程序\n"
                )
            )  # 输入的是字符串类型 要转换
        except ValueError:
            print("请输入正确数字")
            continue

        match goal:
            case 1:
                information_add()
            case 2:
                del_stu()
            case 3:
                adjust_stu()
            case 4:
                view_stu()
            case 5:
                score_rank()
            case 6:
                print("====关闭程序====")
                break
            case _:
                print("输入错误，请重新输入\n")


def information_add():
    students = load_stu()
    while True:
        student = input("请输入学生的姓名、8位学号、性别和考试分数，中间用逗号隔开\n")
        matches = re.search(r"^(.+),(\d{8}),(.+),(\d{1,3})$", student)
        if matches and 0 <= int(matches.group(4)) <= 100:
            exists = any(matches.group(2) == stu[1] for stu in students)
            if exists:
                print("该学号学生已存在\n")
                continue
            else:
                name, number, sex, score = (
                    matches.group(1),
                    matches.group(2),
                    matches.group(3),
                    matches.group(4),
                )
                print(name, number, sex, score)
                with open("student.csv", "a", newline="", encoding="gbk") as file:
                    writer = csv.writer(file)
                    writer.writerow([name, number, sex, score])
                    print("添加成功\n")
                    break
        else:
            print("输入内容不合规，请重新输入\n")



def adjust_stu():
    students = load_stu()
    adjust1 = input("请输入需要修改的学生学号\n")
    found = False 
    changed = False # 当找到这个学生就结束遍历并输出成功，不能直接在if下写 else 会输出
    for stu in students:
        if stu[1] == adjust1:
            while True:
                try:
                    x= int(input("请选择需要修改哪个信息\n1.姓名\n2.学号\n3.性别\n4.成绩\n5.结束修改\n"))
                except ValueError:
                    print("输入错误")
                    continue
                match x:
                    case 1:
                        change_name = input("输入新姓名\n")
                        matches = re.search(r"^(.+)$",change_name)
                        if matches:
                            stu[0] = change_name
                            changed = True
                            print(f"已修改完成{stu}\n")
                        else:
                            print("输入格式错误")
                    case 2:
                        change_number = input("输入新的学号\n")
                        matches = re.search(r"^(\d{8})$",change_number)
                        if matches:
                            exists = any(matches.group(1) == stu[1] for stu in students)
                            if exists:
                                print("该学号学生已存在\n")
                                continue
                            stu[1] = change_number
                            changed = True
                            print(f"已修改完成{stu}\n")
                        else:
                            print("输入格式错误")
                    case 3:
                        change_sex = input("输入新性别\n")
                        matches = re.search(r"^(.+)$",change_sex)
                        if matches:
                            stu[2] = change_sex
                            changed = True
                            print(f"已修改完成{stu}\n")
                        else:
                            print("输入格式错误")

                    case 4:
                        change_score = input("输入新成绩\n")
                        matches = re.search(r"^(\d{1,3})$",change_score)
                        if matches and 0 <= int(matches.group(1)) <= 100:
                            stu[3] = change_score
                            changed = True
                            print(f"已修改完成{stu}\n")
                        else:
                            print("输入格式错误")
                    case 5:
                        print("修改已结束\n")
                        found =True
                        break
                    case _:
                        print("输入错误，请重新输入\n")

            

    if found:
        save_stu(students)

    else:
        print("未找到该学生\n")



def del_stu():
    students = load_stu()
    flag = False
    dels = input("输入需要删除的学生学号\n")
    for stu in students:
        if stu[1] == dels:
            students.remove(stu)
            flag = True
            break 
    if flag:
        print("已删除成功\n")
        save_stu(students)
    else:
        print("未找到该学生\n")

def score_rank():
    all_score = []
    # 防止空列表报错

    result = sorted(load_stu(), key=lambda student: int(student[3]), reverse=True)
    for stu in result:
        all_score.append(int(stu[3]))
        print(f"{stu[0]}:{stu[3]}")
    if not all_score:
        print("暂无学生数据\n")
        return
    max_score = max(all_score)
    min_score = min(all_score)
    avg_score = statistics.mean(all_score)
    print(f"最高分为{max_score},最低分为{min_score},平均分为{avg_score}\n")
   


def view_stu():
    students = load_stu()
    if not students:
        print("暂无学生信息\n")
        return
    print("="*40+"学生信息"+"="*40)
    print(f"{'姓名':<10}{'学号':<15}{'性别':<8}{'成绩':>10}")
    print("-"*88)
    for name,number,sex,score in students:
        print(f"{name:<10}{number:<15}{sex:<10}{score:>10}")
    print("="*88)
    print(f"共有{len(students)}名学生")
        



if __name__ == "__main__":
    main()
