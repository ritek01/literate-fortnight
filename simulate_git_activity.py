#!/usr/bin/env python3
import os
import random
import string
import subprocess
import time
from pathlib import Path

# Configuration
NUM_FILES = 2345  # Slightly over 2000 files
NUM_DIRS = 20
FILE_EXTENSIONS = ['.txt', '.md', '.json', '.yaml', '.yml']
CONTENT_LENGTH_MIN = 10
CONTENT_LENGTH_MAX = 100

# File operation counts for each commit
FILES_TO_MODIFY = 500
FILES_TO_DELETE = 200
FILES_TO_RENAME = 150

def random_content(length=None):
    """Generate random content for files"""
    if length is None:
        length = random.randint(CONTENT_LENGTH_MIN, CONTENT_LENGTH_MAX)
    return ''.join(random.choice(string.ascii_letters + string.digits + ' \n') for _ in range(length))

def run_git_command(command, *args):
    """Run a git command and print the output"""
    cmd = ['git', command] + list(args)
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, 
                           capture_output=True, 
                           text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Success: {result.stdout}")
    return result

def create_files():
    """Create the initial set of files in various directories"""
    print(f"Creating {NUM_FILES} files across {NUM_DIRS} directories...")
    
    # Create directories
    directories = []
    for i in range(NUM_DIRS):
        dir_name = f"dir_new1_1{i+1}"
        os.makedirs(dir_name, exist_ok=True)
        directories.append(dir_name)
    
    # Create files
    created_files = []
    for i in range(NUM_FILES):
        # Select a directory
        directory = random.choice(directories)
        # Create a filename
        extension = random.choice(FILE_EXTENSIONS)
        filename = f"file_{i+1}{extension}"
        filepath = os.path.join(directory, filename)
        
        # Write random content to the file
        with open(filepath, 'w') as f:
            f.write(random_content())
        
        created_files.append(filepath)
    
    print(f"Created {len(created_files)} files")
    return created_files

def commit_files(message):
    """Add all files and create a commit"""
    run_git_command("add", ".")
    run_git_command("commit", "-m", message)

def modify_files(files, count):
    """Modify a subset of files"""
    print(f"Modifying {count} files...")
    files_to_modify = random.sample(files, min(count, len(files)))
    
    for file_path in files_to_modify:
        if os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(random_content())
    
    return files_to_modify

def delete_files(files, count):
    """Delete a subset of files"""
    print(f"Deleting {count} files...")
    files_to_delete = random.sample(files, min(count, len(files)))
    
    for file_path in files_to_delete:
        if os.path.exists(file_path):
            os.remove(file_path)
    
    return files_to_delete

def rename_files(files, count):
    """Rename a subset of files"""
    print(f"Renaming {count} files...")
    files_to_rename = random.sample(files, min(count, len(files)))
    renamed_files = []
    
    for file_path in files_to_rename:
        if os.path.exists(file_path):
            directory = os.path.dirname(file_path)
            extension = os.path.splitext(file_path)[1]
            new_name = f"renamed_{int(time.time())}_{random.randint(1000, 9999)}{extension}"
            new_path = os.path.join(directory, new_name)
            
            os.rename(file_path, new_path)
            renamed_files.append(new_path)
    
    return renamed_files

def main():
    # Create initial files
    print("Step 1: Creating initial files...")
    all_files = create_files()
    commit_files("Initial commit with 278+ files")
    
    # Modify files
    # print("\nStep 2: Modifying files...")
    # remaining_files = list(all_files)  # Make a copy
    # modified_files = modify_files(remaining_files, FILES_TO_MODIFY)
    # commit_files(f"Modified {len(modified_files)} files")
    
    # # Delete files
    # print("\nStep 3: Deleting files...")
    # deleted_files = delete_files(remaining_files, FILES_TO_DELETE)
    # Remove deleted files from our tracking list
    # for file in deleted_files:
    #     if file in remaining_files:
    #         remaining_files.remove(file)
    # commit_files(f"Deleted {len(deleted_files)} files")
    
    # # Rename files
    # print("\nStep 4: Renaming files...")
    # renamed_files = rename_files(remaining_files, FILES_TO_RENAME)
    # # Update our tracking list with new filenames
    # for old_file in renamed_files:
    #     if old_file in remaining_files:
    #         remaining_files.remove(old_file)
    # commit_files(f"Renamed {len(renamed_files)} files")
    
    # # Final modifications
    # print("\nStep 5: Final modifications...")
    # final_modified = modify_files(remaining_files, FILES_TO_MODIFY // 2)
    # commit_files(f"Final modifications to {len(final_modified)} files")
    
    # Push changes
    print("\nPushing changes to remote...")
    run_git_command("push", "-u", "origin", "main")
    
    print("\nSimulation complete!")

if __name__ == "__main__":
    main()
