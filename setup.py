from setuptools import find_packages, setup

print("Hello, world!")


def read_requirements():
    with open("requirements.txt", "r") as req_file:
        return req_file.readlines()


setup(
    name="improved-spork",
    version="0.1.0",
    packages=find_packages(),
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            # If you want to create command-line executables, you can define them here.
            # e.g.: 'my-command=your_project_name.framework.main:main',
        ],
    },
    python_requires=">=3.9",  # Adjust this to your desired minimum Python version
)
