Banking Management System README
Welcome to the Banking Management System README. This document provides an overview of the banking system, its features, setup instructions, and usage guidelines.

Table of Contents
Overview
Features
Setup Instructions
Usage
Contact details
License

## Overview
This project implements a simple banking system in Python using object-oriented programming principles and SQLite for database management. It allows users to perform various account actions such as depositing money, withdrawing funds, changing passwords, and viewing account details.

## Features
Account Actions:
Deposit: Add funds to an existing account.
Withdraw: Remove funds from an existing account.
Change Password: Update the password associated with an account.
Show Account Details: Display account holder's information and balance.

Secure Authentication:
Password validation using a secure method.

Database Management:
SQLite database ("banking_management.db") integration for storing account information securely.

## Setup Instructions
Prerequisites
Python 3.x installed on your system.
SQLite

Installation
Clone the repository:
git clone https://github.com/your_username/banking-system.git
cd banking-system

Install dependencies:
pip install -r requirements.txt

Create the database tables:
python banking_system.py
The system uses SQLite for database operations. Ensure banking_management.db is present and accessible.

## Usage
Run the main program to interact with the banking system:
python main.py

Follow the prompts to perform actions:
Enter account number and password to authenticate.
Select from available actions (C: Change Password, D: Deposit, W: Withdraw, S: Show Account Details, Q: Quit).
Follow on-screen instructions for each action.

## Contact details:
zuha.haider110@gmail.com

## License
This project is licensed under the MIT License - see the LICENSE file for details.