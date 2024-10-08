def add_new_keys(keys: list[str], existing_dict: dict) -> dict:
    """
    Adds a new nested dictionary structure to the existing dictionary
    based on the provided list of keys. Each key will have 'points' and
    'max_points' initialized to 0.
    
    Args:
        keys (list of str): A list of keys representing the path in the dictionary.
        existing_dict (dict): The existing dictionary to update.
    
    Returns:
        dict: The updated dictionary.
    """
    current_dict: dict = existing_dict['points']

    for key in keys:
        # Check if the key exists
        if key not in current_dict:
            # Create the new structure
            current_dict[key] = {
                'points': 0,
                'max_points': 0
            }
        
        # Move deeper into the dictionary for the next key
        current_dict = current_dict[key]

    return existing_dict


if __name__ == '__main__':
    # Example usage
    initial_dict = {
        'points': {
            'prawa': {
                'points': 0,
                'max_points': 0,
                'sznury_choragwia': {
                    'points': 0,
                    'max_points': 3
                }
            },
            'sznury_choragwia': {
                'points': 0,
                'max_points': 0,
                'prawa': {
                    'points': 0,
                    'max_points': 0
                }
            }
        }
    }

    # Example keys to add
    keys = ['prawa', 'sznury_choragwia', 'postacie', 'funkcje']
    new_dict = add_new_keys(keys, initial_dict)

    # Print the updated dictionary
    import yaml
    print(yaml.dump(new_dict, allow_unicode=True))