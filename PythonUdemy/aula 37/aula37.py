def show_op(lista):
    print(f'A lista de tarefas é:{lista}')


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer!')
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return
    last_redo = redo_list.pop()
    todo_list.append(last_redo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa, undo, redo ou ls: ')

        if todo == 'ls':
            show_op(todo_list)

        elif todo == 'undo':
            do_undo(todo_list, redo_list)
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
        else:
            todo_list.append(todo)
