import sublime
import sublime_plugin
import re

class ShowGotoFilePanel(sublime_plugin.WindowCommand):
  def run(self):
    text = self._extract_class_name() or self._extract_path() or ''
    self.window.run_command('show_overlay', {'overlay': 'goto', 'text': text,
      "show_files": True})

  def _extract_class_name(self):
    view = self.window.active_view()
    if view == None or len(view.sel()) == 0:
      return None

    sel = view.sel()[0]
    text = view.substr(sel)
    is_class_name = ((
        'entity.name.type.class' in view.scope_name(sel.begin()) and
        'entity.name.type.class' in view.scope_name(sel.end() - 1)
      ) or (
        'support.class' in view.scope_name(sel.begin()) and
        'support.class' in view.scope_name(sel.end() - 1)
      ) and
      not sel.empty() and
      "\n" not in text
    )

    if not is_class_name:
      return None

    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text

  def _extract_path(self):
    view = self.window.active_view()
    if view == None or len(view.sel()) == 0:
      return None

    sel = view.sel()[0]
    if sel.empty() or 'string' not in view.scope_name(sel.a):
      return None

    text = view.substr(sel)
    if '/' not in text and re.search(r'\.[\w\-]{2,}$', text) == None:
      return None

    return text