# Song of the Month Data Analysis

**Estimated Time:** 4-6 total human hours  
**Difficulty:** ⭐⭐⭐⭐ (Advanced)  
**Prerequisites:** CSV processing, large datasets, string manipulation, performance awareness  
**Good for:** Students ready for real-world data challenges

*Data provided by: https://chart2000.com/*

## ⚠️ Critical Performance Warnings

### Dataset Size Reality Check
- **14,650 rows** of data - this will impact performance
- Loading may take 5-10 seconds on slower machines
- Displaying all results will overwhelm the console
- **Always limit output** (show first 10-20 results max)
- Consider working with filtered subsets for development

### Development Strategy
1. **Start with recent data only** (2020-2024) for faster testing
2. **Test with small samples** before processing full dataset
3. **Add result limits** to all display functions
4. **Expect slower response times** compared to previous activities

## The Data Structure

**Columns:** month,position,artist,song,indicative_revenue,us,uk,de,fr,ca,au

- **month**: Format "Jan-2000" (need to parse year/month separately)
- **position**: Chart position (1-50)
- **artist**: Artist name (may contain special characters)
- **song**: Song title (may contain commas, quotes)
- **indicative_revenue**: Revenue in thousands USD (may be empty/"-")
- **us/uk/de/fr/ca/au**: Country chart positions (number or "-")

## Task Progression

### Task 1: Data Processing Foundation (90 minutes)
**Critical First Steps:**
- Load CSV with error handling
- Parse month column into separate year/month
- Handle missing/invalid data ("-" entries)
- **Test with 2020+ data only initially**

**Success Criteria:**
- Can load data without crashes
- Display basic dataset info (total songs, year range)
- Show first 5 rows in readable format

### Task 2: Search and Analysis (120 minutes)
**Core Features (Pick 3-4):**
- Artist search (case-insensitive, partial matching)
- Song title search
- Year-based filtering
- Revenue-based sorting
- Country chart analysis
- CSV export functionality

**Implementation Priority:**
1. Artist search (most straightforward)
2. Year filtering (useful for manageable subsets)
3. Revenue sorting (demonstrates data conversion)
4. Export feature (reinforces file I/O skills)

**Performance Requirements:**
- Limit all search results to first 20 matches
- Add loading messages for operations taking >2 seconds
- Allow customer to cancel long operations

### Task 3: Interactive Quiz (60 minutes)
**Choose ONE approach - don't attempt all:**

**Option A: Song Guessing Game**
- Show artist name + first letter of each word
- Customer guesses complete song title
- Track score over multiple rounds

**Option B: Multiple Choice Quiz**
- Show artist, provide 4 song options (1 correct, 3 random)
- Generate questions from popular songs only
- Include feedback with chart position info

**Option C: Chart Knowledge Quiz**
- "Which song reached #1 in [year]?"
- "Name a song by [artist] that charted in the UK (or country of your choice from included options)"
- "True/false: [song] made more than $X revenue"

## Data Processing Challenges

### String Parsing Issues
```python
# Month parsing: "Jan-2000" -> year=2000, month="Jan"
month_parts = row[0].split("-")
if len(month_parts) == 2:
    month, year = month_parts[0], int(month_parts[1])
```

### Revenue Data Handling
```python
# Revenue may be empty, "-", or numeric string
try:
    revenue = float(row[4]) if row[4] and row[4] != '-' else 0
except ValueError:
    revenue = 0
```

### Chart Position Processing
```python
# Country positions: number or "-"
us_position = int(row[5]) if row[5] != '-' else None
```

## Memory and Performance Optimisation

### Filtering for Development
```python
# Work with recent data during development
recent_data = [row for row in data if "2020" in row[0] or "2021" in row[0]]
```

### Result Limiting
```python
# Always limit output
def display_results(matches, limit=20):
    for i, item in enumerate(matches[:limit]):
        print(f"{i+1}. {item}")
    if len(matches) > limit:
        print(f"... and {len(matches) - limit} more results")
```

## Common Implementation Pitfalls

### Memory Issues
- **Problem**: Loading full dataset multiple times
- **Solution**: Load once, filter as needed

### Console Flooding  
- **Problem**: Displaying thousands of results
- **Solution**: Always use result limits and pagination

### String Encoding
- **Problem**: Special characters in artist/song names
- **Solution**: Use UTF-8 encoding when opening files

### Empty Data Fields
- **Problem**: Assuming all fields have valid data
- **Solution**: Check for "-" and empty strings consistently

## Testing Strategy

### Phase 1: Data Loading
- Verify file loads without errors
- Check data structure with known songs
- Confirm year parsing works correctly

### Phase 2: Search Functions
- Test with well-known artists (Beatles, Taylor Swift)
- Verify case-insensitive search works
- Test edge cases (artists with special characters)

### Phase 3: Performance
- Time operations with full dataset
- Ensure UI remains responsive
- Test with various search terms

## Pair Programming Structure

### Driver Responsibilities
- Focus on implementing specific functions
- Handle file I/O and data parsing
- Debug syntax and logic errors

### Navigator Responsibilities  
- Watch for performance issues
- Suggest result limiting strategies
- Keep track of memory usage patterns
- Plan next features based on current progress

### Good Switch Points
- After completing data loading
- Between different search functions
- When moving from search to quiz features
- After implementing each major analysis feature

## Time Management Reality

### Hour 1: Data Foundation
- Get basic file loading working
- Parse first few rows successfully
- Handle basic errors

### Hour 2: Search Implementation
- Implement artist search with result limiting
- Test with known data

### Hour 3: Additional Features
- Add one more search type OR basic sorting
- Focus on making existing features solid

### Hour 4: Quiz or Polish
- Either implement simple quiz OR improve user interface
- Add error handling and input validation

### Hours 5-6: Extensions (Optional)
- Additional quiz types OR export features
- Performance optimisation
- Advanced analysis features

## Success Criteria

### Minimum Viable Product
- Loads dataset successfully
- Performs artist search with limited results
- Handles missing data gracefully
- Includes basic user interface

### Full Implementation
- Multiple search/filter options
- Interactive quiz component
- Export functionality
- Proper error handling and customer feedback potential

### Performance Benchmarks
- Dataset loads in under 10 seconds
- Search results appear in under 3 seconds
- No memory-related crashes
- User interface remains responsive

## Extension Challenges

### Data Analysis
- Find trends by decade
- Compare country chart performance
- Revenue analysis by genre/year
- Artist career trajectory tracking

### Advanced Features
- Song recommendation based on preferences
- Chart position prediction
- Interactive data visualisation
- Playlist generation from chart data

## Assessment Example Rubric Overview

### Functionality (50%)
- Core features work reliably
- Handles large dataset appropriately
- Quiz component is engaging and functional

### Performance (30%)
- Manages memory efficiently
- Provides responsive user experience
- Implements appropriate result limiting

### Code Quality (20%)
- Clear data processing logic
- Appropriate error handling
- Efficient algorithms for search/sort operations

**Technical Notes**:
- Import random module: `import random`
- Use `random.choice(data)` for random selection
- Consider filtering to popular songs only

## Getting Started Checklist
- [ ] Load data successfully
- [ ] Display first 5 rows to understand structure
- [ ] Implement basic artist search
- [ ] Test with small data subset
- [ ] Add one sorting option
- [ ] Choose and implement one quiz type

## Testing Strategy
1. Start with 2020-2024 data only
2. Test search with well-known artists
3. Verify export functionality creates valid CSV
4. Test quiz with recognisable songs