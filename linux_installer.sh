#!/usr/bin/env bash

#made by Akansh

if [ "$(id -u)" -eq 0 ]
then
    echo 'Do not run this installer script as root.'
    exit 1
fi

echo ""
echo "Starting installation"
echo ""

echo "Cleaning older version of this app if it is present"
if [ -f "/usr/share/icons/adb-fm.png" ]
then
    sudo rm "/usr/share/icons/adb-fm.png"
fi
if [ -f "/usr/bin/adb-fm" ]
then
    sudo rm "/usr/bin/adb-fm"
fi
if [ -f "/usr/share/applications/ADB-File-Manager.desktop" ]
then
    sudo rm "/usr/share/applications/ADB-File-Manager.desktop"
fi
echo "Cleaning finished"
echo ""

if command -v python3 > /dev/null 2>&1
then
    echo "Python3 is installed"
else
    echo "Python3 is not installed. Install it and re-run the script"
    exit 1
fi

if command -v pip3 > /dev/null 2>&1
then
    echo "pip3 is installed"
else
    echo "pip3 is not installed. Install it and re-run the script"
    exit 1
fi

if python3 -m venv --help > /dev/null 2>&1
then
    echo "venv is installed"
    echo ""
    echo "Testing venv"
    if python3 -m venv venv_test > /dev/null 2>&1
    then
        echo "venv works"
        rm -rf venv_test
    else
        rm -rf venv_test
        echo "venv does not work"
        echo "Try installing python3-venv"
        exit 1
    fi
else
    echo "venv is not installed. Install it and re-run the script"
    exit 1
fi

ip="yes"
pm="none"

echo ""
echo "Checking installed package manager."
if [[ -f "/usr/bin/apt" ]]
then
    echo "Package manager is apt"
    pm="apt"
elif [[ -f "/usr/bin/pacman" ]]
then
    echo "Package manager is pacman"
    pm="pac"
elif [[ -f "/usr/bin/dnf" ]]
then
    echo "Package manager is dnf"
    pm="dnf"
else
    echo ""
    echo "This app needs ADB and xcb-cursor package to be installed for it work. Unfortunately this installer only works on distributions that utilize the following package managers:\n1) pacman\n2) apt\n3) dnf"
    echo ""
    echo "Although the application works on all distributions, this installer script doesn't support installing ADB and xcb-cursor on every distro. You can manually install these packages and then rerun this script."
    pm="other"
fi


case "$pm" in
    apt)
        echo ""
        echo "Installing android-sdk-platform-tools"
        echo ""
        sudo apt update
        sudo apt install android-sdk-platform-tools -y
        echo ""
        echo "Installing libxcb-cursor0 (required for PySide6)"
        echo ""
        sudo apt install libxcb-cursor0 -y

        if command -v adb >/dev/null 2>&1
        then
            echo ""
            echo "ADB is installed"
        else
            echo ""
            echo "ADB is not installed"
            ip="no"
        fi

        if dpkg -s "libxcb-cursor0" >/dev/null 2>&1
        then
            echo ""
            echo "libxcb-cursor is installed"
        else
            echo ""
            echo "libxcb-cursor is not installed"
            ip="no"
        fi
        ;;
    pac)
        echo ""
        echo "Installing android-tools"
        echo ""
        sudo pacman -Sy android-tools --noconfirm
        echo ""
        echo "Installing xcb-util-cursor (required for PySide6)"
        echo ""
        sudo pacman -S xcb-util-cursor --noconfirm

        if command -v adb >/dev/null 2>&1
        then
            echo ""
            echo "ADB is installed"
        else
            echo ""
            echo "ADB is not installed"
            ip="no"
        fi
        
        if pacman -Q "xcb-util-cursor" >/dev/null 2>&1
        then
            echo ""
            echo "xcb-util-cursor is installed"
        else
            echo ""
            echo "xcb-util-cursor is not installed"
            ip="no"
        fi
        ;;
    dnf)
        echo ""
        echo "Installing android-tools"
        echo ""
        sudo dnf install android-tools -y
        echo ""
        echo "Installing xcb-util-cursor (required for PySide6)"
        echo ""
        sudo dnf install xcb-util-cursor -y

        if command -v adb >/dev/null 2>&1
        then
            echo ""
            echo "ADB is installed"
        else
            echo ""
            echo "ADB is not installed"
            ip="no"
        fi

        if dnf list installed "xcb-util-cursor" >/dev/null 2>&1
        then
            echo ""
            echo "xcb-util-cursor is installed"
        else
            echo ""
            echo "xcb-util-cursor is not installed"
            ip="no"
        fi
        ;;
    other)
        echo ""
        read -p "If you have manually installed ADB and xcb-cursor and wish to install the app, please enter (yes/no): " ip
        ;;
esac

if [[ "${ip,,}" == "yes" ]]
then
    echo ""
    echo "Initial checks completed"
    echo ""
    echo "Starting app compilation"
    echo ""
    echo "Setting up the environment"
    echo ""

    python3 -m venv ./venv
    source venv/bin/activate
    pip install pyside6 pyinstaller

    echo ""
    echo "Verifying environment"
    echo ""

    if python3 -c "import PySide6" > /dev/null 2>&1
    then
        echo "Successfully installed PySide6"
    else
        echo "Could not install PySide6"
        exit 1
    fi

    if python3 -c "import PyInstaller" > /dev/null 2>&1
    then
        echo "Successfully installed PyInstaller"
    else
        echo "Could not install PyInstaller"
        exit 1
    fi

    echo "Environment successfully verified"

    echo ""
    echo "Starting app compilation"
    echo ""

    if python3 -m PyInstaller --onefile --windowed --add-data="icons:icons" --name="adb-fm" main.py --clean
    then
        echo "Successfully compiled the app"
    else
        echo "Compilation unsuccessful"
        exit 1
    fi

    echo ""
    echo "The compiled app is stored in dist folder"
    echo ""
    echo "Moving files to their respective directories"

    sudo mv "icons/alticon-adb-fm.png" "/usr/share/icons/"
    sudo mv "dist/adb-fm" "/usr/local/bin/"
    echo -e "[Desktop Entry]\\n\\nType=Application\\nVersion=1.0\\nName=ADB File Manager\\nComment=Utilizes ADB for seamless file management between Android and desktop.\\nExec=adb-fm\\nIcon=/usr/share/icons/alticon-adb-fm.png\\nTerminal=false\\nCategories=Utility;" > ADB-File-Manager.desktop
    sudo mv ADB-File-Manager.desktop /usr/share/applications/
    sudo chmod +x /usr/share/applications/ADB-File-Manager.desktop
    sudo chmod +x /usr/local/bin/adb-fm

    echo ""
    echo "Successfully moved files"
    echo ""
    echo "ADB File Manager has been successfully installed on your device."
else
    echo ""
    echo "Exiting..."
    exit 1
fi