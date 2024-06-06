import socket

def split_into_chunks(s, chunk_size):
    return [s[i:i + chunk_size] for i in range(0, len(s), chunk_size)]


def transposition_decrypt(text, keyword):
    # Calculate number of columns and rows
    num_of_columns = len(keyword)
    num_of_rows = len(text) // num_of_columns  # Ceiling division

    # Sort the keyword to determine the order of columns
    sorted_keyword = sorted(keyword)
    order = {char: i for i, char in enumerate(sorted_keyword)}

    # Split the text into chunks by cols
    text_grid = split_into_chunks(text, num_of_rows)
    print(text_grid)

    # Create the empty grid
    grid = [''] * num_of_columns
    
    # Fill the grid with text according to the order of keyword
    for i, key in enumerate(keyword):
        grid[i] = text_grid[order[key]]

    # Reconstruct the text row by row
    plaintext = ''
    for row in range(num_of_rows):
        for col in range(num_of_columns):
            plaintext += grid[col][row]

    # 0 1 2 3 4
    # S A L U T
    # 2 0 1 4 3
    # B u n a _
    # d i m i n
    # e a t a a
    
    print(grid)
    
    return plaintext

# Set up server
server_ip = '127.0.0.1'
server_port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((server_ip, server_port))
    s.listen()
    print("Server is listening...")

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        encrypted_message = conn.recv(1024).decode()
        keyword = input("Enter the transposition keyword used by the client: ")
        decrypted_message = transposition_decrypt(encrypted_message, keyword)
        print(f"Encrypted message: {encrypted_message}")
        print(f"Decrypted message: {decrypted_message}")
