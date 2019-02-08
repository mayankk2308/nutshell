# Nutshell

Written in **Python 3**, this program allows users to automate seemingly tedious and multi-step processes through the application of **Unix** commands. We hope to leverage searchable menus and even HotKeys to make it easy and efficient for users to run these tasks.

## Supported Commands

The program supports the following commands:
* **Find** - to find a file on disk (using unix **find**)
* **Move** - to move one file or directory to another (using unix **mv**)
* **Rename** - to rename file (using unix **mv**)
* **Copy** - to copy one file to destination (using unix **rsync**)
* **Open** - to open a file (using unix **open**)
* **Organize** - given a directory and a document type (or every found type), cluster them into folders per type

## Applications

Nutshell has the following advantages for non-programmers:
* Extremely easy-to-use
* Ability to perform complex tasks with a single click
* Easily adopt more capabilities into the system, making Nutshell a more personal application

The most interesting aspect about Nutshell is its flexibility, being easy to expand and extremely scalable:
* Can add more scripts to the `scripts/` folder to leverage more powerful **unix** capabilities
* Builds on **python** as a foundation that adds more flexibility, programming paradigms, and applications of rich libraries
* Provides seamless integration between **unix** and **python** to create unique solutions to problems
* Allows for a robust user interface platform (still pre-alpha) for **unix**

Nutshell is currently **pre-alpha** - we think it has great potential to enable powerful capabilities with little to no syntax knowledge overhead.


## Logging

The application also includes a convenient logging system that maintains a systematic list of commands and results in a subdirectory called `logs`. Logs are ordered by date and captured per session.


## License

This project is available under the MIT license. See the license file for more information.
