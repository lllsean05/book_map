import requests

url = 'http://127.0.0.1:5000/books'
books = [
    {"title": "Forest Gump", "country": "USA"},
    {"title": "A Crane Among Wolves", "country": "Canada"},
    {"title": "Flow by the wind", "country": "USA"},
    {"title": "The Little Prince", "country": "France"},
    {"title": "The Metamorphosis", "country": "Germany"},
    {"title": "Mango Trees", "country": "Brazil"},
    {"title": "Meet Me at the Lake", "country": "Canada"},
    {"title": "Norwegian Wood", "country": "Japan"},
    {"title": "The Fatal Shore", "country": "Australia"},
    {"title": "The God of Small Things", "country": "India"}
]

for book in books:
    response = requests.post(url, json=book)
    print(response.json())
