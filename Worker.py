import subprocess

from PySide2.QtCore import QObject, Slot, Signal,QRunnable
from MakeVideo import MakeVideo

class Communicate(QObject):

    signal_to_terminal = Signal(str)
    signal_to_progress_bar = Signal(int)
    signal_to_terminal_last_line = Signal(str)
    signal_when_complete=Signal(bool)


class WorkerThread_ffmpeg(QRunnable):

    def __init__(self,zip_location,video_name,video_location,cooking_method):
        super(WorkerThread_ffmpeg, self).__init__()
        self.signals = Communicate()

        if cooking_method=="fast":
            self.makevideo = MakeVideo(zip_location, video_name, video_location, "fast")
        elif cooking_method=="slow":
            self.makevideo = MakeVideo(zip_location, video_name, video_location, "slow")


    @Slot()
    def run(self):

        try:
            self.makevideo.zip_extract()
            self.send_to_terminal("Zip is Extracted . . . Done")

        except:

            self.send_to_terminal("Zip is not Extracted ... Try Again ")
            self.makevideo.clear()
            return

        try:
            self.makevideo.go_to_move()
            self.send_to_terminal("Moving Clips to root Folder . . . Done")
        except Exception as e:
            self.send_to_terminal("Moving Clips to root Folder is not Done ... Try Again " + "\n" + str(e))
            self.makevideo.clear()
            return

        try:
            self.makevideo.rename()
            self.send_to_terminal("Renaming Clips . . . Done")
        except:
            self.send_to_terminal("Renaming Clips is not Done ... Try Again ")
            self.makevideo.clear()
            return

        try:
            self.makevideo.delete()
            self.send_to_terminal("Deleting Small CLips . . . Done")
        except:
            self.send_to_terminal("Deleting Small CLips  ... Try Again ")
            self.makevideo.clear()
            return

        try:
            self.makevideo.create_list()
            self.makevideo.sort_nicely()
            self.send_to_terminal("Creating list for CLips . . . Done")
        except:
            self.send_to_terminal("Creating list not Done   ... Try Again ")
            self.makevideo.clear()
            return
        try:
            process = subprocess.Popen(self.makevideo.cook_videos(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       universal_newlines=True)
            for line in process.stdout:

                try:
                    size=int(line.split()[6][:-2])*1024

                    progress=int(size*100/self.makevideo.zip_size)
                    self.signals.signal_to_progress_bar.emit(progress)
                    self.signals.signal_to_terminal_last_line.emit(line)
                except:
                    pass


        except:
            self.send_to_terminal("Video cooking not Done   ... Try Again ")
            self.makevideo.clear()
            return
        self.signals.signal_when_complete.emit(True)




    def send_to_terminal(self,text):
        self.signals.signal_to_terminal.emit(text)

class WorkerThread_merge(QRunnable):

    def __init__(self,zip_location,video_name,video_location):
        super(WorkerThread_merge, self).__init__()
        self.signals = Communicate()
        self.makevideo = MakeVideo(zip_location, video_name, video_location, "fast")



    def run(self):

        try:
            self.makevideo.zip_extract()
            self.send_to_terminal("Zip is Extracted . . . Done")

        except:

            self.send_to_terminal("Zip is not Extracted ... Try Again ")
            self.makevideo.clear()
            return

        try:
            self.makevideo.go_to_move()
            self.send_to_terminal("Moving Clips to root Folder . . . Done")
        except Exception as e:
            self.send_to_terminal("Moving Clips to root Folder is not Done ... Try Again " + "\n" + str(e))
            self.makevideo.clear()
            return

        try:
            self.makevideo.rename()
            self.send_to_terminal("Renaming Clips . . . Done")
        except:
            self.send_to_terminal("Renaming Clips is not Done ... Try Again ")
            self.makevideo.clear()
            return

        try:
            self.makevideo.delete()
            self.send_to_terminal("Deleting Small CLips . . . Done")
        except:
            self.send_to_terminal("Deleting Small CLips  ... Try Again ")
            self.makevideo.clear()
            return
        try:
            self.makevideo.merge()
            self.send_to_terminal("Merging  Clips . . . Done")
        except:
            self.send_to_terminal("Merging Clips not Done  ... Try Again ")
            self.makevideo.clear()
            return
        self.signals.signal_when_complete.emit(True)

    def send_to_terminal(self,text):
        self.signals.signal_to_terminal.emit(text)
