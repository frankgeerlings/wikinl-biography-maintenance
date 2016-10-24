# -*- coding: utf-8 -*-

import pywikibot, re, doctest
from pywikibot import pagegenerators
from pprint import pprint

editSummary = u'Robot: Periodiek onderhoud – verwijderen rode links (zie [[Gebruiker:Frank Geerlings/Toelichting/Biografielijsten|toelichting]])'

def keep_line(existence_test, regel):
	"""
	If this returns false, then the article the line links to was deleted. It returns
	True if the line doesn't match the pattern for biography summary list items, so any
	line that is unexpected can be left untouched.

	If a line matches the pattern and the first link points to a missing article, it is not kept:

	>>> keep_line(lambda _: False, '* [[Leia Organa|Prinses Leia Organa]], rebellenleider')
	False

	Variant with bold occurs at times, special case:

	>>> keep_line(lambda _: False, "* '''[[Yoda]]''', spiritueel begeleider")
	False

	Lines that don't match the pattern are kept:

	>>> keep_line(lambda _: False, '* Bla')
	True

	Empty lines are kept:

	>>> keep_line(lambda _: False, '')
	True
	"""
	resultaat = re.match(r'\*\s+(\'\'\')?\[\[(.*?)(\|.*?)?\]\](.*?)$', regel)

	if (resultaat == None):
		return True

	precruft, artikel, omschrijving, rest = resultaat.groups()

	return existence_test(artikel)

	# return "* %s[[%s%s]]%s" % (precruft or '', artikel, omschrijving, rest)

def biografieCleanup(site, p):
	lines = [i for i in p.text.split('\n') if keep_line(lambda artikel: pywikibot.Page(site, artikel).exists(), i)]

	result = '\n'.join(lines)

	if result is not p.text:
		p.text = result
		p.save(editSummary, minor=False)

def main(*args):
	local_args = pywikibot.handle_args(args)

	site = pywikibot.Site(code="nl", fam="wikipedia")

	cat = u'Categorie:Biografielijsten'

	c = pywikibot.Category(site, cat)
	gen = pagegenerators.CategorizedPageGenerator(c)

	for p in gen:
		biografieCleanup(site, p)

if __name__ == "__main__":
	try:
		main()
	except Exception:
		pywikibot.error("Fatal error:", exc_info=True)
