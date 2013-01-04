#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import sublime
import sublime_plugin

# fix for import order

sys.path.append(os.path.join(sublime.packages_path(), 'LiveReload'))
LiveReload = __import__('LiveReload')
sys.path.remove(os.path.join(sublime.packages_path(), 'LiveReload'))


class SimpleRefreshLongDelay(LiveReload.Plugin, sublime_plugin.EventListener):

    title = 'Simple Reload with delay(500ms)'
    description = 'Wait 500ms then refresh page, when file is saved'
    file_types = '*'

    def on_post_save(self, view):
        ref = self
        sublime.set_timeout(lambda: ref.refresh(os.path.basename(view.file_name())), 500)
