__version__ = "0.1.0"


def read_accounts():
    conn = sqlite3.connect('banking_management.db')
    cursor = conn.cursor()
    cursor.execute('Select * From accounts')
    accounts = cursor.fetchall()

    for account in accounts:
        print(account)


    conn.close()
