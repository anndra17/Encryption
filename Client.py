import socket, string

def transposition_encrypt(text, keyword):
    
    # Calculate number of columns and rows
    num_of_columns = len(keyword)
    num_of_rows = len(text) // num_of_columns  

    # Iterator for filling missing characters
    alphabet_iter = iter(string.ascii_lowercase) 

    # Create the empty grid
    grid = [''] * num_of_columns

    # Fill the grid with text characters column by column
    col = 0
    for symbol in text:
        grid[col] += symbol
        col += 1
        if col == num_of_columns:
            col = 0


    # Fill missing characters in each column
    for i in range(num_of_columns):
        while len(grid[i]) <= num_of_rows:
            grid[i] += next(alphabet_iter)


    # Sort the columns by the keyword
    sorted_columns = sorted(zip(keyword, grid))
    sorted_grid = [col[1] for col in sorted_columns]

    return ''.join(sorted_grid)

# Connect to server
server_ip = '127.0.0.1'
server_port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server_ip, server_port))

    # Get message from user
    message = input("Enter a message to encrypt: ")
    keyword = input("Enter the transposition keyword: ")
    encrypted_message = transposition_encrypt(message, keyword)
    s.sendall(encrypted_message.encode())
