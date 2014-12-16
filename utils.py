# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import subprocess
import re
from bs4 import BeautifulSoup


def maps_encode(start, finish):
    start_enc = re.sub(' ', '+', start)
    finish_enc = re.sub(' ', '+', finish)
    url = 'https://www.google.com/maps/dir/%s/%s' % (start_enc, finish_enc)
    return url


def get_gmaps_html(req):
    p = subprocess.Popen(["phantomjs", "spooky.js", req],
                         stdout=subprocess.PIPE)
    gmaps_html = {'html': p.communicate()[0]}
    return gmaps_html


def get_trip_stats(html):
    soup = BeautifulSoup(html)
    raw_traffic = soup.find_all('div', class_='altroute-rcol altroute-aux')
    raw_distance = soup.find_all('div', class_='altroute-rcol altroute-info')

    traffic_string = raw_traffic[0].find('span').text
    distance_string = raw_distance[0].find('span').text

    traffic_regex = re.compile("[0-9]+")
    distance_regex = re.compile("[0-9]+\.[0-9]+")

    traffic = traffic_regex.findall(traffic_string)[0]
    distance = distance_regex.findall(distance_string)[0]

    stats = {'minutes': float(traffic), 'miles': float(distance)}
    return stats


def trip_stats(source, dest):
    request_url = maps_encode(source, dest)
    html = get_gmaps_html(request_url)['html']
    d = get_trip_stats(html)
    return {'destination': dest, 'source': source, 'trip_info': d}
