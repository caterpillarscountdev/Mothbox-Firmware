#!/usr/bin/python3

'''
Copies configuration and log files to current nightly photos dataset
'''


import shutil, tempfile, os

from datetime import datetime, timedelta

from .settings import Settings

root_path = os.path.dirname(os.path.realpath(__file__))
photo_path = os.path.join(root_path, 'photos')
logs_path = os.path.join(root_path, 'logs')

logs = ['Attract_On_log.txt', 'Scheduler_log.txt', 'Backup_log.txt', 'TakePhoto_log.txt', 'Upload_log.txt']
confs = ['site_metadata.csv', 'schedule_settings.csv', 'camera_settings.csv']


def dated_folder(base_path=photo_path, now=None):
  """
  Return a folder path with the current date in the format YYYY-MM-DD.

  Args:
      base_path: The base path where the folder will be created.

  Returns:
      The full path to the created folder.
  """
  if not now:
      now = datetime.now()
  # Adjust for time between 12:00 pm and 11:59 am next day
  if 12 <= now.hour < 24:
    date_str = now.strftime("%Y-%m-%d")
  else:
    # Add a day if time is between 12:00 pm and next day's 11:59 am
    date_str = (now - timedelta(days=1)).strftime("%Y-%m-%d")
  folder_path = os.path.join(base_path, date_str)
  if not os.path.exists(folder_path):
      return None
  return folder_path


now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Adjust the format as needed

dest = dated_folder()

if not dest:
    print(f"{formatted_time} No photos folder for today")
else:
    s = Settings()
    with open(os.path.join(dest, "metadata.json"), 'w') as json_file:
      json.file.write(s.to_json())
    with tempfile.TemporaryDirectory() as tempd:
        templogs = os.path.join(tempd, 'logs')
        os.mkdir(templogs)
        for f in logs:
            try:
                shutil.copy(os.path.join(logs_path, f), templogs)
            except FileNotFoundError:
                print("file not found", f, "continuing")
        tempconf = os.path.join(tempd, 'config')
        os.mkdir(tempconf)
        for f in confs:
            try:
                shutil.copy(os.path.join(root_path, f), tempconf)
            except FileNotFoundError:
                print("file not found", f, "continuing")
        shutil.make_archive(os.path.join(dest, 'metadata'), 'zip', tempd)
