# Robocopy GUI Project

## Overview

This project is a Python-based graphical user interface (GUI) application designed to simplify the usage of Robocopy, a powerful command-line tool for file copying, synchronization, and mirroring in Windows. With this GUI, users can easily configure their Robocopy tasks, manage advanced settings, and monitor progress without having to memorize complex command-line arguments.

The application supports:
- Basic folder selection for source and destination.
- Advanced Robocopy options, configurable through an "Excel-like" settings window.
- Real-time progress tracking and logging.
- The ability to generate a standalone, single-file executable for ease of use.

---

## Features

1. **User-Friendly GUI**:
   - Easily select source and destination folders.
   - Toggle advanced Robocopy flags using an interactive settings table.
   - Monitor progress and view logs in real-time.

2. **Advanced Settings**:
   - Configure all available Robocopy flags through a customizable table.
   - Enable/disable specific flags and input custom values for parameters.

3. **Standalone Executable**:
   - Option to generate a single-file executable for running the application without requiring Python or dependencies on the target system.

---

## Installation

### Prerequisites
1. **Python**: Make sure Python 3.x is installed on your system. You can download it from [Python.org](https://www.python.org/).
2. **Dependencies**:
   Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Run the Python Script
To run the application directly using Python:
```bash
python main.py
```

### Generate a Single-File Executable
To create a standalone executable, you can use **PyInstaller**, a popular tool for packaging Python scripts into executables.

#### Steps:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Generate the executable:
   ```bash
   pyinstaller --onefile main.py
   ```

3. After running this command, the standalone executable will be generated in the `dist` folder.

4. Run the generated executable:
   ```bash
   ./dist/main.exe
   ```

### Note:
- The standalone executable can be shared and run on systems without Python installed.
- Ensure that all required files (such as `config.txt`) are available in the same directory as the executable or use absolute paths.

---

## File Structure

```
.
├── main.py               # Main application script
├── robocopy_logic.py     # Contains the logic for handling Robocopy operations
├── advanced_settings.py  # Handles the advanced settings window
├── requirements.txt      # List of dependencies for the project
├── README.md             # Documentation for the project
└── config.txt            # (Optional) Configuration file for saving user settings
```

---

## Contribution

Feel free to fork this repository and submit pull requests to improve the project. Suggestions and improvements are always welcome!

---

## License

This project is open source and distributed under the MIT License.

---

This `README.md` provides users with clear instructions on running the project and creating an executable. If you'd like to add additional sections or make changes, just let me know!
