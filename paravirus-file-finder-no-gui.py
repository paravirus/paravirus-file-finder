import os

class FileSearchApp:
    def search_file(self, target_filename):
        found_paths = self.find_files(target_filename)

        if found_paths:
            results = []
            for path in found_paths:
                results.append(f"File '{target_filename}' found at:\n{path}\n\n")
            return results
        else:
            return [f"File '{target_filename}' not found in any directory and its subdirectories."]

    def find_files(self, filename):
        found_paths = []
        for root, dirs, files in os.walk('/'):
            if filename in files:
                found_paths.append(os.path.join(root, filename))
        return found_paths

def main():
    app = FileSearchApp()
    target_filename = input("Enter the filename: ")
    if not target_filename:
        print("Please enter a filename.")
        return

    results = app.search_file(target_filename)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
