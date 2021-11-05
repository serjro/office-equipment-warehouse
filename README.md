**Склад оргтехники.**

1. Реализован класса «Дата», функция-конструктор которого принимает дату в виде строки формата «день-месяц-год». В рамках класса реализовано два метода. Первый, с декоратором @classmethod, извлекает число, месяц, год и преобразовывает их тип к типу «Число». Второй, с декоратором @staticmethod, проводит валидацию числа, месяца и года (например, месяц — от 1 до 12). 
2. Создан собственный класс-исключение, обрабатывающий ситуацию деления на нуль. При вводе пользователем нуля в качестве делителя программа корректно обрабатывает эту ситуацию и не завершиться с ошибкой.
3. Реализован класс-исключение, который проверяет содержимое списка на наличие только чисел, запрашивает у пользователя данные и заполнять список. Класс-исключение контролирует типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Пользователь может вводить только числа и строки. При вводе пользователем очередного элемента реализована проверка типа элемента и вносениек его в список, только если введено число. Класс-исключение не позволяет пользователю ввести текст (не число) и отображает соответствующее сообщение. При этом работа скрипта не завершается.
4. Создан класс, описывающий склад. А также класс «Оргтехника», который является базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определены параметры, общие для приведенных типов. В классах-наследниках реализованы параметры, уникальные для каждого типа оргтехники. 
5. Разработаны методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Реализован механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. Добавлен раздел «Операции с комплексными числами», cоздан класс «Complex»(Комплексное число), добавлена перегрузка методов сложения и умножения комплексных чисел. 
