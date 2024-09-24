#!/bin/bash

# Prompt the user for installation method
echo "Would you like to install packages in a virtual environment(Recommended)? (y/n)"
read -r install_in_venv

if [[ "$install_in_venv" == "y" ]]; then
    # Create a Python virtual environment
    VENV_DIR="venv"

    if [ ! -d "$VENV_DIR" ]; then
        echo "Creating virtual environment..."
        python3 -m venv "$VENV_DIR"
    fi

    # Activate the virtual environment
    source "$VENV_DIR/bin/activate"

    # Upgrade pip
    pip install --upgrade pip

    echo "Installing packages in the virtual environment..."
else
    echo "Installing packages system-wide..."
fi

# Install required Python packages line by line
pip install mediapipe
pip install numpy
pip install pandas
pip install opencv-python
pip install tensorflow
pip install keras
pip install pygame

# Note: Tkinter is usually included with Python. If not, you can install it with:
if [[ "$install_in_venv" == "n" ]]; then
    sudo apt install python3-tk -y
fi

# Notify user of completion
echo "All required packages have been installed."

# Deactivate the virtual environment if it was activated
if [[ "$install_in_venv" == "y" ]]; then
    deactivate
fi
