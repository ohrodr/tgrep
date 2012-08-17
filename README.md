# Tgrep 

Tgrep is a simple utility to retrieve time series from a RFC 5424 or RFC 3164 logfile.  The intent is to only scrape the log until the time frame has been reached.  There is optional usage of regex to further filter the logfile.  There is no tokenization of the syslog message.


Current version: 0.0.1

## Getting Started

Find a log file to search, and pass the appropriate options.

## Installation

python setup.py install
/usr/bin/tgrep --help 

## Contact

In the remote possibility that there exist bugs in this code, please report them to:
<https://github.com/ohrodr/tgrep/issues>

Follow [@oh_rodr](http://twitter.com/oh_rodr) on Twitter for updates.

## Authors:
* Robb O'Driscoll <http://twitter.com/oh_rodr>

## License
Copyright 2012 Twitter, Inc.

Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0

