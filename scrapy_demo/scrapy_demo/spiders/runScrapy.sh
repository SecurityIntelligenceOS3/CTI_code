#!/bin/bash
# This will run the crawler each 10 min

while true; 
	do scrapy crawl pastebin;
 	sleep 600; 
done
