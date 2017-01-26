
import os
import sys
import webbrowser
from markdown import markdown



if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('usage: <markdown file>')
        exit()

    markdown_file = sys.argv[1]
    html_file = os.path.splitext(markdown_file)[0] + '.html'
    with open(markdown_file) as fd:
        html = markdown(fd.read())
    with open(html_file, 'w') as fd:
        fd.write(html)
    webbrowser.open(html_file)
