#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Manage users via the API Connector.
"""

from __future__ import annotations
from meerschaum.utils.typing import Optional, Any, List, SuccessTuple

def get_users(
        self,
        debug : bool = False,
        **kw : Any
    ) -> List[str]:
    """

    Parameters
    ----------
    debug : bool :
         (Default value = False)
    **kw : Any :
        

    Returns
    -------
    type
        

    """
    from meerschaum.config.static import _static_config
    import json
    response = self.get(
        f"{_static_config()['api']['endpoints']['users']}",
        debug = debug,
        use_token = False
    )
    if not response:
        return []
    try:
        return response.json()
    except Exception as e:
        return []

def edit_user(
        self,
        user : 'meerschaum._internal.User.User',
        debug : bool = False,
        **kw : Any
    ) -> SuccessTuple:
    """Edit an existing user.

    Parameters
    ----------
    user : 'meerschaum._internal.User.User' :
        
    debug : bool :
         (Default value = False)
    **kw : Any :
        

    Returns
    -------

    """
    import json
    from meerschaum.config.static import _static_config
    r_url = f"{_static_config()['api']['endpoints']['users']}/{user.username}/edit"
    params = {
        'password' : user.password,
        'email' : user.email,
        'attributes' : user.attributes,
    }
    response = self.post(r_url, json=user.attributes, params=params, debug=debug)
    try:
        _json = json.loads(response.text)
        if isinstance(_json, dict) and 'detail' in _json:
            return False, _json['detail']
        success_tuple = tuple(_json)
    except:
        msg = response.text if response else f"Failed to edit user '{user}'."
        return False, msg

    return tuple(success_tuple)

def register_user(
        self,
        user : 'meerschaum._internal.User.User',
        debug : bool = False,
        **kw : Any
    ) -> SuccessTuple:
    """Register a new user.

    Parameters
    ----------
    user : 'meerschaum._internal.User.User' :
        
    debug : bool :
         (Default value = False)
    **kw : Any :
        

    Returns
    -------

    """
    import json
    from meerschaum.config.static import _static_config
    r_url = f"{_static_config()['api']['endpoints']['users']}/{user.username}/register"
    params = {
        'password' : user.password,
        'email' : user.email,
        'attributes' : user.attributes,
    }
    response = self.post(r_url, json=user.attributes, params=params, debug=debug)
    try:
        _json = json.loads(response.text)
        if isinstance(_json, dict) and 'detail' in _json:
            return False, _json['detail']
        success_tuple = tuple(_json)
    except Exception:
        msg = response.text if response else f"Failed to register user '{user}'"
        return False, msg

    return tuple(success_tuple)
    
def get_user_id(
        self,
        user : 'meerschaum._internal.User.User',
        debug : bool = False,
        **kw
    ) -> Optional[int]:
    """Get a user's ID.

    Parameters
    ----------
    user : 'meerschaum._internal.User.User' :
        
    debug : bool :
         (Default value = False)
    **kw :
        

    Returns
    -------

    """
    from meerschaum.config.static import _static_config
    import json
    r_url = f"{_static_config()['api']['endpoints']['users']}/{user.username}/id"
    response = self.get(r_url, debug=debug, **kw)
    try:
        user_id = int(json.loads(response.text))
    except Exception as e:
        user_id = None
    return user_id

def delete_user(
        self,
        user : 'meerschaum._internal.User.User',
        debug : bool = False,
        **kw
    ) -> SuccessTuple:
    """Delete a user.

    Parameters
    ----------
    user : 'meerschaum._internal.User.User' :
        
    debug : bool :
         (Default value = False)
    **kw :
        

    Returns
    -------

    """
    from meerschaum.config.static import _static_config
    import json
    r_url = f"{_static_config()['api']['endpoints']['users']}/{user.username}"
    response = self.delete(r_url, debug=debug)
    try:
        _json = json.loads(response.text)
        if isinstance(_json, dict) and 'detail' in _json:
            return False, _json['detail']
        success_tuple = tuple(_json)
    except Exception as e:
        success_tuple = False, f"Failed to delete user '{user.username}'."
    return success_tuple

def get_user_attributes(
        self,
        user : 'meerschaum._internal.User.User',
        debug : bool = False,
        **kw
    ) -> int:
    """Get a user's attributes.

    Parameters
    ----------
    user : 'meerschaum._internal.User.User' :
        
    debug : bool :
         (Default value = False)
    **kw :
        

    Returns
    -------

    """
    from meerschaum.config.static import _static_config
    import json
    r_url = f"{_static_config()['api']['endpoints']['users']}/{user.username}/attributes"
    response = self.get(r_url, debug=debug, **kw)
    try:
        attributes = json.loads(response.text)
    except Exception as e:
        attributes = None
    return attributes

#############################
# Chaining functions below. #
#############################

def get_user_password_hash(
        self,
        user : 'meerschaum._internal.User.User',
        debug : bool = False,
        **kw
    ) -> Optional[str]:
    """If configured, get a user's password hash.

    Parameters
    ----------
    user : 'meerschaum._internal.User.User' :
        
    debug : bool :
         (Default value = False)
    **kw :
        

    Returns
    -------

    """
    from meerschaum.config.static import _static_config
    r_url = _static_config()['api']['endpoints']['users'] + '/' + user.username + '/password_hash'
    response = self.get(r_url, debug=debug, **kw)
    if not response:
        return None
    return response.json()

def get_user_type(
        self,
        user : 'meerschaum._internal.User.User',
        debug : bool = False,
        **kw
    ) -> Optional[str]:
    """If configured, get a user's type.

    Parameters
    ----------
    user : 'meerschaum._internal.User.User' :
        
    debug : bool :
         (Default value = False)
    **kw :
        

    Returns
    -------

    """
    from meerschaum.config.static import _static_config
    r_url = _static_config()['api']['endpoints']['users'] + '/' + user.username + '/type'
    response = self.get(r_url, debug=debug, **kw)
    if not response:
        return None
    return response.json()
