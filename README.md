# Smart Mood journal
This is a mood journal that is pretty smart, but also entirely depends on you to be smart.

The aim of this mood journal is to help you understand your feelings, and analyse them over a period of time. 

Using pandas, this journal will read your emotions, help you analyse what caused the emotion, and your general response over time.

You can also edit the list of emotions, and the feeling associated with them.

## Requirements
Smart Mood Journal recommends Python 3.13 at least, however, python 2.x versions do work as well

- On Windows:
  Download the right version from the official python.org website (https://www.python.org/downloads/)

- On macOS:
  Download Python from their official website(https://www.python.org/downloads/). This may also be done using Homebrew on the terminal.

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
sudo apt install python3-pip
```
- Fedora:
```
sudo dnf install python3
sudo dnf install python3-pip
```
- Arch:
```
sudo pacman -S python3
sudo pacman -S python-pip
```
- CentOS/Red Hat:
```
sudo yum install python
sudo yum install python-pip
```

- openSUSE:
```
sudo zypper install python
sudo zypper install python-pip
```

- macOS:
  Ensure Homebrew is installed

```
bash brew install python
```

Then install pandas and matplotlib

- Using pip:

  ```
  pip install pandas
  pip install matplotlib
  ```

- Using npm:

  ```
  npm install pandas
  npm install matplotlib
  ```

## Troubleshooting

If the program doesn't run, or gives an error, make sure that you have Python installed by running:
```
python --version
```
If not installed, install Python.

If python is installed, but error occurs while trying to run, python may not be installed, instead of:
```
python journal.py
```
You may run:
```
python3 journal.py
```
Also check if pandas and matplotlib are installed 
- Using pip:
```
pip list
```
- Using npm:
```
npm list
```

