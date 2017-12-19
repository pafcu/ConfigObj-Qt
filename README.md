ConfigObj-Qt provides a methods to convert between QSettings and ConfigObj objects. Thus, you can easily store your settings using Qt in a platform-specific way while still being able to utilize the powerful properties of ConfigObj.

The library contains two functions, from_QSettings which converts from a QSettings object to a ConfigObj object and to_QSettings, which converts from a ConfigObj to a QSettings object.

A short example:

```
	import sys
	from PyQt4.QtGui import QApplication
	from PyQt4.QtCore import QSettings
	import configobj
	conf = """
	p1 = 1
	"""
	app = QApplication(sys.argv)
	app.setApplicationName('configtest')
	app.setOrganizationName('foo')
	config = configobj.ConfigObj(conf.split('\n'))
	settings = to_QSettings(config)
	config2 = from_QSettings(settings)
	print(config == config2)

```

Support the developer if you like this software:

[![Donate using Liberapay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/saparvia/donate)
