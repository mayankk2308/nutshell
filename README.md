# Natural Language Unix

Written in **Python 3**, this program allows users to automate seemingly tedious and multi-step processes through the application of **Unix** commands using natural language. In the future, we may also incorporate speech recognition, blurring the limitations of precise syntax programming.

## Supported Commands

The program supports the following commands:
* **Find** - to find a file on disk (using unix **find**)
* **Move** - to move one file or directory to another (using unix **mv**)
* **Rename** - to rename file (using unix **mv**)
* **Copy** - to copy one file to destination (using unix **rsync**)
* **Open** - to open a file (using unix **open**)
* **Organize** - given a directory and a document type (or every found type), cluster them into folders per type

## Applications

NLU has the following advantages for non-programmers:
* Extremely easy-to-use natural language syntax
* Ability to perform complex tasks with a single command
* Easily adopt more capabilities into the system, making NLU a more personal application

The most interesting aspect about NLU is its flexibility, being easy to expand and extremely scalable:
* Can add more scripts to the `scripts/` folder to leverage more powerful **unix** capabilities
* Builds on **python** as a foundation that adds more flexibility, programming paradigms, and applications of rich libraries
* Provides seamless integration between **unix** and **python** to create unique solutions to problems
* Allows for a robust user interface platform (still pre-alpha) for **unix**

NLU is currently **pre-alpha** - we think it has great potential to enable powerful capabilities with little to no syntax knowledge overhead.

## Examples

Some requests could be as follows:
```
organize everything in Documents
```

This will organize every file type into a separate folder for that type.

```
open HelloWorld.java
```

This will open the the file with the OS-default application for that type.

## Logging

The application also includes a convenient logging system that maintains a systematic list of commands and results in a subdirectory called `logs`. Logs are ordered by date and captured per session.

## Ground Rules

Due to certain limitations we have laid out some ground rules for the usage of this application as mentioned below:

* File/Folder names must not contain spaces within them.
* File/Folder names must not contain keywords used in the application (command names such as open, find etc.)


## License

This project is available under the MIT license. See the license file for more information.
