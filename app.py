from flask import Flask, render_template, request

app = Flask(__name__)

books = [
    {"Title": "Harry Potter and the Sorcerer’s Stone", "Author": "J.K. Rowling", "Available": "Yes"},
    {"Title": "1984", "Author": "George Orwell", "Available": "Yes"},
    {"Title": "The Hound of the Baskervilles", "Author": "Arthur Conan Doyle", "Available": "Yes"},
]

def search_books(query):
    query = query.lower()
    return [book for book in books if query in book["Title"].lower() or query in book["Author"].lower()]

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        query = request.form.get("query")
        results = search_books(query)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
