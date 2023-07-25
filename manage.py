#!/usr/bin/env python
&quot;&quot;&quot;Django&#39;s command-line utility for administrative tasks.&quot;&quot;&quot;
import os
import sys
def main():
  os.environ.setdefault(&#39;DJANGO_SETTINGS_MODULE&#39;, &#39;youtubecomments.settings&#39;)
  try:
    from django.core.management import execute_from_command_line
  except ImportError as exc:
    raise ImportError(
      "couldn't import Django. Are you sure it's  installed"
      "available on your PYTHONPATH environment variable? Did you"
      "forget to activate a virtual environment?"
    ) from exc
  execute_from_command_line(sys.argv)

if name == &#39; main &#39;:
  main()
