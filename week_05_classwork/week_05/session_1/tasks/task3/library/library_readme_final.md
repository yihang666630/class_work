# Personal Library Management System

**Estimated Time:** 3-5 total human hours
**Difficulty:** ⭐⭐⭐ (Intermediate)  
**Prerequisites:** File I/O, dictionaries, functions, loops  
**Good for:** Students who want structured, achievable goals

## Quick Start Guide

### Phase 1: Get Basic Structure Working (60 minutes)
1. Focus on getting basic add/display functionality working first
2. Use simple print statements to test your data structures
3. Don't worry about file persistence initially

### Phase 2: Add File Operations (90 minutes)
4. Add file saving functionality once core features work
5. Test save/load with simple text format
6. Handle file not found errors gracefully

### Phase 3: Include Search Features (60 minutes)
7. Implement search functionality  
8. Add input validation and error handling
9. Improve user interface and formatting

## Core Requirements (Must Complete)

1. **Data Structure**: Create a list to hold books, where each book is a dictionary with keys: title, author, year, and genre
2. **Add Books**: Implement function to add new books with customer prompted to add details
3. **File Saving**: Save books to 'library.txt' in readable format
4. **File Loading**: Load books from 'library.txt' at program start
5. **Display Library**: Show all books in user-friendly format
6. **Search Feature**: Search books by title or author
7. **Menu System**: Main loop with menu for all operations

## Extension Ideas (Optional - Choose 1-2)

- **Import Data**: Use the provided books.csv for additional book information
- **Categories**: Add genre filtering and organization
- **Sorting**: Sort books by title, author, or year
- **Export Options**: Save library in different formats (CSV, formatted text)
- **Borrowing System**: Track which books are lent out and to whom
- **Ratings**: Add personal ratings and review system

## Data Structure Examples

### Book Dictionary
```python
book = {
    "title": "1984",
    "author": "George Orwell", 
    "year": 1949,
    "genre": "Dystopian Fiction"
}
```

### Library List
```python
library = [
    {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian Fiction"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction"}
]
```

## File Format Suggestion

Choose a simple, readable format for your library.txt file:
```
1984 by George Orwell (1949) - Dystopian Fiction
To Kill a Mockingbird by Harper Lee (1960) - Fiction
The Great Gatsby by F. Scott Fitzgerald (1925) - Classic Literature
```

## Implementation Tips

### File Operations
- Use try/except for file operations to handle missing files
- Open files in append mode ('a') if you want to preserve existing data
- Use write mode ('w') if you want to overwrite the file completely

### Search Functionality
- Convert search terms to lowercase for case-insensitive matching
- Search both title and author fields
- Consider partial matching (e.g., "Orwell" finds "George Orwell")

### Input Validation
- Check for empty strings in customer input
- Validate year as a number
- Handle invalid menu choices gracefully

## Testing Strategy

### Start Small
1. Create 2-3 test books manually in your code
2. Verify display function works correctly
3. Test each menu option individually

### File Operations
1. Test saving with a small library
2. Delete the file and test loading (should handle gracefully)
3. Verify data persistence between program runs

### Edge Cases
- Empty library
- Search terms that don't match anything
- Invalid customer input (letters for year, empty fields)
- File permissions issues

## Common Challenges and Solutions

### Challenge: Parsing saved file back into dictionaries
**Solution**: Use a consistent format and string methods
```python
# If saving as: "Title by Author (Year) - Genre"
line = "1984 by George Orwell (1949) - Dystopian Fiction"
# Use split() and string manipulation to extract parts
```

### Challenge: Handling empty file or missing file
**Solution**: Use try/except and return empty list
```python
try:
    with open(filename, "r") as f:
        # read file
except FileNotFoundError:
    return []  # Empty library for new users
```

### Challenge: Search not finding anything
**Solution**: Make search case-insensitive and informative
```python
search_term = search_term.lower()
if search_term in book['title'].lower() or search_term in book['author'].lower():
    # Found match
```

## Pair Programming Suggestions

- **Driver Focus**: Implementing specific functions (add_book, save_library)
- **Navigator Focus**: Reviewing data flow and suggesting edge cases
- **Good Switch Points**: After completing each major function
- **Shared Decisions**: File format choice, menu structure, error handling approach

## Assessment Criteria Example Rubric

### Functionality (60%)
- All 7 core requirements implemented and working
- Proper error handling for file operations
- Menu system functions correctly

### Code Quality (25%)
- Clear function names and structure
- Appropriate use of data structures
- Consistent formatting and style

### User Experience (15%)
- Intuitive menu system
- Clear prompts and feedback
- Graceful handling of user errors

## Time Management Tips

- **Hour 1**: Get basic add/display working with hardcoded data
- **Hour 2**: Implement file saving functionality
- **Hour 3**: Add file loading and fix any bugs
- **Hour 4**: Implement search feature
- **Hour 5**: Polish interface and add error handling

## Success Indicators

You're on track if:
- You can add books and see them displayed
- Your program doesn't crash with invalid input
- File save/load works consistently
- Search returns expected results
- Code is organised into clear functions