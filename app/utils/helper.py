from datetime import datetime


def format_datetime(dt: datetime) -> str:
    #Format timestamps consistently across the app.
    
    return dt.strftime("%d %b %Y • %I:%M %p")
