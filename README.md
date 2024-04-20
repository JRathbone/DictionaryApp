
# Multi-value Dictionary App

## Author: Justin R. Rathbone
## Date: 19 April 2024

### Description:
This Multi-value Dictionary App allows users to store key-value pairs where each key can have multiple values associated with it. Users can perform various operations such as adding a member, removing a member, clearing the dictionary, checking if a key or member exists, and more.

### How to Use:
0. Clone this repository and open in your preferred IDE
1. From your terminal/CMD enter `python ./app.py` to run the application (this may vary depending on your     setup. I am on Mac)
2. Enter commands in the following format:
   - To add a member: `ADD key value`
   - To remove a member: `REMOVE key value`
   - To remove all members for a key: `REMOVEALL key`
   - To clear the dictionary: `CLEAR`
   - To check if a key exists: `KEYEXISTS key`
   - To check if a member exists: `MEMBEREXISTS key value`
   - To get all members for a key: `MEMBERS key`
   - To get all keys: `KEYS`
   - To get all members across all keys: `ALLMEMBERS`
   - To get all key-value pairs: `ITEMS`
   - To upload data from a file: `UPLOAD filename` (addtional feature I added. not in instructions)
   - To exit the application: `EXIT`

### How to Run Testcases:
1. From your terminal/CMD enter "python ./tests.py" (this may vary depending on your setup. I am on Mac)
2. Test cases will automatically run for every method in app.py
3. Output from text cases can be viewed in the output/terminal

### Example Usage:
```
> ADD fruit apple
) ADDED
> ADD fruit banana
) ADDED
> ADD fruit cherry
) ADDED
> KEYS
1) fruit
> MEMBERS fruit
1) apple
2) banana
3) cherry
> REMOVE fruit banana
) Removed
> MEMBEREXISTS fruit banana
) False
> REMOVEALL fruit
) Removed
> KEYS
(empty set)
> EXIT
```

### Additional Notes:
- Each command should be entered in the specified format to ensure proper execution.
- Error messages will be displayed for invalid inputs or operations.
