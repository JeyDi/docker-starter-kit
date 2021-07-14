# Bandit

Bandit is a tool for security code check in Python.

Code security is very important! So always check your code!

References:
- https://calmcode.io/bandit/cli.html

Install bandit
`python -m pip install bandit`

Launch bandit to check the security issues on a single file:
`bandit bad.py`

To test a Python Module or a project:
`bandit -r clumper`

(List of all security test listing)[https://bandit.readthedocs.io/en/latest/plugins/index.html#complete-test-plugin-listing]

The process is:
1. launch bandit in a folder or in a file
2. Check the security issue reference in the documentation
3. Find a possible solution or workaround based on the bandit report

If you want to **avoid** the security check on a specific code line you can add at the end of the line the comment syntax: `#nosec`

You can use Black also as a pre commit hook for the CI/CD automatic pipeline:
```yml
-   repo: https://github.com/Lucas-C/pre-commit-hooks-bandit
    rev: v1.0.5
    hooks:
    -   id: python-bandit-vulnerability-check
        args: [--skip, "B101", --recursive, clumper]
```