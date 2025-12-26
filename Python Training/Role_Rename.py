'''
Rename App
Create a CSV with two headers Original Role Name, New Role Name. 
Add the original and new role names below them, and save as a CSV.
When you open the app, add your Bundle path and your CSV path, then run.

The App will disable the old roles, then move them to the 00_Disabled folder.
It will then create the new xmls with the new file name and name/displayName values.
'''
import os
import csv
import re
import customtkinter as ctk
import logging
import shutil
import importlib
import subprocess
import sys

# Set up logging
logging.basicConfig(level=logging.INFO)

def install_missing_modules(modules):
    """Install any missing modules."""
    for module in modules:
        try:
            importlib.import_module(module)
        except ImportError:
            logging.warning(f"Module '{module}' not found. Installing...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])

# List of required modules
required_modules = ['customtkinter', 'logging', 'os', 'csv', 're', 'shutil']
install_missing_modules(required_modules)

def find_file_recursive(folder, file_name):
    """Search for a file recursively in the given folder."""
    for root, dirs, files in os.walk(folder):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

def format_file_name(role_name):
    """Format the role name into a valid file name."""
    formatted_name = re.sub(r'[^\w\-]', '_', role_name)
    return f"NAB_Bundle_{formatted_name}.xml"

def escape_special_characters(role_name):
    """Escape special characters for XML."""
    replacements = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&apos;'
    }
    for key, value in replacements.items():
        role_name = role_name.replace(key, value)
    return role_name

def process_role(row, bundle_folder, disabled_folder):
    """Process a single role from the CSV."""
    original_role = row['Original Role Name'].strip()
    new_role = row['New Role Name'].strip()

    # Escape special characters in the new role name
    new_role_escaped = escape_special_characters(new_role)

    old_file_name = format_file_name(original_role)
    new_file_name = format_file_name(new_role)

    logging.info(f"Searching for file: {old_file_name}")
    old_file_path = find_file_recursive(bundle_folder, old_file_name)

    if old_file_path:
        logging.info(f"Found file at: {old_file_path}")
    else:
        logging.warning(f"File not found: {old_file_name}")
        return original_role  # Return the original role if not found

    new_file_path = os.path.join(os.path.dirname(old_file_path), new_file_name)

    try:
        # Read the contents of the original file
        with open(old_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Use regex to modify the content for the new file
        content_new = re.sub(r'(displayName=")[^"]*(")\s+(name=")[^"]*(")', r'\1' + new_role_escaped + r'\2 \3' + new_role_escaped + r'\4', content)

        # Write the new file without the disabled attribute
        with open(new_file_path, 'w', encoding='utf-8') as file:
            file.write(content_new)
        logging.info(f"New file created: {new_file_path}")

        # Now, modify the original content to add the disabled attribute
        content_disabled = re.sub(r'(<Bundle\s+)', r'\1disabled="true" ', content)

        # Move the original file to the disabled folder with the disabled attribute
        disabled_file_path = os.path.join(disabled_folder, old_file_name)
        with open(disabled_file_path, 'w', encoding='utf-8') as file:
            file.write(content_disabled)
        logging.info(f"Original file disabled and moved to: {disabled_file_path}")

        # Remove the original file if it exists
        if os.path.exists(old_file_path):
            os.remove(old_file_path)
            logging.info(f"Original file removed: {old_file_path}")

    except Exception as e:
        logging.error(f"Unexpected error processing {old_file_name}: {e}")
        return original_role  # Return the original role if there's an error

    return None  # Return None if processed successfully

def process_files(csv_file, bundle_folder, disabled_folder):
    """Process all roles from the CSV file."""
    not_found_roles = []

    if not os.path.exists(csv_file):
        logging.error("CSV file not found.")
        return

    try:
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            headers = reader.fieldnames
            logging.info(f"CSV Headers: {headers}")

            for row in reader:
                if 'Original Role Name' not in row or 'New Role Name' not in row:
                    logging.error("CSV format error: Missing required headers.")
                    return

                not_found_role = process_role(row, bundle_folder, disabled_folder)
                if not_found_role:
                    not_found_roles.append(not_found_role)

        # Create a text file for roles not found
        if not_found_roles:
            not_found_file = os.path.join(bundle_folder, "not_found_roles.txt")
            with open(not_found_file, 'w') as f:
                for role in not_found_roles:
                    f.write(f"{role}\n")
            logging.info(f"Roles not found file created: {not_found_file}")

        logging.info("Process completed successfully.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

# Create the main application window
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue", "light-blue"

app = ctk.CTk()  # Create a CTk window
app.title("Role Renaming Tool")
app.geometry("450x300")

# Create and place widgets
bundle_folder_label = ctk.CTkLabel(app, text="Bundle Folder:")
bundle_folder_label.pack(pady=(10, 0))

bundle_folder_entry = ctk.CTkEntry(app, width=400, placeholder_text='Add the Bundle Path here')
bundle_folder_entry.pack(pady=(0, 10))

bundle_folder_button = ctk.CTkButton(app, text="Browse", command=lambda: bundle_folder_entry.insert(0, ctk.filedialog.askdirectory()))
bundle_folder_button.pack(pady=(0, 10))

csv_file_label = ctk.CTkLabel(app, text="CSV File:")
csv_file_label.pack(pady=(10, 0))

csv_file_entry = ctk.CTkEntry(app, width=400, placeholder_text='Headers = Original Role Name, New Role Name')
csv_file_entry.pack(pady=(0, 10))

csv_file_button = ctk.CTkButton(app, text="Browse", command=lambda: csv_file_entry.insert(0, ctk.filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])))
csv_file_button.pack(pady=(0, 10))

execute_button = ctk.CTkButton(app, text="Execute", command=lambda: execute_process())
execute_button.pack(pady=(10, 0))

# Function to execute the process
def execute_process():
    bundle_folder = bundle_folder_entry.get()
    csv_file = csv_file_entry.get()
    
    # Define the Disabled folder path
    disabled_folder = os.path.join(bundle_folder, "00_Disabled")
    
    # Check if the Disabled folder exists, if not, create it
    if not os.path.exists(disabled_folder):
        os.makedirs(disabled_folder)
        logging.info(f"Created folder: {disabled_folder}")
    
    execute_button.configure(state='disabled')  # Disable the button
    try:
        logging.info("Starting processing...")
        process_files(csv_file, bundle_folder, disabled_folder)
    finally:
        execute_button.configure(state='normal')  # Re-enable the button

# Start the application
app.mainloop()
