def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def rot47(text):
    result = []
    for char in text:
        if '!' <= char <= '~':
            result.append(chr((ord(char) - 33 + 47) % 94 + 33))
        else:
            result.append(char)
    return ''.join(result)

def menu():
    print("Menu:")
    print("1. Encrypt using ROT13")
    print("2. Decrypt using ROT13")
    print("3. Encrypt using ROT47")
    print("4. Decrypt using ROT47")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            text = input("Enter the text to encrypt using ROT13: ")
            print("Encrypted text:", rot13(text))
        elif choice == '2':
            text = input("Enter the text to decrypt using ROT13: ")
            print("Decrypted text:", rot13(text))  
        elif choice == '3':
            text = input("Enter the text to encrypt using ROT47: ")
            print("Encrypted text:", rot47(text))
        elif choice == '4':
            text = input("Enter the text to decrypt using ROT47: ")
            print("Decrypted text:", rot47(text))  
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
