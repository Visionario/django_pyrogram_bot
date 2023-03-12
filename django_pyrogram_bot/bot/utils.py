import json
import pathlib


class RunningBot:
    """
    Manage Running Bot info using a JSON file.
    """

    data_file = "running_bot_data.json"

    def read_data(self):
        """Get info about running bot. If not found then return None, maybe BOT is not running"""
        try:
            with open(self.data_file, "r") as json_file:
                data = json.load(json_file)
            return data
        except BaseException as e:
            # print(e.args)
            return None

    def save_data(self, data: dict):
        """Save info about running bot into json file"""
        with open(self.data_file, "w") as json_file:
            json.dump(data, json_file)

    def delete_data(self):
        """Delete file"""
        pathlib.Path(self.data_file).unlink()
