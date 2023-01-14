import pickle
from datetime import datetime

class Task():
    
    def __init__(self, desc, prio):
        self.desc = desc
        self.prio = prio
        self.date = datetime.now()
        
    def __str__(self):
        delta = datetime.now() - self.date
        date = self.date.strftime("%d/%m/%Y")
        
        return f'{self.desc} - created {date}, {delta.days} days ago'


def prio_sort(task):
    return task.prio


class ToDoList:
    
    def __init__(self, file):
        self.file = file
        
        try:
            with open(self.file, 'rb') as file:
                list = pickle.load(file)
        except:
            test1 = Task('first', 100)
            test2 = Task('second', 50)
            test3 = Task('most important', 500)
            test_list = [test1, test2, test3]
            list = test_list
        
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
        for index, task in enumerate(self.list):
            print(f'{index+1} - {task}')
            
    def save(self):
        with open(self.file, 'wb') as file:
            pickle.dump(self.list, file)
        
if __name__ == '__main__':
    
    file_path = 'todo_list.pickle'
    list = ToDoList(file_path)
    menu = """
Menu:
1 - add task
2 - delete task
3 - show tasks
0 - close app
Please select option: """
    
    option = ''

    while option != '0':
        
        option = input(menu)
        if option == '1':
            list.add_task()
        elif option == '2':
            list.show_list()
            list.delete_task()
        elif option == '3':
            list.show_list()
        elif option == '0':
            list.save()
    