
import os
import sys
import webbrowser
from markdown import markdown

from boxes import BoxExtension


def header(css:str=None) -> str:
    if css:
        return '<head> <link rel="stylesheet" href="{}"> </head>'.format(css)
    return ''


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('usage: <markdown file> <path to font awesome css file>')
        exit()

    markdown_file = sys.argv[1]
    path_to_fa = sys.argv[2]
    assert os.path.exists(path_to_fa)
    html_file = os.path.splitext(markdown_file)[0] + '.html'
    with open(markdown_file) as fd:
        html = markdown(fd.read(), extensions=[BoxExtension()])
    with open(html_file, 'w') as fd:
        fd.write(header(css=path_to_fa))
        fd.write(html)
    webbrowser.open(html_file)
