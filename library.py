"""
Library Management System

- Manage books using dictionaries and lists.
- Each book: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- *args for searching (title, author).
- **kwargs for adding flexible details (year, genre, etc.).
"""

library = []

def add_book(id, title, author, **kwargs):
    """Add a new book into the library with flexible details."""
    book = {
        "id": id,
        "title": title,
        "author": author,
        "available": True
    }
    # Add optional details (like year, genre)
    for key, value in kwargs.items():
        book[key] = value

    library.append(book)
    return f"Book '{title}' added successfully!"


def search_books(*search_params):
    """Search for books by multiple keywords (title, author)."""
    results = []
    for book in library:
        for param in search_params:
            if (param.lower() in book["title"].lower()) or (param.lower() in book["author"].lower()):
                results.append(book)
                break  # avoid duplicates
    return results


def borrow_book(book_id):
    """Borrow a book if available."""
    for book in library:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                return f"You borrowed '{book['title']}'."
            else:
                return f"Book '{book['title']}' is not available."
    return f"Book with ID {book_id} not found."


def return_book(book_id):
    """Return a borrowed book."""
    for book in library:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                return f"You returned '{book['title']}'."
            else:
                return f"Book '{book['title']}' was not borrowed."
    return f"Book with ID {book_id} not found."


# --- Demo ---
print(add_book(1, "Python Basics", "John Doe", year=2021, genre="Programming"))
print(add_book(2, "AI for Beginners", "Jane Smith"))
print(add_book(3, "Data Structures", "Alice Johnson", year=2019))

print("\n--- Search Results ---")
print(search_books("Python", "Jane"))

print("\n--- Borrowing ---")
print(borrow_book(1))
print(borrow_book(1))

print("\n--- Returning ---")
print(return_book(1))
print(return_book(1))

print("\n--- Library State ---")
print(library)

