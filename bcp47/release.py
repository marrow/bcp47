"""Release information for the bcp47 package."""

from collections import namedtuple

level_map = {'plan': '.dev'}

version_info = namedtuple('version_info', ('major', 'minor', 'micro', 'releaselevel', 'serial'))(1, 0, 0, 'plan', 1)
version = ".".join([str(i) for i in version_info[:3]]) + \
		((level_map.get(version_info.releaselevel, version_info.releaselevel[0]) + \
		str(version_info.serial)) if version_info.releaselevel != 'final' else '')

author = namedtuple('Author', ['name', 'email'])("Alice Bevan-McGregor", 'alice@gothcandy.com')

description = "An IETF BCP47 datatype and serializer, with support for Unicode extensions."
url = 'https://github.com/marrow/bcp47/'
