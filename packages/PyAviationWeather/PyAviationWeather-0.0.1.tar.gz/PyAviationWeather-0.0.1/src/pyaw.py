from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}


def get_METAR(airport:str, past_n_hour=0):
    """
    Get the METAR for specific airport.
    """
    assert isinstance(airport, str)
    assert isinstance(past_n_hour,int)
    url = f"http://aviationweather.gov/metar/data?ids={airport}&format=raw&hours={past_n_hour}&taf=off&layout=off"
    r=requests.get(url, headers=headers)
    soup1 = BeautifulSoup(r.content, 'html5lib')
    res_list = soup1.findAll('code')
    res_list = list(map(lambda x:x.text, res_list))
    return res_list


def get_TAF(airport:str):
    """
    Get the  for specific airport.
    """
    assert isinstance(airport, str)
    url = f"http://aviationweather.gov/metar/data?ids={airport}&format=raw&hours=0&taf=on&layout=off"
    r=requests.get(url, headers=headers)
    soup1 = BeautifulSoup(r.content, 'html5lib')
    res_list = soup1.findAll('code')
    res_list = list(map(lambda x:x.text, res_list))
    res = res_list[-1]  # TAF is the last
    return res.replace(u'\xa0','\n')


class Airport(object):
    def __init__(self) -> None:
        pass


