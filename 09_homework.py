DEFAULT_DICT = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as error:
            print(f'Unknown command "{error.args[0]}". Try again..')
        except TypeError:
            print(f'Wrong input. Try again..')
        except IndexError:
            print(f'invalid command syntax. Try again..')
        except ValueError as error:
            print(f'Error,{error.args[0]}. Try again...')
    return wrapper
    

@input_error
def get_user_input():
    user_input = input('Enter command: ').lower().split(' ')
    return user_input


@input_error
def get_handler(actions):
    return OPERATIONS[actions]


def hello_func(user_input):
    print('How can I help you?')


@input_error
def add_func(user_input):
    DEFAULT_DICT[user_input[1]] = int(user_input[2])
    print(f'New contact added')


@input_error
def change_func(user_input):
    DEFAULT_DICT[user_input[1]] = int(user_input[2])
    print(f'Phone number has been changed')


@input_error
def phone_func(user_input):
    print(DEFAULT_DICT[user_input[1]])


def show_all_func(user_input):
    print(DEFAULT_DICT)


def break_func(user_input):
    result = 'stop loop'
    print('Good bye!')
    return result

OPERATIONS = {
    'hello': hello_func,
    'add': add_func,
    'change': change_func,
    'phone': phone_func,
    'show all': show_all_func,
    'good bye': break_func,
    'close': break_func,
    'exit': break_func
}

# @input_error
def main():
    
    while True:

        user_input = get_user_input()
        
        if user_input == ['']:
            continue
        elif user_input[0] in 'show':
            actions = 'show all'
        else:
            actions = user_input[0]
        
        handler = get_handler(actions)        
        if handler is None:
            continue
        
        result = handler(user_input)
        if result == 'stop loop':
            break
        
if __name__ == '__main__':
    main()


# def main():

#     while True:
#         user_input = input('Enter command...:').lower()
#         if user_input == 'hello':
#             print('How can I help you?')
#         elif user_input.startswith('add'):
#             splited_input = user_input.split(' ')
#             DEFAULT_DIC[splited_input[1]] = splited_input[2]
#             print(DEFAULT_DIC)
#         elif user_input.startswith('change'):
#             splited_input = user_input.split(' ')
#             DEFAULT_DIC[splited_input[1]] = splited_input[2]
#         elif user_input.startswith('phone'):
#             splited_input = user_input.split(' ')
#             print(DEFAULT_DIC[splited_input[1]])
#         elif user_input.startswith('show all'):
#             print(DEFAULT_DIC)
#         elif user_input.startswith('good bye') or user_input.startswith('close') or user_input.startswith('exit'):
#             print('Good bye!')
#             break
    # if str(user_input).startswith('good bye') or str(user_input).startswith('close') or str(user_input).startswith('exit'):
    #     print('Good bye!')
    #     break
# if handler == break_func:
    #     break

    


"""
Задание
Напишите консольного бота помощника, который будет распознавать команды, вводимые с клавиатуры, 
и отвечать согласно введенной команде.

Бот помощник должен стать для нас прототипом приложения-ассистента. Приложение-ассистент в первом 
приближении должен уметь работать с книгой контактов и календарем. В этой домашней работе сосредоточимся 
на интерфейсе самого бота. Наиболее простой и удобный на начальном этапе разработки интерфейс - это консольное 
приложение CLI (Command Line Interface). CLI достаточно просто реализовать. Любой CLI состоит из трех основных элементов:

Парсер команд. Часть, которая отвечает за разбор введенных пользователем строк, выделение из строки ключевых 
слов и модификаторов команд.
Функции обработчики команд — набор функций, которые ещё называют handler, они отвечают за непосредственное выполнение команд.
Цикл запрос-ответ. Эта часть приложения отвечает за получение от пользователя данных и возврат пользователю 
ответа от функции-handlerа.
На первом этапе наш бот-ассистент должен уметь сохранять имя и номер телефона, находить номер телефона по имени, 
изменять записанный номер телефона, выводить в консоль все записи, которые сохранил. Чтобы реализовать такую 
несложную логику, воспользуемся словарем. В словаре будем хранить имя пользователя как ключ и номер телефона как значение.

Условия
Бот должен находиться в бесконечном цикле, ожидая команды пользователя.
Бот завершает свою работу, если встречает слова: .
Бот не чувствительный к регистру вводимых команд.
Бот принимает команды:
"hello", отвечает в консоль "How can I help you?"
"add ...". По этой команде бот сохраняет в памяти (в словаре например) новый контакт. Вместо ... 
пользователь вводит имя и номер телефона, обязательно через пробел.
"change ..." По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта. Вместо ... 
пользователь вводит имя и номер телефона, обязательно через пробел.
"phone ...." По этой команде бот выводит в консоль номер телефона для указанного контакта. Вместо ... 
пользователь вводит имя контакта, чей номер нужно показать.
"show all". По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.
"good bye", "close", "exit" по любой из этих команд бот завершает свою роботу после того, как выведет в консоль "Good bye!".
Все ошибки пользовательского ввода должны обрабатываться при помощи декоратора input_error. 
Этот декоратор отвечает за возврат пользователю сообщений вида "Enter user name", "Give me name and phone please" и т.п. 
Декоратор input_error должен обрабатывать исключения, которые возникают в функциях-handler 
(KeyError, ValueError, IndexError) и возвращать соответствующий ответ пользователю.
Логика команд реализована в отдельных функциях и эти функции принимают на вход одну или несколько строк и возвращают строку.
Вся логика взаимодействия с пользователем реализована в функции main, все print и input происходят только там.
"""
