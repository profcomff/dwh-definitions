import profcomff_definitions


def check_existing_table(table_name: str):
    """
    Checks if a table class exists in database by its name.
    """
    classes = profcomff_definitions.tables
    matches = []

    for existing_class in classes:
        if existing_class[0] == table_name:
            matches.append(existing_class[1])
    if len(matches) == 0:
        raise ModuleNotFoundError("No matching class found for table " + table_name)
    if len(matches) > 1:
        print("Multiple matching classes found for table " + table_name)
        print("Please choose wich class should be imported")
        for i in range(len(matches)):
            print(f"{i})", matches[i])
        choice = int(input())
        if choice not in range(len(matches)):
            raise ValueError("Invalid choice")
        table_class = matches[choice]
    else:
        table_class = matches[0]

    return table_class
