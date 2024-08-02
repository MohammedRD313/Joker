def media_type(content_type):
    if content_type.startswith('application/json'):
        return 'JSON'
    elif content_type.startswith('text/html'):
        return 'HTML'
    elif content_type.startswith('text/plain'):
        return 'Plain Text'
    else:
        return 'Unknown'
