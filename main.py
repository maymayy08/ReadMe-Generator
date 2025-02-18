# Inport# Check if readme file exist, if exist, it will print out "File already existed!"
from readme_generator import ReadMeGenerator

def main():
    # Create an instance of the main class (ReadMeGenerator)
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

