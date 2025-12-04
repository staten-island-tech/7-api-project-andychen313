""" import requests
def getPoke(poke):
    requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur")
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

pokemon = getPoke("Pikachu")
print(pokemon['types'],['weight']) """

""" import tkinter as tk

window = tk.Tk()
window.title("Reverse Message")
window.geometry("400x250")
window.resizable(False, False)
prompt=tk.Label(window, text = "Type your message below: ", font = ("Times New Roman", 14))
prompt.pack(pady=10)
entry = tk.Entry(window, font = ("Times New Roman", 14), width = 30)
entry.pack(pady=5)
result_label = tk.Label(window, text="", font=("Times New Roman", 14, "bold"), fg="blue")
result_label.pack(pady=15)
def reverse_message():
    text = entry.get()
    reversed_text = text[::-1]
    result_label.config(text=f"Backwards: {reversed_text}")
reverse_button = tk.Button(window, text="Reverse Message!", font = ("Times New Roman", 14), command=reverse_message)
reverse_button.pack(pady=10)
    
window.mainloop() """

""" from logging import root """
""" import tkinter as tk
import requests
import threading

def receive_api_data():
    try:
        requests.get("https://api-sports.io/documentation/nba/v2")
        response = requests.get("https://api-nba-v1.p.rapidapi.com/seasons/")
        if response.status_code != 200:
            update_label("Error fetching data!")
            return None
        data = response.json()
        update_label(data)
    except Exception as e:
        update_label(f"Error: {e}")
        return {
            "results": data["results"],
            "seasons"
        }

def update_label(text):
    label.config(text = text)

def button():
    threading.Thread(target=receive_api_data, args=("38242",), daemon=True).start()

window = tk.Tk()
window.title("Fun Fact Generator")
window.geometry("400x250")
label = tk.Label(window, text = "Click the button to fetch data.", font = ("Times New Roman", 14), wraplength = 300)
label.pack(pady=20)
result_label = tk.Label(window, text="Fact: ", font=("Times New Roman", 14, "bold"), fg="blue")
result_label.pack(pady=15)
button_fetch = tk.Button(window, text = "Press to fetch facts!", font = ("Times New Roman", 14), command = button)
button_fetch.pack()
window.mainloop() """

import tkinter as tk
import requests
import threading

def receive_api_data(country, year, month, day):
    try:
        url = f"https://holidays.abstractapi.com/v1/"
        paramaters = {
            "country": country,
            "year": year,
            "month": month,
            "day": day,
        }
        response = requests.get(url, params=paramaters)
        if response.status_code != 200:
            update_label("Error fetching data!")
            return None
        data = response.json()
        if not data:
            update_label("Sorry! No holidays found for the given date!")
        update_label(data)
    except Exception as e:
        update_label(f"Error: {e}")
    
def update_label(text):
    result_label.config(text = text)

def button():
    country = entry_country.get().strip().upper()
    year = entry_year.get().strip()
    month = entry_month.get().strip()
    day = entry_day.get().strip()
    
    threading.Thread(target=receive_api_data, args=(country, year, month, day,), daemon=True).start()

root = tk.Tk()
root.title("Public Holiday Generator")
root.geometry("400x250")
label = tk.Label(root, text = "Country:", font = ("Times New Roman", 14), wraplength = 300)
entry_country = tk.Entry(root, font = ("Times New Roman", 14), width = 10)
label.pack(pady = 5)
entry_country.pack(pady = 5)
label_year = tk.Label(root, text = "Year:", font = ("Times New Roman", 14), wraplength = 300)
entry_year = tk.Entry(root, font = ("Times New Roman", 14), width = 10)
label_year.pack(pady = 10)
entry_year.pack(pady = 5)
label_month = tk.Label(root, text = "Month:", font = ("Times New Roman", 14), wraplength = 300)
entry_month = tk.Entry(root, font = ("Times New Roman", 14), width = 10)
label_month.pack(pady = 10)
entry_month.pack(pady = 5)
label_day = tk.Label(root, text = "Day:", font = ("Times New Roman", 14), wraplength = 300)
entry_day = tk.Entry(root, font = ("Times New Roman", 14), width = 10)
label_day.pack(pady = 10)
entry_day.pack(pady = 5)
result_label = tk.Label(root, text = "Holiday Data: ", font = ("Times New Roman", 14, "bold"), fg = "blue")
result_label.pack(pady = 15)


button_fetch = tk.Button(root, text = "Press to fetch holiday data!", font = ("Times New Roman", 14), command = button)
button_fetch.pack()
root.mainloop()