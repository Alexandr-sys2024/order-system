import tkinter as tk
from tkinter import ttk, messagebox
from database import init_db, add_order, get_orders, complete_order

def add_order_gui():
    add_order(customer_name_entry.get(), order_details_entry.get())
    customer_name_entry.delete(0, tk.END)
    order_details_entry.delete(0, tk.END)
    view_orders()

def view_orders():
    for i in tree.get_children():
        tree.delete(i)
    rows = get_orders()
    for row in rows:
        tree.insert("", tk.END, values=row)

def complete_order_gui():
    selected_item = tree.selection()
    if selected_item:
        order_id = tree.item(selected_item, 'values')[0]
        complete_order(order_id)
        view_orders()
    else:
        messagebox.showwarning("Предупреждение", "Выберите заказ для завершения")

app = tk.Tk()
app.title("Система управления заказами")

tk.Label(app, text="Имя клиента").pack()
customer_name_entry = tk.Entry(app)
customer_name_entry.pack()

tk.Label(app, text="Детали заказа").pack()
order_details_entry = tk.Entry(app)
order_details_entry.pack()

tk.Button(app, text="Добавить заказ", command=add_order_gui).pack()
tk.Button(app, text="Завершить заказ", command=complete_order_gui).pack()

columns = ("id", "customer_name", "order_details", "status")
tree = ttk.Treeview(app, columns=columns, show="headings")
for column in columns:
    tree.heading(column, text=column)
tree.pack()

init_db()
view_orders()
app.mainloop()