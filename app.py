# Multi-value Dictionary App
# Author: Justin R. Rathbone
# Date: 19 April 2024

def main():
    # Initialize an empty dictionary to store key-value pairs
    data = {}

    # Get user input
    while True:
        user_input = input("> ")

        # Check if user wants to exit
        if user_input.lower() == 'exit':
            break

        # Split input by space to get key and value
        input_parts = user_input.split()
        if len(input_parts) == 0:
            print(") ERROR: Invalid input")
        else:
            method_name = input_parts[0].upper()

            if method_name == "KEYS":
                if len(input_parts) == 1 and isinstance(input_parts[0],str):
                    KEYS(data)
                else:
                    print(") ERROR: Invalid input format or parameters")
            elif method_name == "MEMBERS":
                if len(input_parts) == 2 and isinstance(input_parts[1], str):
                    parameters = input_parts[1:]
                    MEMBERS(data, parameters[0])
                else:
                    print(") ERROR: Invalid input format or parameters")
            elif method_name == "ADD":
                if len(input_parts) == 3 and all(isinstance(param, str) for param in input_parts[1:]):
                    parameters = input_parts[1:]
                    ADD(data, parameters[0], parameters[1])
                else:
                    print(") ERROR: Invalid input format or parameters")
            elif method_name == "REMOVE":
                if len(input_parts) == 3 and all(isinstance(param, str) for param in input_parts[1:]):
                    parameters = input_parts[1:]
                    REMOVE(data, parameters[0], parameters[1])
                else:
                    print(") ERROR: Invalid input format or parameters")
            elif method_name == "REMOVEALL":
                if len(input_parts) == 2 and isinstance(input_parts[1], str):
                    parameters = input_parts[1:]
                    REMOVEALL(data, parameters[0])
                else:
                    print(") ERROR: Invalid input format or parameters")
            elif method_name == "CLEAR":
                if len(input_parts) == 1 and isinstance(input_parts[0],str):
                    CLEAR(data)
                else:
                    print(") ERROR: Invalid input format or parameters")
            elif method_name == "KEYEXISTS":
                if len(input_parts) == 2 and isinstance(input_parts[1], str):
                    parameters = input_parts[1:]
                    KEYEXISTS(data, parameters[0])
                else:
                    print(") ERROR: Invalid input format or parameters")
            elif method_name == "MEMBEREXISTS":
                if len(input_parts) == 3 and all(isinstance(param, str) for param in input_parts[1:]):
                    parameters = input_parts[1:]
                    MEMBEREXISTS(data, parameters[0], parameters[1])
                else:
                    print(") ERROR: Invalid input format or parameters")
            elif method_name == "ALLMEMBERS":
                if len(input_parts) == 1 and isinstance(input_parts[0],str):
                    ALLMEMBERS(data)
                else:
                    print(") ERROR: Invalid input format or parameters")
            elif method_name == "ITEMS":
                if len(input_parts) == 1 and isinstance(input_parts[0],str):
                    ITEMS(data)
                else:
                    print(") ERROR: Invalid input format or parameters")
            elif method_name == "UPLOAD":
                if len(input_parts) == 2 and isinstance(input_parts[1], str):
                    parameters = input_parts[1:]
                    UPLOAD(data, parameters[0])
                else:
                    print(") ERROR: Invalid input format or parameters")
            else:
                print(") ERROR: invalid method name")

# INFO: Returns all the keys in the dictionary.  Order is not guaranteed.
def KEYS(dictionary):
    if len(dictionary) == 0:
        print("(empty set)")
    else:
        count = 1
        for key in dictionary:
            print(f"{count}) {key}")
            count += 1

# INFO: Returns the collection of strings for the given key. Return order is not guaranteed. Returns an error if the key does not exists.
def MEMBERS(dictionary, key):
    if len(dictionary) == 0:
        print(") ERROR: Key is empty")
    else:
        count = 1
        if key not in dictionary:
            print(") ERROR: Key does not exist")
        else:
            for member in dictionary[key]:
                print(f"{count}) {member}")
                count += 1

# INFO: Adds a member to a collection for a given key. Displays an error if the member already exists for the key.
def ADD(dictionary, key, member):
    if key in dictionary:
        if member in dictionary[key]:
            print(") ERROR: Member already exists")
        else:
            dictionary[key].append(member)
            print(") ADDED")
    else:
        dictionary[key] = [member]
        print(") ADDED")

# INFO: Removes a member from a key.  If the last member is removed from the key, the key is removed from the dictionary. 
#       If the key or member does not exist, displays an error.
def REMOVE(dictionary, key, member):
    # Check if the key exists in the dictionary
    if key in dictionary:
        # Check if the value exists for the key
        if member in dictionary[key]:
            # Remove the value from the list of values for the key
            dictionary[key].remove(member)
            print(") Removed")
            # Check if there are any values left for the key
            if not dictionary[key]:
                # If no values left, remove the key from the dictionary
                del dictionary[key]
        else:
            print(") Error: Member does not exist")
    else:
        print(") Error: Key does not exist")

# INFO: Removes all members for a key and removes the key from the dictionary. Returns an error if the key does not exist.
def REMOVEALL(dictionary, key):

    # Check if the key exists in the dictionary
    if key in dictionary:
        # Remove all members for the key
        del dictionary[key]
        print(") Removed")
    else:
        print(") Error: Key does not exist in the dictionary.")

# INFO: Removes all keys and all members from the dictionary.
def CLEAR(dictionary):
    if len(dictionary) == 0:
        print("(empty set)")
    else:
        dictionary.clear()
        print(") Cleared")

# INFO: Returns whether a key exists or not.
def KEYEXISTS(dictionary, key):
    if key in dictionary:
        print(") True")
    else:
        print(") False")

# INFO: Returns whether a member exists within a key.  Returns false if the key does not exist.
def MEMBEREXISTS(dictionary, key, member):
    if key in dictionary and member in dictionary[key]:
        print(") True")
    else:
        print(") False")

# INFO: Returns all the members in the dictionary.  Returns nothing if there are none. Order is not guaranteed.
def ALLMEMBERS(dictionary):
    if len(dictionary) == 0:
        print("(empty set)")
    else:
        counter = 1
        for key, values in dictionary.items():
            for value in values:
                print(f"{counter}) {value}")
                counter += 1

# INFO: Returns all keys in the dictionary and all of their members.  Returns nothing if there are none.  Order is not guaranteed.
def ITEMS(dictionary):
    if len(dictionary) == 0:
        print("(empty set)")
    else:
        counter = 1
        for key, values in dictionary.items():
            for value in values:
                print(f"{counter}) {key}: {value}")
                counter += 1

# INFO: Adds multiple key:value pairs to the dictionary based on a text file. Returns error if file is invalid or null
def UPLOAD(dictionary, filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split(':')
                ADD(dictionary, key.strip(), value.strip())
        print("File uploaded successfully.")
        print(dictionary)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: Invalid format in the file. Each line should contain a key-value pair separated by ':'.")


if __name__ == "__main__":
    main()
