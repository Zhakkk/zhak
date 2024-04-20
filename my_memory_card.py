from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle
from random import randint
class Question():
    def __init__(
self, question, right_answer, 
wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
q1 = Question('Что будет более удобным для создания сайта?','HTML','C','Unity','Python')
question_list.append(q1)
q2 = Question('Кто создал С++?', 'Бьёрн Страуструп', 'Марк Цукерберг', 'Герб Саттер', "Джузеппе Гарибальди")
question_list.append(q2)
q3 = Question('Какую последовательность создания (отрисовки) квадрата?',' from turtle import* /for i in range(4):/forward(100)/right(90)', 'from turtle import* /for i in range(4):/forward(100)/right(20)',  'from turtle import*/for i in range(7):/forward(100)/right(20)','from turtle import* /for i in range(4):/forward(100)/right(90))')
question_list.append(q3)
q4 = Question('Кто создал чат gpt?', 'OpenAI', 'Сэр Тим Бернерс-Ли', 'CloseAI', 'Деннис Ритчи')
question_list.append(q4)
q5 = Question('Для чего больше подходит массив данных типа dict?', 'Хранение данных в библиотеке', 'Хранение кол-ва заработанных магазином денег', 'Отрисовка квадрата', 'Хранение последовательности цифр, только с целью вычислить среднее арифметическое')
question_list.append(q5)
q6 = Question('Массив данных LIFO (last in, first out)', 'queue','stack','list','dict')
question_list.append(q6)
q7 = Question('Что нужно поставить после dict?', '()', '>>', '<<', "[]")
question_list.append(q7)
q8 = Question('какое маскимальное значение в 32-х битной системе исчесления?', ' 2147483647','2147483646','2^64','18446744073709551616')
question_list.append(q8)
q9 = Question('Один из популярных языков для написания блокчейна?', 'Solidity','PHP', 'ReCycle', 'AllSafe')
question_list.append(q9)

def show_result():
    AnswerGroupBox.show()
    RadioGroupBox.hide()
    button.setText('Следующий вопрос')
    check_answer()

def show_question():
    AnswerGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)    
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    main_win.number_question += 1
    ask(question_list[main_win.number_question%len(question_list)])

def start_test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_question()

def ask(q: Question):
    shuffle(answers)
    answer_text.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

def check_answer():
    main_win.count_question += 1
    if answers[0].isChecked():
        main_win.count_true_answers+=1
        resultQuestion.setText('Правильно')
        answer.setText('Вы молодец!'
        + f'\nСтатистика вопросов и ответов: {main_win.count_true_answers}/{ main_win.count_question}')
    else:
        resultQuestion.setText('Неправильно')
        answer.setText('Правильный ответ: ' + answers[0].text()
        + f'\nСтатистика вопросов и ответов: {main_win.count_true_answers}/{main_win.count_question}' )


app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)


main_win.number_question = 0
main_win.count_question = 0
main_win.count_true_answers = 0

#Форма для вопроса
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

#Создание группы объектов для отображения результата
AnswerGroupBox = QGroupBox("Результат теста:")
resultQuestion = QLabel('Неправильно')
answer = QLabel('Правильный ответ')
answerLayout = QVBoxLayout()
answerLayout.addWidget(resultQuestion)
answerLayout.addWidget(answer, alignment=Qt.AlignCenter)
AnswerGroupBox.setLayout(answerLayout)



#Верхняя надпись. Сам вопрос
answer_text = QLabel('Какой национальности не существует?')
#Кнопка ответить
button = QPushButton('Ответить')
button.clicked.connect(start_test)

#Самый главный лэяут
total_layout = QVBoxLayout()
total_layout.addWidget(answer_text, alignment=Qt.AlignCenter)
total_layout.addWidget(answer_text, alignment=Qt.AlignCenter)
total_layout.addWidget(RadioGroupBox)
total_layout.addWidget(AnswerGroupBox)
total_layout.addWidget(button, alignment=Qt.AlignCenter)

AnswerGroupBox.hide()


main_win.setLayout(total_layout)

main_win.show()
app.exec_()