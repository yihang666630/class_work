# Pokemon Data Analysis - Student Solution
# Data columns: #,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary

import random

def load_pokemon_data(filename):
    """Load Pokemon data from CSV file and convert to proper types"""
    try:
        with open(filename, "r") as f:
            data = f.readlines()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return []
    
    # Skip header and clean data
    raw_data = [line.strip().split(",") for line in data[1:] if line.strip()]
    
    processed_data = []
    for row in raw_data:
        if len(row) >= 13:  # Ensure complete data
            try:
                # Convert data to proper types
                converted_row = [
                    int(row[0]),      # Pokedex number
                    row[1],           # Name
                    row[2],           # Type 1
                    row[3] if row[3] else None,  # Type 2 (might be empty)
                    int(row[4]),      # Total stats
                    int(row[5]),      # HP
                    int(row[6]),      # Attack
                    int(row[7]),      # Defense
                    int(row[8]),      # Sp. Atk
                    int(row[9]),      # Sp. Def
                    int(row[10]),     # Speed
                    int(row[11]),     # Generation
                    row[12].lower() == 'true'  # Legendary (convert to boolean)
                ]
                processed_data.append(converted_row)
            except (ValueError, IndexError):
                print(f"Skipping invalid row: {row}")
                continue
    
    return processed_data

def search_pokemon(data, name):
    """Search for a Pokemon by name (case insensitive)"""
    name = name.lower().strip()
    for pokemon in data:
        if pokemon[1].lower() == name:  # Name is at index 1
            return pokemon
    return None

def pokemon_by_type(data, pokemon_type):
    """Get all Pokemon of a specific type"""
    pokemon_type = pokemon_type.title()  # Capitalize first letter
    matches = []
    
    for pokemon in data:
        # Check both Type 1 and Type 2
        if pokemon[2] == pokemon_type or pokemon[3] == pokemon_type:
            matches.append(pokemon)
    
    return matches

def calculate_type_averages(data, pokemon_type):
    """Calculate average stats for a Pokemon type"""
    type_pokemon = pokemon_by_type(data, pokemon_type)
    
    if not type_pokemon:
        return {}
    
    # Calculate stat totals
    totals = {"HP": 0, "Attack": 0, "Defense": 0, "Sp.Atk": 0, "Sp.Def": 0, "Speed": 0}
    
    for pokemon in type_pokemon:
        totals["HP"] += pokemon[5]
        totals["Attack"] += pokemon[6]
        totals["Defense"] += pokemon[7]
        totals["Sp.Atk"] += pokemon[8]
        totals["Sp.Def"] += pokemon[9]
        totals["Speed"] += pokemon[10]
    
    # Calculate averages
    count = len(type_pokemon)
    averages = {stat: total/count for stat, total in totals.items()}
    
    return averages

def strongest_pokemon(data, stat_name):
    """Find Pokemon with highest value in given stat"""
    stat_indices = {
        "HP": 5, "Attack": 6, "Defense": 7, 
        "Sp.Atk": 8, "Sp.Def": 9, "Speed": 10, "Total": 4
    }
    
    if stat_name not in stat_indices:
        print(f"Invalid stat: {stat_name}")
        return None
    
    stat_index = stat_indices[stat_name]
    
    if not data:
        return None
    
    # Find max value and all Pokemon with that value
    max_stat = max(pokemon[stat_index] for pokemon in data)
    strongest = [pokemon for pokemon in data if pokemon[stat_index] == max_stat]
    
    return strongest

def pokemon_battle_simulator(data, pokemon1_name, pokemon2_name):
    """Simulate a simple battle between two Pokemon"""
    p1 = search_pokemon(data, pokemon1_name)
    p2 = search_pokemon(data, pokemon2_name)
    
    if not p1:
        return f"Pokemon '{pokemon1_name}' not found!"
    if not p2:
        return f"Pokemon '{pokemon2_name}' not found!"
    
    # Simple battle logic based on total stats
    p1_total = p1[4]  # Total stats at index 4
    p2_total = p2[4]
    
    result = f"\nBattle: {p1[1]} vs {p2[1]}\n"
    result += f"{p1[1]} Total Stats: {p1_total}\n"
    result += f"{p2[1]} Total Stats: {p2_total}\n"
    
    if p1_total > p2_total:
        result += f"Winner: {p1[1]}!"
    elif p2_total > p1_total:
        result += f"Winner: {p2[1]}!"
    else:
        result += "It's a tie!"
    
    return result

def pokemon_trivia_game(data):
    """Generate a random Pokemon trivia question"""
    if not data:
        print("No Pokemon data available!")
        return False
    
    pokemon = random.choice(data)
    question_types = ["type", "stat", "legendary", "generation"]
    q_type = random.choice(question_types)
    
    # Generate question based on type
    if q_type == "type":
        print(f"What is {pokemon[1]}'s primary type?")
        answer = input("Your answer: ").strip().title()
        correct = pokemon[2]
        
    elif q_type == "stat":
        stat_names = ["HP", "Attack", "Defense"]
        stat = random.choice(stat_names)
        stat_indices = {"HP": 5, "Attack": 6, "Defense": 7}
        print(f"What is {pokemon[1]}'s {stat} stat?")
        try:
            answer = int(input("Your answer: "))
            correct = pokemon[stat_indices[stat]]
        except ValueError:
            print("Please enter a number!")
            return False
            
    elif q_type == "legendary":
        print(f"Is {pokemon[1]} a legendary Pokemon? (yes/no)")
        answer = input("Your answer: ").strip().lower()
        correct = "yes" if pokemon[12] else "no"
        
    elif q_type == "generation":
        print(f"What generation is {pokemon[1]} from?")
        try:
            answer = int(input("Your answer: "))
            correct = pokemon[11]
        except ValueError:
            print("Please enter a number!")
            return False
    
    # Check if answer is correct
    if str(answer).lower() == str(correct).lower():
        print(f"Correct! The answer is {correct}")
        return True
    else:
        print(f"Wrong! The correct answer is {correct}")
        return False

