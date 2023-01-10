# Scrapy tutorial

This is a tutorial for Scrapy, a web crawling and web scraping framework.

## Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## Installation

To install Scrapy, you need to have Python 2.7 or Python 3.3+ installed on your system.

You can install Scrapy using pip:

```bash
pip install Scrapy
```


## Quick start

To create a Scrapy project:

```bash
scrapy startproject tutorial
```

This will create a tutorial directory with the following contents:

```bash
tutorial/
├── scrapy.cfg            # deploy configuration file   
├── tutorial/             # project's Python module, you'll import your code from here
│   ├── __init__.py
│   ├── items.py          # project items definition file
│   ├── middlewares.py    # project middlewares file
│   ├── pipelines.py      # project pipelines file
│   ├── settings.py       # project settings file
│   └── spiders/          # a directory where you'll later put your spiders
│       ├── __init__.py
│       └── ...
```

To create a spider, go to the spiders directory and run:

```bash
scrapy genspider example example.com
```
