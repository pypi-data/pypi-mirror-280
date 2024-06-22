import os
import re
try:
    # py3
    import configparser
except ImportError:
    # py2
    import ConfigParser as configparser # type: ignore

class ReadConfigError(Exception):
    """ errors for read_configs"""

def read_configs(profile=None):
    # We return all these values
    config = {'email': None, 'key': None, 'token': None, 'base_url': None, 'profile': None}

    # envioronment variables override config files - so setup first
    config['email'] = os.getenv('API_EMAIL')
    config['key'] = os.getenv('API_KEY')
    config['token'] = os.getenv('API_TOKEN')
    config['base_url'] = os.getenv('API_URL')

    config['global_request_timeout'] = os.getenv('API_GLOBAL_REQUEST_TIMEOUT')
    config['max_request_retries'] = os.getenv('API_MAX_REQUEST_RETRIES')
    config['http_headers'] = os.getenv('API_HTTP_HEADERS')

    # grab values from config files
    cp = configparser.ConfigParser()
    try:
        cp.read([
            '.apibase.cfg',
            os.path.expanduser('~/.apibase.cfg'),
            os.path.expanduser('~/.apibase/apibase.cfg')
        ])
    except OSError:
        raise ReadConfigError("%s: configuration file error" % ('.apibase.cfg')) from None

    if len(cp.sections()) == 0 and profile is not None and len(profile) > 0:
        # no config file and yet a config name provided - not acceptable!
        raise ReadConfigError("%s: configuration section provided however config file missing" % (profile)) from None

    if profile is None:
        profile = "ApiBase"

    config['profile'] = profile

    if len(profile) > 0 and len(cp.sections()) > 0:
        # we have a configuration file - lets use it

        if not cp.has_section(profile):
            raise ReadConfigError("%s: configuration section missing - configuration file only has these sections: %s" % (profile, ','.join(cp.sections()))) from None

        for option in ['email', 'key', 'token', 'base_url', 'global_request_timeout', 'max_request_retries', 'http_headers']:
            try:
                config_value = cp.get(profile, option)
                if option == 'extras':
                    # we join all values together as one space seperated strings
                    config[option] = re.sub(r"\s+", ' ', config_value)
                elif option == 'http_headers':
                    # we keep lines as is for now
                    config[option] = config_value
                else:
                    config[option] = re.sub(r"\s+", '', config_value)
                if config[option] is None or config[option] == '':
                    config.pop(option)
            except (configparser.NoOptionError, configparser.NoSectionError):
                pass

            # do we have an override for specific calls? (i.e. token.post or email.get etc)
            for method in ['get', 'patch', 'post', 'put', 'delete']:
                option_for_method = option + '.' + method
                try:
                    config_value = cp.get(profile, option_for_method)
                    config[option_for_method] = re.sub(r"\s+", '', config_value)
                    if config[option] is None or config[option] == '':
                        config.pop(option_for_method)
                except (configparser.NoOptionError, configparser.NoSectionError):
                    pass

    # do any final cleanup - only needed for extras and http_headers (which are multiline)
    if 'extras' in config and config['extras'] is not None:
        config['extras'] = config['extras'].strip().split(' ')
    if 'http_headers' in config and config['http_headers'] is not None:
        config['http_headers'] = [h for h in config['http_headers'].split('\n') if len(h) > 0]
        for h in config['http_headers']:
            try:
                t, v = h.split(':', 1)
            except ValueError:
                # clearly a bad header syntax
                raise ReadConfigError('%s: header syntax error' % (h)) from None
            if len(t.strip()) == 0:
                raise ReadConfigError('%s: header syntax error' % (h)) from None

    # remove blank entries
    for x in sorted(config.keys()):
        if config[x] is None or config[x] == '':
            try:
                config.pop(x)
            except KeyError:
                pass

    return config
