# Welcome Screen

A simple Python-based welcome screen that displays a custom message when logging in to your system. It uses a customizable font and animated text to greet the user.

## Features

- Displays a welcome message when you log in.
- Customizable text: Replace the default message with any text you like.
- Animated text effect: The message is revealed character by character.
- Custom font: **ByteBounce** is required for the full effect.

## Prerequisites

To use this project, you need:

- **Python 3.x** installed on your system.
- The **ByteBounce** font installed on your system.

## Installation

### Clone the repository

```bash
git clone https://github.com/moritzbyte/welcome_screen.git
cd welcome_screen

Install the necessary dependencies

Make sure you have Python 3 installed on your system.
Install the ByteBounce font

To use the ByteBounce font, follow these steps:

    Download the ByteBounce.ttf font file from here or any other font provider.

    Move the downloaded .ttf file to the system font directory:

sudo mkdir -p /usr/share/fonts/truetype/ByteBounce
sudo mv ByteBounce.ttf /usr/share/fonts/truetype/ByteBounce/

Update the font cache:

    sudo fc-cache -fv

Usage

    After cloning the repository, navigate to the folder where the script is located.

    To manually run the welcome screen:

python3 login_welcome.py

To make the script run at login, add it to your system's autostart configuration:

    Create a new .desktop file for autostart:

nano ~/.config/autostart/login_welcome.desktop

Füge folgenden Inhalt ein:

        [Desktop Entry]
        Type=Application
        Exec=python3 /path/to/welcome_screen/login_welcome.py
        Hidden=false
        NoDisplay=false
        X-GNOME-Autostart-enabled=true
        Name=Welcome Screen
        Comment=Displays a welcome message at login

        Ersetze /path/to/welcome_screen/ mit dem tatsächlichen Pfad zu deinem geklonten Repository.

        Speichere und schließe die Datei. Der Autostart-Eintrag wird nun beim nächsten Anmelden aktiv sein.

Known Issues

    The script is designed for Linux-based systems. You might need to adjust the settings if you're using macOS or Windows.

    Font rendering might look different based on your system and installed fonts.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    Font used: ByteBounce (this font is required for the full effect).

    Inspired by the "hacker" aesthetic seen in movies and terminal-based applications.
