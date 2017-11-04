# Natural Language Unix

Written in **Python 3**, this program allows users to execute a set of **Unix** commands using natural language. We will also incorporate speech recognition, blurring the limitations of precise syntax programming.

## Supported Commands

The program supports the following commands:
* **Find** - to find a file on disk (using unix **find**)
* **Move** - to move one file or directory to another (using unix **mv**)
* **Move All** - to move more than one file to destination (using unix **mv**)
* **Rename** - to rename file (using unix **mv**)
* **Copy** - to copy one file to destination (using unix **rsync**)
* **Copy All** - to copy multiple files to destination (using unix **rsync**)
* **Open** - to open a file (using unix **open**)
* **Go To** - to go to folder in GUI (using unix **open**)

## Examples

Some requests could be as follows:
```
Find HelloWorld.java
```

This will search the entire user file space for the file and return its location.

```
Open HelloWorld.java
```

This will open the first occurrence of the found file in user space.

```
Rename HelloWorld.java to World.java
```

This will rename the first occurrence of the found file in user space.

## Logging

We will also implement a logging mechanism so that the user may see the underlying changes made to the system using the program.

## License

This project is available under the MIT license. See the license file for more information.
