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

pokemon = getPoke("Bulbasaur")
print(pokemon['types']) """

import tkinter as tk

window = tk.Tk()
window.title("Pokemon Data")
window.geometry("400x250")
window.resizable(False, False)
prompt=tk.Label(window, text = "Type your message below: ", font = ("Times New Roman", 14))
prompt.pack(pady=10)
entry = tk.Entry(window, font = ("Times New Roman", 14), width = 30)
entry.pack(pady=5)
result_label = tk.Label(window, text="", font=("Times New Roman", 14, "bold"), fg="blue")
result_label.pack(pady=15)
def pokemon_data():
    text = entry.get()
    
window.mainloop()