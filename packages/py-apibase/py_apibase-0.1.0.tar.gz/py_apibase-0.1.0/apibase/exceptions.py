class APIError(Exception):

    class _CodeMessage():
        """ a small class to save away an interger and string (the code and the message)"""

        def __init__(self, code, message):
            self._code = code
            self._message = message

        def __int__(self):
            return self._code

        def __str__(self):
            return self._message

        def __repr__(self):
            return '[%d:"%s"]' % (int(self._code), str(self._message))

    def __init__(self, code=0, message=None, error_chain=None, e=None):

        if e and isinstance(e, APIError):
            # create fresh values (i.e copies)
            self._evalue = APIError._CodeMessage(int(e), str(e))
            if getattr(e, '_error_chain', False):
                self._error_chain = [APIError._CodeMessage(int(v), str(v)) for v in e._error_chain]
            return

        self._evalue = APIError._CodeMessage(int(code), str(message))
        if error_chain is not None:
            self._error_chain = []
            for evalue in error_chain:
                if isinstance(evalue, APIError._CodeMessage):
                    v = evalue
                else:
                    v = APIError._CodeMessage(int(evalue['code']), str(evalue['message']))
                self._error_chain.append(v)
        # As we are built off Exception, we need to get our superclass all squared away
        # super().__init__(message)

    def __bool__(self):
        # required because there's a len() function below that can return 0
        # see https://docs.python.org/3/library/stdtypes.html#truth-value-testing
        return True

    def __int__(self):
        return int(self._evalue)

    def __str__(self):
        return str(self._evalue)

    def __repr__(self):
        s = '[%d:"%s"]' % (int(self._evalue), str(self._evalue))
        if getattr(self, '_error_chain', False):
            for evalue in self._error_chain:
                s += ' [%d:"%s"]' % (int(evalue), str(evalue))
        return s

    def __len__(self):
        try:
            return len(getattr(self, '_error_chain'))
        except AttributeError:
            return 0

    def __getitem__(self, ii):
        return self._error_chain[ii]

    def __iter__(self):
        if getattr(self, '_error_chain', False):
            for evalue in self._error_chain:
                yield evalue
        return

    def next(self):
        if getattr(self, '_error_chain', False) is False:
            raise StopIteration


class NetworkError(Exception):
    pass