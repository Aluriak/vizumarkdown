"""Markdown extension allowing the management of github-like checkboxes.

"""

import markdown as md
from markdown.inlinepatterns import Pattern
from markdown.extensions import Extension
from markdown.util import etree


BOX_PATTERN = r'\[([ a-z-]+)\]'
FA_CHAR = {  # shortcuts
    ' ': 'fa-square-o',
    'x': 'fa-check-square-o',
    't': 'fa-tag',
    'f': 'fa-firefox',
}


class BoxPattern(Pattern):
    def handleMatch(self, m):
        boxcontent = m.group(2)
        box_name = FA_CHAR.get(boxcontent, 'fa-' + boxcontent)
        el = etree.Element('i', {'class': 'fa {} fa-fw'.format(box_name)})
        el.text = ''
        return el



class BoxExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('boxpattern', BoxPattern(BOX_PATTERN), '_end')



if __name__ == "__main__":
    import webbrowser
    PATH_TO_FA = 'css/font-awesome-4.7.0/css/font-awesome.min.css'
    html = md.markdown(open('README.mkd').read(), extensions=[BoxExtension()])
    html_file = 'README.html'
    with open(html_file, 'w') as fd:
        fd.write('<head> <link rel="stylesheet" href="{}"> </head>'.format(PATH_TO_FA))
        fd.write('<body>' + html + '</body>')
    webbrowser.open(html_file)
