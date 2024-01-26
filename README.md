WALA Callgraph Builder
=======

### Introduction
This is a simple utility that uses [WALA](https://github.com/wala/WALA) to generate
and serialize callgraphs for Java programs.  It is based on the [WALA-start](https://github.com/wala/WALA-start)
example project, and as such shares the requirements, installation instructions, and license listed below.

In order to generate an _application-only_ callgraph, install and then run

    ./run.py <output> <jar>
	
This will analyze the java program `<jar>`, build a callgraph,
and write to `<output>` a text file containing those callgraph edges originating in application code.

This serialized callgraph can then be used by other analysis tools as needed.

### Requirements

Requirements are:

  * Java 8 or 11

Installation instructions will vary by operating system.

### Installation

Clone the repository, and then run:

    ./gradlew compileJava
    
This will pull in the WALA jars and build the sample code.

### Creating a .jar file

For example, from `test_cases`, run:

```
$ javac SimpleFuns.java
$ jar cfe SimpleFuns.jar SimpleFuns SimpleFuns.class
```

License
-------

All code is available under the [Eclipse Public License](http://www.eclipse.org/legal/epl-v10.html).
