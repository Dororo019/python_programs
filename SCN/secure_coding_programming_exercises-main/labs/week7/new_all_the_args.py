def describe_person(name: str, job: str, *adjectives: str, **possessions: int):
    # Form the first part of the string
    description = f"{name} is a {job} who is {', '.join(adjectives)}."
    
    # Form the second part of the string
    possessions_str = ', '.join([f"a {item} worth {value}" if item != 'shoes' else f"{item} with {value}" for item, value in possessions.items()])
    possessions_description = f" {name} has {possessions_str}."
    
    # Combine both parts
    full_description = description + possessions_description
    
    return full_description

# Test the function
print(describe_person('Gilad', 'teacher', 'happy', 'amazing', 'sooooo cool', bike=2000, house=1000, shoes=20))
