import os
import random
import tkinter as tk
import requests
import zipfile

# URL for the phrase set zip file
url = "http://www.yorku.ca/mack/PhraseSets.zip"
zip_file = "PhraseSets.zip"
data_folder = "Data"
phrase_file = os.path.join(data_folder, "phrases2.txt")

def fetch_and_unzip():
    print("Fetching the zip file...")
    response = requests.get(url)
    with open(zip_file, "wb") as f:
        f.write(response.content)
    print("Unzipping the file...")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(data_folder)
    print("File unzipped successfully.")

def load_phrases():
    with open(phrase_file, "r") as file:
        phrases = [line.strip() for line in file.readlines()]
    return phrases

if not os.path.exists(data_folder):
    os.makedirs(data_folder)

if not os.path.exists(phrase_file):
    if not os.path.exists(zip_file):
        fetch_and_unzip()
    else:
        print("Zip file already exists. Unzipping...")
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(data_folder)

phrases = load_phrases()

current_phrase = None

def show_random_phrase(event=None):
    global current_phrase
    new_phrase = random.choice(phrases)
    while new_phrase == current_phrase:
        new_phrase = random.choice(phrases)
    current_phrase = new_phrase
    label.config(text=current_phrase)

root = tk.Tk()
root.title("Random Phrases")
root.state('zoomed')
root.configure(background='black')
label = tk.Label(root, text="", font=("Helvetica", 48), fg="white", bg="black", wraplength=root.winfo_screenwidth(), justify="center")
label.pack(expand=True)

root.bind("<Button-1>", show_random_phrase)
show_random_phrase()

root.mainloop()
