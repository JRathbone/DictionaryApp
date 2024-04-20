# Multi-value Dictionary App (Test cases)
# Author: Justin R. Rathbone
# Date: 19 April 2024

from app import KEYS,MEMBERS, ADD, REMOVE, REMOVEALL, CLEAR, KEYEXISTS, MEMBEREXISTS, ALLMEMBERS, ITEMS, UPLOAD

##############################################
################ TEST CASES #################
#############################################

def TESTCASES():
    test_KEYS()
    test_MEMBERS()
    test_ADD()
    test_REMOVE()
    test_REMOVEALL()
    test_CLEAR()
    test_KEYEXISTS()
    test_MEMBEREXISTS()
    test_ALLMEMBERS()
    test_ITEMS()
    test_UPLOAD()

def test_KEYS():
    print("Testing KEYS method:")

    # Test case 1: Empty dictionary
    print("Test case 1: Empty dictionary")
    test_dict1 = {}
    print("Expected output: (empty set)")
    print("Actual output:")
    KEYS(test_dict1)
    print()
    
    # Test case 2: Dictionary with one key
    print("Test case 2: Dictionary with one key")
    test_dict2 = {'key1': 'value1'}
    print("Expected output:")
    print("1) key1")
    print("Actual output:")
    KEYS(test_dict2)
    print()
    
    # Test case 3: Dictionary with multiple keys
    print("Test case 3: Dictionary with multiple keys")
    test_dict3 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    print("Expected output:")
    print("1) key1")
    print("2) key2")
    print("3) key3")
    print("Actual output:")
    KEYS(test_dict3)
    print()

def test_MEMBERS():
    print("Testing MEMBERS method:")

    # Test case 1: Key does not exist
    print("Test case 1: Key does not exist")
    test_dict1 = {}
    print("Expected output:")
    print(") ERROR: Key does not exist")
    print("Actual output:")
    MEMBERS(test_dict1, 'key1')
    print()

    # Test case 2: Key exists and has members
    print("Test case 2: Key exists and has members")
    test_dict3 = {'key1': ['member1', 'member2']}
    print("Expected output:")
    print("1) member1")
    print("2) member2")
    print("Actual output:")
    MEMBERS(test_dict3, 'key1')
    print()

def test_ADD():
    print("Testing ADD method:")

    # Test case 1: Add member to an existing key
    print("Test case 1: Add member to an existing key")
    test_dict1 = {'key1': ['member1', 'member2']}
    print("Expected output:")
    print(") ADDED")
    print("Actual output:")
    ADD(test_dict1, 'key1', 'member3')
    print("Updated dictionary:")
    print(test_dict1)
    print()

    # Test case 2: Add member to a new key
    print("Test case 2: Add member to a new key")
    test_dict2 = {'key1': ['member1', 'member2']}
    print("Expected output:")
    print(") ADDED")
    print("Actual output:")
    ADD(test_dict2, 'key2', 'member1')
    print("Updated dictionary:")
    print(test_dict2)
    print()

    # Test case 3: Add existing member to an existing key
    print("Test case 3: Add existing member to an existing key")
    test_dict3 = {'key1': ['member1', 'member2']}
    print("Expected output:")
    print(") ERROR: Member already exists")
    print("Actual output:")
    ADD(test_dict3, 'key1', 'member2')
    print("Updated dictionary:")
    print(test_dict3)
    print()

    # Test case 4: Add to an empty dictionary
    print("Test case 4: Add to an empty dictionary")
    test_dict4 = {}
    print("Expected output:")
    print(") ADDED")
    print("Actual output:")
    ADD(test_dict4, 'key1', 'member1')
    print("Updated dictionary:")
    print(test_dict4)
    print()

