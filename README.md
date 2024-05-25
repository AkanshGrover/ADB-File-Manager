# ADB File Manager

Ever felt that copying files via MTP on Android was slow or caused issues? Introducing ADB File Manager! This program helps you copy, move and delete folders or files between your Android device and computer using ADB protocols. All you need to do is enable Android debugging on your device and connect it to your PC.


  
## How to use the app?

**Windows:**

 1. Download the executable from the [releases](https://github.com/AkanshGrover/ADB-File-Manager/releases).
 2. Simply run the executable file and connect your USB debugging
    enabled Android device to the computer.

  

**Linux:**

 1. Download the compressed zip file from the [releases](https://github.com/AkanshGrover/ADB-File-Manager/releases) and unzip it.
 2. Run `linux_installer.sh` once as root to install the app. After
    installation, just run the app and connect your USB debugging
    enabled Android device to the computer.

  

## How to generate an executable

**Windows:**

  

1. Install the latest version of python.

2. Install Pyside6 and Nuitka using python-pip.

3. Download or clone this repository and open a terminal window from the folder.

4. Run the following command to generate an executable:

```sh

python -m nuitka --onefile --windows-icon-from-ico=icons/alticon.ico  --include-data-dir=windows-adb=windows-adb  --include-data-dir=icons=icons  --include-data-files=windows-adb/adb.exe=windows-adb/adb.exe  --include-data-files=windows-adb/AdbWinApi.dll=windows-adb/AdbWinApi.dll  --include-data-files=windows-adb/AdbWinUsbApi.dll=windows-adb/AdbWinUsbApi.dll  --include-data-files=windows-adb/libwinpthread-1.dll=windows-adb/libwinpthread-1.dll  --enable-plugin=pyside6  --disable-console  main.py

```

  

**Linux:**

1. Install the latest version of python.

2. Install Pyside6 and PyInstaller.

3. Download or clone this repository and open a terminal window from the folder.

4. Run the following command to generate an executable:

```sh

python -m PyInstaller --onefile --windowed --add-data="icons/alticon.png:."  --add-data="icons:."  --name="adb-fm"  main.py  --clean

```



## Screenshots

**Windows:**

This app supports both light and dark modes.

![Pic (1)](https://github.com/AkanshGrover/ADB-File-Manager/assets/163346711/8437ddc6-2a68-4e60-a565-a3af4f15319d)
![Pic (5)](https://github.com/AkanshGrover/ADB-File-Manager/assets/163346711/ff9bb5e7-bff3-4869-8ae3-f6e79768f34e)
![Pic (2)](https://github.com/AkanshGrover/ADB-File-Manager/assets/163346711/5fac5883-4e78-477e-aed1-670414fa5b8e)
![Pic (3)](https://github.com/AkanshGrover/ADB-File-Manager/assets/163346711/78380510-bcba-479a-8e75-9630cb77d417)
![Pic (4)](https://github.com/AkanshGrover/ADB-File-Manager/assets/163346711/0543ea3d-b5db-4dac-9c89-a18bccdca5b7)


**Linux:**

![pic (1)](https://github.com/AkanshGrover/ADB-File-Manager/assets/163346711/90bc0ee7-078e-4737-838c-cc6bfcf4807a)
![pic (4)](https://github.com/AkanshGrover/ADB-File-Manager/assets/163346711/329c85ae-4308-44bf-adea-f67ea9723d3a)
![pic (3)](https://github.com/AkanshGrover/ADB-File-Manager/assets/163346711/24f62c92-e8c6-47ee-b89d-f542f44f6e98)
![pic (2)](https://github.com/AkanshGrover/ADB-File-Manager/assets/163346711/920555d1-404b-4147-8e80-2e0f1033fc24)

