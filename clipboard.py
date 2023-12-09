import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file)

def load_data(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error decoding JSON. File may be corrupted.")
        return {}

def save_command(data):
    key = input("Enter a key: ")
    data[key] = clipboard.paste()
    save_data(SAVED_DATA, data)
    print("Data saved!")

def load_command(data):
    key = input("Enter a key: ")
    if key in data:
        clipboard.copy(data[key])
        print("Data copied to clipboard.")
    else:
        print("Key does not exist.")

def list_command(data):
    print(data)

def main():
    if len(sys.argv) == 2:
        command = sys.argv[1]
        data = load_data(SAVED_DATA)

        if command == "save":
            save_command(data)
        elif command == "load":
            load_command(data)
        elif command == "list":
            list_command(data)
        else:
            print("Unknown command")
    else:
        print("Please pass exactly one command.")

if __name__ == "__main__":
    main()
