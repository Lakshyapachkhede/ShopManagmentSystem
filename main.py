import customer_record
from tkinter import *
import ttkbootstrap as tb
from tkinter import messagebox
import re

root = tb.Window(themename="solar", title="Shop Managment System")
root.geometry("610x500")
root.resizable(False, False)


my_tree = None



def is_valid_email(email):
    # Regular expression for email validation
    pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False




def update_balance(id, value):
    global Customer_details_frame
    if value == '':
        messagebox.showwarning("Update Balance", "Balance must not be Empty")
    else:
        Customer_details_frame.destroy()
        customer_record.update_balance(id, int(value))
        Customer_details(id)



def validate_input(value):
    # Check if the value is empty or consists of digits and/or a plus (+) or minus (-) sign
    if value == "":
        return True
    if value[0] in "+-" and len(value) > 1:
        return value[1:].isdigit()
    return value.isdigit()




def back():
    global Customer_details_frame
    Customer_details_frame.destroy()
    Home_menu()


def left_click(event):
    global my_tree, Home_menu_frame
    item = my_tree.selection()[0]
    selecteed_item_info = my_tree.item(item)["values"]
    Home_menu_frame.destroy()
    Customer_details(customer_record.get_customer_id(selecteed_item_info[0], selecteed_item_info[1]))



def right_click_main_menu(event):
    global my_tree
    item = my_tree.selection()[0]
    selecteed_item_info = my_tree.item(item)["values"]
    right_click_main_menu_widget.post(event.x_root, event.y_root)


def right_click_update_menu(event):
    global my_tree
    item = my_tree.selection()[0]
    selecteed_item_info = my_tree.item(item)["values"]
    right_click_update_menu_widget.post(event.x_root, event.y_root)

def update_customer():
    global Customer_details_frame, my_tree, Home_menu_frame
    item = my_tree.selection()[0]
    selecteed_item_info = my_tree.item(item)["values"]
    Home_menu_frame.destroy()

    Customer_details(customer_record.get_customer_id(selecteed_item_info[0], selecteed_item_info[1]))

def add_customer():
    top = tb.Toplevel(title="Create Customer")
    top.geometry("300x200")
    top.resizable(False, False)

    heading_lbl = tb.Label(top, text="Enter Details", bootstyle='info', font=('Comic Sans MS', 18))
    name_lbl = tb.Label(top, text="Name", bootstyle='primary')
    name_entry = tb.Entry(top, bootstyle='primary')

    phone_lbl = tb.Label(top, text="Phone", bootstyle='primary')
    phone_entry = tb.Entry(top, bootstyle='primary')

    email_lbl = tb.Label(top, text="Email", bootstyle='primary')
    email_entry = tb.Entry(top, bootstyle='primary')

    heading_lbl.grid(row=0, column=0)

    name_lbl.grid(row=1, column=0)
    phone_lbl.grid(row=2, column=0)
    email_lbl.grid(row=3, column=0)

    name_entry.grid(row=1, column=1, sticky="we", padx=(10, 0))
    phone_entry.grid(row=2, column=1, sticky="we", padx=(10, 0))
    email_entry.grid(row=3, column=1, sticky="we", padx=(10, 0))

    confrm_button = tb.Button(top, text="Create", bootstyle='success', command=lambda:confirm_button_function(name_entry.get(), phone_entry.get(), email_entry.get()))
    confrm_button.grid(row=4, column=0, padx=0, pady=20)
    
    def confirm_button_function(name, phone, email):
        global Home_menu_frame
        if name == "":
            messagebox.showwarning("Add Customer", "Name must not be EMPTY.")

        elif not (phone.isdigit() and len(phone) == 10):
            messagebox.showwarning("Add Customer", "Please Enter a valid Phone number.")

        elif not (is_valid_email(email) or email == ""):
            messagebox.showwarning("Add Customer", "Please Enter a valid Email address.")

        else:
            Home_menu_frame.destroy()
            customer_record.create_customer(name, phone, email)
            top.destroy()
            Home_menu()

def delete_customer():
    global my_tree
    item = my_tree.selection()[0]
    selecteed_item_info = my_tree.item(item)["values"]
    selected_item_id = customer_record.get_customer_id(selecteed_item_info[0], selecteed_item_info[1])
    customer_record.remove_customer(selected_item_id, )
    Home_menu_frame.destroy()
    Home_menu()

