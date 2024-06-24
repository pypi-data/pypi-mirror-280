import os
from cifkit.utils import folder
import glob
from cifkit.models.cif import Cif
from cifkit.utils.error_messages import CifParserError
from pathlib import Path


def make_directory_and_move(file_path, dir_path, new_file_path):
    """Create directory if it doesn't exist and move the file."""
    os.makedirs(dir_path, exist_ok=True)
    new_file_path = os.path.join(dir_path, new_file_path)
    os.rename(file_path, new_file_path)


def move_files_based_on_errors(dir_path, process_nested_files=False):
    print(f"\nCIF Preprocessing in {dir_path} begun...\n")

    # Ensure dir_path is a Path object
    dir_path = Path(dir_path)

    # Dictionary to hold directory paths for each error type
    error_op_str = "error_operations"
    error_duplicate_str = "error_duplicate_labels"
    error_wrong_loop_value_str = "error_wrong_loop_value"
    error_coords_str = "error_coords"
    error_invalid_label_str = "error_invalid_label"
    error_others_str = "error_others"

    error_directories = {
        error_op_str: dir_path / error_op_str,
        error_duplicate_str: dir_path / error_duplicate_str,
        error_wrong_loop_value_str: dir_path / error_wrong_loop_value_str,
        error_coords_str: dir_path / error_coords_str,
        error_invalid_label_str: dir_path / error_invalid_label_str,
        error_others_str: dir_path / error_others_str,
    }

    # Ensure all direct

    num_files_moved = {key: 0 for key in error_directories.keys()}

    if process_nested_files:
        file_paths = folder.get_file_paths(
            str(dir_path), add_nested_files=True
        )

    else:
        file_paths = folder.get_file_paths(str(dir_path))

    for i, file_path in enumerate(file_paths, start=1):
        filename = os.path.basename(file_path)
        print(f"Preprocessing {file_path} ({i}/{len(file_paths)})")
        try:
            Cif(file_path)
        except Exception as e:
            error_message = str(e)
            # Example of handling specific errors, adjust as needed
            if "symmetry operation" in error_message:
                error_type = error_op_str
            elif "contains duplicate atom site labels" in error_message:
                error_type = error_duplicate_str
            elif "Wrong number of values in loop" in error_message:
                error_type = error_wrong_loop_value_str
            elif "missing atomic coordinates" in error_message:
                error_type = error_coords_str
            elif "element was not correctly parsed" in error_message:
                error_type = error_invalid_label_str
            else:
                error_type = error_others_str

            make_directory_and_move(
                file_path, error_directories[error_type], filename
            )
            num_files_moved[error_type] += 1
            print(
                f"File {filename} moved to '{error_type}' due to: {error_message}"
            )

    # Display the number of files moved to each folder
    print("\nSUMMARY")
    for error_type, count in num_files_moved.items():
        print(f"# of files moved to '{error_type}' folder: {count}")
    print()
