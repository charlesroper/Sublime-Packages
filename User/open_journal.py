import os
import sublime
import sublime_plugin
from time import localtime, strftime


class JournalCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        window = sublime.active_window()
        if os.path.exists("C:/Dropbox/journal.md"):
            view = window.open_file("C:/Dropbox/journal.md")
            if view.is_loading():
                print "is loading"
                sublime.set_timeout(lambda: self.run(), 100)
            point = view.size() - 1
            while point >= 0:
                if view.find("\S", point):
                    region = view.find("\s+", point)
                    edit = view.begin_edit()
                    if region:
                        view.replace(edit, region, "\n\n")
                    else:
                        view.insert(edit, point + 1, "\n\n")
                    now = strftime("%H:%M", localtime())
                    view.insert(edit, view.size(), "### %s\n\n" % now)
                    view.end_edit(edit)
                    view.sel().clear()
                    view.sel().add(sublime.Region(view.size()))
                    view.show(point)
                    break
                point -= 1
