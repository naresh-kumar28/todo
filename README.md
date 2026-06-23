# Django Todo Application – Learning Journey

## Built a Complete Todo Application with Django

✅ Created a Complete Todo Management System
✅ Implemented Full CRUD Operations
✅ Built Dynamic Templates with Django
✅ Used Django ORM for Database Operations
✅ Implemented Task Filtering & Status Management
✅ Applied Template Inheritance
✅ Integrated Crispy Forms
✅ Added Dynamic Page Titles

---

# PROJECT SETUP & BASICS

1. Create Virtual Environment
2. Activate the Virtual Environment
3. Install Django
4. Update pip
5. Create Project
6. Create App
7. Link App in Settings
8. Create the `urls.py` File in the App
9. Run the Migrate Command
10. Create the Superuser
11. Run the Project
12. Create the Models
13. Register the Models in Admin
14. Login Admin Panel & Add Some Data
15. Create URL Path
16. Create the Views
17. Create Templates Folder
18. Create `home.html` File and Paste the Static Code
19. Write Logic in Views and Fetch the Data from the Database
20. Show Dynamic Data on Homepage

---

# CRUD OPERATIONS

## Add Data from Homepage

1. Create URL Path
2. Create Views
3. Create `add_task.html` File and Paste the Static Code
4. Link Add Task Page URL in Header
5. Template Inheritance
6. Create `base.html`
7. Create `forms.py`
8. Render the Form in Views
9. Install Crispy Forms
10. Write the Logic to Add Task in the Database
11. `order_by('-created_at')`

---

## Edit Task

1. Create URL Path
2. Create Views
3. Create `edit_task.html` File and Paste the Static Code
4. Link Edit Task Page URL in Edit Button
5. Write the Logic to Edit Task in the Database

---

## Delete Task

1. Create URL Path
2. Create Views and Write the Logic to Delete Task
3. Link Delete Task Page URL in Delete Button

---

## Delete All Tasks

1. Create URL Path
2. Create Views and Write the Logic to Delete All Tasks
3. Link Delete All Task Page URL in Clear All Tasks Button

---

## Toggle Task

1. Create URL Path
2. Create Views and Write the Logic to Toggle Task
3. Activate Toggle Task Button

---

# TASK MANAGEMENT FEATURES

## Completed Tasks and Pending Tasks

1. Fetch the Completed Tasks from Database
2. Fetch the Pending Tasks from Database
3. Link Completed Tasks Page URL in Home Page Button
4. Highlight the Button When It Is Active

---

## Filter Pending Tasks

1. Create URL Path
2. Create Views and Write the Logic to Filter Pending Tasks
3. Link Pending Tasks Page URL in Home Page Button
4. Highlight the Button When It Is Active

---

# DYNAMIC PAGE TITLES

### Base Template

```html
<title>{% block title %}{% endblock %}</title>
```

### Home Page

```html
<title>{% block title %}Home - Premium Todo App{% endblock %}</title>
```

### Add Task Page

```html
<title>{% block title %}Add Tasks - Premium Todo App{% endblock %}</title>
```

### Edit Task Page

```html
<title>{% block title %}Edit Tasks - Premium Todo App{% endblock %}</title>
```

---

## Learning Outcome

Through this project, I learned Django project setup, models, admin panel, URL routing, views, templates, forms, CRUD operations, ORM queries, task filtering, template inheritance, crispy forms integration, dynamic page rendering, and complete Todo application development workflow.
