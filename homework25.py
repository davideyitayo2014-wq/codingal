import random
import string

def generate_password(length=12):
    # 1. Define character sets
    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase  # A-Z
    numbers = string.digits         # 0-9
    
    # 2. Make sure password has at least 1 of each (important for Codingal checker)
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(numbers)
    ]
    
    # 3. Fill rest using List Comprehension - this is the advanced part
    all_chars = lower + upper + numbers
    password += [random.choice(all_chars) for _ in range(length - 3)]
    
    # 4. Shuffle using random module (as asked in question)
    random.shuffle(password)
    
    # 5. Convert list to string using join (with list comprehension logic)
    final_password = ''.join(password)
    return final_password

# Test
length = int(input("Enter password length (e.g., 12): "))
print("Generated Password:", generate_password(length))