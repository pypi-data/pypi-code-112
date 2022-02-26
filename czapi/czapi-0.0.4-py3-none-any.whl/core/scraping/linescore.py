# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_linescore.ipynb (unless otherwise specified).

__all__ = ['get_boxscore', 'get_full_boxscore']

# Cell

from .base import make_soup
from .constants import BOXSCORE_KWARGS, LINESCORE_SOUP_TYPE, BOXSCORE_SOUP_TYPE
from .event import get_event_name,get_event_date, get_url, _get_event_name, _get_event_date
from bs4 import BeautifulSoup, Tag
from collections import defaultdict
from typing import List, Union, Optional
from hashlib import sha256

# Internal Cell
def generate_dict_from_table(

    table : Tag

)->Union[dict,defaultdict]:
    """Helper function for returning the curling boxscore from a bs4 Tag object."""
    d = defaultdict(list)
    team = None

    # TODO : add error handling for when no table is passed / None

    if table is None:
        raise ValueError('Table tag is NoneType.')

    # loop through tags in table
    for tag in table.find_all('td'):
        if tag.attrs.get('class') == ['linescoreteam']:
            team = tag.a.string
            d[team] = defaultdict(list)
            d[team]['href'] = tag.a['href']
        elif tag.attrs.get('class') == ['linescorehammer']:
            d[team]['hammer'] = not bool(tag.string) # opposite for some reason
        elif tag.attrs.get('class') == ['linescoreend']:
            d[team]['score'].append(tag.string.strip())
        elif tag.attrs.get('class') == ['linescorefinal']:
            d[team]['finalscore'] = tag.b.string.strip()

    return d

# Internal Cell

def get_boxscore_from_table(

    table : Tag

)->Union[dict,defaultdict]:
    """Wraps generate_dict_from_table for clarity / error handling."""
    try:
        return generate_dict_from_table(table = table)

    except ValueError as e:
        # TODO : change return value based on what makes sense for the API
        return {}

def get_boxscore_from_game_id(

     cz_game_id : str
    ,**request_kwargs
)->Union[dict,defaultdict]:
    """Returns a curling boxscore (dict) based on the cz_game_id."""

    url = 'https://www.curlingzone.com/game.php?1=1&showgameid=%s#1'%cz_game_id
    soup = make_soup(url=url,**request_kwargs)
    return _get_boxscore_from_game_id(soup=soup)

def _get_boxscore_from_game_id(

    soup : BeautifulSoup

)->Union[dict,defaultdict]:

    table = soup.find(**BOXSCORE_KWARGS)

    try:
        return get_boxscore_from_table(table=table)

    except ValueError as e:
        return {}


# Internal Cell

def get_table_from_index(

     tables : List[Tag]
    ,game_number : int

)->Tag:
    """Returns a 'table' Tag object from a list of 'table' Tag objects. This helper function allows for 1 indexing instead of 0."""
    # TODO confirm this is the kind of error handling we want
    if game_number < 1 :
        raise ValueError('Table number must be greater than 0.')

    game_idx = game_number -1

    try:
        return tables[game_idx]
    except IndexError as e:
        raise IndexError(". ".join([str(e),"Are you sure that game number is valid?"]))

def get_boxscore_from_event_draw_game_number(

     cz_event_id : Union[str,int]
    ,cz_draw_id : int
    ,game_number : int
    ,**request_kwargs
)->Union[dict,defaultdict]:
    """Returns a curling boxscore (dict) based on the cz_event_id, cz_draw_id and game_number."""
    url = 'https://curlingzone.com/event.php?eventid=%s&view=Scores&showdrawid=%s#1'%(cz_event_id,cz_draw_id)
    soup = make_soup(url=url,**request_kwargs)

    return _get_boxscore_from_event_draw_game_number(soup=soup,game_number = game_number)



def _get_boxscore_from_event_draw_game_number(

     soup : BeautifulSoup
    ,game_number : int

)->Union[dict,defaultdict]:
    tables = soup.find_all(**BOXSCORE_KWARGS)
    try:
        table = get_table_from_index(tables = tables, game_number = game_number)
        return get_boxscore_from_table(table = table)

    except IndexError as e:
        return {}

    except ValueError as e:
        return {}


