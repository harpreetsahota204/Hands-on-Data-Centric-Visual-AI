import os
import json
import re
import subprocess

def extract_packages_from_first_cell(notebook_path):
    """
    Extracts package names from the first cell of a Jupyter notebook.

    The function looks for a comment starting with '# pip install' in the first cell
    and extracts the package names listed after it.

    Args:
        notebook_path (str): The path to the Jupyter notebook file.

    Returns:
        list: A list of package names extracted from the first cell.
    """
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
            if notebook['cells']:
                first_cell = notebook['cells'][0]
                if first_cell['cell_type'] == 'code':
                    code = ''.join(first_cell['source'])
                    # Find the pip install comment and extract packages
                    match = re.search(r'^\s*#\s*pip\s+install\s+([^\n]+)', code, re.MULTILINE)
                    if match:
                        packages = match.group(1).split()
                        # Filter out non-package arguments
                        packages = [pkg for pkg in packages if not pkg.startswith('-')]
                        return packages
    except Exception as e:
        print(f"Error processing {notebook_path}: {e}")
    return []

def get_conda_package_versions():
    """
    Gets the versions of packages installed in the current conda environment.

    Returns:
        dict: A dictionary mapping package names to their versions.
    """
    result = subprocess.run(['conda', 'list'], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()
    package_versions = {}
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            package_name = parts[0]
            package_version = parts[1]
            package_versions[package_name] = package_version
    return package_versions

def main():
    """
    Main function to generate a requirements.txt file.

    The function scans all directories and subdirectories for Jupyter notebook files,
    extracts package names from the first cell of each notebook, cross-checks the versions
    with the current conda environment, and writes the unique package names with versions
    to a requirements.txt file.
    """
    requirements = set()
    # Get the versions of packages installed in the current conda environment
    package_versions = get_conda_package_versions()
    
    # Walk through all directories and subdirectories
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.ipynb'):
                notebook_path = os.path.join(root, file)
                print(f"Processing {notebook_path}")
                packages = extract_packages_from_first_cell(notebook_path)
                if packages:
                    print(f"Found packages: {packages}")
                # Update the set of requirements with the found packages
                requirements.update(packages)
    
    # Write the unique requirements with versions to requirements.txt
    with open('requirements.txt', 'w') as f:
        for requirement in sorted(requirements):
            if requirement in package_versions:
                f.write(f"{requirement}=={package_versions[requirement]}\n")
            else:
                f.write(f"{requirement}\n")
    print("requirements.txt has been generated.")

if __name__ == '__main__':
    main()