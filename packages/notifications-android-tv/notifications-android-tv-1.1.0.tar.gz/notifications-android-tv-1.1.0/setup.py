# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['notifications_android_tv']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.27.0,<0.28.0']

setup_kwargs = {
    'name': 'notifications-android-tv',
    'version': '1.1.0',
    'description': 'Python API for sending notifications to Android/Fire TVs',
    'long_description': '# Android TV / Fire TV Notifications\n\nPython package that interfaces with [Notifications for Android TV](https://play.google.com/store/apps/details?id=de.cyberdream.androidtv.notifications.google) and [Notifications for Fire TV](https://play.google.com/store/apps/details?id=de.cyberdream.firenotifications.google) to send notifications to your TV.\n\n## Usage\n\n- Install the application on your TV\n- Get the IP of the TV unit\n\n```python\nfrom notifications_android_tv import Notifications\nnotify = Notifications("192.168.1.10")\n# validate connection\ntry:\n    await notify.async_connect()\nexpect ConnectError:\n    return False\nawait notify.async_send(\n    "message text",\n    title="Title text",\n)\n```\n\n## Optional parameters\n\n- `title`: Notification title\n- `duration`: Display the notification for the specified period. Default is 5 seconds\n- `fontsize`: Text font size. Use `FontSizes` class to set the fontsize. Default is `FontSizes.MEDIUM`\n- `position`: Notification position. Use `Positions` class to set position. Default is `Positions.BOTTOM_RIGHT`.\n- `bkgcolor`: Notification background color. Use `BkgColors` class to set color. Default is `BkgColors.GREY`.\n- `transparency`: Background transparency of the notification. Use `Transparencies` class. Default is `Transparencies._0_PERCENT`.\n- `interrupt`: Setting it to `True` makes the notification interactive and can be dismissed or selected to display more details. Default is `False`\n- `icon`: Can be `str` represnting the file path or an `ImageUrlSource` that includes the url and authentication params to fetch the image from a url.\n- `image_file`: Can be `str` represnting the file path or an `ImageUrlSource` that includes the url and authentication params to fetch the image from a url.\n\nRefer to the [example file](example.py) for setting these parameters directly or from a data dictionary (as documented in <https://www.home-assistant.io/integrations/nfandroidtv>)\n',
    'author': 'Rami Mosleh',
    'author_email': 'engrbm87@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/engrbm87/notifications_android_tv',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
