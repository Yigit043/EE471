from custom_classes import MediaItem, Book, DVD, LibraryCollection


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

    # Part 4: LibraryCollection
    print("\n--- Part 4: Library collection ---")
    library = LibraryCollection()
    library.add_item(Book("The Hobbit", "J.R.R. Tolkien", 310))
    library.add_item(DVD("The Matrix", "The Wachowskis", 136))
    library.add_item(MediaItem("National Geographic", "Various"))
    library.add_item(Book("Sapiens", "Yuval Noah Harari", 443))

    print("Items in the library:")
    for item in library.items:
        print(" -", item)

    print("\nAvailable before checkout:", library.list_available())

    print("\n--- Checking out 2 items ---")
    print(library.items[0].checkout())
    print(library.items[1].checkout())

    print("\nAvailable after checkout:", library.list_available())


if __name__ == "__main__":
    main()