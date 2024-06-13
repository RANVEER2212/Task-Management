import datetime
import streamlit as st

tasks = {}

def add_task():
    st.header("Add Task")
    task_name = st.text_input("Enter task name:")
    if task_name:
        if task_name in tasks:
            st.warning("Task already exists.")
            return
        task_description = st.text_area("Enter task description:")
        priority = st.selectbox("Enter task priority:", ['low', 'medium', 'high'])
        due_date = st.date_input("Enter due date:")
        
        reminder_year = st.number_input("Reminder Year", min_value=2000, max_value=2100, step=1, value=2024)
        reminder_month = st.number_input("Reminder Month", min_value=1, max_value=12, step=1, value=6)
        reminder_day = st.number_input("Reminder Day", min_value=1, max_value=31, step=1, value=15)
        reminder_hour = st.number_input("Reminder Hour", min_value=0, max_value=23, step=1, value=14)

        if st.button("Add Task"):
            try:
                reminder_date_time = datetime.datetime(reminder_year, reminder_month, reminder_day, reminder_hour)
            except ValueError:
                st.error("Invalid date and time. Please ensure the date is correct.")
                return

            tasks[task_name] = {
                'description': task_description,
                'priority': priority,
                'due_date': due_date,
                'reminder': reminder_date_time,
                'status': 'incomplete'
            }
            st.success("Task added successfully!")

def remove_task():
    st.header("Remove Task")
    task_name = st.text_input("Enter the task name to remove:")
    if st.button("Remove Task"):
        if task_name in tasks:
            del tasks[task_name]
            st.success("Task removed successfully!")
        else:
            st.error("Task not found.")

def update_task():
    st.header("Update Task")
    task_name = st.text_input("Enter the task name to update:")
    if task_name and task_name in tasks:
        option = st.selectbox("What would you like to update?", ["Description", "Priority", "Due Date", "Status", "Reminder"])
        if option == "Description":
            new_description = st.text_area("Enter new description:")
            if st.button("Update Description"):
                tasks[task_name]['description'] = new_description
                st.success("Description updated successfully!")
        elif option == "Priority":
            new_priority = st.selectbox("Enter new priority:", ['low', 'medium', 'high'])
            if st.button("Update Priority"):
                tasks[task_name]['priority'] = new_priority
                st.success("Priority updated successfully!")
        elif option == "Due Date":
            new_due_date = st.date_input("Enter new due date:")
            if st.button("Update Due Date"):
                tasks[task_name]['due_date'] = new_due_date
                st.success("Due date updated successfully!")
        elif option == "Status":
            new_status = st.selectbox("Enter new status:", ['incomplete', 'complete'])
            if st.button("Update Status"):
                tasks[task_name]['status'] = new_status
                st.success("Status updated successfully!")
        elif option == "Reminder":
            new_reminder_year = st.number_input("Reminder Year", min_value=2000, max_value=2100, step=1, value=2024)
            new_reminder_month = st.number_input("Reminder Month", min_value=1, max_value=12, step=1, value=6)
            new_reminder_day = st.number_input("Reminder Day", min_value=1, max_value=31, step=1, value=15)
            new_reminder_hour = st.number_input("Reminder Hour", min_value=0, max_value=23, step=1, value=14)

            if st.button("Update Reminder"):
                try:
                    new_reminder_date_time = datetime.datetime(new_reminder_year, new_reminder_month, new_reminder_day, new_reminder_hour)
                    tasks[task_name]['reminder'] = new_reminder_date_time
                    st.success("Reminder updated successfully!")
                except ValueError:
                    st.error("Invalid date and time. Please ensure the date is correct.")
                return
            else:
                tasks[task_name]['reminder'] = None
                st.success("Reminder removed successfully!")
    elif task_name:
        st.error("Task not found.")

def view_tasks():
    st.header("View Tasks")
    check_reminders()
    if tasks:
        for task_name, details in tasks.items():
            st.markdown(f"**Name:** {task_name}")
            st.markdown(f"**Description:** {details['description']}")
            st.markdown(f"**Priority:** {details['priority']}")
            st.markdown(f"**Due Date:** {details['due_date']}")
            st.markdown(f"**Reminder:** {details['reminder'] if details['reminder'] else 'No reminder set'}")
            st.markdown(f"**Status:** {details['status']}")
            st.markdown("---")
    else:
        st.info("No tasks available.")

def check_reminders():
    now = datetime.datetime.now()
    for task_name, details in tasks.items():
        reminder = details.get('reminder')
        if reminder and reminder <= now:
            st.warning(f"Reminder: Task '{task_name}' is due for a reminder! (Due on {reminder})")

st.title("Task Management System")

menu = ["Add Task", "Remove Task", "Update Task", "View Tasks"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Task":
    add_task()
elif choice == "Remove Task":
    remove_task()
elif choice == "Update Task":
    update_task()
elif choice == "View Tasks":
    view_tasks()
