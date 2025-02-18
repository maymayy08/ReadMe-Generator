# Import Libraries 
from InquirerPy import prompt
from InquirerPy.base.control import Choice
from rich.console import Console
import os
import time
from rich.progress import track


# Create a console object for rich formatting
console = Console()

# Create main class 
class ReadMeGenerator:

    def __init__(self):
        # Initialize instance variables to store answers
        self.project_title = ""
        self.project_description = ""
        self.installation_instructions = ""
        self.usage_instructions = ""
        self.license_selections = "" 
        self.confirm_license = False
        self.contact = ""
    
    # Create function for prompt questions for users 
    def prompt_users(self):  
        # Define the questions to ask the user
        questions = [
            {
            "type": "input", 
             "name": "project_title",
             "message": "What is your project called?"
             }, 
             {
                 "type": "input",
                 "name": "project_description",
                 "message": "Enter description for your project"
             },
             {
                 "type": "input",
                 "name": "installation_instructions",
                 "message": "How would you like to install dependencies and set up the project?"
             },
             {
                 "type": "input",
                 "name": "usage_instructions",
                 "message": "How would you like to run and use this project?"
             },
             {
                "type": "list",  # Changed to 'list' to show a list of choices using Rich method
                "name": "license_selections",
                "message": "Please select one of the following common licenses you would like to use",
                "choices": [
                    Choice("MIT License"),
                    Choice("Apache License 2.0"),
                    Choice("GNU General Public License (GPL v3)"),
                    Choice("Mozilla Public License 2.0 (MPL 2.0)"),
                    Choice("Creative Commons Licenses (CC0, CC BY etc.)"), 
                    Choice("Unlicense")
                ]
            },
            {   
                "type": "confirm",  
                "name": "confirm_license",  
                "message": "Are you sure you want to procced with this license you have choosen?",
                "default": True
                
            }, 
            {
                "type": "input",
                "name": "contact",
                "message": "Please provide contact"
            },

        ]


        # Collect the answers using InquirerPy's prompt
        answers = prompt(questions)
        
       
        # Store the answers as instance variables so they can be accessed later
        self.project_title = answers['project_title']
        self.project_description = answers['project_description']
        self.installation_instructions = answers['installation_instructions']
        self.usage_instructions = answers['usage_instructions']
        self.license_selections = answers['license_selections']
        self.confirm_license = answers['confirm_license']
        self.contact = answers['contact']

    # Display user's answers
    def display_answers(self):
        console.print(f"👀 Overview of Readme:")
        console.print(f"🚀 Project Title: [bold cyan]{self.project_title}[/bold cyan]")
        console.print(f"📝 Project Description: [bold cyan]{self.project_description}[/bold cyan]")
        console.print(f"🛠️ Installation Instructions: [bold cyan]{self.project_description}[/bold cyan]")
        console.print(f"📦 Usage Instructions: [bold cyan]{self.usage_instructions}[/bold cyan]")
        console.print(f"📄📄 License Selections: [bold cyan]{self.license_selections}[/bold cyan]")
        console.print(f"📋 Contact: [bold cyan]{self.contact} [/bold cyan]")
  
    # Generate Readme template file
    def generate_template_readme(self):
        readme_content = (
                      f"![Project Image](https://files.realpython.com/media/Creating-Good-README.md-Files-for-Your-Python-Projects_Watermarked.034ab572fa3e.jpg)\n\n"
                      f"### 🚀 Project Title\n{self.project_title}\n\n" 
                      f"### 📝 Project Description\n{self.project_description} \n\n"
                      f"### 🛠️ Installation Instructions\n{self.installation_instructions} \n\n"
                      f"### 📦 Usage Instructions\n{self.usage_instructions} \n\n"
                      f"### 📄 License\n{self.license_selections} \n\n"
                      f"### 📋 Contact\n{self.contact} \n\n"
                      f"---\n\n"
                      f"Thank you for using this README generator! We hope you find it useful! 🤗\n\n")
        # Get the current directory and create a readme file
        output_file_path = os.path.join(os.getcwd(), "readme.md")
        # Check if readme file exist, if exist, it will print out "File already existed!"
        if os.path.exists("readme.md"):
            console.print("File already existed!")
        else:
            with open(output_file_path, "w") as file:
                file.write(readme_content)
            console.print("The current directory has been created at:", os.getcwd())
            console.print(f"🎉 Congraulation! You have now successfully created your own readme.md 🙌") 
    # Create simulation for progress bar once readme file generated 
    def progress_simulation():
        console.print("[bold green]Generating readme.md file...")
        for _ in track(range(10), description="Processing..."):
            time.sleep(0.2)  # Simulate work
 


    