def update_name(id):
    global Customer_details_frame

    top = tb.Toplevel(title="Update Name")
    top.geometry("180x150")
    instruction_lbl = tb.Label(top, text="Enter new name:", bootstyle='primary', font=('Comic Sans MS', 12))
    new_name_entry = tb.Entry(top, bootstyle='primary')
    ok_button = tb.Button(top, text="Change", bootstyle='success', command=lambda:update_name_button(id, new_name_entry.get()))
    cancel_button = tb.Button(top, text="Cancel", bootstyle='danger', command=top.destroy)

    instruction_lbl.grid(row=0, column=0, columnspan=2, pady=10)
    new_name_entry.grid(row=1, column=0, columnspan=2,padx=10, pady=(0, 5), sticky="ew")
    ok_button.grid(row=2, column=1, padx=15, pady=5)
    cancel_button.grid(row=2, column=0, padx=15, pady=5)

    def update_name_button(id, new_name):
        global Customer_details_frame 
        if new_name == '':
            messagebox.showwarning("Update Name", "Name must not be Empty")
        else:
            top.destroy()
            customer_record.update_name_by_id(id, new_name)
            Customer_details_frame.destroy()
            Customer_details(id)



def update_phone(id):
    global Customer_details_frame

    top = tb.Toplevel(title="Update Phone")
    top.geometry("180x150")
    instruction_lbl = tb.Label(top, text="Enter new Phone:", bootstyle='primary', font=('Comic Sans MS', 12))
    new_name_entry = tb.Entry(top, bootstyle='primary')
    ok_button = tb.Button(top, text="Change", bootstyle='success', command=lambda:update_name_button(id, new_name_entry.get()))
    cancel_button = tb.Button(top, text="Cancel", bootstyle='danger', command=top.destroy)

    instruction_lbl.grid(row=0, column=0, columnspan=2, pady=10)
    new_name_entry.grid(row=1, column=0, columnspan=2,padx=10, pady=(0, 5), sticky="ew")
    ok_button.grid(row=2, column=1, padx=15, pady=5)
    cancel_button.grid(row=2, column=0, padx=15, pady=5)

    def update_name_button(id, new_phone):
        global Customer_details_frame 
        if not (new_phone.isdigit() and len(new_phone) == 10):
            messagebox.showwarning("Update Name", "Please enter a valid phone number.")
        else:
            top.destroy()
            customer_record.update_phone_by_id(id, new_phone)
            Customer_details_frame.destroy()
            Customer_details(id)


def update_email(id):
    global Customer_details_frame

    top = tb.Toplevel(title="Update Email")
    top.geometry("180x150")
    instruction_lbl = tb.Label(top, text="Enter new Email:", bootstyle='primary', font=('Comic Sans MS', 12))
    new_name_entry = tb.Entry(top, bootstyle='primary')
    ok_button = tb.Button(top, text="Change", bootstyle='success', command=lambda:update_name_button(id, new_name_entry.get()))
    cancel_button = tb.Button(top, text="Cancel", bootstyle='danger', command=top.destroy)

    instruction_lbl.grid(row=0, column=0, columnspan=2, pady=10)
    new_name_entry.grid(row=1, column=0, columnspan=2,padx=10, pady=(0, 5), sticky="ew")
    ok_button.grid(row=2, column=1, padx=15, pady=5)
    cancel_button.grid(row=2, column=0, padx=15, pady=5)

    def update_name_button(id, new_email):
        global Customer_details_frame 
        if not(is_valid_email(new_email)):
            messagebox.showwarning("Update Name", "Please enter a valid email")
        else:
            top.destroy()
            customer_record.update_email_by_id(id, new_email)
            Customer_details_frame.destroy()
            Customer_details(id)


