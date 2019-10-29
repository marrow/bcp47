from typing import List

ERROR_MAP = {
		str.isalpha: "alphabetic",
		str.isalnum: "alphanumeric",
	}


class Tag(str):
	fold = str.lower
	valid = str.isalnum
	minimum = 1
	maximum = 8
	prefix = ''
	
	def __new__(cls, value):
		assert cls.valid(value) and cls.minimum <= len(value) <= cls.maximum, \
				f"A {cls.__name__} must be between {cls.minimum} and {cls.maximum} {ERROR_MAP[cls.valid]} characters."
		
		if cls.fold: value = cls.fold(value)
		return super().__new__(cls, cls._normalize(value))
	
	@classmethod
	def _normalize(cls, value):
		return value
	
	def __repr__(self):
		suffix = f', prefix={self.prefix!r}' if self.prefix else ""
		return f"{self.__class__.__name__}({super().__repr__()}{suffix})"


class Language(Tag):
	valid = str.isalpha
	
	@classmethod
	def _normalize(cls, value):
		# When there is both a 2-character code and a 3-charcter code, MUST use the 2-character code.
		# TODO: Pull this mapping from CLDR.
		return value


class SubTag(Tag):
	prefix = '-'
	
	def __str__(self):
		return f"{self.prefix}{super().__str__()}"


class Script(SubTag):
	fold = str.title
	valid = str.isalpha


class Variant(SubTag):
	minimum = 4
	
	def __new__(cls, value):
		if not value[0].isnumeric():
			assert len(value) >= 5, \
					"Variant subtags must be between 5 and 8 alphanumeric characters, or 4 if beginning with a digit."
		
		super().__new__(cls, value)


class Region(SubTag):
	fold = str.upper


class Extension(SubTag):
	pass


class Private(SubTag):
	prefix = 'x-'


class LanguageTag:
	"""A language as spoken (or written) by human beings for communication of information to other human beings."""
	
	components: List[Tag]
	
	language: Language
	extended: List[SubTag]  # up to 3
	script: SubTag  # 
	region: Region  # usually uppercase
	variant: List[Variant]  # 5-8 characters, or 4 if leading digit
	private: Private  # an optional private-use subtag chain
	
	def __init__(self, *components, **properties):
		"""Initialize a new IETF BCP 47 Language Tag.
		
		May be constructed by passing in a single string value to be parsed, multiple components individually, or may
		be constructed by passing in keyword arguments to define the components by name. Keyword arguments will be
		applied after any parsing of positional strings, permitting initialization and adaption/modification in a
		single operation.
		
		Examples:
		
			canadian_english = LanguageTag("en-CA")
			canadian_french = LanguageTag("fr", "CA")
			french_french = LanguageTag(language="fr", region="FR")
		"""
		
		if len(components) == 1:  # If there is only one argument, it's going to be a compact, serialized form.
			components, = components
			components = components.split('-')
		
		primary, *components = components  # Unpack the first (primary) tag.
		primary = Language(primary)
		sub = (SubTag(i) for i in components)
		
		self.components = [primary, *sub]
	
	def __str__(self):
		return "".join(str(i) for i in self.components)
	
	def __repr__(self):
		return f"{self.__class__.__name__}(\"{self!s}\")"
