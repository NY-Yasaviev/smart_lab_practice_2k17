from docxtpl import DocxTemplate

report = DocxTemplate("templates/report.docx")

changeTag = {'orgName': "Высшая школа информационных технологий и информационных систем",
             'practLeader' : "Абрамский Михаил Михайлович",
             'studGroup':"11-603",
             'compLeader':"Иванов Иван Иванович",
             'studFio':"Винокуров Егор Сергеевич"}
report.render(changeTag)
report.save("prepairDocx/Заполненный отчет.docx")