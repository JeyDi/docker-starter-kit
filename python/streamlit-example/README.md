# Streamlit project example

Streamlit project example.

This is a simple project example with good structure and code organization for dashboard.

The objective of this project is to have a project template for your dashboards.

**Features**:
- Dashboard created with: `Streamlit`
- Beautiful plots with `Plotly`
- Automatic documentation with: `Mkdocs`
- Project organization with `Poetry`
- Linter on the project with: `Flake8`
- Test with `pytest`

## Create the project with Poetry

Follow this steps if you want to create the project from zero.  
Warning = in the project there's already a `pyproject.toml` config file so this commands are not required

```bash
#Initialize the project
poetry init
#compile the 

#Add the libraries
poetry add streamlit matplotlib seaborn plotly plotly-express pandas numpy pytest mkdocs mkdocs-macros-plugin mkdocs-material mkdocstrings mkdocs-autorefs mkdocs-simple-plugin mkdocs-jupyter PyYAML SQLAlchemy

#Add the dev libraries
poetry add -D black bandit flak8 flake8-bandit flake8-isort flake8-builtins

#If you want to use the shell with the venv of the project
poetry shell

#Now you can develop your project
```

## Create the environment in the project

It's important to have installed in your default python (on your machine) the library: `poetry`.

If you want to have a good python tool to manage different python versions use: `pyenv`

If you want to see some documentation about poetry and pyenv please check the documentation or our website (in Italian, sorry...) [Python Biella Group Documentation](https://pythonbiellagroup.github.io/ModernPythonDevelopment)

```bash
#Install the libraries
poetry install

#Launch the project
streamlit run main.py

```

## Launch the Documentation

This project have an automatic documentation system built with `mkdocs`.

To launch the documentation install the dependencies before looking for the previous chapter and then:
```bash
#launch mkdocs in the project
mkdocs serve

```



