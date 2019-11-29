# -*- coding: utf-8 -*-
#
# This file is part of INGInious. See the LICENSE and the COPYRIGHTS files for
# more information about the licensing of this file.

""" Posts the iframe size in an page for an LTI course """
import os
import web


__version__ = "0.1.michelfra"
PATH_TO_PLUGIN = os.path.abspath(os.path.dirname(__file__))

class StaticMockPage(object):
    # TODO: Replace by shared static middleware and let webserver serve the files
    def GET(self, path):
        if not os.path.abspath(PATH_TO_PLUGIN) in os.path.abspath(os.path.join(PATH_TO_PLUGIN, path)):
            raise web.notfound()

        try:
            with open(os.path.join(PATH_TO_PLUGIN, "static", path), 'rb') as file:
                return file.read()
        except:
            raise web.notfound()

    def POST(self, path):
        return self.GET(path)


def init(plugin_manager, _, _2, _3):
    """ Init the plugin """
    plugin_manager.add_page('/plugins/lti_resize_iframe/static/(.+)', StaticMockPage)
    plugin_manager.add_hook("javascript_footer", lambda: "/plugins/lti_resize_iframe/static/lti_resize_iframe.js")
