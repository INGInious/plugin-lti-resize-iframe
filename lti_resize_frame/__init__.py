# -*- coding: utf-8 -*-
#
# This file is part of INGInious. See the LICENSE and the COPYRIGHTS files for
# more information about the licensing of this file.

""" Posts the iframe size in an page for an LTI course """
import os

from flask import send_from_directory
from inginious.frontend.pages.utils import INGIniousPage

__version__ = "0.1.michelfra"
PATH_TO_PLUGIN = os.path.abspath(os.path.dirname(__file__))

class StaticMockPage(INGIniousPage):
    def GET(self, path):
        return send_from_directory(os.path.join(_dir_path, "static"), path)

    def POST(self, path):
        return self.GET(path)

def init(plugin_manager, _, _2, _3):
    """ Init the plugin """
    plugin_manager.add_page('/plugins/lti_resize_iframe/static/<path:path>', StaticMockPage.as_view("ltiresizeframestaticpage"))
    plugin_manager.add_hook("javascript_footer", lambda: "/plugins/lti_resize_iframe/static/lti_resize_iframe.js")
