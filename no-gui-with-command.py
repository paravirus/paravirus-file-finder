import os
import subprocess

class FileSearchApp:
    def search_file(self, target_filename):
        found_paths = self.find_files(target_filename)

        if found_paths:
            return found_paths
        else:
            return [f"File '{target_filename}' not found in any directory and its subdirectories."]

    def find_files(self, filename):
        found_paths = []
        for root, dirs, files in os.walk('/'):
            if filename in files:
                found_paths.append(os.path.join(root, filename))
        return found_paths

def print_welcome():
    welcome_text = """

██████╗░░█████╗░██████╗░░█████╗░██╗░░░██╗██╗██████╗░██╗░░░██╗░███████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║██║██╔══██╗██║░░░██║██╔██╔══╝
██████╔╝███████║██████╔╝███████║╚██╗░██╔╝██║██████╔╝██║░░░██║╚██████╗░
██╔═══╝░██╔══██║██╔══██╗██╔══██║░╚████╔╝░╚═╝██╔══██╗██║░░░██║░╚═██╔██╗
██║░░░░░██║░░██║██║░░██║██║░░██║░░╚██╔╝░░██╗██║░░██║╚██████╔╝███████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝░
                            !File Finder!
   """
    print(welcome_text)

def main():
    print_welcome()

    app = FileSearchApp()
    target_filename = input("Enter the filename: ")
    if not target_filename:
        print("Please enter a filename.")
        return

    results = app.search_file(target_filename)
    if results:
        for index, result in enumerate(results, start=1):
            print(f"{index}. {result}")

        option = input("Select a file by entering its number (or press Enter to exit): ")
        if option:
            try:
                selected_index = int(option) - 1
                if 0 <= selected_index < len(results):
                    selected_path = results[selected_index]
                    print(f"Selected file: {selected_path}")
                    run_command = input("Do you want to run a command on this file? (yes/no): ").lower()
                    if run_command == "yes":
                        command = input("Enter the command to run on the selected file: ")
                        if command:
                            try:
                                full_command = f"{command} {selected_path}"
                                subprocess.run(full_command, shell=True, text=True)
                            except Exception as e:
                                print(f"Error executing command: {e}")
                        else:
                            print("No command provided.")
                    elif run_command == "no":
                        print("No command will be executed.")
                    else:
                        print("Invalid choice.")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input.")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
