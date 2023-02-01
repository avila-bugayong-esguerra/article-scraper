#!/usr/bin/env python3
import argparse
import os
from pathlib import Path


if __name__ ==  "__main__":
    parser = argparse.ArgumentParser(description="article scraper")
    parser.add_argument("--dataset", "-d",
        help="the dataset to be made after articles are scraped (choices: 3000, 5000)",
        default="3000")
    args = parser.parse_args()

    path = os.getcwd()

    if args.dataset == "3000":
        path += "/3000.html"
        if not Path(path).is_file():
            os.system("wget https://raw.githubusercontent.com/jamesesguerra/misc/main/3000.html")
            os.system("sed -i '' 's/5000/3000/' spiders/kami_spider.py")
    elif args.dataset == "5000":
        path += "/5000.html"
        if not Path(path).is_file():
            os.system("wget https://raw.githubusercontent.com/jamesesguerra/misc/main/5000.html")
            os.system("sed -i '' 's/3000/5000/' spiders/kami_spider.py")
    else: 
        print(f"Dataset {args.dataset} isn't a valid option.")

    os.system("scrapy crawl kami -O ../csv_files/kami.csv")

