# ButtonClicker

ButtonClicker is a Python-based script that automates clicking a button on the screen by locating it via an image. The script can be run as a standalone executable, making it easy to share and use without Python installed. This project is open-source and free to use, modify, and share under the selected open-source license.

## Features

- Locate a button on the screen using an image and click it automatically.
- Blocks mouse and keyboard input during the click to prevent interference (optional).
- Allows arguments to configure the scan interval, image location, and input blocking.
- Logs activity with timestamps for better debugging.
- Easy setup and usage with command-line arguments.

## Requirements

- Python 3.6+
- Required Python packages: `pyautogui`, `pygetwindow`, `argparse`

## Installation

### Running from Source

1. Clone the repository:

   ```sh
   git clone https://github.com/nate3D/ButtonClicker.git
   cd ButtonClicker
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the script:

   ```sh
   python ButtonClicker.py --scan_interval 2 --block_input --button_image "image.png"
   ```

### Creating an Executable

If you'd like to create an executable file to run this script without Python, follow these steps:

1. Install `PyInstaller`:

   ```sh
   pip install pyinstaller
   ```

2. Create the executable:

   ```sh
   pyinstaller --onefile ButtonClicker.py
   ```

   Make sure to place `image.png` in the same directory as the executable for it to work correctly.

## Running the Executable (v1.0.0 Release)

A pre-built executable (`ButtonClicker.exe`) is available for version 1.0.0. To run the executable:

1. Download `ButtonClicker.exe` from the [releases page](https://github.com/nate3D/ButtonClicker/releases/tag/1.0.0).
2. Place `image.png` in the same directory as `ButtonClicker.exe`.
3. Run the executible by double-clicking it or from the command line.
4. To specify options from the command line, use the following format:

   ```sh
   ButtonClicker.exe --scan_interval 2 --block_input --button_image "image.png"
   ```

   You can adjust the `--scan_interval` and use `--block_input` as needed. Ensure that the `image.png` is available in the same directory for correct functionality.
5. To stop the script, close the command prompt window or use `Ctrl+C` in the terminal.

## Usage

ButtonClicker can be customized with the following command-line arguments:

- `--scan_interval`: Interval in seconds to scan for the button (default: 1).
- `--block_input`: Block user input during the button click (optional flag).
- `--button_image`: Name of the image file for the button to be clicked (default: `image.png`).

### Example

To run the script with a 2-second scan interval and block input:

```sh
python ButtonClicker.py --scan_interval 2 --block_input --button_image "image.png"
```

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you have any suggestions, feel free to submit an issue or a pull request.

## Disclaimer

Use this script responsibly. The input-blocking feature can prevent normal use of the computer while it is active. Ensure you understand the consequences before enabling this feature.

## Author

Developed by [Your Name].

## Acknowledgments

- [PyAutoGUI](https://pyautogui.readthedocs.io/) for the automation of mouse and keyboard.
- [PyGetWindow](https://github.com/asweigart/PyGetWindow) for window management.

