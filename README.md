# Smart Mood journal
This is a mood journal that is pretty smart, but also entirely depends on you to be smart.

The aim of this mood journal is to help you understand your feelings, and analyse them over a period of time. 

Using pandas, this journal will read your emotions, help you analyse what caused the emotion, and your general response over time.

You can also edit the list of emotions, and the feeling associated with them.

## Requirements
Smart Mood Journal requires Python 3.13 at least 

- On Windows:
  Download the right version (3.13.7+) from the official python.org website (https://www.python.org/downloads/)

- On macOS:
  Download Python (3.13.7+) from their official website(https://www.python.org/downloads/). This may also be done using Homebrew on the terminal.

- On Linux systems:
  Install python3 and pip (npm also works for downloading pandas) using the package manager of your distribution
  
  [Unix Installations](#Installation)

## Usage guide
1. After installing Python, click on the button on this repository named "<> Code" and "Download ZIP"
2. Extract ZIP file to a convenient location on your computer
3. Open Command prompt/Terminal in that location or navigate to the directory using:
  ```
cd <directory_of_mood-journal>
  ```
4. Run the program using:
```
python3 journal.py
```
[Troubleshooting](#Troubleshooting)

## Installation
- Debian:
```
sudo apt install python3
```
```
sudo apt install python3-pip
```
      
- Fedora:
```
sudo dnf install python3
```
```
sudo dnf install python3-pip
```
      
- Arch:
```
sudo pacman -S python3
```
```
sudo pacman -S python-pip
```
      
- CentOS/Red Hat:
```
sudo yum install python3
```
      
- openSUSE:
```
sudo zypper install python3
```

- macOS:
  Ensure Homebrew is installed
```
bash brew install python3
```

## Troubleshooting
If the program doesn't run, or gives an error, make sure that you have Python installed by running:
```
python3 --version
```
If not installed, install Python.

If python is installed, but error happens while trying to run, python3 may not be installed, instead of:
```
python3 journal.py
```
You may run:
```
python journal.py
```