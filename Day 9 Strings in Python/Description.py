# Case Conversion
str.capitalize()
# Returns a string with the first character capitalized and the rest lowercased.

str.lower()
# Converts all characters in the string to lowercase.

str.upper()
# Converts all characters in the string to uppercase.

str.title()
# Converts the first character of each word to uppercase and the rest to lowercase.

str.swapcase()
# Swaps the case of all characters in the string (uppercase to lowercase and vice versa).

str.casefold()
# Converts the string to lowercase in a way that's more aggressive than lower(), suitable for caseless comparisons.

# Alignment
str.center(width, fillchar=' ')
# Centers the string in a field of specified width, padded with fillchar.

str.ljust(width, fillchar=' ')
# Left-aligns the string in a field of specified width, padded with fillchar.

str.rjust(width, fillchar=' ')
# Right-aligns the string in a field of specified width, padded with fillchar.

str.zfill(width)
# Pads the string with zeros on the left until it reaches the specified width.

# Searching
str.find(sub, start=0, end=len(string))
# Returns the lowest index of sub if found, or -1 otherwise.

str.rfind(sub, start=0, end=len(string))
# Returns the highest index of sub if found, or -1 otherwise.

str.index(sub, start=0, end=len(string))
# Like find(), but raises ValueError if sub is not found.

str.rindex(sub, start=0, end=len(string))
# Like rfind(), but raises ValueError if sub is not found.

str.count(sub, start=0, end=len(string))
# Counts the number of non-overlapping occurrences of sub.

Validation
str.isalpha()
# Returns True if all characters in the string are alphabetic.

str.isdigit()
# Returns True if all characters in the string are digits.

str.isalnum()
# Returns True if all characters in the string are alphanumeric.

str.islower()
# Returns True if all characters in the string are lowercase.

str.isupper()
# Returns True if all characters in the string are uppercase.

str.isspace()
# Returns True if the string consists only of whitespace characters.

str.istitle()
# Returns True if the string follows title case rules.

str.isdecimal()
# Returns True if all characters are decimal characters.

str.isnumeric()
# Returns True if all characters are numeric.

str.isidentifier()
# Returns True if the string is a valid Python identifier.

str.isprintable()
# Returns True if all characters in the string are printable.

# Formatting
str.format(*args, **kwargs)
# Formats the string using the given arguments.

str.format_map(mapping)
# Formats the string using a dictionary or mapping.

str.join(iterable)
# Joins the elements of an iterable with the string as the separator.

str.lstrip(chars=None)
# Removes leading characters specified in chars.

str.rstrip(chars=None)
# Removes trailing characters specified in chars.

str.strip(chars=None)
# Removes both leading and trailing characters specified in chars.

str.partition(sep)
# Splits the string into three parts: the part before sep, the separator itself, and the part after.

str.rpartition(sep)
# Like partition(), but searches for sep from the right.

# Splitting
str.split(sep=None, maxsplit=-1)
# Splits the string into a list of substrings.

str.rsplit(sep=None, maxsplit=-1)
# Splits the string into a list of substrings, starting from the right.

str.splitlines(keepends=False)
# Splits the string at line boundaries.

# Replacing
str.replace(old, new, count=-1)
# Replaces occurrences of old with new. The count argument limits the number of replacements.

str.translate(table)
# Replaces characters based on a translation table (created with str.maketrans()).

str.maketrans(x, y=None, z=None)
# Creates a translation table for use with translate().

# Encoding and Decoding
str.encode(encoding='utf-8', errors='strict')
# Encodes the string into bytes.

str.decode(encoding='utf-8', errors='strict') #(on bytes)
# Decodes bytes into a string.

# Other Methods
str.startswith(prefix, start=0, end=len(string))
# Returns True if the string starts with the specified prefix.

str.endswith(suffix, start=0, end=len(string))
# Returns True if the string ends with the specified suffix.

str.expandtabs(tabsize=8)
# Replaces tabs in the string with spaces.