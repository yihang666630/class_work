# Personal Library Management System - Starter Code
# Complete the functions below to create a working library system

# Global list to store all books
library = []

def load_library():
    """Load books from file if it exists
    
    Expected file format: "Title by Author (Year) - Genre"
    Example: "1984 by George Orwell (1949) - Dystopian Fiction"
    """
    global library
    filename = "library.txt"
    
    try:
        with open(filename, "r") as f:
            data = f.readlines()
    except FileNotFoundError:
        print("No existing library file found. Starting with empty library.")
        return
    
    # TODO: Parse each line and convert back to book dictionary
    # Hint: Use .split() to break apart the formatted line
    # Hint: Each book should have keys: title, author, year, genre
    for line in data:
        line = line.strip()
        if line:
            # TODO: Parse "Title by Author (Year) - Genre" format
            # Create dictionary and append to library list
            pass
    
    print(f"Loaded {len(library)} books")

def save_library():
    """Save current library to file in readable format"""
    filename = "library.txt"
    
    try:
        with open(filename, "w") as f:
            # TODO: Write each book in format: "Title by Author (Year) - Genre"
            for book in library:
                # TODO: Format book dictionary into string and write to file
                pass
        print("Library saved successfully!")
    except Exception as e:
        print(f"Error saving library: {e}")

def add_book():
    """Add a new book to the library"""
    print("\n--- Add New Book ---")
    
    # TODO: Get book information from user
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    
    # TODO: Get year with error checking (handle invalid input)
    year = 0  # Replace with proper input handling
    
    genre = input("Enter genre: ").strip()
    
    # TODO: Create book dictionary and add to library
    book = {
        # TODO: Fill in dictionary keys and values
    }
    
    library.append(book)
    print(f"Added '{title}' to library!")

def display_library():
    """Display all books in a formatted way"""
    if not library:
        print("Library is empty!")
        return
    
    print(f"\n--- Your Library ({len(library)} books) ---")
    
    # TODO: Sort books by title (use bubble sort or selection sort - no lambda!)
    # Hint: Compare book["title"].lower() for case-insensitive sorting
    
    # TODO: Display each book in a nice format
    for i, book in enumerate(library, 1):
        # TODO: Print book information clearly
        print(f"{i:2d}. Title: {book['title']}")
        # TODO: Add author, year, genre display
        print()

def search_books():
    """Search for books by title or author"""
    if not library:
        print("Library is empty!")
        return
    
    search_term = input("Enter title or author to search for: ").strip().lower()
    matches = []
    
    # TODO: Search through all books
    for book in library:
        # TODO: Check if search term appears in title or author (case-insensitive)
        # Hint: Use .lower() and 'in' operator
        pass
    
    # TODO: Display results
    if matches:
        print(f"\nFound {len(matches)} matching book(s):")
        # TODO: Display matching books
    else:
        print("No books found matching your search.")

def display_stats():
    """Display interesting statistics about the library"""
    if not library:
        print("Library is empty!")
        return
    
    print(f"\n--- Library Statistics ---")
    print(f"Total books: {len(library)}")
    
    # TODO: Count books by genre
    # Hint: Use a dictionary to count occurrences
    genre_counts = {}
    
    # TODO: Find oldest and newest books
    # Hint: Compare book["year"] values
    
    print("\nBooks by genre:")
    # TODO: Display genre counts
    
    print(f"\nOldest book: {0}")  # TODO: Replace with actual oldest year
    print(f"Newest book: {0}")   # TODO: Replace with actual newest year

def main_menu():
    """Display main menu and handle user choices"""
    while True:
        print("\n=== Personal Library Manager ===")
        print("1. Add a book")
        print("2. View all books")
        print("3. Search books") 
        print("4. Library statistics")
        print("5. Save and exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            display_library()
        elif choice == "3":
            search_books()
        elif choice == "4":
            display_stats()
        elif choice == "5":
            save_library()
            print("Thank you for using Library Manager!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

# Main program
if __name__ == "__main__":
    print("Loading library...")
    load_library()
    main_menu()

# TODO List for completion:
# 1. Complete load_library() - parse file format back to dictionaries
# 2. Complete save_library() - format dictionaries to readable text
# 3. Complete add_book() - handle year input validation
# 4. Complete display_library() - implement sorting without lambda
# 5. Complete search_books() - implement case-insensitive search
# 6. Complete display_stats() - count genres and find year ranges