# Natural Language Unix

Written in **Python 3**, this program allows users to execute a set of **Unix** commands using natural language. We will also incorporate speech recognition, blurring the limitations of precise syntax programming.

## Supported Commands

The program supports the following commands:
* **Find** - to find a file on disk (using unix **find**)
* **Move** - to move one file or directory to another (using unix **mv**)
* **Rename** - to rename file (using unix **mv**)
* **Copy** - to copy one file to destination (using unix **rsync**)
* **Open** - to open a file (using unix **open**)

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

The application also includes a convenient logging system that maintains a systematic list of commands and results in a subdirectory called `logs`.

## Testing

To test the working of the project run the respective commands :

* **Organize** - organize everything in TestOrganize  ***or*** organize pdf in TestOrganize ***or*** organize txt in TestOrganize ***or*** organize dmg in TestOrganize ***or*** organize png in TestOrganize
* **Rename** - rename hack.txt to umass.txt
* **Move** - move drag.txt to TestMove
* **Copy** - copy back.txt to TestCopy
* **Open** - open openthis.txt ***or*** open openthat.txt

## License

This project is available under the MIT license. See the license file for more information.
