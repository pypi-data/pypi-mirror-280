from setuptools import setup, find_packages

setup(
    name="checkers-imp-adv-coding-proj",
    version="0.1.8",
    author="Christian DY",
    author_email="techscreed@gmail.com",
    description="Checkers implementation in python based on the international draughts",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={
        'checkers_main': ['static/*.png', "static/*.ttf", "static/images/*.png", "static/images/checkers.png"],  # Adjust the pattern to match your static file extensions
    },
    install_requires=[
        "pillow",
        "pygame",
        "setuptools"
    ],
    entry_points={
        "console_scripts": [
            "run_checkers_round=checkers_main:main",
        ]
    }
)


