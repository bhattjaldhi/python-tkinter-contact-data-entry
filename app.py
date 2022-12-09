
from tkinter import ttk
from tkinter import *
from model import *
import customtkinter

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"


class App(customtkinter.CTk):

    mode_edit = True
    logged_in = ""

    def __init__(self):
        super().__init__()

        # configure window
        self.title("User data entry")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Data entry", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.btn_add = customtkinter.CTkButton(
            self.sidebar_frame, text="Add", command=self.btn_add_event)
        self.btn_add.grid(row=1, column=0, padx=20, pady=10)
        self.btn_add.grid_forget()

        self.btn_edit = customtkinter.CTkButton(
            self.sidebar_frame, text="Edit", command=self.btn_edit_event)
        self.btn_edit.grid(row=2, column=0, padx=20, pady=10)
        self.btn_edit.grid_forget()

        self.btn_delete = customtkinter.CTkButton(
            self.sidebar_frame, text="Delete", command=self.btn_delete_event)
        self.btn_delete.grid(row=3, column=0, padx=20, pady=10)
        self.btn_delete.grid_forget()

        self.btn_login = customtkinter.CTkButton(
            self.sidebar_frame, text="Login", command=self.btn_login_event)
        self.btn_login.grid(row=1, column=0, padx=20, pady=10)

        self.btn_logout = customtkinter.CTkButton(
            self.sidebar_frame, text="Logout", command=self.btn_logout_event, fg_color="#de5959")
        self.btn_logout.grid(row=5, column=0, padx=20, pady=10)
        self.btn_logout.grid_forget()

        self.btn_close = customtkinter.CTkButton(
            self.sidebar_frame, text="Close", command=self.btn_close_event, fg_color="#de5959")
        self.btn_close.grid(row=6, column=0, padx=20, pady=10)

        # create Treeview
        self.itemTree = ttk.Treeview(self, selectmode="browse")
        self.itemTree["columns"] = ["firstname",
                                    "lastname", "email", "number", "created_by"]
        self.itemTree.grid(row=0, column=1, sticky="nswe", padx=0, pady=0)
        ttk.Style().configure("TreeviewItem", rowheight=30, font=(None, 50))

        # formatting column
        self.itemTree.column("#0", width=0)
        self.itemTree.column("firstname", anchor=W, width=70)
        self.itemTree.column("lastname", anchor=E, width=70)
        self.itemTree.column("email", anchor=E, width=70)
        self.itemTree.column("number", anchor=E, width=70)
        self.itemTree.column("created_by", anchor=W, width=70)

        # Treeview headings
        self.itemTree.heading("#0", text="", anchor=W)
        self.itemTree.heading("firstname", text="First name", anchor=W)
        self.itemTree.heading("lastname", text="Last name", anchor=E)
        self.itemTree.heading("email", text="Email", anchor=E)
        self.itemTree.heading("number", text="Number", anchor=E)
        self.itemTree.heading("created_by", text="Created by", anchor=E)

        # Attach scrollbar to treeview
        self.treeScroll = ttk.Scrollbar(self)
        self.treeScroll.configure(command=self.itemTree.yview)
        self.itemTree.configure(yscrollcommand=self.treeScroll.set)

        self.itemTree.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.treeScroll.grid(row=0, column=2, sticky="nse", padx=0, pady=0)

    # handle logout event
    def btn_logout_event(self):
        self.btn_add.grid_forget()
        self.btn_edit.grid_forget()
        self.btn_delete.grid_forget()
        self.btn_login.grid_configure(row=1, column=0, padx=20, pady=10)
        self.btn_logout.grid_forget()
        for i in self.itemTree.get_children():
            self.itemTree.delete(i)
        self.logged_in = ""

    # handle login event
    def btn_login_event(self):

        self.topLogin = Toplevel(self, bg="gray")
        self.topLogin.title("Login")

        self.topLogin.geometry(f"{500}x{300}")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self.topLogin, width=460)
        self.tabview.grid(row=0, column=0, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Login")
        self.tabview.tab("Login").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Login").grid_columnconfigure(1, weight=3)

        ############ Login ###########
        # username
        label_username = customtkinter.CTkLabel(
            self.tabview.tab("Login"), text="Username:")
        label_username.grid(
            column=0, row=0, sticky=W, padx=5, pady=5)

        self.entry_username = customtkinter.CTkEntry(
            self.tabview.tab("Login"))
        self.entry_username.grid(
            column=1, row=0, sticky=E, padx=5, pady=5)

        # password
        label_password = customtkinter.CTkLabel(
            self.tabview.tab("Login"), text="Password:")
        label_password.grid(
            column=0, row=1, sticky=W, padx=5, pady=5)

        self.entry_password = customtkinter.CTkEntry(
            self.tabview.tab("Login"), show="*")
        self.entry_password.grid(
            column=1, row=1, sticky=E, padx=5, pady=5)

        # error label login
        self.text_login_error = customtkinter.StringVar()
        label_customer_error = customtkinter.CTkLabel(self.tabview.tab(
            "Login"), textvariable=self.text_login_error, text_color="red")
        label_customer_error.grid(column=0, row=4, sticky=W, padx=5, pady=5)

        # button
        btn_customer_submit = customtkinter.CTkButton(self.tabview.tab(
            "Login"), text="Submit", command=self.btn_login_submit)
        btn_customer_submit.grid(column=1, row=3, sticky=E, padx=5, pady=5)

        self.topLogin.mainloop()

    # login user if username and password matches
    def btn_login_submit(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "" or password == "":
            self.text_login_error.set('Please enter username and password')
            return None

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            self.btn_add.grid_configure(row=1, column=0, padx=20, pady=10)
            self.btn_edit.grid_configure(row=2, column=0, padx=20, pady=10)
            self.btn_delete.grid_configure(row=3, column=0, padx=20, pady=10)
            self.btn_logout.grid_configure(row=5, column=0, padx=20, pady=10)
            self.btn_login.grid_forget()
            self.topLogin.destroy()
            self.logged_in = ADMIN_USERNAME
            self.list_records()
            return None

        contact = Contact.select().where((Contact.email == username)
                                         & (Contact.password == password))
        if contact.exists():
            self.btn_add.grid_configure(row=1, column=0, padx=20, pady=10)
            self.btn_edit.grid_configure(row=2, column=0, padx=20, pady=10)
            self.btn_delete.grid_configure(row=3, column=0, padx=20, pady=10)
            self.btn_logout.grid_configure(row=5, column=0, padx=20, pady=10)
            self.btn_login.grid_forget()
            self.topLogin.destroy()
            self.logged_in = contact.get().email
            self.list_records(contact)
            return None

        self.text_login_error.set('Username or password is incorrect')

    # list all records according to user logged in
    def list_records(self, contact=None):
        if contact != None:
            for contact in Contact.select().where((Contact.created_by == self.logged_in) | (Contact.email == self.logged_in)):
                # insert record in the tree view
                self.itemTree.insert(parent='', index='end', values=(
                    contact.first_name, contact.last_name, contact.email, contact.number, contact.created_by))
        else:
            for contact in Contact.select():
                # insert record in the tree view
                self.itemTree.insert(parent='', index='end', values=(
                    contact.first_name, contact.last_name, contact.email, contact.number, contact.created_by))

    # open toplevel window on click of Add button
    def btn_add_event(self):
        self.mode_edit = False
        self.btn_add_edit_event()

    def btn_edit_event(self):
        self.mode_edit = True
        if self.itemTree.focus():
            self.btn_add_edit_event()

    def btn_add_edit_event(self):
        self.top = Toplevel(self, bg="gray")
        self.top.title("Add new entry")

        self.top.geometry(f"{500}x{400}")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self.top, width=460)
        self.tabview.grid(row=0, column=0, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Contact")
        self.tabview.tab("Contact").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Contact").grid_columnconfigure(1, weight=3)

        ############ Contact ###########
        # first name
        label_customer_first_name = customtkinter.CTkLabel(
            self.tabview.tab("Contact"), text="First name:")
        label_customer_first_name.grid(
            column=0, row=0, sticky=W, padx=5, pady=5)

        self.entry_customer_first_name = customtkinter.CTkEntry(
            self.tabview.tab("Contact"))
        self.entry_customer_first_name.grid(
            column=1, row=0, sticky=E, padx=5, pady=5)

        # last name
        label_customer_last_name = customtkinter.CTkLabel(
            self.tabview.tab("Contact"), text="Last name:")
        label_customer_last_name.grid(
            column=0, row=1, sticky=W, padx=5, pady=5)

        self.entry_customer_last_name = customtkinter.CTkEntry(
            self.tabview.tab("Contact"))
        self.entry_customer_last_name.grid(
            column=1, row=1, sticky=E, padx=5, pady=5)

        # email
        label_customer_email = customtkinter.CTkLabel(
            self.tabview.tab("Contact"), text="Email:")
        label_customer_email.grid(column=0, row=2, sticky=W, padx=5, pady=5)

        self.entry_customer_email = customtkinter.CTkEntry(
            self.tabview.tab("Contact"))
        self.entry_customer_email.grid(
            column=1, row=2, sticky=E, padx=5, pady=5)

        # number
        label_customer_number = customtkinter.CTkLabel(
            self.tabview.tab("Contact"), text="Number:")
        label_customer_number.grid(column=0, row=3, sticky=W, padx=5, pady=5)

        self.entry_customer_number = customtkinter.CTkEntry(
            self.tabview.tab("Contact"))
        self.entry_customer_number.grid(
            column=1, row=3, sticky=E, padx=5, pady=5)

        # password
        label_customer_password = customtkinter.CTkLabel(
            self.tabview.tab("Contact"), text="Password:")
        label_customer_password.grid(column=0, row=4, sticky=W, padx=5, pady=5)

        self.entry_customer_password = customtkinter.CTkEntry(
            self.tabview.tab("Contact"), show="*")
        self.entry_customer_password.grid(
            column=1, row=4, sticky=E, padx=5, pady=5)

        # error label
        self.text_customer_error = customtkinter.StringVar()
        label_customer_error = customtkinter.CTkLabel(self.tabview.tab(
            "Contact"), textvariable=self.text_customer_error, text_color="red")
        label_customer_error.grid(column=0, row=5, sticky=W, padx=5, pady=5)

        # button
        btn_customer_submit = customtkinter.CTkButton(self.tabview.tab(
            "Contact"), text="Submit", command=self.btn_customer_submit_event)
        btn_customer_submit.grid(column=1, row=6, sticky=E, padx=5, pady=5)

        # fill entries if it's in edit mode
        if self.mode_edit == True:
            focused_item = self.itemTree.focus()
            values = self.itemTree.item(focused_item)['values']
            self.entry_customer_first_name.insert(0, values[0])
            self.entry_customer_last_name.insert(0, values[1])
            self.entry_customer_email.insert(0, values[2])
            self.entry_customer_number.insert(0, values[3])
            self.entry_customer_email.configure(state="disabled")

        self.top.mainloop()

    # handle delete record event
    def btn_delete_event(self):
        # delete record from the table
        focused_item = self.itemTree.focus()
        email = self.itemTree.item(focused_item)['values'][2]
        query = Contact.get(Contact.email == email)
        query.delete_instance()
        
        selected_item = self.itemTree.selection()[0]
        self.itemTree.delete(selected_item)

    # handle close window event

    def btn_close_event(self):
        self.destroy()

    # event to submit customer entry
    def btn_customer_submit_event(self):
        first_name = self.entry_customer_first_name.get()
        last_name = self.entry_customer_last_name.get()
        email = self.entry_customer_email.get()
        number = self.entry_customer_number.get()
        password = self.entry_customer_password.get()

        record = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'number': number,
            'password': password
        }

        if self.is_validate(record) == True:

            if self.mode_edit == False:
                # insert record in the tree view
                self.itemTree.insert(parent='', index='end', values=(record.get("first_name"), record.get(
                    "last_name"), record.get("email"), record.get("number"), self.logged_in))

                # save record in database
                Contact.create(first_name=first_name,
                               last_name=last_name,
                               email=email,
                               number=number,
                               password=password,
                               created_by=self.logged_in
                               )

            else:
                # update record in database
                contact = Contact.select().where(Contact.email == email).get()
                contact.first_name = record.get('first_name')
                contact.last_name = record.get('last_name')
                contact.number = record.get('number')
                contact.password = record.get('password')
                contact.save()

                focused = self.itemTree.focus()
                self.itemTree.insert("", str(focused)[1:], values=(record.get(
                    "first_name"), record.get("last_name"), record.get("email"), record.get("number"), self.logged_in))
                self.itemTree.delete(focused)

            self.reset_error()
            self.top.destroy()

    # reset validation errors
    def reset_error(self):
        self.text_customer_error.set('')

    # validate user entry
    def is_validate(self, record):

        if record.get("first_name") == "":
            self.text_customer_error.set('Please enter first name')
            return False

        if record.get("last_name") == "":
            self.text_customer_error.set('Please enter last name')
            return False

        if record.get("email") == "":
            self.text_customer_error.set('Please enter email')
            return False

        if record.get("number") == "":
            self.text_customer_error.set('Please enter number')
            return False

        if record.get("password") == "":
            self.text_customer_error.set('Please enter password')
            return False

        # check if user is already exists in the database
        if self.mode_edit !=True and record.get("email") != "":
            contact = Contact.select().where(Contact.email == record.get("email"))
            if contact.exists():
                self.text_customer_error.set('User already exists')
                return False

        return True


if __name__ == "__main__":
    app = App()
    app.mainloop()
