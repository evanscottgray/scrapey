# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import subprocess
import re
from bs4 import BeautifulSoup


def maps_encode(start, finish):
    start_enc = re.sub(' ', '+', start)
    start_enc = '1+Fanatical+Pl,+San+Antonio,+TX+78218'
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
    li = soup.find_all("li", class_="dir-altroute altroute-current")
    td = soup.find_all("td", class_="ddw-addr")
    results = {}

    if li:
        info = BeautifulSoup(str(li[0]))
        parsed_info = [text for text in info.stripped_strings]
        if len(parsed_info) >= 5:
            results['distance'] = str(parsed_info[0])
            results['eta_in_current_traffic'] = str(parsed_info[3].split(':')[-1]).strip()
            results['route'] = str(parsed_info[4])
        else:
            print 'Hard Coded divs have changed :('
    else:
        print 'Could Not Find Route!'

    if len(td) >= 1 :
        dest = BeautifulSoup(str(td[1]))
        parsed_dest = [text for text in dest.stripped_strings]
        if len(parsed_dest) >= 3:
            results['destination_name'] = str(parsed_dest[0])
            results['street_address'] = str(parsed_dest[1])
            results['city_state'] = str(parsed_dest[2])
            try:
                results['phone_number'] = str(parsed_dest[3])
            except:
                pass
    else:
        print 'Could Not Find Dest'

    return results


def trip_stats(source, dest):
    request_url = maps_encode(source, dest)
    html = get_gmaps_html(request_url)['html']
    
    d = get_trip_stats(html)
    destination = d.get('destination_name', dest)
    street = d.get('street_address', None)
    city_state = d.get('city_state', None)

    distance = d.get('distance', None)
    eta = d.get('eta_in_current_traffic', None)
    route = d.get('route', None)

    trip_info = {'distance': distance, 'eta': eta, 'route': route}
    
    return {'destination': destination, 'street': street, 'trip_info': trip_info}
