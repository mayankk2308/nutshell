# Script Processor
A simple script to generate the string version of entire script file. Created for ease of conversion of script to string while making commands for NLU. Accounts for tabs and newlines as one would expect.

## Usage
Download and make it executable. Of all the options used, make sure that the one specifying the path is mentioned last.

### Options

- #### Relative Path (`-r=|--relative=`)
  Provide relative path to script from `pwd`
- #### Absolute Path (`-a=|--absolute=`)
  Provide absolute path to script
- #### Test String (`-t|--test`)
  Output the created string with proper formatting
- ####  Ignore Sub-String (`-i=|--ignore=`)
  Ignore lines containing a specific substring

## Limitation
- Adds a newline at the end of the string
