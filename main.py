import tkinter as tk
from tkinter import ttk

import  sqlite3

app = tk.Tk()
app.title("Система управления заказами")

tk.Label(app, text="Имя клиента").pack()

customer_name_entry = tk.Entry(app)
customer_name_entry.pack()

tk.Label(app, text="Детали заказа").pack()

order_details_entry = tk.Entry(app)
order_details_entry.pack()

add_button = tk.Button(app, text="Добавить заказ")
add_button.pack()

columns = ("id", "customer_name", "order_details", "status")
tree = ttk.Treeview(app, columns=columns, show="headings")
for column in columns:
    tree.heading(column,text=column)
tree.pack()

app.mainloop()