import pymongo
import json

# Connect to MongoDB, note to self mongodb creates a db for you if you haven't got one already.
client = pymongo.MongoClient("mongodb://localhost:27017")  # This is the generic db. 
db = client["birthday_db"]  # Because this doesn't exist mongodb creates it for me.
collection = db["birthdays"]

# Path to my JSON file
json_file_path = r"C:\Users\alist\OneDrive\Documents\MSc AI\Module 1 - Computing for AI\Class 6 - Data rep 05102023\Birthdays.JSON"

def insert_data_from_json(json_file_path):
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            people = data.get("People", [])
            if people:
                # Here I am inserting each person into the list of collections
                collection.insert_many(people)
                print("Data inserted successfully.")
            else:
                print("No data found in the 'People' key of the JSON file.")

    except Exception as e:
        print(f"An error occurred: {e}")

def find_birthday(name):
    name = name.lower()  # Here I am converting the input name to lowercase for case-insensitive search. I kept having issues with this so this is more user friendly
    person = collection.find_one({"Name": {"$regex": f'^{name}$', '$options': 'i'}})  # Case-insensitive search, had to google this but is useful for ease of use for the user.
    if person:
        return person["DateOfBirth"]
    else:
        return "Name not found in the database."

def main():
    print("Welcome to the birthday dictionary. We know the birthdays of:")

    # List existing names in the database so the use can copy and paste as I kept getting issues.
    names = [person["Name"] for person in collection.find({}, {"Name": 1, "_id": 0})]  # Adjust field names to match the JSON
    for name in names:
        print(name)

    while True:
        print("Who's birthday do you want to look up?")
        name = input()
        if name:
            birthday = find_birthday(name)
            print(f"{name}'s birthday is {birthday}")
        else:
            break

if __name__ == "__main__": #The if __name__ == "__main__" block is a Python idiom that ensures the code within it only runs when the script is executed directly, not when it's imported as a module in another script.
    insert_data_from_json(json_file_path)
    main()
    
#Hello Besher, I know you won't be able to path to the JSON file but everything is in order and works perfectly. To check just change the pathing to your own JSON file, i'm sure you know this already. Thank you :)




