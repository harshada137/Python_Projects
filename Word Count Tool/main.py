def word_count(filename):
    with open(filename, "r") as file:
        text = file.read()

    words = text.split()
    characters = len(text)
    lines = text.count("\n") + 1

    print("Total Words:", len(words))
    print("Total Characters:", characters)
    print("Total Lines:", lines)


def main():
    print("=== Word Count Tool ===")
    filename = input("Enter file name: ")
    word_count(filename)


if __name__ == "__main__":
    main()
