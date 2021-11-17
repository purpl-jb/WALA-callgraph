#!/usr/bin/env python

# Generate an application-only callgraph for a Java program using WALA.
# run as: run.py <output> <jarfile_1> <jarfile_2> ... <jarfile_n>
# in order to:
#  (1) analyze <jarfile> with WALA from all public methods in <entry_class>
#  (2) write to <output> a text file containing all application-code-to-application-code callgraph edges
# (where <entry_class> is of the form form foo/bar/Baz for class 'Baz' in package 'foo.bar')

import subprocess
import sys

# entry_class = sys.argv[1]
output_path = sys.argv[1]
jarfiles = sys.argv[2:]

with open("scopefile.tmp", "w") as scopefile:
    scopefile.write("Primordial,Java,stdlib,none\n\Primordial,Java,jarFile,primordial.jar.model\n")
    for jarfile in jarfiles:
        scopefile.write("Application,java,jarFile,%s\n" % jarfile)

gradle_cmd = './gradlew run --args="-scopeFile scopefile.tmp -out %s"' % output_path

subprocess.call(gradle_cmd, shell=True)

subprocess.call(["rm", "scopefile.tmp"])
