# Helper scripts to run linux like command in window command line tool

## TODO:
1. make it run in windows/linux/mac without typing python3
2. Add arguments parser; have -l to should linux path and -w to should windows path
3. Add checks to check whether it is a linux path or windows path
4. Also add functionalities to convert windows path to linux path; add -p "<path>"
5. Support different types of representations of windows drive symbols; win subsystem use /mnt/c while cygwin may use a different format to represent drives. Add some options to handle both cases
6. make cd to accept both linux and windows path
