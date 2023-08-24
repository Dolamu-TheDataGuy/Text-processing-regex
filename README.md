# Regular Expression(Regex) Concept

This is a repository on regex, regex is a generic concept to all programming language for handling the string data type. They are very useful for extracting peculiar information in a large pool of content.

* `re module`

* `Methods to search for matches`

* `Method on a match object`

* `Meta characters`

* `More special sequences`

* `Sets`

* `Quantifier`

* `Conditions`  

* `Grouping`

* `Modification`

* `Compilation flags`

## Methods on a match

1. `match()`: Determines if the RE matches at the beginning of the string, returns the item if it exist at the beginning of the text.

2. `search()`: Scan through a string, looking for any location where this RE matches.

3. `findall()`: Find all substrings where the RE matches, and returns them as a list.

4. `finditer()`: Find all substrings where the RE matches, and returns them as an iterator.

## Modification methods

1. `split()`: Returns a list where the string has been split at each match.

2. `sub()`: Replaces one or many matches with a string.

All meta characters: . * ^ $ + ? { } [ ] \ | ( )

## Regex Wildcards

* `.` - any characters (except newline character).

* `*` - zero (0) or more repetitions.

* `^` - starts with "^David".

* `$` - ends with "world$

* `+` - one (1) or more repetitions.

* `?` - zero (0) or one (1) repetition.

* `{m}` - m repetitons

* `{m, n}` - m to n repetitons.

* `[]` - a set of characters "[a-z]".

* `\` - escape character or raw character "\\t"

* `|` - either or "fall|stand"

* `( )` - capture and group.

## More special characters

* `\d`: Matches any decimal digit; [0-9].

* `\D`: Mathces any non-digit character.

* `\s`: Matches any whitespace character; (space " " tab \t newline "\n").

* `\S`: Matches any non-whitespace character.

* `\w`: Matches any alphanumeric (word) character; [a-zA-Z0-9_].

* `\W`: Matches any non-alphanumeric characters.

* `\b`: Matches where the specified characters are at the beginning or at the end of a word.

* `\B`: Matches where the specified characters are present. but NOT at the beginning (or a )

## Quantifier

1. `*`: 0 or more

2. `+`: 1 or more

3. `?`: 0 or 1, -> optional character

4. `{4}`: exact number

5. `{4,6}`: range numbers (min, max)

## Compilation Flags

* `ASCII`, A: Makes several escapes like \w, \b, \s and \d match only on ASCII characters.
* `DOTALL`, S: Make . match any character, including newlines.
* `IGNORECASE`, I: Do case-insensitive matches.
* `LOCALE`, L: Do a locale-aware match.
* `MULTILINE`, M: Multi-line matching, affecting ^ and $.
* `VERBOSE`, X (for 'extended'): Enable verbose REs, which can be organized more cleanly.