# Internal Cell
def _get_boxscore(

     soup : BeautifulSoup
    ,soup_type : str
    ,**game_kwargs

)->Union[dict,defaultdict]:

    soup_type = soup_type.lower()

    if soup_type == LINESCORE_SOUP_TYPE:
        return _get_boxscore_from_event_draw_game_number(soup=soup,**game_kwargs)
    elif soup_type == BOXSCORE_SOUP_TYPE:
        return _get_boxscore_from_game_id(soup=soup,**game_kwargs)
    else:
        raise NotImplementedError("%s soup type is not implemented."%soup_type)

# Cell
def get_boxscore(

     cz_event_id : Optional[Union[str,int]] = None
    ,cz_draw_id : Optional[int] = None
    ,game_number : Optional[int] = None
    ,cz_game_id : Optional[Union[str,str]] = None
    ,**request_kwargs
)->defaultdict:
    """Returns a curling boxscore (dict) based on the cz_event_id, cz_draw_id and game_number or the cz_game_id.
       Not recommended for use as it makes too many get requests (slow). Use get_full_boxscore instead.

    """

    option_1 = [cz_event_id, cz_draw_id,game_number]
    option_2 = cz_game_id

    if all([all(option_1), option_2]) or not any([all(option_1),option_2]):
        raise ValueError("One combination of cz_event_id, cz_draw_id and game_number or cz_game_id must be non NoneType.")

    if all(option_1):
        return get_boxscore_from_event_draw_game_number(cz_event_id = cz_event_id,cz_draw_id = cz_draw_id, game_number = game_number, **request_kwargs)
    else:
        return get_boxscore_from_game_id(cz_game_id)

# Cell
def _get_full_boxscore(
     cz_event_id : Optional[Union[str,int]] = None
    ,cz_draw_id : Optional[int] = None
    ,game_number : Optional[int] = None
    ,cz_game_id : Optional[Union[str,int]] = None
    ,**request_kwargs

)->dict:
    """
        Returns a curling boxscore (dict) with data hash based on the cz_event_id, cz_draw_id and game_number or the cz_game_id.
        Depreciated since this makes too many get requests (slow).
    """

    # seems like redundant get requests - can probably be cut down - future development
    event = get_event_name(cz_event_id = cz_event_id, cz_game_id = cz_game_id, **request_kwargs)
    date = get_event_date(cz_event_id = cz_event_id, cz_game_id = cz_game_id, **request_kwargs)
    boxscore = get_boxscore(cz_event_id = cz_event_id, cz_draw_id = cz_draw_id, game_number = game_number, cz_game_id = cz_game_id, **request_kwargs)


    _hash = sha256(str(boxscore).encode('utf-8')).hexdigest()

    return {d[0]:{**d[-1],'date':date,'event':event,'hash':_hash} for d in boxscore.items()}


def get_full_boxscore(

     cz_event_id : Optional[Union[str,int]] = None
    ,cz_draw_id : Optional[int] = None
    ,game_number : Optional[int] = None
    ,cz_game_id : Optional[Union[str,int]] = None
    ,**request_kwargs


)->dict:
    """
        Returns a curling boxscore (dict) with data hash based on the cz_event_id, cz_draw_id and game_number or the cz_game_id.
        get_full_boxscore limits the number of get_requests that are made to the CurlingZone site.
    """

    option_1 = [cz_event_id, cz_draw_id,game_number]
    option_2 = cz_game_id

    if all([all(option_1), option_2]) or not any([all(option_1),option_2]):
        raise ValueError("One combination of cz_event_id, cz_draw_id and game_number or cz_game_id must be non NoneType.")

    if all(option_1):
        soup_type = LINESCORE_SOUP_TYPE
        url_kwargs = {
             'cz_event_id' : cz_event_id
            ,'cz_draw_id' : cz_draw_id
        }
        game_kwargs = {
            'game_number' : game_number
        }
    else:
        soup_type = BOXSCORE_SOUP_TYPE
        url_kwargs = {
            'cz_game_id' : cz_game_id
        }
        game_kwargs = {}


    url = get_url(soup_type = soup_type, **url_kwargs)
    soup = make_soup(url=url,**request_kwargs)

    event = _get_event_name(soup=soup,soup_type = soup_type)
    date = _get_event_date(soup=soup,soup_type = soup_type)
    boxscore = _get_boxscore(soup=soup,soup_type=soup_type,**game_kwargs)

    # will utf-8 always work?
    _hash = sha256(str(boxscore).encode('utf-8')).hexdigest()

    return {d[0]:{**d[-1],'date':date,'event':event,'hash':_hash} for d in boxscore.items()}

