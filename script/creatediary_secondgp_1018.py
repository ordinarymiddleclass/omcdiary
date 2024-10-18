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

def from_exposure (d):
    exposure = datetime(2024, 9, 28)
    return relativedelta.relativedelta(d, exposure) 

def from_licence (d):
    """
        Calculate time difference between given datetime d and 2017-10-12.
    """
    birthday = datetime(2017, 10, 12)
    return relativedelta.relativedelta(d, birthday) 

def from_epoch (d):
    epoch = datetime(1970, 1, 1)
    return relativedelta.relativedelta(d, epoch)

def from_gp (d):
    gp = datetime(2019, 9, 28)
    return relativedelta.relativedelta(d, gp)

def format_utc_en (d):
    return d.strftime("%B %d, %Y (UTC)")

def format_utc_zh (d):    
    zhyear = "世界協調時間{0}年".format(d.year)
    zhday = "{0}月{1}日".format(d.month, d.day)
    rocyear = "(中華民國{0}年，令和{1}年)".format(d.year-1911, d.year-2018)
    return zhyear + rocyear + zhday

def format_epoch_en (d):
    epoch = from_epoch(d)     
    return "Unix Epoch {} year {} month {} day".format(epoch.years+1, epoch.months, epoch.days)

def format_epoch_zh (d):
    epoch = from_epoch(d)     
    return "Unix 紀元 {} 年 {} 月 {} 日".format(epoch.years+1, epoch.months, epoch.days)

def format_weekday_en (d):
    return d.strftime ("%A")

def format_weekday_zh (d):
    return zhweekday[int(d.strftime ("%w"))]

def format_gp_en (d):
    gp = from_gp(d)
    return "Globus Pallidum year {} month {} day {}".format(gp.years+1, gp.months, gp.days)

def format_gp_zh (d):
    gp = from_gp(d)
    return "蒼白球紀元 {} 年 {} 月 {} 日".format(gp.years+1, gp.months, gp.days)

def format_tracking (d1, d2, s):
    daycount = relativedelta.relativedelta(d1, d2)
    return "{}(此目標目前追蹤 {} 年 {} 月 {} 日)".format(s, daycount.years, daycount.months, daycount.days)

def format_age (d):
    li = lazymdwriter.convenient_list("年齡 Age")
    age = from_my_birthday (d)
    licence_age = from_licence (d)
    exposure = from_exposure (d)
    years = age.years
    months = age.months
    days = age.days
    licence_years = licence_age.years
    licence_months = licence_age.months
    licence_days = licence_age.days
    exposure_years = exposure.years
    exposure_months = exposure.months
    exposure_days = exposure.days

    li.add_ul('{} years {} months {} days old / {} years {} months {} days after acquiring ROC Surgical Pathology Licence'.format(years, months, days, licence_years, licence_months, licence_days))
    li.add_ul('{} 歲 {} 個月 {} 天 / 成為病理專科醫師 {} 年 {} 個月 {} 天 / 日誌被入侵 {} 年 {} 個月 {} 天'.format(years, months, days, licence_years, licence_months, licence_days, exposure_years, exposure_months, exposure_days))   
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
    gp = datetime(2019, 9, 28)
    n = (d - gp).days
    gpserial = "%04d"%n
    briefdate = d.strftime ("%Y%m%d")
    return "蒼白球日誌{}_gpdiary{}_{}".format(gpserial, gpserial, briefdate)

def format_filename (d):    
    gp = datetime(2019, 9, 28)
    n = (d - gp).days
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
    ("大學生專題(現在似乎要focus在文字分析了，也就是加拿大鮮肉那邊)。", datetime(2024, 7, 16)), 
    ("籌備嶄新的病理學及病理實驗教材。", datetime(2024, 7, 22)), 
    ("H大合作的切片影像分析企劃，對方已經開始訓練了，2024/9/9去催了第一次進度。", datetime(2024, 1, 23)), 
    ("加拿大鮮肉合作的文字分析企劃，已經交出了第二批指示。2024/9月已正式發薪，2024/9/14開跑，然後已經分成兩組在進行，似乎比想像中的要快，2024年10月18日已經完成部分資料標注。", datetime(2024, 1, 23)),
    ("BL學科搬遷，冰箱已經上去了，2024/10/17確認了工程進度，似乎要評鑒後才能進行。", datetime(2024, 1, 23)),
    ("偶爾要念點病理書。", datetime(2024, 1, 23)),
    ]
timemachine = [
    "2025年授袍講稿，蒼白球日誌1662",
    "2025年授袍講稿二，蒼白球日誌1663",
]

for i in range(100):
    newday = datetime.now() + timedelta(days=i)
    create_file(newday, rootpath)

