import urllib2
import logging
import os

logger = logging.getLogger("syncsketchGUI")

DEFAULT = "https://www.syncsketch.com"
ENV_VAR = "SYNCSKETCH_URL"

def _get_env_or_default_url(env_var, default):
    try:
        url = os.environ[env_var]
        urllib2.urlopen(url)

    except KeyError:
        logger.info(
            "Environment Variable [{}] for Host URL not found. Using default URL: {}".format(env_var, default))
        url = default
    
    except ValueError as err:
        logger.warning(
            "URL set in env variable [{}] not valid: '{}'. Using default URL {}".format(env_var, err, default))
        url = default
    
    except urllib2.URLError as err:
        logger.warning(
            "Cannot reach URL set in env variable [{}: {}]: '{}'. Using default URL {}".format(env_var, url, err.reason, default))
        url = default
    
    else:
        logger.info("Using URL [{}] defined in env var [{}]".format(url, env_var))
    
    return url


_BASE = _get_env_or_default_url(ENV_VAR, DEFAULT)



def build_abs(path):
    '''
    Build an absolute URL using the configured API HOST URL and the provided path
    '''
    return urllib2.urlparse.urljoin(_BASE, path)


