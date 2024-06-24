## ApplePyLog

A simple logging library for small projects.
There are 4 Logging levels:
* Error
* Info
* Warn
* Debug

You can write to any of these levels and change the current log level of what gets printed from the logger
The log levels work as the order above so a log level of Error will only print Error logs
A log level of Warn will print Warn, Info and Error logs but not Debug
The default log level is Warn

You can pass in any writer with type TextIO, the default is sys.stdout but you can also pass in file writers

You can also specify an alternate writer, which defaults to None, which will write the same as the main writer, this can be useful to write your logs to stdout and also save them to a file. 
This alternate writer also has its own log level that can be specified, also with default of WARN.
