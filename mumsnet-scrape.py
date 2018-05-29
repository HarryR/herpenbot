#!/usr/bin/env python
import requests
import random
import time

# todo download mumsnet from archive.org

if __name__ == "__main__":
    user_agent = 'MumsNet Marcov Chain';
    start_id = 3177671-1000
    id_count = 10000
    base_url = 'https://www.mumsnet.com/Talk/ethical_living/'
    sess = requests.Session()
    outfile = open('data/topics-mumsnet.txt', 'a')
    for N in range(start_id, start_id-id_count, -1):
        url = base_url + str(N)        
        resp = sess.get(url)
        if resp.history:
            data = resp.url.split('/')
            assert data[3] == 'Talk'
            topic, title = data[4:]
            title = title.split('-')[1:]
            outfile.write(topic+'='+' '.join(title) + "\n" )
    outfile.close()
        
