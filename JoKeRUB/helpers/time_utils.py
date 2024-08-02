def time_formatter(timestamp):
    """
    تنسيق الطابع الزمني إلى تنسيق مقروء.

    :param timestamp: الطابع الزمني (مثلاً: 1633039200)
    :return: التاريخ والوقت بشكل مقروء (مثلاً: '2021-10-01 00:00:00')
    """
    from datetime import datetime
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
