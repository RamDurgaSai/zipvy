# -*- coding: utf-8 -*-
import os,zipfile,sys,glob,re,shutil

class MakeVideo:

    def __init__(self, zip_location,video_name,video_location,cooking_method):
        self.zip_location=zip_location
        self.zip_size=os.path.getsize(self.zip_location)
        self.video_name = video_name

        self.video_location = video_location


        self.temp=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Temp')
        self.pwd =os.path.join(os.path.join(os.environ['USERPROFILE']), 'Temp', self.video_name)

        self.clear_temp(self.temp)
        if not os.path.exists(self.pwd):
            os.makedirs(self.pwd)


        self.list_path = os.path.join(self.pwd, "list.txt")
        if cooking_method=="fast":
            self.ffmpeg_command_list=['ffmpeg -y -f concat  -i "' , str(self.list_path) ,'" -safe 0  -c copy' , ' "' , str(
                    self.video_location) , '.mp4" ']
            self.ffmpeg_command = str(
                'ffmpeg -y -f concat  -i "' + str(self.list_path) + '" -safe 0  -c copy' + ' "' + str(
                    self.video_location) + '.mp4" ')
        elif cooking_method=="slow":
            self.ffmpeg_command_list = [
            'ffmpeg -y -f concat  -i "', str(self.list_path), '" -safe 0  ', ' "', str(
                self.video_location), '.mp4" ']
            self.ffmpeg_command = str(
                'ffmpeg -y -f concat  -i "' + str(self.list_path) + '" -safe 0  ' + ' "' + str(
                    self.video_location) + '.mp4" ')





    def zip_extract(self):
        with zipfile.ZipFile(self.zip_location, 'r') as zip_ref:
            zip_ref.extractall(self.pwd)
    def go_to_move(self):
        self.move_to_root_folder(self.pwd,self.pwd)
    def move_to_root_folder(self,root_path,cur_path):




        for filename in os.listdir(cur_path):
            if os.path.isfile(os.path.join(cur_path, filename)):
                shutil.move(os.path.join(cur_path, filename), os.path.join(root_path, filename))
            elif os.path.isdir(os.path.join(cur_path, filename)):
                self.move_to_root_folder(root_path, os.path.join(cur_path, filename))
            else:
                sys.exit("Should never reach here.")
        if cur_path != root_path:
            os.rmdir(cur_path)

    def rename(self):


        path = self.pwd

        for filename in os.listdir(path):
            my_source = os.path.join(path, filename)
            new_filename = filename[:-4] + ".mp4"
            my_dest = os.path.join(path, new_filename)

            # rename() function will
            # rename all the files

            os.rename(my_source, my_dest)



    def delete(self):
        param=self.pwd


        for root, _, files in os.walk(param):
            for f in files:
                fullpath = os.path.join(root, f)
                try:
                    if os.path.getsize(fullpath) < 100 * 1024:  # set file size in kb
                        os.remove(fullpath)
                except WindowsError:
                    pass

    def create_list(self):
        param = self.pwd

        os.chdir(param)
        with open("list.txt", "a") as f:
            for file in glob.glob("*.mp4"):
                # f = open("output.txt", "a")
                # print(file,file=f)
                print("file '", file, "'", file=f, sep='')

    def sort_nicely(self):

        list_path=self.list_path

        output_file = list_path

        """ Sort the given list in the way that humans expect.
        """
        with open(output_file, "r") as txt:
            file = txt.read()

        list = file.split('\n')  # converts to list
        convert = lambda text: int(text) if text.isdigit() else text
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        list.sort(key=alphanum_key)

        with open(output_file, 'w') as f:
            for item in list:
                f.write("%s\n" % item)

    def cook_videos(self):



        ffmpeg_command=self.ffmpeg_command



        #ffmpeg_output = subprocess.run(ffmpeg_command, shell=True, capture_output=True)


        return ffmpeg_command



    def clear(self):
        try:
            if os.path.isdir(self.pwd):
                for file in os.listdir(self.pwd):
                    os.remove(os.path.jion(self.pwd,file))
                shutil.rmtree(self.pwd, ignore_errors=True)
            if os.path.isfile(self.pwd):
                shutil.rmtree(self.pwd, ignore_errors=True)
        except:
            pass


    def clear_temp(self,pwd):
        try:
            shutil.rmtree(pwd)
        except:
            pass

        '''for filename in os.listdir(pwd):
            if os.path.isfile(os.path.join(pwd, filename)):
                os.remove(os.path.join(pwd, filename))
            elif os.path.isdir(os.path.join(pwd, filename)):
                self.clear_temp(os.path.join(pwd, filename))
            else:
                sys.exit("Should never reach here.")

            if pwd != os.path.join(pwd,filename):
                os.rmdir(os.path.join(pwd,filename))

        '''

    def merge(self):
        param = self.pwd
        os.chdir(param)
        with open("list.txt", "a") as f:
            for file in glob.glob("*.mp4"):
                # f = open("output.txt", "a")
                # print(file,file=f)
                print(file, file=f, sep='')

        self.sort_nicely()

        with open(str(self.video_location+".mp4"),"ab") as video:
            print(str(self.video_location+".mp4"))

            with open(self.list_path,'r') as list:
                list=list.readlines()
                for file in list:

                    if file != list[0]:
                        file=str(file)[:-1]

                        file_path = os.path.join(self.pwd, file)

                        with open(file_path, "rb") as clip:
                            clip_data=clip.read()
                            video.write(clip_data)






