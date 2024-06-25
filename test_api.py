import requests

def add_book(title, author):
    book = {"title": title, "author": author}
    response = requests.post("http://127.0.0.1:5000/books", json=book)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

# Add some books
add_book("To Kill a Mockingbird", "Harper Lee")
add_book("1984", "George Orwell")
add_book("Pride and Prejudice", "Jane Austen")

# Get all books
response = requests.get("http://127.0.0.1:5000/books")
print("\nAll books:")
print(response.json())