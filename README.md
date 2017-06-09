# Wikipedia-NL biography maintenance

This script operates on Dutch Wikipedia (with the MediaWiki API exposed through pywikibot) and cleans up the [biography section][biografie] by removing links to articles that were added there in the past but have been removed from the Wiki. In other words, it removes red links.

Any user can run the script at any time, but considering that it takes quite a while to run and deletions don't actually occur that often, it doesn't currently run in a schedule. It is run ad hoc by a bot named [Geerlings' robot][frankrobot].

[frankrobot]: https://nl.wikipedia.org/wiki/Gebruiker:Geerlings%27_robot
[biografie]: https://nl.wikipedia.org/wiki/Biografielijst
