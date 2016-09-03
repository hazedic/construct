#-------------------------------------------------------------------------------
# py3compat.py
#
# Some Python2&3 compatibility code
#-------------------------------------------------------------------------------
import sys
PY3 = sys.version_info[0] == 3
from io import BytesIO, StringIO


if PY3:
    def bchr(i):
        """Converts int (0 through 255) into b'...' character."""
        return bytes((i,))

    def u(s):
        return s

    def int2byte(i):
        return bytes((i,))

    def byte2int(b):
        return b

    def str2bytes(s):
        return s.encode("latin-1")

    def str2unicode(s):
        return s

    def bytes2str(b):
        return b.decode('latin-1')

    def decodebytes(b, encoding):
        return bytes(b, encoding)

    advance_iterator = next
        
else:
    int2byte = chr
    byte2int = ord

    def bchr(i):
        """Converts int (0 through 255) into b'...' character."""
        return chr(i)

    def u(s):
        return unicode(s, "unicode_escape")

    def str2bytes(s):
        return s

    def str2unicode(s):
        return unicode(s, "unicode_escape")

    def bytes2str(b):
        return b

    def decodebytes(b, encoding):
        return b.decode(encoding)

    def advance_iterator(it):
        return it.next()

