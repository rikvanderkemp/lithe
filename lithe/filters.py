import markdown


def markdown_filter(value):
    """
        Just convert plain text to markdown
    """
    return markdown.markdown(
        value,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.abbr',
            'markdown.extensions.attr_list',
            'markdown.extensions.def_list',
            'markdown.extensions.fenced_code',
            'markdown.extensions.footnotes',
            'markdown.extensions.tables',
            'markdown.extensions.smart_strong',
            'markdown.extensions.codehilite',
            'markdown.extensions.meta',
            'markdown.extensions.nl2br',
            'markdown.extensions.sane_lists',
            'markdown.extensions.smarty',
            'markdown.extensions.toc'
        ])
