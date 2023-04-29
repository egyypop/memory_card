from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QButtonGroup, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox)
from random import shuffle,randint
class Question():
    def __init__(self, question, right_answer,wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question('Какой национальности не существует?','Герзинцы','Энцы','Алеуты','Чулымцы'))
question_list.append(Question('Сколько спутников у Сатурна','82','54','16','164'))
question_list.append(Question('Как переводится выражение "сбит с толку"','disinterested','enormity','Unabashed','irregardless'))


appl = QApplication([])
scr = QWidget()
scr.setWindowTitle('Мемори')
question = QLabel('Какой национальности не существует?')
answer1 = QRadioButton('Энцы')
answer2 = QRadioButton('Герзинцы')
answer3 = QRadioButton('Алеуты')
answer4 = QRadioButton('Чулымцы')
group_ans = QGroupBox('Варианты ответов:')
group_but = QButtonGroup()
group_but.addButton(answer1)
group_but.addButton(answer2)
group_but.addButton(answer3)
group_but.addButton(answer4)
line_ans1 = QHBoxLayout()
line_ans2 = QVBoxLayout()
line_ans3 = QVBoxLayout()
line_ans2.addWidget(answer1)
line_ans2.addWidget(answer2)
line_ans3.addWidget(answer3)
line_ans3.addWidget(answer4)
line_ans1.addLayout(line_ans2)
line_ans1.addLayout(line_ans3)
group_ans.setLayout(line_ans1)
ansgroup = QGroupBox('Результат теста')
line_ans4 = QLabel('Правильно')
line_ans5 = QLabel('тут будет правильный ответ')
line_res = QVBoxLayout()
line_res.addWidget(line_ans4, alignment=(Qt.AlignLeft))
line_res.addWidget(line_ans5, alignment=(Qt.AlignCenter))
ansgroup.setLayout(line_res)
pubutt = QPushButton('Ответить')
goriz_line1 = QHBoxLayout()
goriz_line2 = QHBoxLayout()
goriz_line3 = QHBoxLayout()
goriz_line1.addWidget(question, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
goriz_line2.addWidget(group_ans)
goriz_line2.addWidget(ansgroup)
ansgroup.hide()

goriz_line3.addStretch(1)
goriz_line3.addWidget(pubutt, stretch=2)
goriz_line3.addStretch(1)
Line = QVBoxLayout()
Line.addLayout(goriz_line1)
Line.addLayout(goriz_line2)
Line.addLayout(goriz_line3)
def show_result():
    ansgroup.show()
    group_ans.hide()
    pubutt.setText('Следующий вопрос')
def show_question():
    ansgroup.hide()
    group_ans.show()
    pubutt.setText('Ответить')
    group_but.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    group_but.setExclusive(True)
spicok=[answer1, answer2, answer3, answer4]
def ask(clque):
    shuffle(spicok)
    spicok[0].setText(clque.right_answer)
    spicok[1].setText(clque.wrong1)
    spicok[2].setText(clque.wrong2)
    spicok[3].setText(clque.wrong3)
    question.setText(clque.question)
    line_ans5.setText(clque.right_answer)
    show_question()
def show_correct(res):
    line_ans4.setText(res)
    show_result()
def check_answer():
    if spicok[0].isChecked():
        show_correct('Правильно')
        scr.numbans +=1
        print('Статистика\nВсего вопросов:',scr.total,'\nПравельные ответы',scr.numbans,'\nРейтинг',scr.numbans/scr.total*100)

    else:
        show_correct('Неправильно')
scr.question_number = -1
def next_question():
    scr.total +=1 


    question_number = randint(0,len(question_list)-1)
    ask(question_list[question_number])
def click():
    if pubutt.text() == 'Ответить':
        check_answer()
    else:
        next_question()



    
    

scr.setLayout(Line)



pubutt.clicked.connect(click)
scr.total = 0
scr.numbans = 0
next_question()
scr.show()
scr.resize(500, 500)
appl.exec()

