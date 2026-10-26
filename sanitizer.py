# Import Path to work with file and folder paths.
from pathlib import Path

# Import argparse to read options entered in the terminal.
import argparse

# Create the object that will define and read terminal arguments.
parser = argparse.ArgumentParser()

# Counters: all start at zero.
renamed_count = 0      # Number of files actually renamed
skipped_count = 0      # Number of files skipped
previewed_count = 0    # Number of rename operations previewed

# Define the command-line options our program accepts.
parser.add_argument("--dir", required=True)  # Folder to process
parser.add_argument("--ext")                  # Optional file extension
parser.add_argument("--prefix", default="cleaned_")  # New filename prefix
parser.add_argument("--dry-run", action="store_true")  # Preview instead of renaming

# Read the options supplied by the user in the terminal.
args = parser.parse_args()

# Convert the supplied folder path into a Path object.
data_dir = Path(args.dir)

# Continue only if the supplied path is a directory.
if data_dir.is_dir():

    # Go through each item directly inside the directory.
    for file_path in data_dir.iterdir():

        # Ignore folders and process files only.
        if file_path.is_file():

            # If no extension was supplied, accept every file.
            # Otherwise, compare the file extension with the requested one.
            # This allows both "csv" and ".csv" as input.
            if args.ext is None or file_path.suffix == "." + args.ext.strip("."):

                # Skip files that already start with the requested prefix.
                if file_path.name.startswith(args.prefix):
                    skipped_count += 1
                    print("SKIPPED: File already has prefix:", file_path.name)

                    # Skip the remaining code for this file
                    # and continue to the next item.
                    continue

                # Build the proposed new filename.
                new_name = args.prefix + file_path.name

                # Build the new path in the same directory.
                new_path = file_path.with_name(new_name)

                # Avoid renaming if the destination already exists.
                if new_path.exists():
                    print("SKIPPED: File already exists:", new_path.name)
                    skipped_count += 1

                else:
                    # If dry-run is enabled, preview the change only.
                    if args.dry_run:
                        print("DRY RUN:", file_path.name, "->", new_path.name)
                        previewed_count += 1

                    else:
                        # Actually rename the file.
                        file_path.rename(new_path)
                        print("Renamed:", file_path.name, "->", new_path.name)
                        renamed_count += 1

# Handle a path that exists but isn't a directory.
elif data_dir.exists():
    parser.error(f"ERROR: The provided path exists, but it is not a directory: {data_dir}")

# Handle a path that doesn't exist.
else:
    parser.error(f"Path does not exist: {data_dir}")

# Print a summary of the operations performed.
print("Summary:")
print("Renamed_file_count:", renamed_count)
print("Skipped_file_count:", skipped_count)
print("Previewed_file_count:", previewed_count)