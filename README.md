# 🛤️ Bellman-Ford algorithm 

## Table of Contents

- [Overview](#overview)
- [Technologies](#technologies)
- [Folder Organization](#folder-organization)
- [Setup](#setup)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Overview: Key Functionalities

This project implements a shortest path finder using both Flask and Streamlit. Users can input graph data and retrieve the shortest path between vertices.

## Structure
- **Flask App**
  - **app.py**: Main Flask application logic.
  - **templates/**: Directory containing HTML templates.
    - **form.html**: Input form for graph data.
    - **result.html**: Display results (distance and path).
  - **servicees.py**: is the main class which performs the Bellman-Ford algorithm 

- **Streamlit App**
  - **main.py**: Main Streamlit application logic for the same functionality.

## Features
- Users can input:
  - Number of vertices.
  - Edges in JSON format.
  - Start and end vertices.
  - Maximum number of stops.
- Displays the shortest path and its distance for both Flask and Streamlit applications.


# Tools & Libraries Used

# Tools and Libraries Used

1. **Programming Language**: [![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=yellow)](https://www.python.org/)
2. **Web Framework**: [![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
3. **Web Application Framework**: [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B24?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)


## Folder Organization

```

📁.templates
└──
    └── 🌐form.html
    └── 🌐result.html

🐍algorithm.py
🐍app.py
🐍main.py
📝README.md
🐍services.py
📝requirements.txt

```

### Folder Structure: A Deep Dive

- **📁 templates**: This folder contains HTML files for user interaction
  - **🌐 `form.html`**: Input collection form
  - **🌐 `result.html`**: Displays the results

- **🐍 `algorithm.py`**: Contains the Bellman-Ford algorithm general implementation 
- **🐍 `app.py`**: Main application logic for Flask
- **🐍 `main.py`**: Entry point for the Streamlit app
- **📝 `README.md`**: Documentation for the project
- **🐍 `services.py`**: Contains the Bellman-Ford algorithm and performs the operaion by accepting input from the user
- **📝 `requirements.txt`**: List of dependencies for the project

## Setup

1. Clone the repo

```bash
git clone https://github.com/Bereket-07/User_Analysis_and_Engagement.git
```

2. Change directory

```bash
cd my_repo_name
```

3. Install all dependencies

```bash
pip install -r requirements.txt
```
5. Start the Flask app

```bash
python  app.py
```

5. Start the streamlit app

```bash
streamlit run main.py
```

## Contributing

We welcome contributions to this project! To get started, please follow these guidelines:

### How to Contribute

1. **Fork the repository**: Click the "Fork" button at the top right of this page to create your own copy of the repository.
2. **Clone your fork**: Clone the forked repository to your local machine.
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
3. **Create a new branch**: Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature/your-feature
   ```
4. **Make your changes**: Implement your feature or fix the bug. Ensure your code adheres to the project's coding standards and style.
5. **Commit your changes**: Commit your changes with a descriptive message.
   ```bash
   git add .
   git commit -m 'Add new feature or fix bug'
   ```
6. **Push your branch**: Push your branch to your forked repository.
   ```bash
   git push origin feature/your-feature
   ```
7. **Create a Pull Request**: Go to the repository on GitHub, switch to your branch, and click the `New Pull Request` button. Provide a detailed description of your changes and submit the pull request.

## Additional Information

- **Bug Reports**: If you find a bug, please open an issue in the repository with details about the problem.

- **Feature Requests**: If you have ideas for new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License

### Summary

The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). It is a simple and easy-to-understand license that places very few restrictions on reuse, making it a popular choice for open source projects.

By using this project, you agree to include the original copyright notice and permission notice in any copies or substantial portions of the software.
