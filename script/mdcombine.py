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

def combine_md_files(sourcefolder, outputfile):
    #write the combined file
    with open(outputfile, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(GPHEADER) + '\n\n')
        #list all files in the sourcefolder
        sourcefiles = [f for f in sourcefolder.iterdir() if f.is_file()]
        for file in sourcefiles:
            with open(file, 'r', encoding='utf-8') as infile:
                try:
                    outfile.write(infile.read() + '\n\n')
                except:
                    pass

#move to script folder
os.chdir(Path(__file__).parent)
#read a subfolder of markdown files in /omcdiary_sourcefiles
sourcefolder = Path("../omcdiary_sourcefiles")
#list all subfolders of sourcefolder, don't look at the files
subfolders = [f for f in sourcefolder.iterdir() if f.is_dir()]
print(subfolders)

#for each subfolder, output a combined markdown file named subfoldername.md
for subfolder in subfolders:
    outputfile = Path("../omcdiary_export") / (subfolder.name + ".md")
    combine_md_files(subfolder, outputfile)
    print(f"combined {subfolder} into {outputfile}")
