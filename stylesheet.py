import os
import sys
import logging
# Make the example runnable without the need to install and include ui
# sys.path.append(os.path.dirname(__file__))
# sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../..'))
# sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../ui'))

# # Must be in this place, after setting path, to not need to install
# from stylesheets import qdarkstyle  # noqa: E402
# from stylesheets.qdarkstyle.dark.palette import DarkPalette  # noqa: E402
# from stylesheets.qdarkstyle.light.palette import LightPalette  # noqa: E402



logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
dirname = os.path.dirname(__file__).replace('\\', '/')


def set_default(app):
    # set styleSheet
    styleSheetPath = '{}/stylesheets/darkmode/darkmode.css'.format(dirname)
    if os.path.exists(styleSheetPath):
        try:
            app.setStyle('plastique')
            with open(styleSheetPath, 'r') as f:
                data = f.read()
                app.setStyleSheet(data + 'QLabel { color : white; }')

        except Exception as e:
            logger.info(str(e))


# def set_qdarkstyle(app):
#     style = qdarkstyle.load_stylesheet(palette=DarkPalette)
#     app.setStyleSheet(style)

