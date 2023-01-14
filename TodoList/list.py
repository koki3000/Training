class Task():
    
    def __init__(self, desc, prio):
        self.desc = desc
        self.prio = prio
        
    def __str__(self):
        return f'{self.desc}'


def prio_sort(task):
    return task.prio

def show_list(list):
    list.sort(reverse=True, key=prio_sort)
    cnt = 1
    print('\nTasks:')
    for task in list:
        print(f'{cnt} - {task}')
        cnt += 1
        
if __name__ == '__main__':
    
    menu = """
Menu:
1 - add task
2 - delete task
3 - show tasks
0 - close app
Please select option: """
    
    option = ''
    test1 = Task('pierwsze', 100)
    test2 = Task('drugie', 50)
    test3 = Task('najwazniejsze', 500)
    list = [test1, test2, test3]

    while option != '0':
        option = input(menu)
        if option == '1':
            desc = input('Please input task description: ')
            prio = input('Please input task priority: ')
            new_task = Task(desc, int(prio))
            print(new_task)
            list.append(new_task)
        elif option == '2':
            show_list(list)
            delete = input('Which task do you want to delete: ')
            del list[int(delete)-1]
        elif option == '3':
            show_list(list)
