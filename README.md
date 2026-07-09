# Flask Task Manager

This project is a task management web application developed with **Python (Flask)** and **SQLite**. It allows users to organize their tasks by priority, category, and due date.

## About the Project

The application includes the basic **CRUD** operations, along with an intelligent task sorting algorithm and an intuitive user interface to improve the user experience.

## Features

- **Full CRUD Operations:** Create, edit, update, and delete tasks.
- **Smart Sorting Algorithm:** Tasks are automatically sorted based on:
  1. Incomplete tasks first
  2. Priority level (High → Medium → Low)
  3. Due date (nearest first)
- **Priority Management:** Assign **Low**, **Medium**, or **High** priority levels with color-coded labels.
- **Category Management:** Organize tasks into categories such as **School**, **Work**, and **Project**.
- **Due Date Tracking:** Set due dates and automatically highlight overdue tasks.
- **Search Functionality:** Instantly filter tasks by title.
- **User-Friendly Interface:** Responsive interface built with Bootstrap 5, including visual indicators for completed tasks.

## Tech Stack

| Category | Technologies |
|----------|--------------|
| **Backend** | Python, Flask |
| **Database** | SQLite, SQLAlchemy |
| **Frontend** | Bootstrap 5, HTML, CSS |
| **Template Engine** | Jinja2 |
