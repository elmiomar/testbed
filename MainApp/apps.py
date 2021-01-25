from django.apps import AppConfig

"""
This class is the main class that allows the IOT component to connect to a protocol when launching the project.
"""


class MainAppConfig(AppConfig):
    name = 'MainApp'

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)

    def ready(self):
        from TestBed import settings
        if hasattr(settings, 'RUN_MAIN'):
            run_main = settings.RUN_MAIN
        else:
            run_main = False

        if not run_main:
            from MainApp.processor.MainProcessor import MainProcessor
            main_processor = MainProcessor()
            main_processor.connect_protocol()

