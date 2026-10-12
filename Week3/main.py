from custom_classes import MediaItem


def main():
    # İki MediaItem örneği: bir kitap ve bir film
    book = MediaItem("1984", "George Orwell")
    movie = MediaItem("Inception", "Christopher Nolan")

    print("--- Initial state ---")
    print(book)
    print(movie)

    print("\n--- Checking out the book ---")
    print(book.checkout())
    print(book)

    print("\n--- Trying to check out the same book again ---")
    print(book.checkout())

    print("\n--- Final state ---")
    print(book)
    print(movie)

    print("\n--- Returning the book ---")
    book.return_item()
    print(book)


if __name__ == "__main__":
    main()