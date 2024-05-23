#!/usr/bin/env bash

#made by Akansh

if [ "$(id -u)" -ne 0 ]; then
        echo 'This installer script must be run as root.'
        exit 1
fi


echo ""
echo "Checking installed package manager."
if [[ -f "/usr/bin/apt" ]]
then
    echo "Starting installation"
    echo ""
    echo "Package manager is apt"
    apt update && apt-get install android-sdk-platform-tools
elif [[ -f "/usr/bin/pacman" ]]
then
    echo "Starting installation"
    echo ""
    echo "Package manager is pacman"
    pacman -Sy android-tools
elif [[ -f "/usr/bin/dnf" ]]
then
    echo "Starting installation"
    echo ""
    echo "Package manager is dnf"
    dnf install android-tools
else
    echo ""
    echo -e "Unfortunately this installer only works on distributions that utilize the following package managers:\n1) pacman\n2) apt\n3) dnf"
    echo ""
    echo "Although the application works on all distributions, this installer script doesn't support installing android tools on every distro. You can manually install android tools and then rerun this script."
    echo ""
    read -p "If you have manually installed android-tools and wish to install the app, please enter "\install"\ : " ip
fi

if [[ -f "/usr/bin/adb" ]]
then
    echo ""
    echo "Successfully install adb"
    echo ""
    ip="install"
else
    echo ""
    echo "Installation failed"
    exit 1
fi

if [[ $ip=="install" ]]
then
    mv adb-fm.png /usr/share/icons/
    mv adb-fm /usr/bin/
    echo -e "[Desktop Entry]\\n\\nType=Application\\nVersion=1.0\\nName=ADB File Manager\\nComment=Utilizes ADB for seamless file management between Android and desktop.\\nExec=adb-fm\\nIcon=/usr/share/icons/adb-fm.png\\nTerminal=false\\nCategories=Utility" >> ADB-File-Manager.desktop
    mv ADB-File-Manager.desktop /usr/share/applications/
    chmod +x /usr/share/applications/ADB-File-Manager.desktop
    chmod +x /usr/bin/adb-fm
    echo "Finished installation"
fi