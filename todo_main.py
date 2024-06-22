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
    print("\n"+ "\n" + "="*40)
    print(Fore.YELLOW+"""
__        __   _                            _          _____         _
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   |_   _|__   __| | ___  
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    | |/ _ \ / _` |/ _ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |   | | (_) | (_| | (_) |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/    |_|\___/ \__,_|\___/ 
""")
    print("="*40 + "\n")
welcome_message()

def display_menu():
    print(Fore.GREEN + "\n" + "="*40)
    print(Fore.GREEN + " " + LANG['menu']['title'])
    print("="*40)
    for option in LANG['menu']['options']:
        print(Fore.YELLOW + option)
    print(Fore.GREEN + "="*40 + "\n")

def help_command():
    display_menu()

def add_todo():
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
    todos = load_todos()
    if not todos:
        print(Fore.YELLOW + "\n" + LANG['messages']['no_todos'] + "\n")
        return
    print(Fore.GREEN + "\n" + LANG['messages']['your_todos'])
    print(Fore.GREEN + "-"*40)
    for index, todo in enumerate(todos, start=1):
        status = Fore.RED + LANG['status']['not_done'] if not todo["done"] else Fore.GREEN + LANG['status']['done']
        print(Fore.CYAN + f"{index}. {status} {todo['datetime_Year']}/{todo['datetime_Month']}/{todo['datetime_Day']}/{todo['datetime_Hour']} | {todo['task']}")
    print(Fore.GREEN + "-"*40 + "\n")

def update_todo():
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
    now_Month = datetime.datetime.now().month
    print(calendar.month(2023, now_Month, w=3, l=2))

def reporting_todo():
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

def delete_todo():
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
        elif choice in ['1', 'add', 'a']:
            add_todo()
        elif choice in ['2', 'view', 'v']:
            view_todo()
        elif choice in ['3', 'update', 'u']:
            update_todo()
        elif choice in ['4', 'calendar', "c"]:
            calendar_todo()
        elif choice in ['5', 'reporting', 'r']:
            reporting_todo()
        elif choice in ['6', 'delete', 'd']:
            delete_todo()
        elif choice in ['7', 'exit', 'e']:
            print(Fore.GREEN + "\n" + LANG['messages']['goodbye'] + "\n")
            break
        else:
            print(Fore.RED + "\n" + LANG['messages']['invalid_choice'] + "\n")

if __name__ == "__main__":
    main()
