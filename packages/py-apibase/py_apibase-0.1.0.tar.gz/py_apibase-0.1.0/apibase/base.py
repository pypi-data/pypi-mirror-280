import json
import keyword

from .logging_helper import Logger
from .network import APINetwork
from .utils import user_agent, build_curl
from .exceptions import APIError, NetworkError


DEFAULT_GLOBAL_REQUEST_TIMEOUT = 5
DEFAULT_MAX_REQUEST_RETRIES = 5


class ApiBase():

    class _ApiBase():
        """ :meta private: """

        def __init__(self, config):
            """ :meta private: """

            self.network = None
            self.config = config

            # username, password
            self.username = config['username'] if 'username' in config else None
            self.password = config['password'] if 'password' in config else None
            self.api_key = config['key'] if 'key' in config else None
            self.api_token = config['token'] if 'token' in config else None

            # We must have a base_url value
            self.base_url = config['base_url']

            self.raw = config['raw']
            self.use_sessions = config['use_sessions']
            self.global_request_timeout = config['global_request_timeout'] if 'global_request_timeout' in config else DEFAULT_GLOBAL_REQUEST_TIMEOUT
            self.max_request_retries = config['max_request_retries'] if 'max_request_retries' in config else DEFAULT_MAX_REQUEST_RETRIES
            
            self.method_maps = config['method_maps']

            try:
                self.global_request_timeout = int(self.global_request_timeout)
            except (TypeError, ValueError):
                self.global_request_timeout = DEFAULT_GLOBAL_REQUEST_TIMEOUT
            try:
                self.max_request_retries = int(self.max_request_retries)
            except (TypeError, ValueError):
                self.max_request_retries = DEFAULT_MAX_REQUEST_RETRIES
            self.additional_http_headers = config['http_headers'] if 'http_headers' in config else None
            self.profile = config['profile']

            self.network = APINetwork(
                use_sessions=self.use_sessions,
                global_request_timeout=self.global_request_timeout,
                max_request_retries=self.max_request_retries
            )
            self.user_agent = user_agent()

            self.logger = Logger(config['debug']).getLogger() if 'debug' in config and config['debug'] else None

        def __del__(self):
            if self.network:
                del self.network
                self.network = None

        def _add_headers(self, method, data, files, content_type=None):
            """ Add default headers """
            self.headers = {}
            self.headers['User-Agent'] = self.user_agent
            if method == 'GET':
                # no content type needed - except we throw in a default just for grin's
                self.headers['Content-Type'] = 'application/json'
            elif content_type is not None and method in content_type:
                # this api endpoint and this method requires a specific content type.
                ct = content_type[method]
                if isinstance(ct, list):
                    # How do we choose from more than one content type?
                    found = False
                    for t in ct:
                        # we have to match against the data type - arggg!
                        if 'application/octet-stream' == t and isinstance(data, (bytes,bytearray)):
                            self.headers['Content-Type'] = t
                            found = True
                            break
                        if 'application/json' == t and isinstance(data, (list,dict)):
                            self.headers['Content-Type'] = t
                            found = True
                            break
                        if 'application/javascript' == t and isinstance(data, str):
                            self.headers['Content-Type'] = t
                            found = True
                            break
                    if not found:
                        # punt - pick first - we can't do anything else!
                        self.headers['Content-Type'] = ct[0]
                else:
                    self.headers['Content-Type'] = ct
            else:
                # default choice
                self.headers['Content-Type'] = 'application/json'

            # now adjust Content-Type based on data and files
            if method != 'GET':
                if self.headers['Content-Type'] == 'application/json' and isinstance(data, str):
                    # passing javascript vs JSON
                    self.headers['Content-Type'] = 'application/javascript'
                if self.headers['Content-Type'] == 'application/json' and isinstance(data, (bytes,bytearray)):
                    # passing binary file vs JSON
                    self.headers['Content-Type'] = 'application/octet-stream'
                if data and len(data) > 0 and self.headers['Content-Type'] == 'multipart/form-data':
                    # convert from params to files (i.e multipart/form-data)
                    if files is None:
                        files = set()
                    for k,v in data.items():
                        if isinstance(v, (dict, list)):
                            files.add((k, (None, json.dumps(v), 'application/json')))
                        else:
                            files.add((k, (None, v)))
                    # we have replaced data's values into files
                    data = None
                if data is not None and len(data) == 0:
                    data = None
                if files is not None and len(files) == 0:
                    files = None
                if data is None and files is None and self.headers['Content-Type'] == 'multipart/form-data':
                    # can't have zero length multipart/form-data and as there's no data or files; we don't need it
                    del self.headers['Content-Type']
                if files:
                    # overwrite Content-Type as we are uploading data
                    self.headers['Content-Type'] = 'multipart/form-data'
                    # however something isn't right and this works ... look at again later!
                    del self.headers['Content-Type']
            if self.additional_http_headers:
                for h in self.additional_http_headers:
                    t, v = h.split(':', 1)
                    t = t.strip()
                    v = v.strip()
                    if len(v) > 0 and ((v[0] == '"' and v[-1] == '"') or (v[0] == "'" and v[-1] == "'")):
                        v = v[1:-1]
                    self.headers[t] = v
            return data, files

        def _add_auth_headers(self, method):
            """ Add authentication headers """

            v = 'username' + '.' + method.lower()
            username = self.config[v] if v in self.config else self.username
            v = 'password' + '.' + method.lower()
            password = self.config[v] if v in self.config else self.password
            v = 'key' + '.' + method.lower()
            api_key = self.config[v] if v in self.config else self.api_key
            v = 'token' + '.' + method.lower()
            api_token = self.config[v] if v in self.config else self.api_token

            if username is None and api_key is None and api_token is None:
                if self.logger:
                    self.logger.debug('neither username/key or token defined')
                raise APIError(0, 'neither username/key or token defined')


            #if username is not None and api_key is None and api_token is None:
            #    if self.logger:
            #        self.logger.debug('email defined however neither key or token defined')
            #    raise APIError(0, 'email defined however neither key or token defined')

            # We know at this point that at-least one api_* is set and no confusion!

            if username is None and api_token is not None:
                # post issue-114 - token is used
                self.headers['Authorization'] = 'Bearer %s' % (api_token)
            elif username is None and api_key is not None:
                # pre issue-114 - key is used vs token - backward compat
                self.headers['Authorization'] = 'Bearer %s' % (api_key)
            elif api_key is not None and api_token is not None:
                self.headers['ApiKey'] = api_key
                self.headers['Authorization'] = f"Bearer {api_token}"
            else:
                raise APIError(0, 'coding issue!')

        def _add_certtoken_headers(self, method):
            """ Add authentication headers """

            v = 'certtoken' + '.' + method.lower()
            if v in self.config:
                api_certtoken = self.config[v] # use specific value for this method
            else:
                api_certtoken = self.api_certtoken # use generic value for all methods

            if api_certtoken is None:
                if self.logger:
                    self.logger.debug('no cert token defined')
                raise APIError(0, 'no cert token defined')
            self.headers['X-Auth-User-Service-Key'] = api_certtoken

        def do_not_available(self, method, parts, identifiers, params=None, data=None, files=None, content_type=None):
            # base class simply returns not available - no processing of any arguments
            if self.logger:
                self.logger.debug('call for this method not available')
            raise APIError(0, 'call for this method not available')

        def do_no_auth(self, method, parts, identifiers, params=None, data=None, files=None, content_type=None):
            data, files = self._add_headers(method, data, files, content_type)
            # We decide at this point if we are sending json or string data
            if isinstance(data, (str,bytes,bytearray)):
                return self._call(method, parts, identifiers, params, data, None, files)
            return self._call(method, parts, identifiers, params, None, data, files)

        def do_auth(self, method, parts, identifiers, params=None, data=None, files=None, content_type=None):
            data, files = self._add_headers(method, data, files, content_type)
            self._add_auth_headers(method)
            # We decide at this point if we are sending json or string data
            if isinstance(data, (str,bytes,bytearray)):
                return self._call(method, parts, identifiers, params, data, None, files)
            return self._call(method, parts, identifiers, params, None, data, files)

        def do_auth_unwrapped(self, method, parts, identifiers, params=None, data=None, files=None, content_type=None):
            data, files = self._add_headers(method, data, files, content_type)
            self._add_auth_headers(method)
            # We decide at this point if we are sending json or string data
            if isinstance(data, (str,bytes,bytearray)):
                return self._call_unwrapped(method, parts, identifiers, params, data, None, files)
            return self._call_unwrapped(method, parts, identifiers, params, None, data, files)

        def do_certauth(self, method, parts, identifiers, params=None, data=None, files=None, content_type=None):
            data, files = self._add_headers(method, data, files, content_type)
            self._add_certtoken_headers(method)
            # We decide at this point if we are sending json or string data
            if isinstance(data, (str,bytes,bytearray)):
                return self._call(method, parts, identifiers, params, data, None, files)
            return self._call(method, parts, identifiers, params, None, data, files)

        def _call_network(self, method, headers, parts, identifiers, params, data_str, data_json, files):
            if (method is None) or (parts[0] is None):
                # should never happen
                raise APIError(0, 'You must specify a method and endpoint')

            if len(parts) > 1 and parts[1] is not None or (data_str is not None and method == 'GET'):
                if identifiers[0] is None:
                    raise APIError(0, 'You must specify first identifier')
                if identifiers[1] is None:
                    url = (self.base_url + '/'
                           + parts[0] + '/'
                           + str(identifiers[0]) + '/'
                           + parts[1])
                else:
                    url = (self.base_url + '/'
                           + parts[0] + '/'
                           + str(identifiers[0]) + '/'
                           + parts[1] + '/'
                           + str(identifiers[1]))
            else:
                if identifiers[0] is None:
                    url = (self.base_url + '/'
                           + parts[0])
                else:
                    url = (self.base_url + '/'
                           + parts[0] + '/'
                           + str(identifiers[0]))

            if len(parts) > 2 and parts[2]:
                url += '/' + parts[2]
                if identifiers[2]:
                    url += '/' + str(identifiers[2])
                if len(parts) > 3 and parts[3]:
                    url += '/' + parts[3]
                    if identifiers[3]:
                        url += '/' + str(identifiers[3])
                    if len(parts) > 4 and parts[4]:
                        url += '/' + parts[4]

            if self.method_maps.get(method) is not None:
                url += '/' + self.method_maps[method]

            if self.logger:
                msg = build_curl(method, url, headers, params, data_str, data_json, files)
                self.logger.debug('Call: emulated curl command ...\n%s', msg)

            try:
                response = self.network(method, url, headers, params, data_str, data_json, files)
            except NetworkError as e:
                if self.logger:
                    self.logger.debug('Call: network error: %s', e)
                raise APIError(0, str(e)) from None
            except Exception as e:
                if self.logger:
                    self.logger.debug('Call: network exception! %s', e)
                raise APIError(0, 'network exception: %s' % (e)) from None

            # Create response_{type|code|data}
            try:
                response_type = response.headers['Content-Type']
                if ';' in response_type:
                    # remove the ;paramaters part (like charset=, etc.)
                    response_type = response_type[0:response_type.rfind(';')]
                response_type = response_type.strip().lower()
            except KeyError:
                # API should always response; but if it doesn't; here's the default
                response_type = 'application/octet-stream'
            response_code = response.status_code
            response_data = response.content
            if not isinstance(response_data, (str, bytes, bytearray)):
                # the more I think about it; then less likely this will ever be called
                try:
                    response_data = response_data.decode('utf-8')
                except UnicodeDecodeError:
                    pass

            if self.logger:
                if 'text/' == response_type[0:5] or response_type in ['application/javascript', 'application/json']:
                    if len(response_data) > 180:
                        self.logger.debug('Response: %d, %s, %s...', response_code, response_type, response_data[0:180])
                    else:
                        self.logger.debug('Response: %d, %s, %s', response_code, response_type, response_data)
                else:
                    self.logger.debug('Response: %d, %s, %s', response_code, response_type, '...')

            if response_code == 429:
                # 429 Too Many Requests
                # The HTTP 429 Too Many Requests response status code indicates the user
                # has sent too many requests in a given amount of time ("rate limiting").
                # A Retry-After header might be included to this response indicating how
                # long to wait before making a new request.
                try:
                    retry_after = response.headers['Retry-After']
                except (KeyError,IndexError):
                    retry_after = ''
                # XXX/TODO no processing for now - but could try again within library
                if self.logger:
                    self.logger.debug('Response: 429 Header Retry-After: %s', retry_after)

            # if response_code in [400,401,403,404,405,412,500]:
            if 400 <= response_code <= 499 or response_code == 500:
                # The /certificates API call insists on a 500 error return and yet has valid error data
                # Other API calls can return 400 or 4xx with valid response data
                # lets check and convert if able
                try:
                    j = json.loads(response_data)
                    if len(j) == 2 and 'code' in j and 'error' in j:
                        # This is an incorrect response from the API (happens on 404's) - but we can handle it cleanly here
                        # {\n  "code": 1000,\n  "error": "not_found"\n}
                        response_data = '{"errors": [{"code": %d, "message": "%s"}], "success": false, "result": null}' % (j['code'], j['error'])
                        response_data = response_data.encode()
                        response_code = 200
                    elif 'success' in j and 'errors' in j:
                        # yippe - try to continue by allowing to process fully
                        response_code = 200
                    else:
                        pass
                except (ValueError, json.decoder.JSONDecodeError):
                    # ignore - maybe a real error that's not json, let proceed!
                    pass

            if 500 <= response_code <= 599:
                # 500 Internal Server Error
                # 501 Not Implemented
                # 502 Bad Gateway
                # 503 Service Unavailable
                # 504 Gateway Timeout
                # 505 HTTP Version Not Supported
                # 506 Variant Also Negotiates
                # 507 Insufficient Storage
                # 508 Loop Detected
                # 509 Unassigned
                # 510 Not Extended
                # 511 Network Authentication Required

                # the libary doesn't deal with these errors, just pass upwards!
                # there's no value to add and the returned data is questionable or not useful
                response.raise_for_status()

                # should not be reached
                raise APIError(0, 'internal error in status code processing')

            # if 400 <= response_code <= 499:
            #    # 400 Bad Request
            #    # 401 Unauthorized
            #    # 403 Forbidden
            #    # 405 Method Not Allowed
            #    # 415 Unsupported Media Type
            #    # 429 Too many requests
            #
            #    # don't deal with these errors, just pass upwards!
            #    response.raise_for_status()

            # if 300 <= response_code <= 399:
            #    # 304 Not Modified
            #
            #    # don't deal with these errors, just pass upwards!
            #    response.raise_for_status()

            # should be a 200 response at this point

            return [response_type, response_code, response_data]

        def _raw(self, method, headers, parts, identifiers, params, data_str, data_json, files):
            [response_type, response_code, response_data] = self._call_network(method,
                                                                               headers, parts,
                                                                               identifiers,
                                                                               params, data_str, data_json, files)

            # API can return HTTP code OK, CREATED, ACCEPTED, or NO-CONTENT - all of which are a-ok.
            if response_code not in [200, 201, 202, 204]:
                # 3xx & 4xx errors (5xx's handled above)
                response_data = {'success': False,
                                 'errors': [{'code': response_code, 'message':'HTTP response code %d' % response_code}],
                                 'result': str(response_data)}

                # it would be nice to return the error code and content type values; but not quite yet
                return response_data

            if response_type == 'application/json':
                # API says it's JSON; so it better be parsable as JSON
                # NDJSON is returned by Enterprise Log Share i.e. /zones/:id/logs/received
                if hasattr(response_data, 'decode'):
                    try:
                        response_data = response_data.decode('utf-8')
                    except UnicodeDecodeError:
                        # clearly not a string that can be decoded!
                        if self.logger:
                            self.logger.debug('Response: decode(utf-8) failed, reverting to binary response')
                        # return binary
                        return {'success': True, 'result': response_data}
                try:
                    if response_data == '':
                        # This should really be 'null' but it isn't. Even then, it's wrong!
                        response_data = None
                    else:
                        response_data = json.loads(response_data)
                except (ValueError,json.decoder.JSONDecodeError):
                    # Lets see if it's NDJSON data
                    # NDJSON is a series of JSON elements with newlines between each element
                    try:
                        r = []
                        for line in response_data.splitlines():
                            r.append(json.loads(line))
                        response_data = r
                    except (ValueError, json.decoder.JSONDecodeError):
                        # While this should not happen; it's always possible
                        if self.logger:
                            self.logger.debug('Response data not JSON: %r', response_data)
                        raise APIError(0, 'JSON parse failed.') from None                
                
                return response_data

            if response_type in ['text/plain', 'application/octet-stream']:
                # API says it's text; but maybe it's actually JSON? - should be fixed in API
                if hasattr(response_data, 'decode'):
                    try:
                        response_data = response_data.decode('utf-8')
                    except UnicodeDecodeError:
                        # clearly not a string that can be decoded!
                        if self.logger:
                            self.logger.debug('Response: decode(utf-8) failed, reverting to binary response')
                        # return binary
                        return {'success': True, 'result': response_data}
                try:
                    if response_data == '':
                        # This should really be 'null' but it isn't. Even then, it's wrong!
                        response_data = None
                    else:
                        response_data = json.loads(response_data)
                except (ValueError, json.decoder.JSONDecodeError):
                    # So it wasn't JSON - moving on as if it's text!
                    pass
                if isinstance(response_data, dict) and 'success' in response_data:
                    return response_data
                return {'success': True, 'result': response_data}

            if response_type in ['text/javascript', 'application/javascript', 'text/html', 'text/css', 'text/csv']:
                if hasattr(response_data, 'decode'):
                    try:
                        response_data = response_data.decode('utf-8')
                    except UnicodeDecodeError:
                        # clearly not a string that can be decoded!
                        if self.logger:
                            self.logger.debug('Response: decode(utf-8) failed, reverting to binary response')
                        # return binary
                        return {'success': True, 'result': response_data}
                return {'success': True, 'result': str(response_data)}

            if response_type in ['application/pdf', 'application/zip'] or response_type[0:6] in ['audio/', 'image/', 'video/']:
                # it's raw/binary - just pass thru
                return {'success': True, 'result': response_data}

            # Assuming nothing - but continuing anyway as if its a string
            if hasattr(response_data, 'decode'):
                try:
                    response_data = response_data.decode('utf-8')
                except UnicodeDecodeError:
                    # clearly not a string that can be decoded!
                    if self.logger:
                        self.logger.debug('Response: decode(utf-8) failed, reverting to binary response')
                    # return binary
                    return {'success': True, 'result': response_data}
            return {'success': True, 'result': str(response_data)}

        def _call(self, method, parts, identifiers, params, data_str, data_json, files):

            response_data = self._raw(method, self.headers, parts, identifiers, params, data_str, data_json, files)

            if getattr(self, 'process_response', None) is not None:
                response_data =  self.process_response(response_data)

            # Sanatize the returned results - just in case API is messed up
            if 'success' not in response_data:
                # { "data": null, "errors": [ { "message": "request must be a POST", "path": null, "extensions": { "timestamp": "20...
                # XXX/TODO should be retested and aybe recoded/deleted
                if 'errors' in response_data:
                    if response_data['errors'] is None:
                        # Only happens on /graphql call
                        if self.logger:
                            self.logger.debug('Response: assuming success = "True"')
                        response_data['success'] = True
                    else:
                        if self.logger:
                            self.logger.debug('Response: assuming success = "False"')
                        # The following only happens on /graphql call
                        try:
                            message = response_data['errors'][0]['message']
                        except KeyError:
                            message = ''
                        try:
                            location = str(response_data['errors'][0]['location'])
                        except KeyError:
                            location = ''
                        try:
                            path = '>'.join(response_data['errors'][0]['path'])
                        except KeyError:
                            path = ''
                        response_data['errors'] = [{'code': 99999, 'message': message + ' - ' + location + ' - ' + path}]
                        response_data['success'] = False
                else:
                    if 'result' not in response_data:
                        # Only happens on /certificates call
                        # should be fixed in /certificates API
                        # may well be fixed by now
                        if self.logger:
                            self.logger.debug('Response: assuming success = "False"')
                        r = response_data
                        response_data['errors'] = []
                        response_data['errors'].append(r)
                        response_data['success'] = False
                    else:
                        if self.logger:
                            self.logger.debug('Response: assuming success = "True"')
                        response_data['success'] = True

            if response_data['success'] is False:
                if 'errors' in response_data and response_data['errors'] is not None:
                    errors = response_data['errors'][0]
                else:
                    errors = {}
                if 'code' in errors:
                    code = errors['code']
                else:
                    code = 99998
                if 'message' in errors:
                    message = errors['message']
                elif 'error' in errors:
                    message = errors['error']
                else:
                    message = ''
                # if 'messages' in response_data:
                #     errors['error_chain'] = response_data['messages']
                if 'error_chain' in errors:
                    error_chain = errors['error_chain']
                    for error in error_chain:
                        if self.logger:
                            self.logger.debug('Response: error %d %s - chain', error['code'], error['message'])
                    if self.logger:
                        self.logger.debug('Response: error %d %s', code, message)
                    raise APIError(code, message, error_chain)

                if self.logger:
                    self.logger.debug('Response: error %d %s', code, message)
                raise APIError(code, message)

            if self.raw:
                result = {}
                # theres always a result value - unless it's a graphql query
                try:
                    result['result'] = response_data['result']
                except KeyError:
                    result['result'] = response_data
                # theres may not be a result_info on every call
                if 'result_info' in response_data:
                    result['result_info'] = response_data['result_info']
                # no need to return success, errors, or messages as they return via an exception
            else:
                # theres always a result value - unless it's a graphql query
                try:
                    result = response_data['result']
                except KeyError:
                    result = response_data

            if self.logger:
                if isinstance(result, (str, dict, list)):
                    if len(str(result)) > 180:
                        self.logger.debug('Response: %s...', str(result)[0:180].replace('\n', ' '))
                    else:
                        self.logger.debug('Response: %s', str(result).replace('\n', ' '))
                elif isinstance(result, (bytes,bytearray)):
                    self.logger.debug('Response: %s', result[0:180])
                else:
                    self.logger.debug('Response: %s', '...')
            return result

        def _call_unwrapped(self, method, parts, identifiers, params, data_str, data_json, files):
            response_data = self._raw(method, self.headers, parts, identifiers, params, data_str, data_json, files)
            if self.logger:
                self.logger.debug('Response: %s', response_data)
            result = response_data
            return result

        def _read_from_web(self, url):
            try:
                if self.logger:
                    self.logger.debug('Call: doit!')
                response = self.network('GET', url)
                if self.logger:
                    self.logger.debug('Call: done!')
            except Exception as e:
                if self.logger:
                    self.logger.debug('Call: exception! "%s"', e)
                raise APIError(0, 'connection failed.') from None

            return response.text

    class _Base():
        """ :meta private: """

        def __init__(self, base, parts, content_type=None):
            self._base = base
            self._parts = parts
            if content_type:
                self._content_type = content_type
            self._do = self._base.do_not_available

        def __call__(self, identifier1=None, identifier2=None, identifier3=None, identifier4=None, params=None, data=None):
            # This is the same as a get()
            return self.get(identifier1, identifier2, identifier3, identifier4, params=params, data=data)

        def __str__(self):
            return '[' + '/' + '/:id/'.join(self._parts) + ']'

        def __repr__(self):
            return '[' + '/' + '/:id/'.join(self._parts) + ']'

        def get(self, identifier1=None, identifier2=None, identifier3=None, identifier4=None, params=None, data=None):
            try:
                if getattr(self, '_content_type', False):
                    return self._do('GET', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data, self._content_type)
                return self._do('GET', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data)
            except APIError as e:
                raise APIError(e=e) from None

        def patch(self, identifier1=None, identifier2=None, identifier3=None, identifier4=None, params=None, data=None):
            try:
                if getattr(self, '_content_type', False):
                    return self._do('PATCH', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data, self._content_type)
                return self._do('PATCH', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data)
            except APIError as e:
                raise APIError(e=e) from None

        def post(self, identifier1=None, identifier2=None, identifier3=None, identifier4=None, params=None, data=None, files=None):
            try:
                if getattr(self, '_content_type', False):
                    return self._do('POST', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data, files, self._content_type)
                return self._do('POST', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data, files)
            except APIError as e:
                raise APIError(e=e) from None

        def put(self, identifier1=None, identifier2=None, identifier3=None, identifier4=None, params=None, data=None, files=None):
            try:
                if getattr(self, '_content_type', False):
                    return self._do('PUT', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data, files, self._content_type)
                return self._do('PUT', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data, files)
            except APIError as e:
                raise APIError(e=e) from None

        def delete(self, identifier1=None, identifier2=None, identifier3=None, identifier4=None, params=None, data=None):
            try:
                if getattr(self, '_content_type', False):
                    return self._do('DELETE', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data, self._content_type)
                return self._do('DELETE', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data)
            except APIError as e:
                raise APIError(e=e) from None

    class _BaseUnused(_Base):
        """ :meta private: """

        def __init__(self, base, parts, content_type):
            super().__init__(base, parts, content_type)
            self._do = self._base.do_not_available

    class _BaseNoAuth(_Base):
        """ :meta private: """

        def __init__(self, base, parts, content_type):
            super().__init__(base, parts, content_type)
            self._do = self._base.do_no_auth
            self._valid = True

        def patch(self, identifier1=None, identifier2=None, identifier3=None, identifier4=None, params=None, data=None):
            try:
                if getattr(self, '_content_type', False):
                    return self._base.do_not_available('PATCH', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data, self._content_type)
                return self._base.do_not_available('PATCH', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data)
            except APIError as e:
                raise APIError(e=e) from None

        def post(self, identifier1=None, identifier2=None, identifier3=None, identifier4=None, params=None, data=None, files=None):
            try:
                if getattr(self, '_content_type', False):
                    return self._base.do_not_available('POST', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data, files, self._content_type)
                return self._base.do_not_available('POST', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data, files)
            except APIError as e:
                raise APIError(e=e) from None

        def put(self, identifier1=None, identifier2=None, identifier3=None, identifier4=None, params=None, data=None, files=None):
            try:
                if getattr(self, '_content_type', False):
                    return self._base.do_not_available('PUT', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data, self._content_type)
                return self._base.do_not_available('PUT', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data)
            except APIError as e:
                raise APIError(e=e) from None

        def delete(self, identifier1=None, identifier2=None, identifier3=None, identifier4=None, params=None, data=None):
            try:
                if getattr(self, '_content_type', False):
                    return self._base.do_not_available('DELETE', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data, self._content_type)
                return self._base.do_not_available('DELETE', self._parts, [identifier1, identifier2, identifier3, identifier4], params, data)
            except APIError as e:
                raise APIError(e=e) from None

    class _BaseAuth(_Base):
        """ :meta private: """

        def __init__(self, base, parts, content_type):
            super().__init__(base, parts, content_type)
            self._do = self._base.do_auth
            self._valid = True

    class _BaseAuthUnwrapped(_Base):
        """ :meta private: """

        def __init__(self, base, parts, content_type):
            super().__init__(base, parts, content_type)
            self._do = self._base.do_auth_unwrapped
            self._valid = True

    class _CFbaseAuthCert(_Base):
        """ :meta private: """

        def __init__(self, base, parts, content_type):
            super().__init__(base, parts, content_type)
            self._do = self._base.do_certauth
            self._valid = True

    @classmethod
    def sanitize_verb(cls, v):
        """ sanitize_verb """
        # keywords are also changed to have underscore appended so it can used with Python code
        if keyword.iskeyword(v):
            v = v + '_'
        # AI functions introduce '@' symbol - i.e .../@cf/... they are replaced with at_
        if '@' == v[0]:
            v = 'at_' + v[1:]
        # AI functions introduce '.' symbol - i.e 1.0 they are replaced with underscore
        if '.' in v:
            v = v.replace('.','_')
        # dashes (vs underscores) cause issues in Python and other languages. they are replaced with underscores
        if '-' in v:
            v = v.replace('-','_')
        return v

    def add_carefully(self, t, *parts, content_type=None):
        """ add_carefully()
        """
        self.add(t, parts, content_type, auto=False)

    def add(self, t, *parts, content_type=None, auto=True):
        """ add()

        :param t: type of API call.
        :param p1: part1 of API call.
        :param p2: part1 of API call.
        :param p3: part1 of API call.
        :param p4: part1 of API call.
        :param p5: part1 of API call.
        :param content_type: optional value for the HTTP Content-Type for an API call.

        add() is the core fuction that creates a new API endpoint that can be called later on.
        """

        api_sections = []
        for p in parts:
            api_sections += p.split('/')

        branch = self
        for api_part in api_sections[0:-1]:
            try:
                branch = getattr(branch, ApiBase.sanitize_verb(api_part))
            except AttributeError:
                # missing path - should never happen unless api_v4 is a busted file or add_all() used
                if not auto:
                    raise APIError(0, 'api load: api_part **%s** missing when adding path /%s' % (api_part, '/'.join(api_sections))) from None
                # create intermediate path as required
                f = self._CFbaseUnused(self._base, parts, content_type=None)
                setattr(branch, ApiBase.sanitize_verb(api_part), f)
                branch = getattr(branch, ApiBase.sanitize_verb(api_part))

        api_part = api_sections[-1]
        try:
            branch = getattr(branch, ApiBase.sanitize_verb(api_part))
            # we only are here becuase the name already exists - don't let it overwrite - should never happen unless api_v4 is a busted file
            raise APIError(0, 'api load: duplicate api_part found: %s/**%s**' % ('/'.join(api_sections[0:-1]), api_part))
        except AttributeError:
            # this is the required behavior - i.e. it's a new node to create
            pass

        if t == 'VOID':
            f = self._BaseUnused(self._base, parts, content_type=None)
        elif t == 'OPEN':
            f = self._BaseNoAuth(self._base, parts, content_type=content_type)
        elif t == 'AUTH':
            f = self._BaseAuth(self._base, parts, content_type=content_type)
        else:
            # should never happen
            raise APIError(0, 'api load type mismatch')

        setattr(branch, ApiBase.sanitize_verb(api_part), f)

    def find(self, cmd):
        """ find()

        :param cmd: API in slash format
        :return: fuction to call for that API

        You can use this call to convert a string API command into the actual function call
        """
        m = self
        for verb in cmd.split('/'):
            if verb == '' or verb[0] == ':':
                continue
            try:
                m = getattr(m, ApiBase.sanitize_verb(verb))
            except AttributeError:
                raise AttributeError('%s: not found' % (verb)) from None
        return m

    def api_list(self):
        """ api_list()

        :return: list of API calls

        A recursive walk of the api tree returning a list of api calls
        """
        return self._api_list(m=self)

    def _api_list(self, m=None, s=''):
        """ :meta private: """
        w = []
        for n in sorted(dir(m)):
            if n[0] == '_':
                # internal
                continue
            if n in ['delete', 'get', 'patch', 'post', 'put']:
                # gone too far
                continue
            try:
                a = getattr(m, n)
            except AttributeError:
                # really should not happen!
                raise APIError(0, '%s: not found - should not happen' % (n)) from None
            d = dir(a)
            if '_base' not in d:
                continue
            # it's a known api call - lets show the result and continue down the tree
            if '_parts' in d and '_valid' in d:
                if 'delete' in d or 'get' in d or 'patch' in d or 'post' in d or 'put' in d:
                    # only show the result if a call exists for this part
                    if n[-1] == '_':
                        if keyword.iskeyword(n[:-1]):
                            # should always be a keyword - but now nothing needs to be done
                            pass
                        # remove the extra keyword postfix'ed with underscore
                        w.append(str(a)[1:-1])
                    else:
                        # handle underscores by returning the actual API call vs the method name
                        w.append(str(a)[1:-1])
            # now recurse downwards into the tree
            w = w + self._api_list(a, s + '/' + n)
        return w

    def api_from_openapi(self, url=None):
        """ api_from_openapi()

        :param url: OpenAPI URL or None if you use the built official URL

        """

        return self._base.api_from_openapi(url)    

    def __del__(self):
        """ :meta private: """

        if self._base:
            del self._base
            self._base = None

    def __call__(self):
        """ :meta private: """

        raise TypeError('object is not callable')

    def __enter__(self):
        """ :meta private: """
        return self

    def __exit__(self, t, v, tb):
        """ :meta private: """
        if t is None:
            return True
        # pretend we didn't deal with raised error - which is true
        return False

    def __str__(self):
        """ :meta private: """

        if self._base.username is None:
            s = '["%s","%s"]' % (self._base.profile, 'REDACTED')
        else:
            s = '["%s","%s","%s"]' % (self._base.profile, self._base.username, 'REDACTED')
        return s

    def __repr__(self):
        """ :meta private: """

        if self._base.api_email is None:
            s = '%s,%s("%s","%s","%s","%s",%s,"%s")' % (
                self.__module__, type(self).__name__,
                self._base.profile, 'REDACTED', 'REDACTED',
                self._base.base_url, self._base.raw, self._base.user_agent
            )
        else:
            s = '%s,%s("%s","%s","%s","%s","%s",%s,"%s")' % (
                self.__module__, type(self).__name__,
                self._base.profile, self._base.api_email, 'REDACTED', 'REDACTED',
                self._base.base_url, self._base.raw, self._base.user_agent
            )
        return s

    def __getattr__(self, key):
        """ :meta private: """

        # this code will expand later
        if key in dir(self):
            return self[key]
        # this is call to a non-existent endpoint
        raise AttributeError(key)
