import csv
from prettytable import PrettyTable
import pandas as pd


def read_lines():
    with open("tasks.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        tasks = [line for line in reader]
    return tasks


# În prima faza se adaugă categoriile dorite de la tastatură:
# exemplu: Introduceți categoriile de task uri:
def set_categories():
    """Cere definirea categoriilor si le salvează într-un fișier."""
    keep_adding = True
    categories = ''
    while keep_adding:
        category = input('Enter a category name: ').lower()

        # Trebuie să aveți grijă că o categorie poate să existe o singură dată (nu se accepta dubluri, ex curs, cumpărături, muncă, cadouri, curs este greșit)
        while category in categories:
            print()
            category = input('Existing category, please chose a new name: ').lower()
        continue_adding = input('Do you want to add another category? (y/n): ')
        while continue_adding not in 'yn':
            print()
            continue_adding = input('Do you want to add another category\nPlease answer only with `y` or `n`: ')
        keep_adding = True if continue_adding == 'y' else False
        categories += category + ','
    try:
        with open('categories.csv', 'a') as categories_file:
            categories_file.write(categories)
    except FileNotFoundError:
        with open('categories.csv', 'w') as categories_file:
            categories_file.write(categories)


def task_input():
    """Cere date pentru salvarea unui task."""
    ask_for_task = True
    while ask_for_task:
        # se va cere de la tastatura, pe rand introducerea unui task de la tastatura: ex: rezolvare tema
        task = input('Enter task: ')

        # De asemenea, la adăugarea task urilor se va avea grijă și la compararea textelor task urilor, dacă textul respectiv există, nu se poate adăuga.
        try:
            with open("tasks.csv", "r") as f:
                reader = csv.reader(f, delimiter=",")
                tasks = [line[0] for line in reader]
        except FileNotFoundError:
            pass
        while task in tasks:
            print()
            task = input('Existing task! Please enter a new one: ')

        # se va cere introducerea unei date limite de realizare a task-ului respectiv, ex:  02.10.2020 21:30
        deadline = input('Enter deadline for the task: ')

        # se va adăuga o persoană responsabilă cu realizarea task ului respectiv: ex: Ion Vasile
        assigned = input('Enter name of the person assigned to solve the task: ').title()

        # Se va adăuga o categorie din care task-ul face parte. Ex. curs
        with open('categories.csv', 'r') as file:
            existing_categories = file.read()
        category = input(f'Enter category of the task: \nChoices are: {existing_categories} ')

        # Categoria trebuie să existe. În cazul în care nu există, se afișează mesaj de eroare.
        while category not in existing_categories:
            print()
            category = input(f'Selected category is not available, please choose again from available categories. \n'
                             f'Available categories are: {existing_categories} ')

        # Se vor adăuga un număr infinit de task uri, după ce utilizatorul confirmă faptul că a terminat de introdus task
        another_task = input('Do you want to add another task? (y/n) ')
        while another_task not in 'yn':
            print()
            another_task = input('Do you want to add another task?\n'
                                 'Please enter `y` or `n` only: ')
        ask_for_task = True if another_task == 'y' else False

        # Datele se salvează in fișiere.
        try:
            with open('tasks.csv', 'a') as tasks_file:
                tasks_file.write(f'{task},{deadline},{assigned},{category}\n')
        except FileNotFoundError:
            with open('tasks.csv', 'w') as tasks_file:
                tasks_file.write(f'{task},{deadline},{assigned},{category}')
    return True


def options():
    # Se afișează un meniu din care utilizatorul poate alege să realizeze următoarele operații:
    print()
    print('What do you want to do next?\nSelect from the options below by entering the option number:')
    available_options = [
        '0. Exit\n'
        '1. List tasks\n'
        '2. Filter tasks\n'
        '3. Sort tasks\n'
        '4. Add a new task\n'
        '5. Edit a task\n'
        '6. Delete a task\n'
        '7. Add a new category\n'
    ]

    while True:
        try:
            option = int(input(available_options[0]))
            if option in range(8):
                break
        except ValueError:
            print('That is not a valid option, try again... ')
    return option


def list_tasks():
    table = PrettyTable()
    """Listează task-urile salvate."""

    # 1. Listare date: în afișarea inițială a datelor se realizează o sortare în funcție de categorie.
    tasks = read_lines()

    # sortam după categorie
    sorted_by_category = sorted(tasks, key=lambda x: x[3])
    table.field_names = ['Task', 'Date', 'Name', 'Category']
    table.add_rows(sorted_by_category)
    table.align = 'l'
    return table


def filter_tasks():
    table = PrettyTable()
    tasks = read_lines()

    # Criteriile de filtrare sunt: (se cere de la tastatură câmpul după care se realizează filtrarea)
    #  Task, Dată, Persoană responsabilă, Categorie
    column_filter = 'test'
    while column_filter not in 'tndc':
        column_filter = input('What do you want to filter, task/name/date/category ?\n'
                              'Please choose by entering the initial (eg for task enter `t`):  ').lower()

    # după alegerea câmpului de la tastatură se cere introducerea unui string utilizat pentru filtrarea în lista inițială de date,
    # astfel încât din lista inițială să rămână doar datele care conțin / încep cu valoarea introdusă
    if column_filter == 't':
        filtered_list = list(set([row[0] for row in tasks]))
    elif column_filter == 'd':
        filtered_list = list(set([row[1] for row in tasks]))
    elif column_filter == 'n':
        filtered_list = list(set([row[2] for row in tasks]))
    elif column_filter == 'c':
        filtered_list = list(set([row[3] for row in tasks]))

    word_filter = ''
    while word_filter not in filtered_list:
        word_filter = input(f'Enter filter condition:\n'
                            f'Filter conditions MUST match exactly !!!\n'
                            f'Available options are: {filtered_list} ')

    # se afișează lista rămasă
    result_list = [x for x in tasks if word_filter in x]
    table.field_names = ['Task', 'Date', 'Name', 'Category']
    table.add_rows(result_list)
    table.align = 'l'
    return table


def sort_option():
    print('How would you like to sort the tasks? Select from the options:')
    available_options = [
        '1. Ascending order of tasks\n'
        '2. Descending order of tasks:\n'
        '3. Ascending dates\n'
        '4. Descending dates\n'
        '5. Ascending names\n'
        '6. Descending names\n'
        '7. Ascending categories\n'
        '8. Descending categories\n'
    ]
    while True:
        try:
            option = int(input(available_options[0]))
            if option in range(1, 9):
                break
            else:
                print('That is not a valid option, try again... ')
        except ValueError:
            print('That is not a valid option, try again... ')
    return option


def sort_tasks(option):
    table = PrettyTable()
    tasks = read_lines()

    # sortare ascendentă task
    if option == 1:
        sort = sorted(tasks, key=lambda x: x[0])

    #  sortare descendentă task
    elif option == 2:
        sort = sorted(tasks, key=lambda x: x[0], reverse=True)

    #  sortare ascendentă data
    elif option == 3:
        sort = sorted(tasks, key=lambda x: x[1])

    # sortare descendentă data
    elif option == 4:
        sort = sorted(tasks, key=lambda x: x[1], reverse=True)

    # sortare ascendentă persoana responsabilă
    elif option == 5:
        sort = sorted(tasks, key=lambda x: x[2])

    # sortare descendentă persoană responsabilă
    elif option == 6:
        sort = sorted(tasks, key=lambda x: x[2], reverse=True)

    # sortare ascendentă categorie
    elif option == 7:
        sort = sorted(tasks, key=lambda x: x[3])

    # sortare descendentă categorie
    elif option == 8:
        sort = sorted(tasks, key=lambda x: x[3], reverse=True)

    table.field_names = ['Task', 'Date', 'Name', 'Category']
    table.align = 'l'
    table.add_rows(sort)
    return table


def edit_task():
    # 5. Editarea detaliilor referitoare la task, dată, persoană sau categorie
    # dintr-un anumit task ales de utilizator de la tastatură
    tasks = read_lines()
    filtered_tasks = list(set([row[0] for row in tasks]))
    task_to_edit = input('Which task do you want to edit?\n '
                         f'Current tasks are: {filtered_tasks}\n')
    while task_to_edit not in filtered_tasks:
        task_to_edit = input('Which task do you want to edit?\n '
                             'Task must match an existing task\n'
                             f'Current tasks are: {filtered_tasks}\n')
    new_value = input('Enter new task name: ')
    df = pd.read_csv('tasks.csv', names=['Task', 'Date', 'Name', 'Category'])
    index = df.index[df['Task'] == task_to_edit]
    df.loc[index, 'Task'] = new_value
    return df.to_csv('tasks.csv', header=False, index=False)


def delete_task():
    # 6. Ștergerea unui task din lista inițială.
    tasks = read_lines()
    filtered_tasks = list(set([row[0] for row in tasks]))
    task_to_delete = input('Which task do you want to delete?\n '
                           f'Current tasks are: {filtered_tasks}\n')
    while task_to_delete not in filtered_tasks:
        task_to_delete = input('Which task do you want to delete?\n '
                               'Task must match an existing task\n'
                               f'Current tasks are: {filtered_tasks}\n')
    df = pd.read_csv('tasks.csv', names=['Task', 'Date', 'Name', 'Category'])
    # df.drop(df.index[df['Task'] == task_to_delete]) => nu merge!! to debug
    df = df[df.Task != task_to_delete]
    return df.to_csv('tasks.csv', header=False, index=False)


def check_choice(choice):
    if choice == 1:
        return list_tasks()
    elif choice == 2:
        return filter_tasks()
    elif choice == 3:
        option = sort_option()
        return sort_tasks(option)
    elif choice == 4:
        # 4. Adăugarea unui nou task în lista inițială
        return task_input()
    elif choice == 5:
        return edit_task()
    elif choice == 6:
        return delete_task()
    elif choice == 7:
        return set_categories()
    return exit()


def todo_app():
    print(80 * '-')
    print(25 * " ", 'Welcome to your TASKS app!')
    print(80 * '-')
    choice = options()
    while choice != 0:
        check_choice(choice)
        choice = options()


if __name__ == '__main__':
    todo_app()
