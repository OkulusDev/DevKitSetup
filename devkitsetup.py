import sys
import subprocess
import dks
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox


class DevKitSetupUI(QtWidgets.QMainWindow, dks.Ui_MainWindow):
	def __init__(self):
		###### Инициализация и установка UI ######
		super().__init__()
		self.setupUi(self)
		self.setFixedSize(785, 602)
		self.setWindowTitle('DevKitSetup')

		self.linux_distros = ['Arch/Manjaro', 'Debian/Ubuntu']

		self.linux_distribution = 'Arch/Manjaro'
		self.comboBox.activated.connect(self.select_linux_distro)

		self.jre17_btn.clicked.connect(self.install_jre17)

	def install_jre17(self):
		if self.linux_distribution == 'Arch/Manjaro':
			msg = QMessageBox(self)
			msg.setWindowTitle("Установка JRE17")
			msg.exec_()
			
			command = subprocess.call('sudo pacman -S --needed - < pkgslists/jre17.txt', shell=True)
			msg = QMessageBox(self)
			msg.setWindowTitle("Установка JRE17")
			msg.setText(str(command.decode()))
			
			msg.exec_()

	def select_linux_distro(self, idx):
		self.linux_distribution = self.linux_distros[idx]
		print(self.linux_distros[idx])


def main():
	app = QtWidgets.QApplication(sys.argv)
	window = DevKitSetupUI()
	window.show()
	app.exec()


if __name__ == '__main__':
	main()
