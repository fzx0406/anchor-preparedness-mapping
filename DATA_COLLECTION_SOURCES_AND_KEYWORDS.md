# Data collection sources and search keywords

This page documents the news and report collection channels and search vocabulary supplied by the authors for the shipping-risk study.

## Collection channels

The collection strategy lists 16 report, news and company-information channels.

| No. | Source | Channel type | Official website |
| --- | --- | --- | --- |
| 1 | United Nations Conference on Trade and Development (UNCTAD) | Institutional reports | [unctad.org](https://unctad.org/) |
| 2 | International Maritime Organization (IMO) | Institutional reports | [imo.org](https://www.imo.org/) |
| 3 | International Chamber of Shipping (ICS) | Institutional reports | [ics-shipping.org](https://www.ics-shipping.org/) |
| 4 | The Maritime Executive | Specialist maritime news | [maritime-executive.com](https://maritime-executive.com/) |
| 5 | MarineLink | Specialist maritime news | [marinelink.com](https://www.marinelink.com/) |
| 6 | Riviera Maritime Media | Specialist maritime news | [rivieramm.com](https://www.rivieramm.com/) |
| 7 | Seatrade Maritime | Specialist maritime news | [seatrade-maritime.com](https://www.seatrade-maritime.com/) |
| 8 | Splash247 | Specialist maritime news | [splash247.com](https://splash247.com/) |
| 9 | The Loadstar | Specialist logistics and maritime news | [theloadstar.com](https://theloadstar.com/) |
| 10 | Maersk | Shipping-company information | [maersk.com](https://www.maersk.com/) |
| 11 | Lloyd's List | Specialist maritime news | [lloydslist.com](https://www.lloydslist.com/) |
| 12 | CNN | General news | [cnn.com](https://www.cnn.com/) |
| 13 | Reuters | General news | [reuters.com](https://www.reuters.com/) |
| 14 | The New York Times | General news | [nytimes.com](https://www.nytimes.com/) |
| 15 | Fox News | General news | [foxnews.com](https://www.foxnews.com/) |
| 16 | Bloomberg | General and business news | [bloomberg.com](https://www.bloomberg.com/) |

### Institutional report entry points

The following report pages are recorded in the collection document:

- UNCTAD, *Review of Maritime Transport*: [publication search](https://unctad.org/publications-search?f%5B0%5D=product%3A393).
- IMO, *Piracy and Armed Robbery Reports*: [report page](https://www.imo.org/en/ourwork/security/pages/piracy-reports-default.aspx).
- ICS, *Maritime Barometer*: [report page](https://www.ics-shipping.org/supporting-shipping/ics-maritime-barometer/).

## Search strategy

The original strategy combines an object group with an event group. It contains 16 object terms and 21 event terms. `OR` joins alternatives within each group, and `AND` combines the two groups. Quotation marks and multiword terms are preserved from the supplied document.

### Object terms

`port`, `container`, `shipping`, `terminal`, `bulk`, `container yard`, `seaport`, `maritime`, `cargo ship`, `tanker`, `liner shipping`, `shipping line`, `port authority`, `sea lane`, `trade lane`, `shipping corridor`.

### Event terms

`disruption`, `delay`, `incident`, `congestion`, `shutdown`, `backlog`, `collision`, `accident`, `explosion`, `strike`, `labor shortage`, `attack`, `piracy`, `reroute`, `diversion`, `suspension`, `sanctions`, `export restriction`, `regulatory change`, `extreme weather`, `hurricane`.

### Complete Boolean query

```text
("port" OR "container" OR "shipping" OR "terminal" OR "bulk"
 OR "container yard" OR "seaport" OR "maritime"
 OR "cargo ship" OR "tanker" OR "liner shipping"
 OR "shipping line" OR "port authority"
 OR "sea lane" OR "trade lane" OR "shipping corridor")

AND

("disruption" OR "delay" OR "incident" OR "congestion" OR "shutdown"
 OR "backlog" OR "collision" OR "accident" OR "explosion"
 OR "strike" OR "labor shortage" OR "attack" OR "piracy"
 OR "reroute" OR "diversion" OR "suspension"
 OR "sanctions" OR "export restriction" OR "regulatory change"
 OR "extreme weather" OR "hurricane")
```

A copyable plain-text version is available in [news_search_query.txt](news_search_query.txt).

## Documentation scope

This page reproduces the collection-channel list and Boolean vocabulary from the author-provided document. Article counts, source-by-year coverage and source-specific retrieval execution require the corresponding collection records; they are not established by the channel list alone.

Source names and layout have been standardized for readability. The query terms and Boolean operators are unchanged, with line endings normalized. The supplied document's SHA-256 digest is `229ae2bd621b00cc0b35bf7fa46f43ee0e7b6729c8cf41bcf195135096d35d4c`.
