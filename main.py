# Import file modules
from readme_generator import ReadMeGenerator
import pyfiglet

# Create an instance of the main class (ReadMeGenerator)
def main():

    # Generate an ASCII art banner 
    message = "Welcome"  
    ascii_banner = pyfiglet.figlet_format(message, font="ghost")
    
    # Print the ASCII art in the console
    print(ascii_banner)
    
    output = ReadMeGenerator()
    # Prompt user for answer questions
    output.prompt_users()  
    # Display user's answers
    output.display_answers()
    # Simulation progress bar 
    ReadMeGenerator.progress_simulation()
    # Generate a ReadMe file 
    output.generate_template_readme()
    
# Execute Main 
if __name__ == "__main__":
  main()




