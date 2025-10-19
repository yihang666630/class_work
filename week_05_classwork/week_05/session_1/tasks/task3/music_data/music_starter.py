# Music Chart Data Analysis - Starter Code
# Complete the functions below to create a working music data analysis program

# Global variable to store music data
music_data = []

def load_music_data():
    """Load and process music chart data from CSV
    
    CSV columns: month,position,artist,song,indicative_revenue,us,uk,de,fr,ca,au
    Example: "Jan-2000,1,Britney Spears,Oops!... I Did It Again,1250,-,2,1,-,-,-"
    """
    global music_data
    filename = "monthly_songs.csv"
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = f.readlines()
    except FileNotFoundError:
        print("Error: monthly_songs.csv not found!")
        return False
    
    print("Loading music data... (this may take a moment)")
    
    # TODO: Process each line (skip header)
    for line in data[1:]:  # Skip header row
        line = line.strip()
        if line:
            row = line.split(",")
            if len(row) >= 11:  # Ensure we have all columns
                try:
                    # TODO: Parse month-year (e.g., "Jan-2000")
                    month_year = row[0].split("-")
                    if len(month_year) == 2:
                        month = month_year[0]
                        year = 0  # TODO: Convert month_year[1] to int
                    else:
                        month = "Unknown"
                        year = 0
                    
                    # TODO: Create song dictionary
                    song = {
                        "month": month,
                        "year": year,
                        "position": 0,      # TODO: Convert row[1] to int
                        "artist": "",       # TODO: Set to row[2]
                        "song": "",         # TODO: Set to row[3]
                        "revenue": 0.0,     # TODO: Convert row[4] to float (handle "-" and empty values)
                        "us_chart": None,   # TODO: Convert row[5] to int if not "-", else None
                        "uk_chart": None    # TODO: Convert row[6] to int if not "-", else None
                    }
                    music_data.append(song)
                    
                except (ValueError, IndexError):
                    # Skip invalid rows
                    continue
    
    print(f"Loaded {len(music_data)} song entries!")
    return True

def search_by_artist():
    """Search for songs by a specific artist"""
    artist_name = input("Enter artist name: ").strip().lower()
    matches = []
    
    # TODO: Search through all songs
    for song in music_data:
        # TODO: Check if artist_name appears in song["artist"] (case-insensitive)
        # Hint: Use .lower() and 'in' operator
        pass
    
    if matches:
        print(f"\nFound {len(matches)} songs by artists matching '{artist_name}':")
        
        # TODO: Sort by year (newest first) using bubble sort
        # Hint: Compare song["year"] values
        for i in range(len(matches)):
            for j in range(len(matches) - 1 - i):
                # TODO: Sort by year (newer first), then by position (lower number = better)
                pass
        
        # TODO: Display results (limit to first 15)
        for i, song in enumerate(matches[:15]):
            # TODO: Display song info nicely
            revenue_str = f"${song['revenue']:.0f}k" if song['revenue'] > 0 else "Unknown"
            print(f"  {song['song']} - #{song['position']} in {song['month']}-{song['year']} (Revenue: {revenue_str})")
        
        if len(matches) > 15:
            print(f"  ... and {len(matches) - 15} more")
    else:
        print(f"No songs found for artist matching '{artist_name}'")

def songs_by_year():
    """Find all songs from a specific year"""
    try:
        year = int(input("Enter year (2000-2024): "))
        if year < 2000 or year > 2024:
            print("Please enter a year between 2000 and 2024")
            return
    except ValueError:
        print("Please enter a valid year")
        return
    
    # TODO: Find all songs from that year
    year_songs = []
    for song in music_data:
        # TODO: Check if song["year"] matches the requested year
        pass
    
    if year_songs:
        print(f"\nFound {len(year_songs)} songs from {year}")
        
        # TODO: Sort by chart position (best positions first) using selection sort
        for i in range(len(year_songs)):
            min_index = i
            for j in range(i + 1, len(year_songs)):
                # TODO: Find song with better (lower) position
                pass
            # TODO: Swap songs
        
        print(f"Top 20 songs from {year}:")
        # TODO: Display top 20 songs
        for i, song in enumerate(year_songs[:20]):
            print(f"  {i+1:2d}. {song['artist']} - {song['song']} (#{song['position']} in {song['month']}-{year})")
    else:
        print(f"No songs found from {year}")

