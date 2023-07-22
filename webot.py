# User detail
user_info = {
    "name": input('Enter your name: '),
    "work": input("Enter your work: "),
    "projects": [ 
        {"name": "project 1", "description": "this is my project"},
        {"name": "project 2", "description": "this is my project"},
    ],
    "contact":{
        "email": input('Enter your email: '),
        "phone": input('Enter your phone number: '),
    }
}

# HTML template
homepage_template = """
<!DOCTYPE html>
<html>
<head>
    <title>{name} - Personal Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>{name}</h1>
    </header>
    <nav>
        <ul>
            <li><a href="#about">About</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    <main>
        <section id="about">
            <h2>About Me</h2>
            <p>I am a passionate {work}</p>
        </section>
        <section id="projects">
            <h2>Projects</h2>
            <ul>
                {projects}
            </ul>
        </section>
        <section id="contact">
            <h2>Contact</h2>
            <ul>
                <li>Email: <a href="mailto:{email}">{email}</a></li>
                <li>Phone: {phone}</li>
            </ul>
        </section>
    </main>
    <footer>
        <p>&copy; {name} {year}</p>
    </footer>
</body>
</html>
"""

project_template = """
    <li>
        <h3>{name}</h3>
        <p>{description}</p>
    </li>
"""

# Generate project list
project_list = ""
for project in user_info["projects"]:
    project_list += project_template.format(name=project["name"], description=project["description"])

# Get the current year
from datetime import datetime
current_year = datetime.now().year

# Combine all data with HTML template
homepage = homepage_template.format(
    name=user_info["name"],
    work=user_info["work"],
    projects=project_list,
    email=user_info["contact"]["email"],
    phone=user_info["contact"]["phone"],
    year=current_year
)

# Save the generated HTML to a file
with open('index.html', 'w') as file:
    file.write(homepage)
