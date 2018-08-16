import os
import schedule
import shutil
import time

def job():
    source_folder = r'C:\Users\Sgavari\Desktop\Pythonscript\Test'    
    destination_folder = r'C:\Users\Sgavari\Desktop\Pythonscript\Test'  

    for src_dir, dirs, files in os.walk(source_folder):
        dst_dir = src_dir.replace(source_folder, destination_folder, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.copy(src_file, dst_dir)

schedule.every().day.at("9:52").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
