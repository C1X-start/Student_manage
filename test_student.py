import pytest
import student

def test_load_stu(tmp_path,monkeypatch):
    monkeypatch.chdir(tmp_path)
    result = student.load_stu()
    assert result == []

def test_save_stu(tmp_path,monkeypatch):
    monkeypatch.chdir(tmp_path)
    students = [["陈奕迅","20261111","男","99"],["李小龙","20251819","男","50"]]
    student.save_stu(students)
    result = student.load_stu()
    assert students == result

def test_information_stu(tmp_path,monkeypatch):
    monkeypatch.chdir(tmp_path)
    inputs = iter(["柯基,10111121,女,89"]) #iter多次输入
    monkeypatch.setattr("builtins.input",lambda prompt:next(inputs))#临时替换input函数
    student.information_add()
    result = student.load_stu()
    assert result == [["柯基","10111121","女","89"]]

def test_del_stu(tmp_path,monkeypatch):
    monkeypatch.chdir(tmp_path)
    students = [["陈奕迅","20261111","男","99"],["李小龙","20251819","男","50"]]
    student.save_stu(students)
    inputs = iter(["20261111"])
    monkeypatch.setattr("builtins.input",lambda prompt: next(inputs))
    student.del_stu()
    result =student.load_stu()
    assert result == [["李小龙","20251819","男","50"]]

def test_score_rank(tmp_path,monkeypatch,capsys):
    monkeypatch.chdir(tmp_path)
    students = [["陈奕迅","20261111","男","100"],["李小龙","20251819","男","50"]]
    student.save_stu(students)
    student.score_rank()
    output = capsys.readouterr().out
    assert output.index("陈奕迅:100") < output.index("李小龙:50")
    assert "最高分为100" in output
    assert "最低分为50" in output
    assert "平均分为75" in output


    