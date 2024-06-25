from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

books = []

class Books(Resource):
    def get(self):
        return {'books': books}, 200

    def post(self):
        book = request.get_json()
        books.append(book)
        return book, 201

class Book(Resource):
    def get(self, book_id):
        if book_id < len(books):
            return books[book_id], 200
        return {'message': 'Book not found'}, 404

    def put(self, book_id):
        if book_id < len(books):
            book = request.get_json()
            books[book_id] = book
            return book, 200
        return {'message': 'Book not found'}, 404

    def delete(self, book_id):
        if book_id < len(books):
            del books[book_id]
            return {'message': 'Book deleted'}, 200
        return {'message': 'Book not found'}, 404

api.add_resource(Books, '/books')
api.add_resource(Book, '/books/<int:book_id>')

@app.route('/countries')
def get_countries():
    countries = list(set(book['country'] for book in books if 'country' in book))
    return jsonify(countries)

if __name__ == '__main__':
    app.run(debug=True)