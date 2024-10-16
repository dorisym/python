from datetime import datetime


def dateFormat():
    now = datetime.now()
    formatted_date = now.strftime("%Y%m%d%H%M%S")
    print("格式化的日期是22:", formatted_date)
    return formatted_date