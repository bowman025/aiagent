import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        target_dir_list = os.listdir(target_dir)
        files_list = []
        for filename in target_dir_list:
            filepath = os.path.join(target_dir, filename)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_list.append(
                f"- {filename}: file-size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_list)
    except Exception as e:
        return f"Error listing files: {e}"
