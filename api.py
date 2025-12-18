
""" def receive_api_data(fruits):
    try:
        requests.get("https://www.fruityvice.com/api/fruit/all")
        response = requests.get(f"https://www.fruityvice.com/api/fruit/{fruits.lower()}")
        
        data = response.json()

        update_label(data)
    except Exception as e:
        update_label(f"Error: {e}")

def update_label(text):
    label.config(text=text)

def button_activation():
    fruit_name = entry_name.get().strip().lower()
    threading.Thread(target=receive_api_data, args=(fruit_name,), daemon=True).start()

root = tk.Tk()
root.title("Fruit Data")
root.geometry("900x600")
result_label = tk.Label(root, text = "Fruit Found: ", font = ("Comic Sans", 14, "bold"), fg = "blue")
result_label.pack(pady = 10)
label = tk.Label(root, text = "Fruit: ", font = ("Comic Sans", 14), wraplength = 755, fg = "blue")
entry_name = tk.Entry(root, font = ("Comic Sans", 14), width = 10)
label.pack(pady = 50)
entry_name.pack(pady = 5)


button_fetch = tk.Button(root, text = "Press to fetch fruit data!", font = ("Comic Sans", 14), bg = "black", fg = "white", command = button_activation)
button_fetch.pack(pady = 30)
root.mainloop() """

import requests
import tkinter as tk

root = tk.Tk()
root.title("Fruit Data")
root.geometry("900x600")
root.resizable(False, False)
result_label = tk.Label(root, text = "Fruit Found: ", font = ("Comic Sans", 14, "bold"), fg = "blue")
result_label.pack(pady = 10)
entry = tk.Entry(root, font = ("Comic Sans", 14), width = 10)
entry.pack(pady=10)
name_label = tk.Label(root, text = "", font = ("Comic Sans", 14), wraplength = 755, fg = "blue")
id_label = tk.Label(root, text = "", font = ("Comic Sans", 14), wraplength = 755, fg = "blue")
family_label = tk.Label(root, text = "", font = ("Comic Sans", 14), wraplength = 755, fg = "blue")
nutritions_label = tk.Label(root, text = "", font = ("Comic Sans", 14), wraplength = 755, fg = "blue")
name_label.pack(pady = 10)
id_label.pack(pady = 10)
family_label.pack(pady=10)
nutritions_label.pack(pady=10)

def receive_api_data():
    try:
        fruits = entry.get()
        response = requests.get(f"https://www.fruityvice.com/api/fruit/{fruits.lower()}")
        
        data = response.json()
        name_label.config(text = f"Name: {data["name"]}")
        id_label.config(text = f"Id: {data["id"]}")
        family_label.config(text = f"Family: {data["family"]}")
        nutritions_label.config(text = f"Nutritions: {data["nutritions"]}")
    except Exception:
        name_label.config(text= "Error! Fruit not found!")
        id_label.config(text = "")
        family_label.config(text = "")
        nutritions_label.config(text = "")

button = tk.Button(root, text = "Press to fetch fruit data!", font = ("Comic Sans", 14), bg = "black", fg = "white", command = receive_api_data)
button.pack(pady=40)
root.mainloop()
