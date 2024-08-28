def main():
    input_string = "prashant:2004-05-15,rajkumar:2004-10-22,satveek:1992-01-12"
    entries = input_string.split(',')
    
    birthday_dict = {}
    
    for entry in entries:
        name, birthday = entry.split(':')
        birthday_dict[name] = birthday

    result = []
    for name, birthday in birthday_dict.items():
        result.append(f"{name} is born on {birthday}")
    
    output_string = '\n'.join(result)
    
    print(output_string)

if __name__ == "__main__":
    main()
