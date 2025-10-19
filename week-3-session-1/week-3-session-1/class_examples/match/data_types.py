def handle_input():
    user_input = input("Enter something (int, str, or list): ")
    try:
        user_input = eval(user_input)
    except:
        pass
    match user_input:
        case int():
            print(f"Integer received: {user_input}")
        case str():
            print(f"String received: {user_input}")
        case list() if len(user_input) > 0:
            print(f"List received with {len(user_input)} elements")
        case _:
            print("Unknown input type")

# Example usage
handle_input(10)                # Output: Integer received: 10
handle_input("Hello")           # Output: String received: Hello
handle_input([1, 2, 3])         # Output: List received with 3 elements
