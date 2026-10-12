from custom_classes import MediaItem, Book, DVD


def main():
    # Part 2: Genel MediaItem örnekleri
    book = MediaItem("1984", "George Orwell")
    movie = MediaItem("Inception", "Christopher Nolan")

    print("--- Part 2: Generic items ---")
    print(book)
    print(movie)
    print(book.checkout())
    print(book)

    # Part 3: Alt sınıflar
    print("\n--- Part 3: Book subclass ---")
    novel = Book("Dune", "Frank Herbert", 412)
    print(novel)

    print("\n--- Part 3: DVD subclass ---")
    dvd = DVD("Interstellar", "Christopher Nolan", 169)
    print(dvd)

    print("\n--- Checking out the DVD ---")
    print(dvd.checkout())
    print(dvd)

    print("\n--- Trying to check out the same DVD again ---")
    print(dvd.checkout())


if __name__ == "__main__":
    main()

