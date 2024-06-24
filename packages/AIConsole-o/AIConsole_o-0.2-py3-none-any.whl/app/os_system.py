import platform
import sys

def get_system_info():
    system_info = {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Platform": platform.platform(),
        "Python Version": sys.version,
        "Python Implementation": platform.python_implementation(),
        "Architecture": platform.architecture(),
        "Node": platform.node(),
    }

    return system_info

def display_system_info():
    info = get_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")
    
    

