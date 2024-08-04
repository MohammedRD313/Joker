def media_type(content_type):
    # تأكد من أن content_type هو نص
    if isinstance(content_type, str):
        if content_type.startswith('application/json'):
            return 'JSON'
        elif content_type.startswith('text/html'):
            return 'HTML'
        elif content_type.startswith('text/plain'):
            return 'Plain Text'
        else:
            return 'Unknown'
    else:
        # إذا لم يكن content_type نصًا، ارجع 'Unknown'
        return 'Unknown'
