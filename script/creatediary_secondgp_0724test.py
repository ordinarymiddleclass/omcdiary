GPHEADER =[ '[_metadata_:encoding]: - "utf-8"',
        '[_metadata_:language]: - "zh-Hant-TW"',
        '[_metadata_:fileformat]: - "markdown"',
        '[_metadata_:MIME_type]: - "text/plain"',
        '[_metadata_:markdown_version]: - "commonmark version 0.30"',
        '[_metadata_:markdown_spec]: - "https://spec.commonmark.org/0.30/"']
zhweekday = ["星期日", "星期一", "星期二",
            "星期三", "星期四", "星期五", "星期六"]

from datetime import datetime
from datetime import timedelta
from dateutil import relativedelta
import os.path
from pathlib import Path
import lazymdwriter


def from_my_birthday (d):
    """
        Calculate time difference between given datetime d and 1986-4-23.
    """
    birthday = datetime(1986, 4, 23)
    return relativedelta.relativedelta(d, birthday) 

def from_licence (d):
    """
        Calculate time difference between given datetime d and 2017-10-12.
    """
    birthday = datetime(2017, 10, 12)
    return relativedelta.relativedelta(d, birthday) 

def from_epoch (d):
    return (d - datetime(1970,1,1)).days

def from_gp (d):
    return (d - datetime(2019,9,28)).days

def format_utc_en (d):
    return d.strftime("%B %d, %Y (UTC)")

def format_utc_zh (d):    
    zhyear = "世界協調時間{0}年".format(d.year)
    zhday = "{0}月{1}日".format(d.month, d.day)
    rocyear = "(中華民國{0}年，令和{1}年)".format(d.year-1911, d.year-2018)
    return zhyear + rocyear + zhday

def format_epoch_en (d):
    return "{} days since Unix Epoch".format(from_epoch(d))

def format_epoch_zh (d):
    return "Unix 紀元 {} 日".format(from_epoch(d))

def format_weekday_en (d):
    return d.strftime ("%A")

def format_weekday_zh (d):
    return zhweekday[int(d.strftime ("%w"))]

def format_gp_en (d):
    return "Globus Pallidum day {}".format(from_gp(d))

def format_gp_zh (d):
    return "蒼白球紀元第{}日".format(from_gp(d))

def format_tracking (d1, d2, s):
    daycount = (d1 - d2).days
    return "{}(此目標目前追蹤第{}天)".format(s, daycount)

def format_age (d):
    li = lazymdwriter.convenient_list("年齡 Age")
    age = from_my_birthday (d)
    licence_age = from_licence (d)
    years = age.years
    months = age.months
    days = age.days
    licence_years = licence_age.years
    licence_months = licence_age.months
    licence_days = licence_age.days
    li.add_ul('{} years {} months {} days old / {} years {} months {} days after acquiring ROC Surgical Pathology Licence'.format(years, months, days, licence_years, licence_months, licence_days))
    li.add_ul('{} 歲 {} 個月 {} 天 / 成為病理專科醫師 {} 年 {} 個月 {} 天'.format(years, months, days, licence_years, licence_months, licence_days))
    return li.compile()

def format_date_information (d):
    li = lazymdwriter.convenient_list("日期 Date")
    date_information_zh = format_utc_zh(d) + " / " + format_epoch_zh(d) + \
        " / " + format_weekday_zh(d) + " / " + format_gp_zh (d)
    date_information_en = format_utc_en(d) + " / " + format_epoch_en(d) + \
        " / " + format_weekday_en(d) + " / " + format_gp_en(d)    
    li.add_ul(date_information_zh)
    li.add_ul(date_information_en)
    li.add_ul("特殊註記:")
    return li.compile()

def format_title (d):
    n = from_gp (d)
    gpserial = "%04d"%n
    briefdate = d.strftime ("%Y%m%d")
    return "蒼白球日誌{}_gpdiary{}_{}".format(gpserial, gpserial, briefdate)

def format_filename (d):    
    n = from_gp (d)
    gpserial = "%04d"%n
    briefdate = d.strftime ("%Y%m%d")
    return "gpdiary{}_{}".format(gpserial, briefdate) + ".md"

def create_filehead(d):
    date_information = format_date_information(d)
    age_information = format_age(d)
    title = lazymdwriter.lazy_header(format_title (d), 1)
    return title + date_information + age_information 


def create_template_body(d, tasklist = [("test", datetime(2024, 1, 23)), ("test", datetime(2024, 1, 23))]):
    upper_body = lazymdwriter.convenient_list("本文 Content")
    lower_body = lazymdwriter.convenient_list("注釋 Comment")
    appendix = lazymdwriter.convenient_list("附錄 Appendix")
    upper_body.add_ol("", 1)
    upper_body.add_ol("工作紀要", 2)
    for task in tasklist:
        upper_body.add_secondol(format_tracking(d, task[1], task[0]))
    #upper_body.add_secondol(format_tracking(datetime.now(), datetime(2024, 1, 23), "test")
    appendix.add_ul("時光機")
    for item in timemachine:
        appendix.add_secondol(item)
    return upper_body.compile() + lower_body.compile() + appendix.compile()

def create_template(d, tasklist = [("test", datetime(2024, 1, 23)), ("test", datetime(2024, 1, 23))]):
    head = "\n".join(GPHEADER)
    return head + "\n\n" + create_filehead(d) + create_template_body(d, tasklist)

def create_file(d, path):
    newfilepath = path / format_filename (d)
    if os.path.exists(newfilepath):
        print("file already exists")
        pass
    else:
        with newfilepath.open("w", encoding="utf-8") as f:
            f.write(create_template(d, tasklist))

current_path = Path(os.path.realpath(__file__))
root = current_path.parent.parent
rootpath = root / "scripttest"
tasklist = [
    ("開始帶大學生做影像分析。", datetime(2024, 7, 16)), 
    ("籌備嶄新的病理學及病理實驗教材。", datetime(2024, 7, 22)), 
    ("H大合作的切片影像分析企劃，對方已經開始訓練了。", datetime(2024, 1, 23)), 
    ("加拿大鮮肉合作的文字分析企劃，已經交出了第二批指示。8月會開始發給他們薪水，到時就可以好好盯進度。", datetime(2024, 1, 23)),
    ("BL學科搬遷，主要是助理在規劃，但偶爾也要盯一下 ", datetime(2024, 1, 23)),
    ("偶爾要念點病理書。", datetime(2024, 1, 23)),
    ]
timemachine = [
    "2025年授袍講稿，蒼白球日誌1662",
    "2025年授袍講稿二，蒼白球日誌1663",
]

for i in range(100):
    newday = datetime.now() + timedelta(days=i)
    create_file(newday, rootpath)

