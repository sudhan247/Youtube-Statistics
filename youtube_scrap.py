import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse
import re
import sys
import calendar
import os
month={calendar.month_abbr[month]:'0'+str(month)if month<10 else str(month) for month in range(1,13)}

def getnum(arg):
    return int(''.join([i for i in arg if i.isdigit()]))

def getstat(url):
    response=requests.get(url)
    souped=BeautifulSoup(response.text, "html.parser")
    scripts=souped.find_all('script')
    rec=dict() 
    for i in scripts:
        res=str(i)     
        if 'window["ytInitialData"]' in res:
            rec['video_link']=url
            rec['video_views']=getnum(re.findall(r'[0-9,-]* views',res)[0])
            rec['likes']=getnum(re.findall(r'[0-9,-]* likes',res)[0])
            rec['dislikes']=getnum(re.findall(r'[0-9,-]* dislikes',res)[0])
            rec['uploaded date']=re.findall(r'"dateText":{"simpleText":"[0-9]{1,2} [A-Z][a-z][a-z] [0-9]{4}"}',res)[0]
            rec['uploaded date']=re.findall(r'[0-9]{1,2} [A-Z][a-z][a-z] [0-9]{4}',rec['uploaded date'])[0].split()
            rec['uploaded date'][1]=month[rec['uploaded date'][1]]
            rec['uploaded date']='-'.join(rec['uploaded date'])
    return rec

def process(inp):
    df=pd.DataFrame(columns = ['video_link','uploaded date','video_views','likes','dislikes'])
    for url in inp:
        try:
            df=df.append(getstat(url),ignore_index=True)
            print(df.tail(1).to_string())
        except:
            print('Some error occurred while fetching this URL:{0}'.format(url))
    return df

def main(argv):
    parser = argparse.ArgumentParser(add_help=False, description=('Get Youtube statistics without any API'))
    parser.add_argument('--help', '-h', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')
    parser.add_argument('--youtubeurl', '-y', help='Link of Youtube video for which to get statistics')
    parser.add_argument('--input','-i',help='Input filename (Text format delimited by new line)')
    parser.add_argument('--output', '-o', help='Output filename (output format is in csv)')
    args = parser.parse_args(argv)
    if args.input and args.output:
        try:
            fp=open(args.input,'r')
            
            inp=fp.read().split('\n')
            fp.close()
            if (args.input.rfind('\\'))!=-1:
                output=(args.input[:args.input.rfind('\\')]+'\\'+args.output+'.csv')
            else:
                output=os.getcwd()+'\\'+args.output+'.csv'              
            process(inp).to_csv(output,index=False)
        except:
            print('Some problem occured with specified INPUT FILE/Access Denied while writing the OUTPUT FILE')
    elif args.youtubeurl:
        try:
            print(getstat(args.youtubeurl))
        except:
            print('Some problem occured with specified URL')

if __name__ == "__main__":
    main(sys.argv[1:])



