from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list is empty')
def given_empty_todo_list(context):
    context.todo = ToDoList()


@given('the to-do list contains tasks')
def given_todo_list_with_tasks(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(row['Task'])


@given('the to-do list contains tasks with status')
def given_todo_list_with_task_status(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(row['Task'])
        if row['Status'] == 'completed':
            context.todo.mark_completed(row['Task'])

@when('the user adds a task "{task}"')
def when_user_adds_single_task(context, task):
    context.todo.add_task(task)

@when('the user adds the following tasks')
def when_user_adds_multiple_tasks(context):
    for row in context.table:
        context.todo.add_task(row['Task'])

@when('the user lists all tasks')
def when_user_lists_tasks(context):
    context.output = context.todo.list_tasks()

@when('the user marks task "{task}" as completed')
def when_user_marks_task_completed(context, task):
    context.todo.mark_completed(task)


@when('the user clears the to-do list')
def when_user_clears_todo_list(context):
    context.todo.clear_tasks()

@then('the to-do list should contain "{task}"')
def then_todo_list_should_contain_task(context, task):
    tasks = [t['task'] for t in context.todo.list_tasks()]
    assert task in tasks

@then('the output should contain')
def then_output_should_contain_tasks(context):
    expected = [row['Task'] for row in context.table]
    actual = [t['task'] for t in context.todo.list_tasks()]
    for task in expected:
        assert task in actual

@then('the to-do list should show task "{task}" as completed')
def then_task_should_be_completed(context, task):
    for t in context.todo.list_tasks():
        if t['task'] == task:
            assert t['completed'] is True

@then('the to-do list should be empty')
def then_todo_list_should_be_empty(context):
    assert context.todo.list_tasks() == []

@then('the to-do list should still be empty')
def then_todo_list_should_still_be_empty(context):
    assert context.todo.list_tasks() == []

@then('the to-do list should contain')
def then_todo_list_should_contain_tasks(context):
    expected = [row['Task'] for row in context.table]
    actual = [t['task'] for t in context.todo.list_tasks()]
    for task in expected:
        assert task in actual
