from bs4 import BeautifulSoup

def parse_html(html_content):
    """
    Parses HTML to extract:
    - Readable text from common content tags.
    - Metadata from <meta> tags.

    Args:
        html_content (str): Raw HTML string.

    Returns:
        list: Combined content from tags and meta fields.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    text_items = []

    # 1. Extract main content tags
    content_tags = ['p', 'h1', 'h2', 'h3', 'li', 'article']
    for tag in content_tags:
        for element in soup.find_all(tag):
            text = element.get_text(strip=True)
            if text:
                text_items.append(text)

    # 2. Extract metadata from <meta> tags
    meta_fields = ['description', 'keywords', 'author', 'og:title', 'og:description', 'twitter:description']

    for meta in soup.find_all('meta'):
        name = meta.get('name', '').lower()
        prop = meta.get('property', '').lower()
        content = meta.get('content', '')

        if name in meta_fields or prop in meta_fields:
            if content:
                text_items.append(content.strip())

    return text_items
# HTML parser placeholder
