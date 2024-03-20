import os

# Function to create a directory
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created successfully.")
    else:
        print(f"Directory '{directory}' already exists.")

# Function to create a file
def create_file(directory, filename, content=""):
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            file.write(content)
        print(f"File '{filename}' created successfully.")
    else:
        print(f"File '{filename}' already exists.")

# Create project directory
project_dir = "python-tutorials"
create_directory(project_dir)

# Create static directory and its subdirectories
static_dir = os.path.join(project_dir, "static")
create_directory(static_dir)
create_directory(os.path.join(static_dir, "css"))
create_directory(os.path.join(static_dir, "js"))
create_directory(os.path.join(static_dir, "images"))

# Create templates directory
templates_dir = os.path.join(project_dir, "templates")
create_directory(templates_dir)

# Create tutorials directory
tutorials_dir = os.path.join(project_dir, "tutorials")
create_directory(tutorials_dir)

# Create README file
create_file(project_dir, "README.md", "Welcome to my Python Tutorials project!")

# Create index.py file
create_file(project_dir, "index.py")

# Create base.html file
create_file(templates_dir, "base.html", "<html>\n<head>\n</head>\n<body>\n{% block content %}{% endblock %}\n</body>\n</html>")

# Create tutorial.html file
create_file(templates_dir, "tutorial.html", "<html>\n<head>\n</head>\n<body>\n<h1>{{ title }}</h1>\n<div>{{ content }}</div>\n</body>\n</html>")

# Create Markdown files for tutorials
tutorials = [
    "Variables & Memory Management",
    "Numeric Types",
    "Variable Scopes",
    "Closures",
    "Decorators",
    "Sequence Types",
    "Iterables & Iterators",
    "Generators",
    "Context Managers"
]

for tutorial in tutorials:
    filename = f"{tutorial.lower().replace(' ', '_')}.md"
    create_file(tutorials_dir, filename, f"# {tutorial}\n\nWrite your tutorial content here.")

print("Project structure created successfully.")
