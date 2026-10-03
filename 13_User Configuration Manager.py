def add_setting(settings: dict, new_set: tuple):
    key = new_set[0].lower()
    value = new_set[1].lower()
    
    if key in settings.keys(): 
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings: dict, new_set:tuple):
    key = new_set[0].lower()
    value = new_set[1].lower()

    if key in settings.keys():
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, key):
    key = key.lower()

    if key in settings.keys():
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings: dict):
    if not settings:
        return "No settings available."
    else:
        return "Current User Settings:\n" + "\n".join(f"{key.capitalize()}: {value}" for key, value in settings.items()) + "\n"
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

print(view_settings(test_settings))