#made by Akansh
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QMessageBox, QInputDialog)
from PySide6.QtCore import QThread, Signal
from mainui import Ui_MainWindow
from mainui_dialog import Ui_Dialog
from mainui_pb import ProgressBar_Dialog
from mainui_folderdialog import Folder_Dialog
from mainuiwadb_dialog import Ui_Wadb_Dialog
import sys
import subprocess
import os

class Subprocess_cmd(QThread):
    finished = Signal()

    def __init__(self, aop="", fop="", cp_cmd="", del_cmd=""):
        super().__init__()
        self.adb_operation = aop #adb operations like pull or push
        self.file_operation = fop #file operations like cut, copy or delete
        self.copy_cmd = cp_cmd
        self.del_cmd = del_cmd

    def run(self):
        if self.adb_operation != "":
            copy_cmd = subprocess.Popen(self.copy_cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            while copy_cmd.poll() is None:
                QApplication.processEvents()
                print(self.adb_operation)
            if self.file_operation == "Cut":
                del_cmd = subprocess.Popen(self.del_cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                while del_cmd.poll() is None:
                    QApplication.processEvents()
                    print(self.file_operation)
        else:
            if self.file_operation == "delete":
                del_cmd = subprocess.Popen(self.del_cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                while del_cmd.poll() is None:
                    QApplication.processEvents()
                    print(self.file_operation)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.back_btn.clicked.connect(self.back_btn_func)
        self.ui.forward_btn.clicked.connect(self.forward_btn_func)
        self.ui.newfolder_btn.clicked.connect(self.create_new_folder)
        self.ui.copy_btn.clicked.connect(self.copy_cut_fun)
        self.ui.cut_btn.clicked.connect(self.copy_cut_fun)
        self.ui.delete_btn.clicked.connect(self.delete_btn_func)

        self.ui.currentloc_lineedit.returnPressed.connect(self.new_path_entered)

        self.ui.tabWidget.currentChanged.connect(self.tab_changed_new)

        self.ui.computer_list.itemActivated.connect(self.open_f_func)
        self.font = QFont()
        self.font.setPointSize(11)

        self.ui.computer_list.setFont(self.font)

        self.ui.adb_list.itemActivated.connect(self.open_f_func)
        self.ui.adb_list.setFont(self.font)

        self.start_app_stuff()

        try:
            print(self.selected_device)
        except AttributeError:
            print("closing")
            print(subprocess.Popen(f"{self.adb_exec} kill-server", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().decode("utf-8").strip())
            print("closed")
            sys.exit()


    def init_win_dialog(self, n):
        def refresh_list():
            subprocess.Popen(f"{self.adb_exec} kill-server", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().decode("utf-8").strip().split("\n")
            a = subprocess.Popen(f"{self.adb_exec} devices", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().decode("utf-8").strip().split("\n")
            ui.devices_list.clear()
            if len(a) == 2:
                ui.ndevices_label.setText(f"{len(a)-1} device connected")
            else:
                ui.ndevices_label.setText(f"{len(a)-1} devices connected")
            for i in range(1, len(a)):
                ui.devices_list.addItem(a[i])

        def select_device(item):
            self.selected_device = item.text().split()[0]
            device_chooser.close()
            self.main_start()

        def show_dialog(title, text, btn):
            a = QMessageBox()
            a.setWindowTitle(title)
            a.setText(text)
            a.setWindowIcon(self.icon)
            if btn == "ok":
                a.setStandardButtons(QMessageBox.Ok)
                a.setIcon(QMessageBox.Information)
            elif btn == "yes":
                a.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                a.setIcon(QMessageBox.Question)
            button = a.exec()
            return button
        
        def pair_or_connect():
            a = show_dialog("ADB File Manager", "Have you ever previously paired your Android device with this device on the same Wi-Fi network?", "yes")
            if a == QMessageBox.Yes:
                connect_device()
            else:
                use_wadb()

        def connect_device():
            QMessageBox.information(self, "How to use Wireless debugging", "Enter IP Address and Port mentioned in the main page in the next window.")
            ip_port, ok = QInputDialog.getText(self, "ADB File Manager", "Enter IP address and port:                                                  ")
            if ok and ip_port:
                op = subprocess.Popen([self.adb_exec, "connect", ip_port.strip()], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().decode("utf-8").strip().split(" ")
                if "connected" in op:
                    self.selected_device = op[-1]
                    device_chooser.close()
                    self.main_start()
                else:
                    QMessageBox.critical(self, "Error", "Could not connect")
                    connect_device()
            elif not ok:
                pass
            else:
                QMessageBox.critical(self, "Error", "Data not entered!")
                connect_device()

        def use_wadb():
            def pair_connect_device():
                ip = ui.ipa_input.text().strip()
                pin = ui.pin_input.text().strip().encode("utf-8")
                #pair device
                if ip != "" and pin != "":
                    a = subprocess.Popen([self.adb_exec, "pair", ip], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                    stdout_data, stderr_data = a.communicate(pin + b"\n")
                    #connect device
                    if "Successfully" in stdout_data.decode("utf-8").strip().split(" "):
                        QMessageBox.information(self, "How to use Wireless debugging", "Successfully paired device.")
                        connect_device()
                    else:
                        QMessageBox.critical(self, "Error", "Pairing unsuccessful")
                else:
                    QMessageBox.critical(self, "Error", "Data not entered!")
                    use_wadb()

            QMessageBox.information(self, "How to use Wireless debugging", "Enable Wireless debugging on your device. Then select \"Pair device with pairing code.\" Enter IP Address and pairing code in the next window.")
            wadb_win = QDialog()
            ui = Ui_Wadb_Dialog()
            ui.setupUi(wadb_win)
            ui.label.setFont(self.font)
            ui.label_2.setFont(self.font)
            ui.buttonBox.accepted.connect(pair_connect_device)
            wadb_win.show()
            wadb_win.exec()

        def exit_app():
            self.closeEvent(None)
            sys.exit()

        device_chooser = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(device_chooser)
        ui.ndevices_label.setText(f"{len(n)-1} devices connected")
        ui.devices_list.setFont(self.font)
        ui.refresh_btn.clicked.connect(refresh_list)
        ui.devices_list.itemActivated.connect(select_device)
        ui.wirelessadb_btn.clicked.connect(pair_or_connect)
        ui.exit_app_btn.clicked.connect(exit_app)
        for i in range(1, len(n)):
            ui.devices_list.addItem(n[i])
        device_chooser.show()
        device_chooser.exec()


    def start_app_stuff(self):
        self.check_os()
        basedir = os.path.dirname(__file__)
        self.icon = QIcon(os.path.join(basedir, 'icons', 'alticon.png'))
        if self.os_name == "win":
            self.adb_exec = os.path.join(basedir, "windows-adb", "adb.exe ")
            import darkdetect
            if not darkdetect.isDark():
                app.setStyle("WindowsVista")
        elif self.os_name == "linux":
            self.adb_exec = "adb"
        else:
            print("OS not supported")
        self.adb_path = "/sdcard"
        a = subprocess.Popen(f"{self.adb_exec} devices", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().decode("utf-8").strip().split("\n")
        if len(a) == 2:
            if a[1].replace("\t", " ").split(" ")[1] != "unauthorized":
                self.selected_device = a[1].split()[0]
                self.main_start()
            else:
                self.init_win_dialog(a)
        elif len(a) > 2:
            self.init_win_dialog(a)
        elif len(a) < 2:
            self.init_win_dialog(a)


    def main_start(self):
        if self.ui.tabWidget.currentIndex() == 0:
            self.fill_computer_list(self.path)
            self.ui.currentloc_lineedit.setText(self.path)
            self.pathlist = [self.path.replace("\r", "")]
            self.forwardpath = []
            self.pathlist_adb = [self.adb_path]
            self.forwardpath_adb = []
            self.ui.forward_btn.setEnabled(False)
            self.ui.back_btn.setEnabled(False)
            self.current_index = 0
            self.base_path_adb = "/sdcard"


    def check_os(self):
        ps = sys.platform
        if ps == "linux":
            self.os_name = ps
            self.path = "/home"
            self.base_path = self.path
        elif ps == "win32":
            self.os_name = "win"
            self.path = "C:\\Users"
            self.base_path = self.path
        elif ps == "darwin":
            self.os_name = "darwin"
            self.path = "idk"
            self.base_path = self.path
        else:
            self.os_name = "not-supported"


    def back_btn_func(self):
        if self.current_index == 0:
            self.path, self.pathlist, self.forwardpath = self.back_main(self.path, self.pathlist, self.forwardpath, self.fill_computer_list)
        elif self.current_index == 1:
            self.adb_path, self.pathlist_adb, self.forwardpath_adb = self.back_main(self.adb_path, self.pathlist_adb, self.forwardpath_adb, self.fill_adb_list)


    def back_main(self, p, backlist, forwardlist, listname):
        if len(backlist) > 1:
            forwardlist.append(backlist[-1])
            backlist.pop()
            p = backlist[-1]
            listname(p)
            self.ui.currentloc_lineedit.setText(p)
            self.ui.forward_btn.setEnabled(True)
            if len(backlist) == 1:
                self.ui.back_btn.setEnabled(False)
            return p, backlist, forwardlist


    def forward_btn_func(self):
        if self.current_index == 0:
            self.path, self.pathlist, self.forwardpath = self.forward_main(self.path, self.pathlist, self.forwardpath, self.fill_computer_list, self.base_path)
        elif self.current_index == 1:
            self.adb_path, self.pathlist_adb, self.forwardpath_adb = self.forward_main(self.adb_path, self.pathlist_adb, self.forwardpath_adb, self.fill_adb_list, self.base_path_adb)


    def forward_main(self, p, backlist, forwardlist, listname, basep):
        if len(forwardlist) > 0:
            p = forwardlist[-1]
            backlist.append(forwardlist[-1])
            forwardlist.pop()
            listname(p)
            self.ui.currentloc_lineedit.setText(p)
            if len(forwardlist) == 0:
                self.ui.forward_btn.setEnabled(False)
            if p != basep:
                self.ui.back_btn.setEnabled(True)
            return p, backlist, forwardlist
        

    def create_new_folder(self):
        def make_folder():
            fname = ui.nfolder_name.text().replace("\r", "")
            if fname != "":
                if self.current_index == 0:
                    if self.os_name == "win":
                        folderpath = self.path.replace("\r", "") + "\\" + fname
                    elif self.os_name == "linux":
                        folderpath = self.path.replace("\r", "") + "/" + fname
                    subprocess.Popen(f"mkdir \"{folderpath}\"", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                    self.fill_computer_list(self.path)
                else:
                    folderpath = self.adb_path.replace("\r", "") + "/" + fname
                    subprocess.Popen(f"{self.adb_exec} shell mkdir \"{folderpath}\"", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                    self.fill_adb_list(self.adb_path)
            else:
                QMessageBox.warning(self, "Warning", "Folder name can't be empty")

        fd = QDialog()
        ui = Folder_Dialog()
        ui.setupUi(fd)
        ui.label.setFont(self.font)
        ui.buttonBox.accepted.connect(make_folder)
        fd.show()
        fd.exec()
        

    def copy_cut_fun(self):
        sender = self.sender()
        if sender.text() == "Copy":
            buttonname = self.ui.copy_btn
        elif sender.text() == "Cut":
            buttonname = self.ui.cut_btn

        if sender.text() in ["Copy", "Cut"]:
            if self.current_index == 0:
                if self.os_name == "win":
                    self.whattocutcopy = self.path.replace("\r", "") + "\\" + str(self.ui.computer_list.currentItem().text().replace("\r", ""))
                elif self.os_name == "linux":
                    self.whattocutcopy = self.path + "/" + str(self.ui.computer_list.currentItem().text())
                self.ui.tabWidget.setCurrentIndex(1)
                self.tab_changed_new(1)
                buttonname.setText("Paste")
            else:
                self.whattocutcopy = self.adb_path.replace("\r", "") + "/" + str(self.ui.adb_list.currentItem().text().replace("\r", ""))
                self.ui.tabWidget.setCurrentIndex(0)
                self.tab_changed_new(0)
                buttonname.setText("Paste")
        else:
            self.paste_main_fun(sender)


    def show_pb_dialog(self, info):
        self.pb = QDialog()
        ui = ProgressBar_Dialog()
        ui.setupUi(self.pb)
        ui.progressBar.setRange(0, 0)
        ui.progressBar.setTextVisible(False)
        ui.progressbar_label.setText(info)
        self.pb.show()


    def subprocesscmd_finished(self):
        self.fill_computer_list(self.path)
        self.fill_adb_list(self.adb_path)


    def paste_main_fun(self, s):
        if s.objectName() == "copy_btn":
            txt = "Copy"
        elif s.objectName() == "cut_btn":
            txt = "Cut"
        
        if self.current_index == 0:
            if self.ui.computer_list.currentItem():
                temp =  str(self.ui.computer_list.currentItem().text().replace("\r", ""))
            else:
                temp = ""
            if self.os_name == "win":
                self.wheretocutcopy =  self.path.replace("\r", "") + "\\" + temp
            elif self.os_name == "linux":
                self.wheretocutcopy =  self.path.replace("\r", "") + "/" + temp

            pulling = f"{self.adb_exec} -s {self.selected_device} pull \"{self.whattocutcopy}\" {self.wheretocutcopy}"

            if txt == "Cut":
                delete = f"{self.adb_exec} -s {self.selected_device} shell rm -rf \"\'{self.whattocutcopy}\'\""
                info = f"Moving {self.whattocutcopy.split("/")[-1]} to { self.wheretocutcopy}"
            else:
                delete = ""
                info = f"Copying {self.whattocutcopy.split("/")[-1]} to { self.wheretocutcopy}"

            self.show_pb_dialog(info)

            self.thread1 = Subprocess_cmd("pulling", txt, pulling, delete)
            self.thread1.finished.connect(self.pb.close)
            self.thread1.finished.connect(self.subprocesscmd_finished)
            self.thread1.start()

            self.whattocutcopy = None
            self.wheretocutcopy = None
            s.setText(txt)
        else:
            if self.ui.adb_list.currentItem():
                temp = str(self.ui.adb_list.currentItem().text().replace("\r", ""))
            else:
                temp = ""
            self.wheretocutcopy = self.adb_path.replace("\r", "") + "/" + temp

            pushing = f"{self.adb_exec} -s {self.selected_device} push \"{self.whattocutcopy}\" \"{self.wheretocutcopy}\""

            if txt == "Cut":
                info = f"Moving {self.whattocutcopy} to { self.wheretocutcopy}"
                if self.os_name == "win":
                    if os.path.isdir(self.whattocutcopy):
                        delete = ["rmdir", "/S", "/Q", self.whattocutcopy]
                    elif os.path.isfile(self.whattocutcopy):
                        delete = ["del", "/F", "/Q", self.whattocutcopy]
                elif self.os_name == "linux":
                    delete = f"rm -rf \"{self.whattocutcopy}\""
            else:
                info = f"Copying {self.whattocutcopy} to { self.wheretocutcopy}"
                delete = ""

            self.show_pb_dialog(info)

            self.thread1 = Subprocess_cmd("pushing", txt, pushing, delete)
            self.thread1.finished.connect(self.pb.close)
            self.thread1.finished.connect(self.subprocesscmd_finished)
            self.thread1.start()

            self.whattocutcopy = ""
            self.wheretocutcopy = ""
            s.setText(txt)


    def delete_btn_func(self):
        if self.current_index == 0:
            if self.os_name == "win":
                self.what_to_delete = self.path.replace("\r", "") + "\\" + str(self.ui.computer_list.currentItem().text().replace("\r", ""))
                info = f"Deleting {self.what_to_delete.split("\\")[-1]}"

                if os.path.isdir(self.what_to_delete):
                    delete = ["rmdir", "/S", "/Q", self.what_to_delete]
                elif os.path.isfile(self.what_to_delete):
                    delete = ["del", "/F", "/Q", self.what_to_delete]
                else:
                    print("file not there")
            elif self.os_name == "linux":
                self.what_to_delete = self.path.replace("\r", "") + "/" + str(self.ui.computer_list.currentItem().text().replace("\r", ""))
                info = f"Deleting {self.what_to_delete.split("/")[-1]}"
                
                delete = f"rm -rf \"{self.what_to_delete}\""
        else:
            self.what_to_delete = self.adb_path.replace("\r", "") + "/" +  str(self.ui.adb_list.currentItem().text().replace("\r", ""))
            info = f"Deleting {self.what_to_delete.split("/")[-1]}"
           
            delete = f"{self.adb_exec} -s {self.selected_device} shell rm -rf \"\'{self.what_to_delete}\'\""

        if delete != "" and self.what_to_delete != "":
            self.show_pb_dialog(info)
            self.thread1 = Subprocess_cmd(fop="delete", del_cmd=delete)
            self.thread1.finished.connect(self.pb.close)
            self.thread1.finished.connect(self.subprocesscmd_finished)
            self.thread1.start()


    def new_path_entered(self):
        if self.current_index == 0:
            self.path = self.ui.currentloc_lineedit.text()
            self.fill_computer_list(self.path)
            self.pathlist.append(self.path.replace("\r", ""))
        else:
            self.adb_path = self.ui.currentloc_lineedit.text()
            self.fill_adb_list(self.adb_path)
            self.pathlist_adb.append(self.adb_path.replace("\r", ""))


    def fill_computer_list(self, thepath):
        self.ui.computer_list.clear()
        if self.os_name == "win":
            self.ui.computer_list.addItems(subprocess.Popen(f"dir \"{thepath}\" /b", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().decode("utf-8", errors="replace").strip().split("\n"))
        elif self.os_name == "linux":
            self.ui.computer_list.addItems(subprocess.Popen(f"ls \"{thepath}\"", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().decode("utf-8", errors="replace").strip().split("\n"))


    def open_f_func(self, item):
        if self.current_index == 0:
            if self.os_name == "win":
                t = self.path.replace("\r", "") + "\\" + item.text().replace("\r", "")
            elif self.os_name == "linux":
                t = self.path.replace("\r", "") + "/" + item.text().replace("\r", "")
            
            if os.path.isdir(t):
                print("a folder")
                self.path = t
                self.fill_computer_list(self.path)
                self.pathlist.append(self.path.replace("\r", ""))
                self.forwardpath.clear()
                self.ui.currentloc_lineedit.setText(self.path)
            elif os.path.isfile(t):
                print("a file")
                print(item.text())
            else:
                print("file note there")

            if len(self.pathlist) > 1:
                self.ui.back_btn.setEnabled(True)

            if len(self.forwardpath) == 0:
                self.ui.forward_btn.setEnabled(False)
        elif self.current_index == 1:
            t = self.adb_path.replace("\r", "") + "/" + item.text().replace("\r", "")
            if subprocess.Popen(f"{self.adb_exec} -s {self.selected_device} shell ls \"\'{t}\'\"", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().decode("utf-8").strip() != t:
                print("folder")
                self.adb_path = t
                self.fill_adb_list(self.adb_path)
                self.ui.currentloc_lineedit.setText(self.adb_path)
                self.pathlist_adb.append(self.adb_path.replace("\r", ""))
                self.forwardpath_adb.clear()
            else:
                print("file")

            if len(self.pathlist_adb) > 1:
                self.ui.back_btn.setEnabled(True)

            if len(self.forwardpath_adb) == 0:
                self.ui.forward_btn.setEnabled(False)


    def fill_adb_list(self, theadb_path):
        self.ui.adb_list.clear()
        self.ui.adb_list.addItems(subprocess.Popen(f"{self.adb_exec} -s {self.selected_device} shell ls \"\'{theadb_path}\'\"", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().decode("utf-8").strip().split("\n"))


    def tab_changed_new(self, index):
        if index == 0:
            self.current_index = 0
            p = self.path
            funcname = self.fill_computer_list
            bcklst = self.pathlist
            fwdlst = self.forwardpath
        else:
            self.current_index = 1
            p = self.adb_path
            funcname = self.fill_adb_list
            bcklst = self.pathlist_adb
            fwdlst = self.forwardpath_adb

        funcname(p)
        if len(fwdlst) >= 1:
            self.ui.forward_btn.setEnabled(True)
        else:
            self.ui.forward_btn.setEnabled(False)
        if len(bcklst) > 1:
            self.ui.back_btn.setEnabled(True)
        else:
            self.ui.back_btn.setEnabled(False)
        self.ui.currentloc_lineedit.setText(p)


    def closeEvent(self, event):
        print("closing")
        print(subprocess.Popen(f"{self.adb_exec} kill-server", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().decode("utf-8").strip())
        print("closed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow()
    window.show()
    sys.exit(app.exec())