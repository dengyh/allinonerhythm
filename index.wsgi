import sae
import sys
import os.path
from allinonerhythm import wsgi
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))

os.environ['DJANG_SETTING_MODULE'] = 'settings'
sys.path.append(os.path.join(os.path.dirname(__file__), 'allinonerhythm'))

application = sae.create_wsgi_app(wsgi.application)