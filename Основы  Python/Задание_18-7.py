import random
# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценку ученика по предмету
        2. Удалить оценку ученика по предмету
        3. Редактировать оценки ученика по предмету
        4. Вывести все оценки по определенному ученику
        5. Вывести средний балл по всем предметам по каждому ученику
        6. Вывести средний балл по каждому предмету по определенному ученику
        7. Вывести все оценки по всем ученикам
        8. Добавить нового ученика
        9. Удалить ученика
        10. Добавить предмет
        11. Удалить предмет
        12. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
        print()
    elif command == 2:
        if command == 2:
            print('2. Удалить оценку ученика по предмету')
            # считываем имя ученика
            student = input('Введите имя ученика: ')
            # считываем название предмета
            class_ = input('Введите предмет: ')
            # считываем оценку
            mark = int(input('Введите оценку, которую нужно удалить: '))
            # если данные введены верно
            if student in students_marks.keys() and class_ in students_marks[student].keys() and mark in marks:
            # удаляем оценку для ученика по предмету
                students_marks[student][class_].remove(mark)
                print(f'Для {student} по предмету {class_} удалена оценка {mark}')
            # неверно введены название предмета, или имя ученика, или оценка
            else:
                print('ОШИБКА: неверное имя ученика, или название предмета, или нет оценки в списке')
            print()
    elif command == 3:
        if command == 3:
            print('3. Редактировать оценки ученика по предмету')
            # считываем имя ученика
            student = input('Введите имя ученика: ')
            # считываем название предмета
            class_ = input('Введите предмет: ')
            # выводим текущие оценки
            print(f'Текущие оценки ученика {student} по предмету {class_}')
            print(f'\t{class_} - {students_marks[student][class_]}')
            # редактируем оценки
            print('Редактируем оценки ученика')
            # считываем номер оценки, которую хотим поменять
            index_marks = int(input('Введите номер оценки, которую хотите поменять, 1-3: '))
            # считываем новую оценку
            new_marks =  int(input('Введите новую оценку: '))
            students_marks[student][class_][index_marks-1] = new_marks
            # выводим новые оценки
            print(f'\t{class_} - {students_marks[student][class_]}')
            print('Оценки отредактированны')
            print()
    elif command == 4:
        print('4. Вывести все оценки по определенному ученику')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # выводим оценки ученика
        print(student)
        for class_ in classes:
            print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 5:
        print('5. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 6:
        print('6. Вывести средний балл по каждому предмету по определенному ученику')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        print(student)
        # находим сумму оценок по предмету
        marks_sum = sum(students_marks[student][class_])
        # находим количество оценок по предмету
        marks_count = len(students_marks[student][class_])
        # выводим средний балл по предмету
        print(f'{class_} - {marks_sum // marks_count}')
        print()
    elif command == 7:
        print('7. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 8:
        print('8. Добавить нового ученика')
        # считываем имя ученика
        new_student = input('Введите имя нового студента: ')
        # добавляем нового ученика и оценки
        students.append(new_student)
        students_marks[new_student] = {
            'Математика':[],
            'Русский язык':[],
            'Информатика':[]
        }
        print('Ученик добавлен')
        # выводим актуальный список учеников
        print('Список учеников:')
        for i in range(len(students)):
            print(f'{i+1}. {students[i]}')
        print()
    elif command == 9:
        print('9. Удалить ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # проверка наличия ученика в списке и удаляем ученика
        if student in students:
            students.remove(student)
            print('Ученик удален')
        else:
            print('Ученика нет в списке')
        # выводим актуальный список учеников
        print('Список учеников:')
        for i in range(len(students)):
            print(f'{i+1}. {students[i]}')
        print()
    elif command == 10:
        print('10. Добавить предмет')
        # считываем название предмета
        new_class_ = input('Введите название нового предмета: ')
        # добавляем предмет и выводим актуальный список
        classes.append(new_class_)
        print('Предмет добавлен')
        print(f'Список предметов:')
        for i in range(len(classes)):
            print(f'{i+1}. {classes[i]}')
        print()
    elif command == 11:
        print('11. Удалить предмет')
        # считываем название предмета
        class_ = input('Введите название предмета: ')
        # проверяем наличие предмета в списке и удаляем предмет
        if class_ in classes:
            classes.remove(class_)
            print('Предмет удален')
        else:
            print('Предмета нет в списке')
        # выводим актуальный список
        print(f'Список предметов:')
        for i in range(len(classes)):
            print(f'{i + 1}. {classes[i]}')
        print()
    elif command == 12:
        print('12. Выход из программы')
        break