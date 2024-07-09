def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args

    if contacts.get(name):
        return "Contact already exist."

    contacts[name] = phone
    return "Contact added."

def list_contacts(contacts):
    output = ""
    for name, phone in contacts.items():
        output = f"{output}Contact:{name} - {phone}\n"
    return output

def show_phone(args, contacts):
    name = args[0]
    phone = contacts.get(name)

    return phone if phone else "Contact not found"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(add_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(list_contacts(contacts))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
