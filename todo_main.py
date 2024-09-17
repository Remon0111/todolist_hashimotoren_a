import json
import os
from colorama import init, Fore, Style
import calendar
import datetime

init(autoreset=True)

DB_FILE = 'todos.json'
CONFIG_FILE = 'config.json'
LANG_DIR = 'languages'
LANG_FILE = 'language_en.json'

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    return {"language": "en"}

def save_config(config):
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file, indent=4)

def load_language():
    global LANG_FILE
    config = load_config()
    if config['language'] == 'ja':
        LANG_FILE = 'language_jp.json'
    else:
        LANG_FILE = 'language_en.json'
    with open(os.path.join(LANG_DIR, LANG_FILE), 'r') as file:
        return json.load(file)

LANG = load_language()

def load_todos():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(DB_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

def welcome_message():
    os.system('clear')
    print("\n"+ "\n" + "="*50)
    print(Fore.YELLOW + """
__        __   _                            _          _____         _
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   |_   _|__   __| | ___  
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    | |/ _ \ / _` |/ _ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |   | | (_) | (_| | (_) |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/    |_|\___/ \__,_|\___/ 
    """)
    print("="*50 + "\n")
    dt = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
    print(Fore.YELLOW + f"{dt.strftime('%A')}  -  {datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}" + "\n")
    print(Fore.CYAN + LANG['menu']['showCommand'] + "\n")

def display_menu():
    print(Fore.GREEN + "\n" + "="*50)
    print(Fore.GREEN + " " + LANG['menu']['title'])
    print("="*50)
    for option in LANG['menu']['options']:
        print(Fore.YELLOW + option)
    print(Fore.GREEN + "="*50 + "\n")

welcome_message()

def help_command():
    os.system('clear')
    display_menu()

def add_todo():
    os.system('clear')
    task = input(Fore.CYAN + LANG['messages']['enter_task'])
    task_datetime_Year = input(Fore.CYAN + LANG['messages']['todo_datetime_Year'])
    task_datetime_Month = input(Fore.CYAN + LANG['messages']['todo_datetime_Month'])
    task_datetime_Day = input(Fore.CYAN + LANG['messages']['todo_datetime_Day'])
    task_datetime_Hour = input(Fore.CYAN + LANG['messages']['todo_datetime_Hour'])
    todos = load_todos()
    todos.append({"task": task, "datetime_Year": task_datetime_Year, "datetime_Month": task_datetime_Month, "datetime_Day": task_datetime_Day, "datetime_Hour": task_datetime_Hour, "done": False})
    save_todos(todos)
    print(Fore.GREEN + "\n" + LANG['messages']['todo_added'] + "\n")

def view_todo():
    os.system('clear')
    todos = load_todos()
    if not todos:
        print(Fore.YELLOW + "\n" + LANG['messages']['no_todos'] + "\n")
        return
    print(Fore.GREEN + "\n" + LANG['messages']['your_todos'])
    print(Fore.GREEN + "-"*50)
    for index, todo in enumerate(todos, start=1):
        status = Fore.RED + LANG['status']['not_done'] if not todo["done"] else Fore.GREEN + LANG['status']['done']
        print(Fore.CYAN + f"{index}. {status} {todo['datetime_Year']}/{todo['datetime_Month']}/{todo['datetime_Day']}/{todo['datetime_Hour']} | {todo['task']}")
    print(Fore.GREEN + "-"*50 + "\n")

def update_todo():
    os.system('clear')
    view_todo()
    todos = load_todos()
    if not todos:
        return
    try:
        index = int(input(Fore.CYAN + LANG['messages']['enter_number_update'])) - 1
        if 0 <= index < len(todos):
            todos[index]["task"] = input(Fore.CYAN + LANG['messages']['enter_new_task'])
            todos[index]["datetime_Year"] = input(Fore.CYAN + LANG['messages']['enter_new_datetime_Year'])
            todos[index]["datetime_Month"] = input(Fore.CYAN + LANG['messages']['enter_new_datetime_Month'])
            todos[index]["datetime_Day"] = input(Fore.CYAN + LANG['messages']['enter_new_datetime_Day'])
            todos[index]["datetime_Hour"] = input(Fore.CYAN + LANG['messages']['enter_new_datetime_Hour'])
            save_todos(todos)
            print(Fore.GREEN + "\n" + LANG['messages']['todo_updated'] + "\n")
        else:
            print(Fore.RED + "\n" + LANG['messages']['invalid_number'] + "\n")
    except ValueError:
        print(Fore.RED + "\n" + LANG['messages']['invalid_input'] + "\n")

def calendar_todo():
    os.system('clear')
    now_Month = datetime.datetime.now().month
    now_Year = datetime.datetime.now().year
    dt = datetime.datetime(now_Year, now_Month, datetime.datetime.now().day)
    cal = calendar.monthcalendar(now_Year, now_Month)
    if now_Month in [1, 2, 12]:
        print(Fore.BLUE + str(now_Year) + "/" + str(now_Month) + "/"+ dt.strftime('%B') + "    winter" + "\n")
        print(Fore.CYAN + "SUN" + Fore.WHITE + "MON" + "TUE" + "WEN" + "THU")
    elif now_Month in [3, 4, 5]:
        print(Fore.LIGHTGREEN_EX + str(now_Year) + "/" + str(now_Month) + "/"+ dt.strftime('%B') + "    spring" + "\n")
    elif now_Month in [6, 7, 8]:
        print(Fore.RED + str(now_Year) + " / " + str(now_Month) + " / "+ dt.strftime('%B') + "    Summer" + "\n")
    elif now_Month in [9, 10, 11]:
        print(Fore.LIGHTYELLOW_EX + str(now_Year) + "/" + str(now_Month) + "/"+ dt.strftime('%B') + "    autumn" + "\n")
    print(Fore.RED + "-"*9 + Fore.WHITE + "-"*39 + Fore.BLUE + "-"*9)
    print(Fore.RED + """|  SUN  |  """ + Fore.WHITE + """MON  |  TUE  |  WED  |  THU  |  FRI""" + Fore.BLUE + """  |  SAT  |""")
    print(Fore.RED + "-"*9 + Fore.WHITE + "-"*39 + Fore.BLUE + "-"*9)
    num2 = 0
    for i in range(len(cal)):
        print("""|""", end=" ")
        for j in range(len(cal[num2])):
            if j == 0:
                print("""      | """, end=" ")
            elif j > 0:
                print(f"""{j}    | """, end=" ")
            elif j > 9:
                print(f"""{j}  | """, end=" ")
        num2 += 1
        print("\n" + """|       |       |       |       |       |       |       | """)
        print(Fore.RED + "-"*9 + Fore.WHITE + "-"*39 + Fore.BLUE + "-"*9)

def reporting_todo():
    os.system('clear')
    view_todo()
    todos = load_todos()
    if not todos:
        return
    try:
        index = int(input(Fore.CYAN + LANG['messages']['enter_reporting'])) - 1
        if 0 <= index < len(todos):
            status = input(Fore.CYAN + LANG['messages']['is_done']).strip().lower()
            todos[index]["done"] = status == "yes"
            save_todos(todos)
        else:
            print(Fore.RED + "\n" + LANG['messages']['invalid_number'] + "\n")
    except ValueError:
        print(Fore.RED + "\n" + LANG['messages']['invalid_input'] + "\n")
    print(Fore.GREEN + "\n" + LANG['messages']['todo_reporting'] + "\n")

def delete_todo():
    os.system('clear')
    view_todo()
    todos = load_todos()
    if not todos:
        return
    try:
        index = int(input(Fore.CYAN + LANG['messages']['enter_number_delete'])) - 1
        if 0 <= index < len(todos):
            todos.pop(index)
            save_todos(todos)
            print(Fore.GREEN + "\n" + LANG['messages']['todo_deleted'] + "\n")
        else:
            print(Fore.RED + "\n" + LANG['messages']['invalid_number'] + "\n")
    except ValueError:
        print(Fore.RED + "\n" + LANG['messages']['invalid_input'] + "\n")

def main():
    while True:
        choice = input(Fore.CYAN + LANG['menu']['prompt']).strip().lower()
        if choice in ['help', 'h']:
            help_command()
        elif choice in ['1', 'add todo', 'add', 'a']:
            add_todo()
        elif choice in ['2','view todos', 'view', 'v']:
            view_todo()
        elif choice in ['3', 'updatetodo', 'update', 'u']:
            update_todo()
        elif choice in ['4', 'calendar todo', 'calendar', "c"]:
            calendar_todo()
        elif choice in ['5', 'reporting todo', 'reporting', 'r']:
            reporting_todo()
        elif choice in ['6', 'delete todo', 'delete', 'd']:
            delete_todo()
        elif choice in ['7', 'exit', 'e']:
            os.system("clear")
            print(Fore.BLUE + "\n"+ "\n" + "="*50)
            print(Fore.GREEN + """  ____                 _ _                _ 
 / ___| ___   ___   __| | |__  _   _  ___| |
| |  _ / _ \ / _ \ / _` | '_ \| | | |/ _ \ |
| |_| | (_) | (_) | (_| | |_) | |_| |  __/_|
 \____|\___/ \___/ \__,_|_.__/ \__, |\___(_)
                               |___/        """ + "\n")
            print(Fore.BLUE + "="*50 + "\n")
            break
        else:
            os.system('clear')
            print(Fore.RED + "\n" + LANG['messages']['invalid_choice'] + "\n")

if __name__ == "__main__":
    main()
