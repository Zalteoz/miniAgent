import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file within the working directory and returns its output (STDOUT and STDERR).",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the Python file to execute (e.g., 'main.py'). Must end in .py.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of command-line arguments to pass to the script (e.g., ['3 + 5']).",
            ),
        },
        required=["file_path"] # args is optional, so it's not in the required list
    ),
)


def run_python_file(working_directory, file_path, args=None):
    working_directory_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))

    #check if the path is valid
    valid_target_file = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

    if not valid_target_file:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if not target_file.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    

    try:
        command = ["python", target_file]
        if args:
            command.extend(args)
        
        process = subprocess.run(command, cwd=working_directory_abs, capture_output=True, text=True, timeout=30)
        
        output_parts = []

        if process.returncode != 0:
            output_parts.append(f"Process exited with code {process.returncode}")

        if process.stdout:
            output_parts.append(f"STDOUT:\n{process.stdout}")
        
        if process.stderr:
            output_parts.append(f"STDERR:\n{process.stderr}")
        
        if not process.stderr and not process.stdout:
            output_parts.append("No output produced")
        
        return "\n".join(output_parts)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    



    

