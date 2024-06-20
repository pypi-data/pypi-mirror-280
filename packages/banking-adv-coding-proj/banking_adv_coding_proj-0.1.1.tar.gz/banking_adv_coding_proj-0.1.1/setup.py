from setuptools import setup, find_packages 

setup(
    name = "banking-adv-coding-proj",
    version = " 0.1.1",
    author = "Zuha Haider",
    author_email = "zuha.haider110@gmail.com",
    description = "A banking system that helps you deposit, withdraw, change account password and shows you your account details.",
    long_description = open("README.md").read(),
    long_description_content_type="text/markdown",
    packages= find_packages(),
    package_data={
        'mypackage' : ['static/*.png', "static/*.ttf"],
    },
    
    entry_point={
        "console_scripts": [
            "run=main",
            "read=options:read_accounts"

        ]
    }
)

