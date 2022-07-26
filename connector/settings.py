import json
import logging
import os
import threading
import time


class Settings:
    """
    A settings object containing all the settings set in the settings file.
    """
    def __init__(self, settingsfile):
        self.filename = settingsfile
        self.settings = None
        self.stamp = None

        if not os.path.exists(self.filename):
            raise FileNotFoundError("The settingsfile {0} could not be found.".format(self.filename))

        logging.info("Initializing settings...")
        self.read_config_file()

    def read_config_file(self):
        with open(self.filename, "r") as file:
            self.settings = json.loads(file.read())["printer"][0]
            self.stamp = os.stat(self.filename).st_mtime
            logging.info("Settings have been loaded.")

    def get(self, setting):
        try:
            return self.settings[setting]
        except ValueError:
            logging.error("Value not found, returning None")
            return None
