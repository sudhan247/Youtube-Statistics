# Youtube_Statistics
An API to scrap the youtube statistics

### Dependencies
* Python 3.6+
* requests
* Beautiful Soup 4
* Pandas

### Installation

    git clone https://github.com/sudhan247/Youtube_Statistics.git
    
    Enter cd Youtube_Statistics
    
    Enter pip install requirements.txt
    

### Usage
```
usage: youtube_scrap.py [--help] [--youtubeurl YOUTUBEURL] [--input INPUT]
                        [--output OUTPUT]

Get Youtube statistics without any API

optional arguments:
  --help, -h            Show this help message and exit
  --youtubeurl YOUTUBEURL, -y YOUTUBEURL
                        Link of Youtube video for which to get statistics
  --input INPUT, -i INPUT
                        Input filename (Text format delimited by new line)
  --output OUTPUT, -o OUTPUT
                        Output filename (output format is in csv)
```

### Single URL
## File in current working directory
```
python youtube_scrap.py --input input.txt --output output
```


### Multiple URL
```
python youtube_scrap.py --youtubeid ScMzIvxBSi4 --output ScMzIvxBSi4.json
```
