import os
import sublime
import sublime_plugin


class JournalCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = sublime.active_window()
        if os.path.exists("C:/Dropbox/journal.md"):
            view = window.open_file("C:/Dropbox/journal.md")
            point = view.size()
            while point >= 0:
                if view.find("\S", point):
                    region = view.find("\s+", point)
                    edit = view.begin_edit()
                    view.replace(edit, region, "\n\n")
                    view.show(view.size())
                    view.end_edit(edit)

                    break
                point -= 1



