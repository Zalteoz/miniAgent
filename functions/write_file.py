import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Creates a new file or overwrites an existing file with specified content. It automatically creates any missing parent directories.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the file to be written (e.g., 'notes.txt' or 'logs/session.log').",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write into the file.",
            ),
        },
        required=["file_path", "content"]
    ),
)


def write_file(working_directory, file_path, content):
    working_directory_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))


    #check if the path is valid
    valid_target_file = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

    if not valid_target_file:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    #make sure that the path to the file exists, create directories if needed
    target_dir = os.path.dirname(target_file)
    os.makedirs(target_dir, exist_ok=True)

    try:
        with open(target_file, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: could not write file {str(e)}"

