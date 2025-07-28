#!/usr/bin/env python3
import os
import random
import string

def generate_random_string(length=8):
    """Generate a random string of specified length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def create_yaml_file(file_path, name, identifier):
    """Create a YAML file with the specified name and identifier."""
    # Create YAML content as a formatted string
    yaml_content = f"""service:
  name: {name}
  identifier: {identifier}
  orgIdentifier: AutoCreate_tests
  serviceDefinition:
    spec: {{}}
    type: Kubernetes
"""
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write YAML file
    with open(file_path, 'w') as f:
        f.write(yaml_content)

def main():
    """Generate 541 YAML files with random names and identifiers."""
    # Create .harness directory if it doesn't exist
    harness_dir = os.path.join(os.getcwd(), '.harness/orgs/AutoCreate_tests/services')
    os.makedirs(harness_dir, exist_ok=True)
    
    print(f"Generating 521 YAML files in {harness_dir}...")
    
    # Generate 541 files
    for i in range(1, 521):
        # Generate random name for the file
        file_name = f"{generate_random_string(6)}_{i}.yaml"
        file_path = os.path.join(harness_dir, file_name)
        
        # Generate random name and identifier for the content
        service_name = generate_random_string(8)
        service_identifier = service_name
        
        # Create the YAML file
        create_yaml_file(file_path, service_name, service_identifier)
        
        # Print progress every 50 files
        if i % 50 == 0:
            print(f"Generated {i} files...")
    
    print(f"Successfully generated 541 YAML files in {harness_dir}")

if __name__ == "__main__":
    main()