# this section is for displaying customers and their information
def Home_menu():

    global Home_menu_frame, my_tree


    Home_menu_frame = tb.Frame(root)
    columns = ("Name", "Phone", "Balance")

    title = tb.Label(Home_menu_frame, text="Yash Kirana", bootstyle='primary', font=('Comic Sans MS', 22))
    my_tree = tb.Treeview(Home_menu_frame, bootstyle='success', columns=columns, show="headings")
    add_customer_button = tb.Button(Home_menu_frame,text="Add Customer", bootstyle='info', command=add_customer)
    my_tree.heading("Name", text="Name")
    my_tree.heading("Phone", text="Phone")
    my_tree.heading("Balance", text="Balance")




    display_list = []
    
    for id in customer_record.get_all_customers_id_list():
        display_list.append((customer_record.get_name_by_id(id), customer_record.get_phone_by_id(id), customer_record.get_balance_by_id(id)))

    for display_item in display_list:
        my_tree.insert("", END, values=display_item)

    Home_menu_frame.pack(fill=BOTH)
    title.grid(row=0, column=0, pady=10, padx=5, sticky="w")
    my_tree.grid(row=1, column=0, sticky="we")
    add_customer_button.grid(row=0, column=0, padx=5, pady=10, sticky="e")
    my_tree.bind("<Button-1>", left_click)
    my_tree.bind("<Button-3>", right_click_main_menu)


#-----------------------------------------------------------------

def Customer_details(id):

    global Customer_details_frame, my_tree, global_id
    global_id = id
    Customer_details_frame = tb.Frame(root)
    back_button = tb.Button(Customer_details_frame,text="<<", bootstyle='success', command=back)
    back_button.grid(row=0, column=0, pady=10)

    heading = tb.Label(Customer_details_frame, text="Customer Details", font=('Comic Sans MS', 20), foreground="white")
    heading.grid(row=0, column=2, pady=10)

    values = customer_record.get_customer_details_by_id(id)

    customer_dict = {
    "Customer ID" : values[0],
    "Customer Name" : values[1],
    "Customer Phone" : values[2],
    "Customer Email" : values[3],
    "Customer Balance" : values[4],

    }

    customer_history = values[5]

    columns = ("Detail", "Value")
    my_tree = tb.Treeview(Customer_details_frame, bootstyle='success', columns=columns, show="headings")

    my_tree.heading("Detail", text="Detail")
    my_tree.heading("Value", text="Value")

    for detail, value in customer_dict.items():
        my_tree.insert("", END, values=(detail, value))

    my_tree.grid(row=1, column=0, columnspan=3, sticky="ew")

    Customer_details_frame.columnconfigure(0, weight=1)
    Customer_details_frame.columnconfigure(1, weight=1)
    Customer_details_frame.columnconfigure(2, weight=1)

    my_tree.bind("<Button-3>", right_click_update_menu)

    update_frame = tb.Frame(Customer_details_frame)
    update_balance_lbl = tb.Label(update_frame,text="Update Balance", bootstyle='secondary')
    update_balance_lbl.grid(row=0, column=0, padx=20)
    validate_cmd = Customer_details_frame.register(validate_input)
    balance_entry = tb.Entry(update_frame, bootstyle='secondary', validate="key", validatecommand=(validate_cmd, "%P"))
    balance_entry.grid(row=0, column=1, padx=20)
    update_button = tb.Button(update_frame, text="Update", command=lambda:update_balance(id, balance_entry.get()))
    update_button.grid(row=0, column=2, padx=20)

    update_frame.grid(row=2, column=0, columnspan=3, sticky="ew", pady=20)


    history_label = tb.Label(Customer_details_frame, text="Customer History", font=('Comic Sans MS', 16), foreground="white")
    history_label.grid(row=3, column=1, pady=10, sticky="w")
    
    customer_history = customer_history + " = " + str(eval(customer_history))

    history_text = tb.Text(Customer_details_frame, height=6, width=50)
    history_text.grid(row=4, column=0, columnspan=3, padx=10, sticky="we")
    history_text.insert(END, customer_history)
    history_text.config(state=DISABLED)


    Customer_details_frame.pack(fill="both")




right_click_main_menu_widget = tb.Menu(root, tearoff=0,)
right_click_main_menu_widget.add_command(label="Add Customer", command=add_customer)
right_click_main_menu_widget.add_command(label="Delete Customer", command=delete_customer)
right_click_main_menu_widget.add_command(label="Update Customer", command=update_customer)

right_click_update_menu_widget = tb.Menu(root, tearoff=0,)
right_click_update_menu_widget.add_command(label="Update Name", command=lambda:update_name(global_id))
right_click_update_menu_widget.add_command(label="Update Phone", command=lambda:update_phone(global_id))
right_click_update_menu_widget.add_command(label="Update Email", command=lambda:update_email(global_id))



if __name__ == '__main__':
    Home_menu()
    root.mainloop()

