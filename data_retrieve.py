#!/usr/bin/env python

import sys
import urllib
import urllib.request
import xml.etree.ElementTree as ET

def getData(first, last):
    path = 'data/' + last + ':' + first + '.xml'
    try:
        # if the data exists locally, use it
        f = open(path)
        XmlData = f.readlines()
    except FileNotFoundError:
        # otherwise, retrieve it from DBLP
        url = 'https://dblp.uni-trier.de/pers/xx/' + last[0].lower() + '/' + last + ':' + first + '.xml'
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            XmlData = list(map(lambda x: x.decode('ascii'), response.readlines()))

    return XmlData


if __name__ == '__main__':
    first, last = sys.argv[1], sys.argv[2]

    Xml = getData(first, last)
    root = ET.fromstringlist(Xml)
    records = root.findall('r')

    lsp = first + '_' + last + '_data.lsp'
    f = open(lsp, 'w')
    f.write('(setq data \'())\n')

    for r in records:
        rr = r[0] # r[0]: <inproceedings> or <article> or ...
        title = rr.findtext('title')
        authors = list(map(lambda x: x.text, rr.findall('author')))

        if rr.tag == 'article':
            booktitle = rr.findtext('journal')
        elif rr.tag == 'inproceedings' or rr.tag == 'incollection':
            booktitle = rr.findtext('booktitle')

        try: # <pages> may not exist (especially when the record is of an arXiv paper)
            pages = rr.findtext('pages').split('-')
            if len(pages) == 1:
                pages.append(pages[0])
        except AttributeError:
            pages = ['0', '0']
        for i, p in enumerate(pages):
            j = p.find(':')
            if j >= 0: # ex: '3:15' -> 15
                pages[i] = p[j+1:]

        authors_str = ' '.join(map(lambda x: '"'+x+'"', authors))
        f.write('(push \'((' + authors_str + ') "' + title + '" "' + booktitle + '" (' + pages[0] + ' ' + pages[1] + ')) data)\n')

    f.close()
