def get_numbers():
    numbers = []
    print("Enter numbers one by one. Type 'done' to finish.")
    while True:
        entry = input("Enter a number (or 'done'): ").strip()
        if entry.lower() == 'done':
            break
        if entry == '':
            print("Input cannot be empty. Try again.")
            continue
        try:
            num = float(entry)
            numbers.append(num)
        except ValueError:
            print("That's not a valid number. Try again.")
    return numbers

def print_stats(numbers):
    if not numbers:
        print("No numbers entered.")
        return
    print(f"Count: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers)/len(numbers):.2f}")
    print(f"Min: {min(numbers)}")
    print(f"Max: {max(numbers)}")

def main():
    name = input("What is your name? ")
    print(f"Hello, {name}! Let's do some math.")
    numbers = get_numbers()
    print_stats(numbers)

if __name__ == "__main__":
    main()
