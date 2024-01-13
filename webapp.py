import streamlit as st
import function

todos = function.get_todos()


def add_todo():
    new_todo = st.session_state["add_new_todo"]+"\n"
    todos.append(new_todo)
    function.write_todos(todos)


st.title("My To Do App")
st.subheader("this is my todo app")
st.write("this is use to productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",  placeholder="add new todo",
              on_change=add_todo, key="add_new_todo")
