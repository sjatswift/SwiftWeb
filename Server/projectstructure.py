import os

def print_project_structure(root_dir, exclude_dirs=None, indent=''):
    if exclude_dirs is None:
        exclude_dirs = []
        
    print(indent + root_dir)
    
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path) and item not in exclude_dirs:
            print_project_structure(item_path, exclude_dirs, indent + '  ')
        else:
            print(indent + '  ' + item)

# Replace 'path_to_your_project' with the actual path to your project's root directory
project_root = './'
exclude_directories = ['env']  # Add any other directories you want to exclude
print_project_structure(project_root, exclude_directories)
