# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = 'Marvin Steadfast'
SITENAME = 'is trying to code'
SITEURL = 'http://code.xsteadfastx.org'
AVATAR = '/theme/images/avatar.png'
TIMEZONE = "Europe/Berlin"
DESCRIPTION = "Der Versuch zu programmieren und Computer Zeugs nieder zu bloggen."

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

GITHUB_URL = 'http://github.com/xsteadfastx/'
TWITTER_NAME = 'xsteadfastx'
#DISQUS_SITENAME = "xsteadfastxistryingtocode"
ISSO_URL = 'http://comments.xsteadfastx.org'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# global metadata to all the contents
#DEFAULT_METADATA = (('yeah', 'it is'),)

# path-specific metadata
EXTRA_PATH_METADATA = {
    #'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    #'extra/robots.txt',
    'extra/CNAME',
    #'code',
    #'notebooks'
    ]

# custom page generated with a jinja2 template
#TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
#foobar = "barbaz"

THEME = 'themes/xsteadfastx-greg'
OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

# plugins
#PLUGIN_PATH = '../pelican-plugins'
#PLUGINS = ['liquid_tags.notebook', 'liquid_tags.include_code',
#           'liquid_tags.img', 'liquid_tags.video']

#CODE_DIR = 'code'
#NOTEBOOK_DIR = 'notebooks'
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
