Coinbase Commerce Transaction Parser for [Koinly.io](https://koinly.io/?via=6BCBDC5B)
===

Requirements
---

1. Python 3

Usage
---

1. Generate a report in Coinbase Commerce for _all_ time and _all_ transactions
1. Remove the first couple of lines which contains the balance information
1. Rename the file to `commerce.csv`
1. Run `python3 commerce.py`
1. Import `koinly.csv` into [Koinly](https://koinly.io/?via=6BCBDC5B)

Caveats
---

- Only payments and withdrawals are supported by the script.

Disclaimer
---

- I do _not_ guarentee the accuracy of the output CSV data and there could be bugs. Speak to a tax professional before filing!

License
---

MIT