from docxtpl import DocxTemplate

doc = DocxTemplate("templates/permit.docx")
changeTag = {'studCours':"COURS",
             'studGroup':"GROUP",
             'departName':"ITIS",
             'contNumber':"CONTRACT",
             'contDate':"CONTRACT_DATE",
             'entityName':"ZAVOD",
             'entityAdress':"ADRESS_ZAVODA",
             'practType':"PRACTIKA",
             'practDateT1':"BEG_DATE_1",
             'practDateF1':"END_DATE_1",
             'practDateT2':"BEG_DATE_2",
             'practDateF2':"END_DATE_2",
             'practDateT3':"BEG_DATE_3",
             'practDateF3':"END_DATE_3",
             'corollary':"ЗАКЛЮЧЕНИЕ_КАФЕДРЫ",
             'mark':"OCENKA",
             'spec':"НАПРАВЛЕНИЕ-ПОДГОТОВКИ",
             'profil':"PROFIL",
             'skill':"КВАЛИФИКАЦИЯ",
             'needActivType':"ACTIV",
             'showUp':"ЯВИЛСЯ",
             'tutor':"НАЧАЛЬНИК",
             'adminReview':"ОТЗЫВ-АДМИНИСТРАЦИИ",
             'departure':"ВЫБЫЛ"}
doc.render(changeTag)
doc.save("prepairDocx/Заполненная путевка.docx")