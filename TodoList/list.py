from list_classes import ToDoList

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