def test_REMOVE():
    print("Testing REMOVE method:")

    # Test case 1: Remove member from an existing key
    print("Test case 1: Remove member from an existing key")
    test_dict1 = {'key1': ['member1', 'member2']}
    print("Expected output:")
    print(") Removed")
    print("Actual output:")
    REMOVE(test_dict1, 'key1', 'member1')
    print("Updated dictionary:")
    print(test_dict1)
    print()

    # Test case 2: Remove non-existing member from an existing key
    print("Test case 2: Remove non-existing member from an existing key")
    test_dict2 = {'key1': ['member1', 'member2']}
    print("Expected output:")
    print(") Error: Member does not exist")
    print("Actual output:")
    REMOVE(test_dict2, 'key1', 'member3')
    print("Updated dictionary:")
    print(test_dict2)
    print()

    # Test case 3: Remove member from a non-existing key
    print("Test case 3: Remove member from a non-existing key")
    test_dict3 = {'key1': ['member1', 'member2']}
    print("Expected output:")
    print(") Error: Key does not exist")
    print("Actual output:")
    REMOVE(test_dict3, 'key2', 'member1')
    print("Updated dictionary:")
    print(test_dict3)
    print()

    # Test case 4: Remove the last member from a key
    print("Test case 4: Remove the last member from a key")
    test_dict4 = {'key1': ['member1']}
    print("Expected output:")
    print(") Removed")
    print("Actual output:")
    REMOVE(test_dict4, 'key1', 'member1')
    print("Updated dictionary:")
    print(test_dict4)
    print()

    # Test case 5: Remove member from an empty dictionary
    print("Test case 5: Remove member from an empty dictionary")
    test_dict5 = {}
    print("Expected output:")
    print(") Error: Key does not exist")
    print("Actual output:")
    REMOVE(test_dict5, 'key1', 'member1')
    print("Updated dictionary:")
    print(test_dict5)
    print()

def test_REMOVEALL():
    print("Testing REMOVEALL method:")

    # Test case 1: Remove key with members
    print("Test case 1: Remove key with members")
    test_dict1 = {'key1': ['value1', 'value2'], 'key2': ['value3']}
    print("Expected output:")
    print(") Removed")
    print("Actual output:")
    REMOVEALL(test_dict1, 'key1')
    print("Updated dictionary:")
    print(test_dict1)
    print()

    # Test case 2: Remove key without members
    print("Test case 2: Remove key without members")
    test_dict2 = {'key1': [], 'key2': ['value3']}
    print("Expected output:")
    print(") Removed")
    print("Actual output:")
    REMOVEALL(test_dict2, 'key1')
    print("Updated dictionary:")
    print(test_dict2)
    print()

    # Test case 3: Key does not exist
    print("Test case 3: Key does not exist")
    test_dict3 = {'key1': ['value1', 'value2'], 'key2': ['value3']}
    print("Expected output:")
    print(") Error: Key does not exist in the dictionary.")
    print("Actual output:")
    REMOVEALL(test_dict3, 'key3')
    print("Updated dictionary:")
    print(test_dict3)
    print()

def test_CLEAR():
    print("Testing CLEAR method:")

    # Test case 1: Clear an empty dictionary
    print("Test case 1: Clear an empty dictionary")
    test_dict1 = {}
    print("Expected output:")
    print("(empty set)")
    print("Actual output:")
    CLEAR(test_dict1)
    print("Updated dictionary:")
    print(test_dict1)
    print()

    # Test case 2: Clear a non-empty dictionary
    print("Test case 2: Clear a non-empty dictionary")
    test_dict2 = {'key1': 'value1', 'key2': 'value2'}
    print("Expected output:")
    print(") Cleared")
    print("Actual output:")
    CLEAR(test_dict2)
    print("Updated dictionary:")
    print(test_dict2)
    print()

