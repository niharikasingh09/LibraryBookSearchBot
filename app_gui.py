import tkinter as tk
from tkinter import scrolledtext

# Dummy data for demo (replace with your actual search function)
books = [
    {"Title": "Harry Potter and the Sorcerer’s Stone", "Author": "J.K. Rowling", "Available": "Yes"},
    {"Title": "1984", "Author": "George Orwell", "Available": "Yes"},
    {"Title": "The Hound of the Baskervilles", "Author": "Arthur Conan Doyle", "Available": "Yes"},
]

def search_books(query):
    query = query.lower()
    results = [book for book in books if query in book["Title"].lower() or query in book["Author"].lower()]
    return results

def on_search():
    query = entry.get()
    results = search_books(query)
    output.delete('1.0', tk.END)
    if results:
        output.insert(tk.END, "📖 Matching Books:\n")
        for book in results:
            output.insert(tk.END, f"{book['Title']} by {book['Author']} - Available: {book['Available']}\n")
    else:
        output.insert(tk.END, "No matching books found.")

# Create window
window = tk.Tk()
window.title("Library Book Search Bot")

# Input box
tk.Label(window, text="Enter book title or author:").pack()
entry = tk.Entry(window, width=50)
entry.pack()

# Search button
search_button = tk.Button(window, text="Search", command=on_search)
search_button.pack()

# Output text area
output = scrolledtext.ScrolledText(window, width=60, height=15)
output.pack()

window.mainloop()
