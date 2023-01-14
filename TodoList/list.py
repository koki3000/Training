class Task():
    
    def __init__(self, desc, prio):
        self.desc = desc
        self.prio = prio
        
    def __str__(self):
        return f'{self.desc}'


def prio_sort(task):
    return task.prio


class ToDoList:
    list = []
    def __init__(self, list):
        self.list = list
    
    def append_task(self, desc, prio):        
        new_task = Task(desc, int(prio))
        self.list.append(new_task)
    
    def add_task(self):
        desc = input('Please input task description: ')
        prio = input('Please input task priority: ')
        self.append_task(desc, prio)
        
    def delete_task(self):
        self.list.sort(reverse=True, key=prio_sort)
        delete = input('Which task do you want to delete: ')
        del self.list[int(delete)-1]

    def show_list(self):
        self.list.sort(reverse=True, key=prio_sort)
        cnt = 1
        print('\nTasks:')
        for task in self.list:
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
    test_list = [test1, test2, test3]
    list = ToDoList(test_list)

    while option != '0':
        
        option = input(menu)
        if option == '1':
            list.add_task()
        elif option == '2':
            list.show_list()
            list.delete_task()
        elif option == '3':
            list.show_list()