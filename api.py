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
    