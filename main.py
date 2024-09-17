zombie_backpack = {
    "weapons": ["bat", "knife", "gun"],
    "bullets": 6,  # Starting with 5 bullets
    "shells": 10,
    "food": ["water", "canned food"],
    "tools": ["flashlight", "rope"]
}

def nice_print_dictionary():
    print("-----nicer print--------")
    for key, value in zombie_backpack.items():
        if isinstance(value, list):
            print(f"{key}: {', '.join(value)}")
        else:
            print(f"{key}: {value}")

# Print the initial state of the backpack.
print("Initial backpack:")
print(zombie_backpack)

# Add a new item to the food section
zombie_backpack["food"].append("tin of beans")
print("\nAdded 'tin of beans' to the food section.")
print(zombie_backpack)

# Remove bullets (e.g., after using some)
bullets_to_remove = 3
if zombie_backpack["bullets"] >= bullets_to_remove:
    zombie_backpack["bullets"] -= bullets_to_remove
    print(f"\nRemoved {bullets_to_remove} bullets. Remaining bullets: {zombie_backpack['bullets']}")
else:
    print("\nNot enough bullets to remove.")

# Add a single item that is not in another category
zombie_backpack["first_aid_kit"] = ["bandages", "antiseptic", "painkillers"]
print("\nAdded 'first aid kit' to the backpack.")
print(zombie_backpack)

# Add a new item: a dog
zombie_backpack["dog"] = "friendly and loyal"
print("\nAdded a 'dog' to the backpack.")
print(zombie_backpack)

# Print the updated state of the backpack
print("\nUpdated backpack:")
print(zombie_backpack)

# Print the contents of the backpack in a nicer format
nice_print_dictionary()
nice_print_dictionary()
nice_print_dictionary()

