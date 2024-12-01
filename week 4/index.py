def modify_file_content(input_filename, output_filename):
    try:
        
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        
        modified_content = "Modified content:\n" + content
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File '{output_filename}' has been written successfully with modified content.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: There was an issue reading or writing to the file.")

# Ask the user for the input and output filenames
input_filename = input("Enter the name of the file to read from: ")
output_filename = input("Enter the name of the file to write to: ")

# Call the function to modify the file
modify_file_content(input_filename, output_filename)
