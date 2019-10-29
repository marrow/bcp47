"""A datatype representation to inspect, validate, and manipulate BCP 47 "Language Tagss".

A language tag is a mechanism of identifying a language, optionally in relation to a country, and with the "Unicode"
extension, the language tag expands to encompass a wide range of internationalization and localization concerns such
as preferred currency, choice of week starting on Sunday or Monday, timezone selection, use of accounting-style
negative numbers (wrapped in parenthesis instead of prefixed by a negative symbol), etc., etc.

The structure was initially defined in [RFC 4646](https://tools.ietf.org/html/rfc4646), later refined and extended in
[RFC 5646](https://tools.ietf.org/html/rfc5646) formalized as ["Best Current Practice" number
47](https://tools.ietf.org/html/bcp47).

"""

from .release import version as __version__
from .tag import LanguageTag


__all__ = [
		'LanguageTag',
	]
