# BioOps File Sanitizer

A beginner Python command-line tool that adds a configurable prefix to filenames in a specified directory.

## Features

- Select files by extension.
- Configure the filename prefix.
- Preview changes using dry-run mode.
- Skip files that already have the requested prefix.
- Skip files when the destination filename already exists.
- Display a summary of renamed, skipped, and previewed files.
- Report invalid directory paths.

## Requirements

- Python 3
- No third-party packages required

## Usage

Preview filename changes:

```powershell
python sanitizer.py --dir rename_practice --dry-run
```

Filter by extension:

```powershell
python sanitizer.py --dir rename_practice --ext csv --dry-run
```

Use a custom prefix:

```powershell
python sanitizer.py --dir rename_practice --ext csv --prefix bioops_ --dry-run
```

Rename files:

```powershell
python sanitizer.py --dir rename_practice --ext csv
```

## Available Options

| Option | Description |
|---|---|
| `--dir` | Required directory to process |
| `--ext` | Optional file extension filter |
| `--prefix` | Filename prefix; defaults to `cleaned_` |
| `--dry-run` | Preview changes without renaming files |
| `-h`, `--help` | Display command-line help |

## Safety

Use dry-run mode before renaming files. Test with disposable files and backups before processing important data.

## Current Status

Initial version implemented and manually tested against several common scenarios. Further automated tests and error-handling improvements are planned.