def display_pokemon_info(pokemon_data):
    """Display detailed information for a single Pokemon"""
    if not pokemon_data:
        print("No Pokemon data to display")
        return
    
    print(f"\n--- {pokemon_data[1]} ---")
    print(f"Pokedex #: {pokemon_data[0]}")
    print(f"Type: {pokemon_data[2]}" + (f"/{pokemon_data[3]}" if pokemon_data[3] else ""))
    print(f"Generation: {pokemon_data[11]}")
    print(f"Legendary: {'Yes' if pokemon_data[12] else 'No'}")
    print(f"\nBase Stats:")
    print(f"  HP:        {pokemon_data[5]}")
    print(f"  Attack:    {pokemon_data[6]}")
    print(f"  Defense:   {pokemon_data[7]}")
    print(f"  Sp. Atk:   {pokemon_data[8]}")
    print(f"  Sp. Def:   {pokemon_data[9]}")
    print(f"  Speed:     {pokemon_data[10]}")
    print(f"  Total:     {pokemon_data[4]}")

def get_type_list(data):
    """Get sorted list of all Pokemon types"""
    types = set()
    for pokemon in data:
        types.add(pokemon[2])  # Type 1
        if pokemon[3]:  # Type 2 if exists
            types.add(pokemon[3])
    return sorted(list(types))

def display_menu():
    """Display main menu options"""
    print("\n=== Pokemon Data Explorer ===")
    print("1. Search Pokemon by name")
    print("2. Pokemon by type")
    print("3. Type statistics analysis") 
    print("4. Find strongest Pokemon")
    print("5. Battle simulator")
    print("6. Pokemon trivia")
    print("7. Random Pokemon info")
    print("8. Exit")

# Main program
if __name__ == "__main__":
    print("Loading Pokemon data...")
    pokemon_data = load_pokemon_data("pokemon.csv")
    print(f"Loaded {len(pokemon_data)} Pokemon")
    
    if not pokemon_data:
        print("No data loaded. Please check if pokemon.csv exists.")
        exit()
    
    # Show available types for reference
    types = get_type_list(pokemon_data)
    print(f"Available types: {', '.join(types)}")
    
    # Main menu loop
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            name = input("Enter Pokemon name: ").strip()
            pokemon = search_pokemon(pokemon_data, name)
            if pokemon:
                display_pokemon_info(pokemon)
            else:
                print(f"Pokemon '{name}' not found!")
        
        elif choice == "2":
            ptype = input("Enter Pokemon type: ").strip()
            matches = pokemon_by_type(pokemon_data, ptype)
            if matches:
                print(f"Found {len(matches)} {ptype}-type Pokemon:")
                for pokemon in matches[:10]:  # Show first 10
                    type_str = pokemon[2] + (f"/{pokemon[3]}" if pokemon[3] else "")
                    print(f"  {pokemon[1]} ({type_str})")
                if len(matches) > 10:
                    print(f"  ... and {len(matches) - 10} more")
            else:
                print(f"No {ptype}-type Pokemon found!")
        
        elif choice == "3":
            ptype = input("Enter Pokemon type for analysis: ").strip()
            averages = calculate_type_averages(pokemon_data, ptype)
            if averages:
                print(f"\nAverage stats for {ptype}-type Pokemon:")
                for stat, avg in averages.items():
                    print(f"  {stat}: {avg:.1f}")
            else:
                print(f"No {ptype}-type Pokemon found!")
        
        elif choice == "4":
            print("Available stats: HP, Attack, Defense, Sp.Atk, Sp.Def, Speed, Total")
            stat = input("Enter stat name: ").strip()
            strongest = strongest_pokemon(pokemon_data, stat)
            if strongest:
                print(f"\nStrongest {stat} Pokemon:")
                stat_indices = {"HP": 5, "Attack": 6, "Defense": 7, "Sp.Atk": 8, "Sp.Def": 9, "Speed": 10, "Total": 4}
                if stat in stat_indices:
                    for pokemon in strongest:
                        stat_value = pokemon[stat_indices[stat]]
                        print(f"  {pokemon[1]} - {stat}: {stat_value}")
        
        elif choice == "5":
            p1 = input("Enter first Pokemon name: ").strip()
            p2 = input("Enter second Pokemon name: ").strip()
            result = pokemon_battle_simulator(pokemon_data, p1, p2)
            print(result)
        
        elif choice == "6":
            print("Pokemon Trivia! Answer 5 questions:")
            score = 0
            for i in range(5):
                print(f"\nQuestion {i+1}/5:")
                if pokemon_trivia_game(pokemon_data):
                    score += 1
            print(f"\nTrivia complete! You scored {score}/5")
        
        elif choice == "7":
            random_pokemon = random.choice(pokemon_data)
            print("Random Pokemon:")
            display_pokemon_info(random_pokemon)
        
        elif choice == "8":
            print("Thanks for exploring Pokemon data!")
            break
        
        else:
            print("Invalid choice. Please enter 1-8.")