from .Display import *
import webbrowser
import os

"""
This class is a processor class which calculates the average of the values given by different sensors of the same type.
It inherits from the Processor class
"""


class MHS35LCD(Display):

    """
        Parameters: List with parameters sensor_name
    """
    def __init__(self,parameters):
        Display.__init__(self)
        """
        We will get the url we want to display
        """
        url = parameters['url']
        if 'display_time' in parameters.keys():
            display_time = parameters['display_time']
        else:
            display_time = 0

        browser = 'chromium'
        browser_path = '/usr/lib/chromium-browser/chromium-browser'
        webbrowser.register(browser, None, webbrowser.BackgroundBrowser(browser_path), 1)
        webbrowser.get(browser).open_new_tab(url)

        """
        We close the navigator after x seconds
        """
        time.sleep(int(display_time))
        os.system("pkill " + browser)
        self.success = 1
