from PySide2.QtCore import QThreadPool,Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow,QApplication,QMessageBox,QFileDialog,QDialog

from PySide2.QtWidgets import QApplication
from main_ui import Ui_MainWindow
import sys,os,subprocess
from MakeVideo import MakeVideo
import pexpect
from Worker import WorkerThread_ffmpeg,WorkerThread_merge


class Zipvy(QMainWindow,Ui_MainWindow):

        def __init__(self):

            super(Zipvy,self).__init__()
            self.setupUi(self)
            self.show()

            # Load default Widgets Values
            # ....
            self.setWindowTitle("Zipvy - To Make Video from Zip")
            self.setWindowIcon(QIcon('images\\icon.ico'))
            self.terminal_output.setReadOnly(True)
            self.terminal_output.setPlainText("Zipvy is Ready....")
            self.progressBar.hide()
            self.label_progress.hide()
            self.same_as_zip_name_checkbox.setChecked(True)


            #Variables ....
            self.algorithm = 0
            self.zip_location=""
            self.zip_name=""
            self.lineEdit_text=""
            self.video_name=""
            self.video_location=""


            #Threads...
            self.threadpool = QThreadPool()

            #Connect Signal to Slots...
            self.same_as_zip_name_checkbox.stateChanged.connect(self.checkbox_stat_changed)
            self.select_zip_button.clicked.connect(self.select_zip)
            self.start_button.clicked.connect(self.start)
            self.algorithm_combobox.currentIndexChanged.connect(self.set_algorithm)
            self.lineEdit.textChanged.connect(self.textedit_text_changed)
            self.toolButton.clicked.connect(self.set_video_location)



        def set_algorithm(self):
            algorithm=str(self.algorithm_combobox.currentIndex())
            if algorithm=="0":
                self.algorithm=0
            elif algorithm=="1":
                self.algorithm=1
            elif algorithm=="2":
                self.algorithm=2
            elif algorithm=="3":
                self.algorithm=3

        def select_zip(self):

            dialog=QFileDialog()
            dialog.setNameFilter("All Zip files (*zip *rar)")
            self.zip_location=dialog.getOpenFileName()[0]
            self.zip_name=os.path.basename(self.zip_location)[:-4]
            self.video_name=self.zip_name
            self.video_location=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos', self.video_name)
            self.send_to_terminal("Selected Zip is ... "+str(self.zip_name))

        def checkbox_stat_changed(self):
            if self.same_as_zip_name_checkbox.checkState() == False:
                self.video_name=self.lineEdit.text()
            elif self.same_as_zip_name_checkbox.checkState() == True:
                self.video_name=self.zip_name

        def textedit_text_changed(self):
            self.lineEdit_text=self.lineEdit.text()
        @Slot(str)
        def send_to_terminal(self,text):
            ''''''
            text="> "+text+'\n'
            self.terminal_output.append(text)

        def set_video_location(self):
            dailog=QFileDialog()
            self.path=dailog.getExistingDirectory()
            self.video_location = os.path.join(self.path, self.video_name)
            self.send_to_terminal(self.video_location + "   is selected for Video Folder")
            
        def start(self):
            if self.same_as_zip_name_checkbox.isChecked():
                self.video_name=self.zip_name
            elif self.lineEdit.text()!="":
                self.video_name=self.lineEdit.text()
            self.video_location=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos', self.video_name)

            if self.algorithm==0:
                dailog=QMessageBox()
                dailog.setText("Select a Algorithm to Continue")
                dailog.setWindowTitle("Select a Algorithm")
                dailog.setStandardButtons(QMessageBox.Ok)
                dailog.exec_()
                return
            self.progressBar.setMaximum(0)
            self.label_progress.show()
            self.progressBar.show()

            if self.algorithm==1:
                worker = WorkerThread_merge(self.zip_location, self.video_name, self.video_location)

            if self.algorithm==2 or self.algorithm==3:

                if self.algorithm==2:
                    worker = WorkerThread_ffmpeg(self.zip_location,self.video_name,self.video_location,"fast")


                if self.algorithm==3:
                    worker = WorkerThread_ffmpeg(self.zip_location,self.video_name,self.video_location,"slow")

            worker.signals.signal_to_terminal.connect(self.send_to_terminal)
            worker.signals.signal_to_progress_bar.connect(self.send_to_progress)
            worker.signals.signal_to_terminal_last_line.connect(self.send_to_terminal_last_line)
            worker.signals.signal_when_complete.connect(self.on_completes)

            self.threadpool.start(worker)


        def on_completes(self,b):

            if b == True:
                self.progressBar.hide()
                self.label_progress.hide()
                self.final_msg="Video Successfully Cooked ... Stored at \n"+self.video_location
                self.terminal_output.append(self.final_msg)

            else:
                pass
        def send_to_terminal_last_line(self,text):
            new_text = text
            '''old_text = self.terminal_output.toPlainText()
            new_text = old_text[:-len(new_text)] + "\n" + new_text'''
            self.terminal_output.setPlainText(new_text)

        def send_to_progress(self,progress):
            self.progressBar.setMaximum(100)
            self.progressBar.setValue(progress)











if __name__ == "__main__":
    app=QApplication(sys.argv)
    zipvy=Zipvy()
    sys.exit(app.exec_())