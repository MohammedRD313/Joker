def readable_time(seconds):
    """
    تحويل عدد الثواني إلى تنسيق زمني مقروء.

    :param seconds: عدد الثواني.
    :return: الزمن في شكل ساعة:دقيقة:ثانية.
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"
