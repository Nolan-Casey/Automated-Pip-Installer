import subprocess
import pkgutil
import sys

def get_imports(file_path):
    with open(file_path, 'r') as file: 
        lines = file.readlines()
    imports = [lines.split()[1] for line in lines if line.startswith('import')]
    return imports

def is_module_installed(module_name): 
    return pkgutil.find_loader(module_name) is not None

def install_module(module_name):
    subprocess.check_call(["pip", "install", module_name])
    
def main(file_path):
    modules = get_imports(file_path)
    for module in modules:
        if not is_module_installed(module):
            print(f"Installing {module}...")
            install_module(module)
            print(f"{module} installed successfully!")
        else:
            print(f"{module} is already installed.")
        
def excute_script(script_path):
    subprocess.run(["python", script_path] + sys.argv[2:])
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the path to the Python script you want to run.")
        sys.exit(1)
    
    target_script = sys.argv[1]
    main(target_script)
    excute_script(target_script)
        
