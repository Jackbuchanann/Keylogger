import hashlib

# Function to calculate SHA-256 hash
def calculate_sha256_hash(input_string):
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
    return sha256_hash

# Main function
def main():
    # Read user input from the console
    user_input = input("Enter the text to calculate SHA-256 hash: ")

    # Calculate SHA-256 hash of the input
    sha256_hash = calculate_sha256_hash(user_input)

    # Print the hash value
    print("SHA-256 hash of the input text is:", sha256_hash)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
