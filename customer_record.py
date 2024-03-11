import sqlite3


# conn = sqlite3.connect("customer_record.db")
conn = sqlite3.connect("customer_record.db")
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE Customers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT UNIQUE,
                email TEXT DEFAULT None,
                balance INTEGER DEFAULT 0,
                history TEXT DEFAULT 0
            )
            """)




def create_customer(name, phone, email=None):
    with conn:
        c.execute("INSERT INTO Customers(name, email, phone) VALUES(:name, :email, :phone)", {"name":name, "email":email, "phone":phone})


def update_balance(id, value):
    balance = c.execute("SELECT balance FROM Customers WHERE id=:id", {"id":id}).fetchone()[0]
    balance+=value
    with conn:
        c.execute("UPDATE Customers SET balance=:balance WHERE id=:id", {"id":id, "balance":balance})
    update_history(id, value)



def update_history(id, value):
    history = c.execute("SELECT history FROM Customers WHERE id=:id", {"id":id}).fetchone()[0]

    if history == '0':
        history = value
    else:
        if "-" in str(value):
            history = history + " - " + str(value).removeprefix("-")
        else:
            history = history + " + " + str(value)
    
    with conn:
        c.execute("UPDATE Customers SET history=:history WHERE id=:id",{"history":history, "id":id})

def update_name_by_id(id, new_name):
    with conn:
        c.execute("UPDATE Customers SET name=? WHERE id=?", (new_name, id))

def update_phone_by_id(id, new_phone):
    with conn:
        c.execute("UPDATE Customers SET phone=? WHERE id=?", (new_phone, id))

def update_email_by_id(id, new_email):
    with conn:
        c.execute("UPDATE Customers SET email=? WHERE id=?", (new_email, id))



def remove_customer(id):
    with conn:
        c.execute(f"DELETE FROM Customers WHERE id=?", (id, ))




def get_all_Customers_name():
    with conn:
        unrefined_names = c.execute("SELECT name FROM Customers").fetchall()
    names_list = [name[0] for name in unrefined_names]

    return names_list



def get_all_Customers_phone():
    with conn:
        unrefined_phones = c.execute("SELECT phone FROM Customers").fetchall()
    phones_list = [phone[0] for phone in unrefined_phones]

    return phones_list



def get_all_Customers_email():
    with conn:
        unrefined_emails = c.execute("SELECT email FROM Customers").fetchall()
    emails_list = [email[0] for email in unrefined_emails]

    return emails_list



def get_all_Customers_balance():
    with conn:
        unrefined_balances = c.execute("SELECT balance FROM Customers").fetchall()
    balance_list = [balance[0] for balance in unrefined_balances]

    return balance_list


def get_customer_id(name, phone, email=None):
    if email:
        result = c.execute("SELECT id FROM Customers WHERE name=:name AND email=:email AND phone=:phone", {"name":name, "email":email, "phone":phone}).fetchone()
    else:
        result = c.execute("SELECT id FROM Customers WHERE name=? AND phone=?", (name, phone)).fetchone()

    if result:
        return result[0]
    else:
        return None



def get_customer_details_by_id(id):
    return c.execute("SELECT * FROM Customers WHERE id=?", (id, )).fetchone()
    

def get_name_by_id(id):
    return c.execute("SELECT name FROM Customers WHERE id=?", (id, )).fetchone()[0]



def get_phone_by_id(id):
    return c.execute("SELECT phone FROM Customers WHERE id=?", (id, )).fetchone()[0]



def get_balance_by_id(id):
    return c.execute("SELECT balance FROM Customers WHERE id=?", (id, )).fetchone()[0]


def get_total_number_of_customers():
    return c.execute("SELECT COUNT(*) FROM Customers").fetchone()[0]


def get_maximum_id():
    return c.execute("SELECT MAX(id) FROM Customers").fetchone()[0]


def get_all_customers_id_list():
    id_list = (c.execute("SELECT DISTINCT id FROM Customers").fetchall())
    id_list = [id[0] for id in id_list]
    return id_list







# if __name__ == '__main__':
#     create_table()