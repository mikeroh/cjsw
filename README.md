# Overview
This project is a tool to retrieve CJSW podcasts from their website, name and
organize them, and set the ID3 tags.

# Setup
To get this script working, some packages are required for python, 
run the following commands to install them.

```python
pip install lxml
pip install requests
pip install pathlib
```


Using Debian, the following packages must be installed before getting lxml.

```bash
apt-get install libxml2-dev libxslt1-dev python-dev
```

# Use
In the directory that this project is cloned to, run the command

```
python scrape.py <target directory>
```

Where ```<target directory>``` is the high level directory to save the podcasts
into. The script will automatically organize the podcasts into sub directories
within ```<target directory>``` based on the genre and program.

##As a cron job
```
python scrape.py <target directory> <genre>
```

For use in a script that requires no user interaction, a specific genre can be
passed to the scraper. All programs in the genre specified by ```<genre``` will
have their latest episodes downloaded.