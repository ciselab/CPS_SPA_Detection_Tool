#!/usr/bin/env python
"""
Data for the test_repository_commits_mining script.
"""
import os
import pathlib
from git import Repo

""" If the location of the local repositories are on a different location, change this here. """
location_github = os.path.join(pathlib.Path.home(), "Documents", "GitHub")

"""
It is possible to manually set the location to a different path.

Explanation:
"name_project": {"local": None, "remote": "url"}
change to:
"name_project": {"local": "/right/here", "remote": "url"}

Changing None to your local path, you overwrite the otherwise build-up path.

If set to None, the local path will bu build-up by function build_repo_dict as follows:
local path = location_github + project_name
Where location_github is given in the top of this file.
"""
# noinspection SpellCheckingInspection
projects = {
	# "AirSim": {"local": None, "remote": "https://github.com/microsoft/AirSim", "sha": None},
	# "android_app_manager": {"local": None, "remote": "https://github.com/ros-android/android_app_manager", "sha": None},
	# "android_camera_driver": {"local": None, "remote": "https://github.com/ros-android/android_camera_driver", "sha": None},
	# "android_sensors_driver": {"local": None, "remote": "https://github.com/ros-android/android_sensors_driver", "sha": None},
	# "apollo": {"local": None, "remote": "https://github.com/ApolloAuto/apollo", "sha": None},
	# "Arduino": {"local": None, "remote": "https://github.com/esp8266/Arduino", "sha": None},
	# "arduino-esp32": {"local": None, "remote": "https://github.com/espressif/arduino-esp32", "sha": None},
	# "Arduino-IRremote": {"local": None, "remote": "https://github.com/z3t0/Arduino-IRremote", "sha": None},
	# "ArduinoJson": {"local": None, "remote": "https://github.com/bblanchon/ArduinoJson", "sha": None},
	# "ardumower": {"local": None, "remote": "https://github.com/Ardumower/ardumower", "sha": None},
	# "ardupilot": {"local": None, "remote": "https://github.com/ArduPilot/ardupilot", "sha": None},
	# "BeamNGpy": {"local": None, "remote": "https://github.com/BeamNG/BeamNGpy.git", "sha": None},
	# "carla": {"local": None, "remote": "https://github.com/carla-simulator/carla", "sha": None},
	# "CoppeliaSimLib": {"local": None, "remote": "https://github.com/CoppeliaRobotics/CoppeliaSimLib", "sha": None},
	# "cylon": {"local": None, "remote": "https://github.com/hybridgroup/cylon", "sha": None},
	# "dronekit-android": {"local": None, "remote": "https://github.com/dronekit/dronekit-android", "sha": None},
	# "dronekit-python": {"local": None, "remote": "https://github.com/dronekit/dronekit-python", "sha": None},
	# "DronePilot": {"local": None, "remote": "https://github.com/alduxvm/DronePilot", "sha": None},
	# "DroneSym": {"local": None, "remote": "https://github.com/scorelab/DroneSym", "sha": None},
	# "dustcloud": {"local": None, "remote": "https://github.com/dgiese/dustcloud", "sha": None},
	# "GAAS": {"local": None, "remote": "https://github.com/generalized-intelligence/GAAS", "sha": None},
	# "gobot": {"local": None, "remote": "https://github.com/hybridgroup/gobot", "sha": None},
	# "grbl": {"local": None, "remote": "https://github.com/gnea/grbl", "sha": None},
	# "johnny-five": {"local": None, "remote": "https://github.com/rwaldron/johnny-five", "sha": None},
	# "librervac-cordlib": {"local": None, "remote": "https://github.com/LibreRVAC/librervac-cordlib", "sha": None},
	# "mavlink": {"local": None, "remote": "https://github.com/mavlink/mavlink", "sha": None},
	# "node-ar-drone": {"local": None, "remote": "https://github.com/felixge/node-ar-drone", "sha": None},
	# "openpilot": {"local": None, "remote": "https://github.com/commaai/openpilot", "sha": None},
	# "PiMower": {"local": None, "remote": "https://github.com/rohmer/PiMower", "sha": None},
	"PX4-Autopilot": {"local": None, "remote": "https://github.com/PX4/Firmware", "sha": None},
	# "pypilot": {"local": None, "remote": "https://github.com/pypilot/pypilot", "sha": None},
	# "qgroundcontrol": {"local": None, "remote": "https://github.com/mavlink/qgroundcontrol", "sha": None},
	# "rfid": {"local": None, "remote": "https://github.com/miguelbalboa/rfid", "sha": None},
	# "robonomics": {"local": None, "remote": "https://github.com/airalab/robonomics", "sha": None},
	# "robonomics-js": {"local": None, "remote": "https://github.com/airalab/robonomics-js", "sha": None},
	# "robonomics_contracts": {"local": None, "remote": "https://github.com/airalab/robonomics_contracts", "sha": None},
	# "stofzuigerrobot": {"local": None, "remote": "https://github.com/alvitawa/stofzuigerrobot", "sha": None},
	# "turtlebot": {"local": None, "remote": "https://github.com/turtlebot/turtlebot", "sha": None},
	# "turtlebot3": {"local": None, "remote": "https://github.com/ROBOTIS-GIT/turtlebot3", "sha": None},
	# "Valetudo": {"local": None, "remote": "https://github.com/Hypfer/Valetudo", "sha": None},
}


def build_repo_dict():
	"""
	If the local repository dictionary key has no value, the value is build-up.
	Assumed is the location of the GitHub path, set previously with variable location_github.
	"""
	for project in projects:
		if projects[project]["local"] is None:
			updated_local = os.path.join(location_github, project)
			projects[project].update({"local": updated_local})


def build_repo_dict_sha():
	"""
	If the sha repository dictionary key has no value, the value is build-up.
	The local path to the repository is needed to be available.
	"""
	for project in projects:
		if projects[project]["local"] is not None:
			if projects[project]["sha"] is None:
				repo = Repo(projects[project]["local"])
				sha = repo.head.object.hexsha
				projects[project].update({"sha": sha})
