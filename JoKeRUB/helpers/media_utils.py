def media_type(message):
    # تحقق من أن message هو كائن يحتوي على content_type
    if hasattr(message, 'content_type') and isinstance(message.content_type, str):
        content_type = message.content_type
        if content_type.startswith('application/json'):
            return 'JSON'
        elif content_type.startswith('text/html'):
            return 'HTML'
        elif content_type.startswith('text/plain'):
            return 'Plain Text'
        elif content_type.startswith('audio/'):
            return 'Audio'
        else:
            return 'Unknown'
    else:
        # إذا لم يكن message يحتوي على content_type نصي، ارجع 'Unknown'
        return 'Unknown'

# مثال على كيفية استخدام الدالة
class Message:
    def __init__(self, content_type):
        self.content_type = content_type

reply = Message('audio/mpeg')
mediatype = media_type(reply)
print(mediatype)  # سيطبع 'Audio'
