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

# Use
In the directory that this project is cloned to, run the command

```
python scrape.py <target directory>
```

Where ```<target directory>``` is the high level directory to save the podcasts
into. The script will automatically organize the podcasts into sub directories
within ```<target directory>``` based on the genre and program.