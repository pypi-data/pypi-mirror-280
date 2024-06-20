""" atlassible/src/atlassible/myself.py

object with information about me, the user 
"""

import logging

logger = logging.getLogger(__name__)

from atlassible import atl_rest_url
from atlassible.atl_utils import get_resource

EXPAND_ALL = "groups,applicationRoles"


def get_me(expand: str = None) -> object:
    url = atl_rest_url + "myself"
    if expand:
        if expand == 'all':
            url += f"?expand={EXPAND_ALL}"
        else:
            url += f"?expand={expand}"
    _, me = get_resource(url)
    return me


## end of file