def highest_revenue_songs():
    """Find songs with the highest revenue"""
    if not music_data:
        print("No data loaded!")
        return
    
    # TODO: Filter out songs with no revenue data
    revenue_songs = []
    for song in music_data:
        # TODO: Only include songs with revenue > 0
        pass
    
    if not revenue_songs:
        print("No revenue data available!")
        return
    
    # TODO: Sort by revenue (highest first) using selection sort
    for i in range(len(revenue_songs)):
        max_index = i
        for j in range(i + 1, len(revenue_songs)):
            # TODO: Find song with higher revenue
            pass
        # TODO: Swap songs
    
    print(f"\nTop 20 Highest Revenue Songs:")
    # TODO: Display top 20 revenue songs
    for i, song in enumerate(revenue_songs[:20]):
        print(f"  {i+1:2d}. {song['artist']} - {song['song']}")
        print(f"      Revenue: ${song['revenue']:.0f}k ({song['month']}-{song['year']})")

def artist_analysis():
    """Analyze an artist's chart performance"""
    artist_name = input("Enter artist name for analysis: ").strip().lower()
    
    # TODO: Find all songs by this artist
    artist_songs = []
    for song in music_data:
        # TODO: Check if artist_name appears in song["artist"] (case-insensitive)
        pass
    
    if not artist_songs:
        print(f"No songs found for artist matching '{artist_name}'")
        return
    
    # TODO: Calculate statistics
    total_songs = len(artist_songs)
    total_revenue = 0  # TODO: Sum up revenue from all songs
    
    # TODO: Find best chart position
    best_position = 50  # Start with worst possible
    for song in artist_songs:
        # TODO: Update best_position if we find a better one
        pass
    
    # TODO: Count years active
    years = []
    for song in artist_songs:
        # TODO: Add year to years list if not already present
        pass
    
    print(f"\n--- Artist Analysis: {artist_songs[0]['artist']} ---")
    print(f"Total songs in charts: {total_songs}")
    print(f"Best chart position: #{best_position}")
    print(f"Total revenue: ${total_revenue:.0f}k")
    # TODO: Display year range and average revenue

def export_year_data():
    """Export all songs from a specific year to a new CSV file"""
    try:
        year = int(input("Enter year to export (2000-2024): "))
        if year < 2000 or year > 2024:
            print("Please enter a year between 2000 and 2024")
            return
    except ValueError:
        print("Please enter a valid year")
        return
    
    # TODO: Find all songs from that year
    year_songs = []
    for song in music_data:
        # TODO: Check if song year matches
        pass
    
    if not year_songs:
        print(f"No songs found from {year}")
        return
    
    # TODO: Write to new CSV file
    filename = f"songs_{year}.csv"
    try:
        with open(filename, "w") as f:
            # TODO: Write header
            # TODO: Write each song's data
            pass
        
        print(f"Exported {len(year_songs)} songs from {year} to {filename}")
        
    except Exception as e:
        print(f"Error exporting data: {e}")

def main_menu():
    """Display menu and handle user choices"""
    while True:
        print("\n=== Music Chart Data Explorer ===")
        print("1. Search by artist")
        print("2. Songs from specific year")
        print("3. Highest revenue songs")
        print("4. Artist analysis")
        print("5. Export year data")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            search_by_artist()
        elif choice == "2":
            songs_by_year()
        elif choice == "3":
            highest_revenue_songs()
        elif choice == "4":
            artist_analysis()
        elif choice == "5":
            export_year_data()
        elif choice == "6":
            print("Thanks for exploring music data!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")

# Main program
if __name__ == "__main__":
    print("Welcome to Music Chart Data Explorer!")
    if load_music_data():
        main_menu()
    else:
        print("Failed to load data. Please ensure monthly_songs.csv is available.")

# TODO List for completion:
# 1. Complete load_music_data() - parse month/year and convert data types
# 2. Complete search_by_artist() - implement search and sorting
# 3. Complete songs_by_year() - filter by year and sort by position
# 4. Complete highest_revenue_songs() - filter and sort by revenue
# 5. Complete artist_analysis() - calculate artist statistics
# 6. Complete export_year_data() - write filtered data to CSV file

# PERFORMANCE TIPS:
# - This dataset is large (14,650+ entries) - expect slower performance
# - Always limit displayed results to prevent console flooding
# - Consider working with recent years (2020-2024) during development