def test_KEYEXISTS():
    print("Testing KEYEXISTS method:")

    # Test case 1: Key exists in dictionary
    print("Test case 1: Key exists in dictionary")
    test_dict1 = {'key1': 'value1', 'key2': 'value2'}
    print("Expected output:")
    print(") True")
    print("Actual output:")
    KEYEXISTS(test_dict1, 'key1')
    print()

    # Test case 2: Key does not exist in dictionary
    print("Test case 2: Key does not exist in dictionary")
    test_dict2 = {'key1': 'value1', 'key2': 'value2'}
    print("Expected output:")
    print(") False")
    print("Actual output:")
    KEYEXISTS(test_dict2, 'key3')
    print()

    # Test case 3: Empty dictionary
    print("Test case 3: Empty dictionary")
    test_dict3 = {}
    print("Expected output:")
    print(") False")
    print("Actual output:")
    KEYEXISTS(test_dict3, 'key1')
    print()

def test_MEMBEREXISTS():
    print("Testing MEMBEREXISTS method:")

    # Test case 1: Key and member exist in dictionary
    print("Test case 1: Key and member exist in dictionary")
    test_dict1 = {'key1': ['member1', 'member2']}
    print("Expected output:")
    print(") True")
    print("Actual output:")
    MEMBEREXISTS(test_dict1, 'key1', 'member1')
    print()

    # Test case 2: Key exists but member does not exist in dictionary
    print("Test case 2: Key exists but member does not exist in dictionary")
    test_dict2 = {'key1': ['member1', 'member2']}
    print("Expected output:")
    print(") False")
    print("Actual output:")
    MEMBEREXISTS(test_dict2, 'key1', 'member3')
    print()

    # Test case 3: Key does not exist in dictionary
    print("Test case 3: Key does not exist in dictionary")
    test_dict3 = {'key1': ['member1', 'member2']}
    print("Expected output:")
    print(") False")
    print("Actual output:")
    MEMBEREXISTS(test_dict3, 'key2', 'member1')
    print()

    # Test case 4: Empty dictionary
    print("Test case 4: Empty dictionary")
    test_dict4 = {}
    print("Expected output:")
    print(") False")
    print("Actual output:")
    MEMBEREXISTS(test_dict4, 'key1', 'member1')
    print()

def test_ALLMEMBERS():
    print("Testing ALLMEMBERS method:")

    # Test case 1: Non-empty dictionary
    print("Test case 1: Non-empty dictionary")
    test_dict1 = {'key1': ['value1', 'value2'], 'key2': ['value3']}
    print("Expected output:")
    print("1) value1")
    print("2) value2")
    print("3) value3")
    print("Actual output:")
    ALLMEMBERS(test_dict1)
    print()

    # Test case 2: Empty dictionary
    print("Test case 2: Empty dictionary")
    test_dict2 = {}
    print("Expected output:")
    print("(empty set)")
    print("Actual output:")
    ALLMEMBERS(test_dict2)
    print()

def test_ITEMS():
    print("Testing ITEMS method:")

    # Test case 1: Non-empty dictionary
    print("Test case 1: Non-empty dictionary")
    test_dict1 = {'key1': ['value1', 'value2'], 'key2': ['value3']}
    print("Expected output:")
    print("1) key1: value1")
    print("2) key1: value2")
    print("3) key2: value3")
    print("Actual output:")
    ITEMS(test_dict1)
    print()

    # Test case 2: Empty dictionary
    print("Test case 2: Empty dictionary")
    test_dict2 = {}
    print("Expected output:")
    print("(empty set)")
    print("Actual output:")
    ITEMS(test_dict2)
    print()

def test_UPLOAD():
    print("Testing file_upload method:")

    # Test case 1: Valid file with key-value pairs
    print("Test case 1: Valid file with key-value pairs")
    filename1 = "values.txt"
    valid_data = {}
    UPLOAD(valid_data, filename1)
    print("Uploaded dictionary:", valid_data)
    print()

    # Test case 2: Invalid file format (no colon separator)
    print("Test case 2: Invalid file format (no colon separator)")
    filename2 = "invalid-data.txt"
    invalid_data = {}
    UPLOAD(invalid_data, filename2)
    print()

    # Test case 3: File not found
    print("Test case 3: File not found")
    filename3 = "nonexistent_file.txt"
    nonexistent_data = {}
    UPLOAD(nonexistent_data, filename3)
    print()

TESTCASES()