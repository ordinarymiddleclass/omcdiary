from convenientpath import convenientpath
from pathlib import Path 
from runpandoc import pandoc_html
from runpandoc import pandoc_txt
from runpandoc import pandoc_tex

def _normalize_text_inner(li):
    if "===" in li[1]:
        li.pop(1)
    if "###### tags" in li[-1]:
        li.pop()
    title = li[0].split("_")
    newtitle_raw = title[2].strip("\n").strip(" #") 
    newtitle_list = [newtitle_raw[:4], newtitle_raw[4:6], newtitle_raw[6:]]
    newtitle = "/".join(newtitle_list)
    adjusted_title = "# " + title[0].strip("# ") + " " + newtitle + " #\n"
    li[0] = adjusted_title
    return "".join(li)

def normalize_text(fp):
    """
        只能使用在照規定寫完的蒼白球日誌
    """
    li = fp.readlines()
    return _normalize_text_inner(li)

def concatmd (li):
    """
        take a list of path of files, and concatenate them 
    """
    destlist = []
    for item in li:
        with item.open("r", encoding="utf-8") as f:
            destlist.append(normalize_text(f))
    return "\n\n".join(destlist)

dest = convenientpath.get_dest("md")
dest_html = convenientpath.get_dest("html")
dest_txt = convenientpath.get_dest("txt")
dest_tex = convenientpath.get_dest("tex")
destfile = dest / "test2.md"
destfile_html = dest_html / "test2.html"
destfile_txt = dest_txt / "test2.txt"
destfile_tex = dest_tex / "test2.tex"

testlist = []
for item in ["201909", "201910", "201911"]:
    source = convenientpath.get_source() / item 
    testlist += sorted(source.glob("*.md"))
newmd = concatmd(testlist)
newmd.replace("---", "")
with destfile.open("w", encoding="utf-8") as f:
    f.write(newmd)
with destfile_html.open("w", encoding="utf-8") as f:
    f.write(pandoc_html(str(destfile)))
with destfile_txt.open("w", encoding="utf-8") as f:
    f.write(pandoc_txt(str(destfile)))
with destfile_tex.open("w", encoding="utf-8") as f:
    f.write(pandoc_tex(str(destfile)))
"""
destlist = []
for item in testlist:
    sourcefile = source / item 
    with sourcefile.open("r", encoding="utf-8") as f:
        destlist.append(normalize_text(f))

    f.write("\n\n".join(destlist))

"""
