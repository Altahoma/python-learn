def get_formatted_name(first_name, last_name):
    """Выводит простое приветствие."""
    full_name = first_name + ' ' + last_name
    return  full_name


while True:
    print("\nPlease tell me your name:")
    print("(enter 'quit' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'quit':
        break
    l_name = input("Last name ")
    if l_name == 'quit':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
