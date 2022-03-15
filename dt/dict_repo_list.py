#!/usr/bin/env python
"""
Data for the test_repository_commits_mining script.
"""
import os
# import pathlib
from git import Repo
from collections import namedtuple

""" If the location of the local repositories are on a different location, change this here. """
# location_github = os.path.join(pathlib.Path.home(), "Documents", "GitHub")
location_github = os.path.join(os.path.expanduser("~"), "projects")		# For Docker usage

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

Large projects: apollo, ardupilot, openpilot, PX4-Autopilot
"""
# noinspection SpellCheckingInspection
projects = {
	"AirSim": {"local": None, "remote": "https://github.com/microsoft/AirSim", "sha": None},
	# "android_app_manager": {"local": None, "remote": "https://github.com/ros-android/android_app_manager", "sha": None},
	# "android_camera_driver": {"local": None, "remote": "https://github.com/ros-android/android_camera_driver", "sha": None},
	# "android_sensors_driver": {"local": None, "remote": "https://github.com/ros-android/android_sensors_driver", "sha": None},
	# "apollo": {"local": None, "remote": "https://github.com/ApolloAuto/apollo", "sha": None},
	"Arduino": {"local": None, "remote": "https://github.com/esp8266/Arduino", "sha": None},
	# "arduino-esp32": {"local": None, "remote": "https://github.com/espressif/arduino-esp32", "sha": None},
	"Arduino-IRremote": {"local": None, "remote": "https://github.com/z3t0/Arduino-IRremote", "sha": None},
	"ArduinoJson": {"local": None, "remote": "https://github.com/bblanchon/ArduinoJson", "sha": None},
	"ardumower": {"local": None, "remote": "https://github.com/Ardumower/ardumower", "sha": None},
	# "ardupilot": {"local": None, "remote": "https://github.com/ArduPilot/ardupilot", "sha": None},
	# "BeamNGpy": {"local": None, "remote": "https://github.com/BeamNG/BeamNGpy.git", "sha": None},
	"carla": {"local": None, "remote": "https://github.com/carla-simulator/carla", "sha": None},
	"CoppeliaSimLib": {"local": None, "remote": "https://github.com/CoppeliaRobotics/CoppeliaSimLib", "sha": None},
	# "cylon": {"local": None, "remote": "https://github.com/hybridgroup/cylon", "sha": None},
	# "dronekit-android": {"local": None, "remote": "https://github.com/dronekit/dronekit-android", "sha": None},
	# "dronekit-python": {"local": None, "remote": "https://github.com/dronekit/dronekit-python", "sha": None},
	# "DronePilot": {"local": None, "remote": "https://github.com/alduxvm/DronePilot", "sha": None},
	# "DroneSym": {"local": None, "remote": "https://github.com/scorelab/DroneSym", "sha": None},
	# "dustcloud": {"local": None, "remote": "https://github.com/dgiese/dustcloud", "sha": None},
	"GAAS": {"local": None, "remote": "https://github.com/generalized-intelligence/GAAS", "sha": None},
	# "gobot": {"local": None, "remote": "https://github.com/hybridgroup/gobot", "sha": None},
	# "grbl": {"local": None, "remote": "https://github.com/gnea/grbl", "sha": None},
	# "johnny-five": {"local": None, "remote": "https://github.com/rwaldron/johnny-five", "sha": None},
	# "librervac-cordlib": {"local": None, "remote": "https://github.com/LibreRVAC/librervac-cordlib", "sha": None},
	# "mavlink": {"local": None, "remote": "https://github.com/mavlink/mavlink", "sha": None},
	# "node-ar-drone": {"local": None, "remote": "https://github.com/felixge/node-ar-drone", "sha": None},
	# "openpilot": {"local": None, "remote": "https://github.com/commaai/openpilot", "sha": None},
	"PiMower": {"local": None, "remote": "https://github.com/rohmer/PiMower", "sha": None},
	# "PX4-Autopilot": {"local": None, "remote": "https://github.com/PX4/Firmware", "sha": None},
	# "pypilot": {"local": None, "remote": "https://github.com/pypilot/pypilot", "sha": None},
	"qgroundcontrol": {"local": None, "remote": "https://github.com/mavlink/qgroundcontrol", "sha": None},
	"rfid": {"local": None, "remote": "https://github.com/miguelbalboa/rfid", "sha": None},
	# "robonomics": {"local": None, "remote": "https://github.com/airalab/robonomics", "sha": None},
	# "robonomics-js": {"local": None, "remote": "https://github.com/airalab/robonomics-js", "sha": None},
	# "robonomics_contracts": {"local": None, "remote": "https://github.com/airalab/robonomics_contracts", "sha": None},
	"stofzuigerrobot": {"local": None, "remote": "https://github.com/alvitawa/stofzuigerrobot", "sha": None},
	"turtlebot": {"local": None, "remote": "https://github.com/turtlebot/turtlebot", "sha": None},
	# "turtlebot3": {"local": None, "remote": "https://github.com/ROBOTIS-GIT/turtlebot3", "sha": None},
	# "Valetudo": {"local": None, "remote": "https://github.com/Hypfer/Valetudo", "sha": None},
	# "Test_CPS_SPA_DT": {"local": None, "remote": "https://github.com/IvDinten/Test_CPS_SPA_DT/tree/main", "sha": None},
}


def build_repo_dict() -> None:
	"""
	If the local repository dictionary key has no value, the value is build-up.
	Assumed is the location of the GitHub path, set previously with variable location_github.
	"""
	for project in projects:
		if projects[project]["local"] is None:
			updated_local = os.path.join(location_github, project)
			projects[project].update({"local": updated_local})


def build_repo_dict_sha() -> None:
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


Path_Entry = namedtuple('Path_Entry', 'top_level recursive')
"""
Setting recursive to True means it is allowed to go through all the directories underneath.
Setting recursive to False means it is only allowed to check the files in this directory, but not underneath.
"""
# noinspection SpellCheckingInspection
projects_modules = {
	"AirSim": [
		Path_Entry("AirLibUnitTests", True), Path_Entry("SGM", True), Path_Entry("GazeboDrone", True),
		Path_Entry("DroneShell", True), Path_Entry("HelloDrone", True), Path_Entry("PX4Scripts", True),
		Path_Entry("PythonClient", True), Path_Entry("AirLib", True), Path_Entry("HelloCar", True),
		Path_Entry("DroneServer", True), Path_Entry("ros", True), Path_Entry("MavLinkCom", True),
		Path_Entry("LogViewer", True), Path_Entry("Unreal", True), Path_Entry("HelloSpawnedDrones", True),
		Path_Entry("tools", True), Path_Entry("cmake", True), Path_Entry("pipelines", True), Path_Entry("Unity", True)
	],
	"android_app_manager": [
		Path_Entry("libs", True), Path_Entry("src", True), Path_Entry("res", True)
	],
	"android_camera_driver": [
		Path_Entry("res", True), Path_Entry("src", True),
	],
	"android_sensors_driver": [
		Path_Entry("res", True), Path_Entry("src", True),
	],
	"apollo": [
		Path_Entry("cyber", True), Path_Entry("third_party", True), Path_Entry("scripts", True),
		Path_Entry("modules", True), Path_Entry(".teamcity", True), Path_Entry("tools", True)
	],
	"Arduino": [
		Path_Entry("package", True), Path_Entry("cores", True), Path_Entry("libraries", True),
		Path_Entry("variants", True), Path_Entry("bootloaders", True), Path_Entry("tools", True)
	],
	"arduino-esp32": [
		Path_Entry("package", True), Path_Entry("cores", True), Path_Entry("libraries", True),
		Path_Entry("variants", True), Path_Entry("tools", True)
	],
	"Arduino-IRremote": [
		Path_Entry("src", True)
	],
	"ArduinoJson": [
		Path_Entry(".vscode", True), Path_Entry("extras", True), Path_Entry("src", True),
	],
	"ardumower": [
		Path_Entry("Dokumentation", True), Path_Entry("cad", True), Path_Entry("code", True),
		Path_Entry("pcb", True), Path_Entry("tools", True)
	],
	"ardupilot": [
		Path_Entry("mk", True), Path_Entry("AntennaTracker", True), Path_Entry("benchmarks", True),
		Path_Entry("ArduPlane", True), Path_Entry("Blimp", True), Path_Entry(".semaphore", True),
		Path_Entry("libraries", True), Path_Entry("modules", True), Path_Entry("Tools", True),
		Path_Entry("ArduSub", True), Path_Entry("ArduCopter", True), Path_Entry("Rover", True)
	],
	"BeamNGpy": [
		Path_Entry("media", True), Path_Entry("env", True), Path_Entry("src", True), Path_Entry(".idea", True)
	],
	"carla": [
		Path_Entry("PythonAPI", True), Path_Entry("LibCarla", True), Path_Entry("Import", True),
		Path_Entry("Co-Simulation", True), Path_Entry("Unreal", True), Path_Entry("Util", True),
	],
	"CoppeliaSimLib": [
		Path_Entry("sourceCode", True), Path_Entry("iconFiles", True), Path_Entry("variousImageFiles", True),
		Path_Entry("qdarkstyle", True), Path_Entry("imageFiles", True), Path_Entry("ui", True),
		Path_Entry("toolbarFiles", True), Path_Entry("targaFiles", True)
	],
	"cylon": [
		Path_Entry("lib", True), Path_Entry("spec", True),
	],
	"dronekit-android": [
		Path_Entry("ClientLib", True), Path_Entry(".utility", True), Path_Entry("samples", True),
		Path_Entry("dependencyLibs", True)
	],
	"dronekit-python": [
		Path_Entry(".circleci", True), Path_Entry("windows", True), Path_Entry("scripts", True),
		Path_Entry("dronekit", True),
	],
	"DronePilot": [
		Path_Entry("modules", True), Path_Entry("logs", True),
	],
	"DroneSym": [
		Path_Entry("dronedb", True), Path_Entry(".dependabot", True), Path_Entry("initScripts", True),
		Path_Entry("dronesym-python", True), Path_Entry("dronesym-frontend", True), Path_Entry("dronesym-node", True)
	],
	"dustcloud": [
		Path_Entry("presentations", True), Path_Entry("dummycloud", True), Path_Entry("devices", True),
		Path_Entry("dustcloud", True),
	],
	"GAAS": [
		Path_Entry("software", True), Path_Entry("demo", True), Path_Entry("hardware", True),
		Path_Entry("simulator", True), Path_Entry("algorithms", True)
	],
	"gobot": [
		Path_Entry("sysfs", True), Path_Entry("platforms", True), Path_Entry(".circleci", True),
		Path_Entry("api", True), Path_Entry("gobottest", True), Path_Entry("drivers", True), Path_Entry("cli", True)
	],
	"grbl": [
		Path_Entry("build", True), Path_Entry("grbl", True),
	],
	"johnny-five": [
		Path_Entry("assets", True), Path_Entry("eg", True), Path_Entry("firmwares", True), Path_Entry("util", True),
		Path_Entry("tpl", True), Path_Entry("lib", True)
	],
	"librervac-cordlib": [
		Path_Entry("t", True),
	],
	"mavlink": [
		Path_Entry("pymavlink", True), Path_Entry("cmake", True), Path_Entry("scripts", True),
		Path_Entry("component_information", True), Path_Entry("message_definitions", True), Path_Entry("external", True)
	],
	"node-ar-drone": [
		Path_Entry("lib", True)
	],
	"openpilot": [
		Path_Entry("rednose_repo", True), Path_Entry("site_scons", True), Path_Entry("installer", True),
		Path_Entry("panda", True), Path_Entry("opendbc", True), Path_Entry("release", True), Path_Entry("selfdrive", True),
		Path_Entry("cereal", True), Path_Entry("phonelibs", True), Path_Entry("pyextra", True), Path_Entry("scripts", True),
		Path_Entry("models", True), Path_Entry("common", True), Path_Entry("external", True), Path_Entry("laika_repo", True),
		Path_Entry("tools", True)
	],
	"PiMower": [
		Path_Entry("Solution", True), Path_Entry("CLI", True), Path_Entry("RobotDaemon", True), Path_Entry("RobotLib", True),
		Path_Entry("RobotController", True), Path_Entry("TestSuite", True), Path_Entry("Arduino", True),
		Path_Entry("3rdParty", True), Path_Entry("TestLibrary", True), Path_Entry("Windows", True)
	],
	"PX4-Autopilot": [
		Path_Entry("boards", True), Path_Entry(".vscode", True), Path_Entry("src", True), Path_Entry("validation", True),
		Path_Entry("ROMFS", True), Path_Entry(".devcontainer", True), Path_Entry("msg", True), Path_Entry("cmake", True),
		Path_Entry("Tools", True), Path_Entry("mavlink", True), Path_Entry("Documentation", True),
		Path_Entry("posix-configs", True), Path_Entry(".ci", True), Path_Entry("platforms", True),
	],
	"pypilot": [
		Path_Entry("pypilot", True), Path_Entry("hat", True), Path_Entry("scripts", True), Path_Entry("arduino", True),
		Path_Entry("ui", True)
	],
	"qgroundcontrol": [
		Path_Entry("custom-example", True), Path_Entry("android", True), Path_Entry("snap", True), Path_Entry("libs", True),
		Path_Entry("translations", True), Path_Entry("VideoReceiverApp", True), Path_Entry("cmake", True),
		Path_Entry("deploy", True), Path_Entry("ios", True), Path_Entry("windows", True), Path_Entry("debian", True),
		Path_Entry("src", True), Path_Entry("resources", True), Path_Entry("tools", True)
	],
	"rfid": [
		Path_Entry("src", True),
	],
	"robonomics": [
		Path_Entry("protocol", True), Path_Entry("primitives", True), Path_Entry("substrate-ros", True),
		Path_Entry("scripts", True), Path_Entry("frame", True), Path_Entry("io", True), Path_Entry("bin", True),
		Path_Entry("cli", True), Path_Entry("runtime", True)
	],
	"robonomics-js": [
		Path_Entry("src", True),
	],
	"robonomics_contracts": [
		Path_Entry("build", True), Path_Entry("migrations", True), Path_Entry("contracts", True),
	],
	"stofzuigerrobot": [
		Path_Entry("library", True), Path_Entry("arduino", True), Path_Entry("app", True)
	],
	"turtlebot": [
		Path_Entry("turtlebot_description", True), Path_Entry("turtlebot_bringup", True), Path_Entry("turtlebot", True),
		Path_Entry("turtlebot_capabilities", True), Path_Entry("turtlebot_teleop", True)
	],
	"turtlebot3": [
		Path_Entry("turtlebot3_description", True), Path_Entry("turtlebot3_navigation", True),
		Path_Entry("turtlebot3_teleop", True), Path_Entry("turtlebot3_bringup", True), Path_Entry("turtlebot3_slam", True),
		Path_Entry("turtlebot3", True), Path_Entry("turtlebot3_example", True)
	],
	"Valetudo": [
		Path_Entry("assets", True), Path_Entry("backend", True), Path_Entry("util", True), Path_Entry("frontend", True),
		Path_Entry("build_dependencies", True), Path_Entry("deployment", True)
	],
	"Test_CPS_SPA_DT": [
		Path_Entry("src", True)
	],
}
