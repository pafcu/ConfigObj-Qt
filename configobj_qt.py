"""Module containing functions to convert between ConfigObj and QSettings objects."""
import configobj
from PyQt4.QtCore import QSettings

def section_path(config):
	"""Get names of section ancestors."""
	section = config
	if section.name == None: # No name => root section => no ancestors
		return []

	path = [section.name]

	# Iterate until root section is reached 
	while section.parent.name != None:
		path.insert(0, section.parent.name)
		section = section.parent

	return path

def to_QSettings(config, clear=True):
	"""Convert ConfigObj to QSettings.
	Note that QSettings are automatically saved so this will overwrite any previous application settings."""
	settings = QSettings()
	if clear:
		settings.clear()

	def walk(section, key):
		"""Copy values from ConfigObj object to QSettings object."""
		if key not in section.defaults: # Don't copy default values
			settings.setValue('/'.join(section_path(section))+'/%s'%key, section[key])
	config.walk(walk)
	return settings

def from_QSettings(settings):
	"""Convert QSettings to ConfigObj. All values are strings."""
	config = configobj.ConfigObj()
	for key in settings.allKeys():
		path = str(key).split('/')
		section = config
		while len(path) > 1:
			section_name = path.pop(0)
			try:
				section = section[section_name]
			except KeyError:
				section[section_name] = {}
				section = section[section_name]
		section[path.pop()] = str(settings.value(key).toPyObject())
	return config

if __name__ == '__main__':
	def main():
		"""Function to test functionality."""
		import sys
		from PyQt4.QtGui import QApplication
		conf = """
		p1 = 1
		[mysection]
		p2 = 2
		[[mysubsection]]
		p3 = 3.14
		"""
		app = QApplication(sys.argv)
		app.setApplicationName('configtest')
		app.setOrganizationName('foo')
		config = configobj.ConfigObj(conf.split('\n'))
		settings = to_QSettings(config)
		config2 = from_QSettings(settings)
		print config == config2
	main()

