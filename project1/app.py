import webview
import os
import sys

# Handle PyInstaller bundle path
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS  # Temporary folder where PyInstaller extracts files
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

html_path = os.path.join(base_dir, 'html', 'index.html')
url = 'file://' + html_path.replace('\\', '/')

window = webview.create_window('My HTML App', url, width=1200, height=800)
webview.start()
