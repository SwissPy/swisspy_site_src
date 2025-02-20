AUTHOR = '@ccdesales'
SITENAME = 'Swiss Python Summit'
SITESUBTITLE = 'A Swiss Python Conference'
SITEURL = 'https://www.python-summit.ch/'
CONFDATE = 'February 16th, 2018'

PATH = 'content'
OUTPUT_PATH = "output"

TIMEZONE = 'Europe/Zurich'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('HSR (Venue)', 'http://hsr.ch/'),
    ('Public Transport', 'https://online.fahrplan.zvv.ch/bin/query.exe/dn?Z=Rapperswil%20SG&date=05.02.2016&time=08%3A30&start=1&REQ0HafasSearchForw=0'),

)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/pythonsummit'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme
THEME = 'nest'

# Minified CSS
NEST_CSS_MINIFY = False

# Add items to top menu
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
    ('Home', '/'),
    #('Register', '/pages/registration.html'),
    #('Call for Proposals', '/pages/call-for-proposals.html'),
    ('Call for Venues', '/pages/call-for-venues.html'),
    ('Help us', '/pages/call-for-helpers.html'),
    ('Program', '/pages/program.html'),
    ('Recordings', '/pages/recordings.html'),
    ('Venue', '/pages/venue.html'),
    ('CoC', '/pages/code-of-conduct.html'),
]

# Add header background image from content/images : 'background.jpg'
NEST_HEADER_IMAGES = 'header.jpg'
NEST_HEADER_LOGO = '/images/python-summit.svg'
NEST_HEADER_OPACITY = '0.3'

# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [
    ('Imprint', '/pages/imprint'),
]
NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_LINKS_COLUMN_TITLE = u'Links'
NEST_COPYRIGHT = u'<strong>CC-BY-SA 2018 Swiss Python Summit</strong>'

# Footer optional
NEST_FOOTER_HTML = '<strong><a href="mailto:info@python-summit.ch">info@python-summit.ch</a></strong><br><br>'

# index.html
NEST_INDEX_HEAD_TITLE = u'Homepage'
NEST_INDEX_HEADER_TITLE = u'Swiss Python Summit'
NEST_INDEX_HEADER_SUBTITLE = u'February 5<sup>th</sup> 2016, Rapperswil SG'
NEST_INDEX_CONTENT_TITLE = u'Last Posts'

# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Archives'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Posts Archives'
NEST_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Archives for all posts'
NEST_ARCHIVES_CONTENT_TITLE = u'Archives'

# article.html
NEST_ARTICLE_HEADER_BY = u'By'
NEST_ARTICLE_HEADER_MODIFIED = u'modified'
NEST_ARTICLE_HEADER_IN = u'in category'

# author.html
NEST_AUTHOR_HEAD_TITLE = u'Posts by'
NEST_AUTHOR_HEAD_DESCRIPTION = u'Posts by'
NEST_AUTHOR_HEADER_SUBTITLE = u'Posts archives'
NEST_AUTHOR_CONTENT_TITLE = u'Posts'

# authors.html
NEST_AUTHORS_HEAD_TITLE = u'Author list'
NEST_AUTHORS_HEAD_DESCRIPTION = u'Author list'
NEST_AUTHORS_HEADER_TITLE = u'Author list'
NEST_AUTHORS_HEADER_SUBTITLE = u'Archives listed by author'

# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Categories'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Archives listed by category'
NEST_CATEGORIES_HEADER_TITLE = u'Categories'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Archives listed by category'

# category.html
NEST_CATEGORY_HEAD_TITLE = u'Category Archive'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Category Archive'
NEST_CATEGORY_HEADER_TITLE = u'Category'
NEST_CATEGORY_HEADER_SUBTITLE = u'Category Archive'

# pagination.html
NEST_PAGINATION_PREVIOUS = u'Previous'
NEST_PAGINATION_NEXT = u'Next'

# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'

# tag.html
NEST_TAG_HEAD_TITLE = u'Tag archives'
NEST_TAG_HEAD_DESCRIPTION = u'Tag archives'
NEST_TAG_HEADER_TITLE = u'Tag'
NEST_TAG_HEADER_SUBTITLE = u'Tag archives'

# tags.html
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Tags List'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'Tags List'
NEST_TAGS_CONTENT_TITLE = u'Tags List'
NEST_TAGS_CONTENT_LIST = u'tagged'

# Static files
STATIC_PATHS = ['images', 'files', 'extra/CNAME', '72cdcf473e0cc473babe4ad68649ce1a.txt']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'}
}
READERS = {'html': None}
