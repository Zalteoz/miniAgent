import os
from config import MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a specific file and returns it as a string. Large files will be truncated.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the file that should be read (e.g., 'main.py' or 'pkg/calculator.py').",
            ),
        },
        required=["file_path"]
    ),
)


def get_file_content(working_directory, file_path):
    working_directory_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))


    #check if the path is valid
    valid_target_file = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

    if not valid_target_file:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" is not a file'
    
    
    try:
        with open(target_file, 'r') as f:
            contents = f.read(MAX_CHARS)
            
            if f.read(1):
                contents += f'\n\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return contents
    except Exception as e:
        return f"Error: could not read file {str(e)}"
    
    
