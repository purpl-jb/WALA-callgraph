#!/usr/bin/env python

# Generate an application-only callgraph for a Java program using WALA.
# run as: run.py <entry_class> <jarfile> <output>
# in order to:
#  (1) analyze <jarfile> with WALA from all public methods in <entry_class>
#  (2) write to <output> a text file containing all application-code-to-application-code callgraph edges
# (where <entry_class> is of the form form foo/bar/Baz for class 'Baz' in package 'foo.bar')

import subprocess
import sys

entry_class = sys.argv[1]
jarfile = sys.argv[2]
output_path = sys.argv[3]

with open("scopefile.tmp", "w") as scopefile:
    scopefile.write("Primordial,Java,stdlib,none\n\Primordial,Java,jarFile,primordial.jar.model\nApplication,java,jarFile,%s" % jarfile)

gradle_cmd = 'gradle run --args="-entryClass %s -scopeFile scopefile.tmp -out %s"' % (entry_class, output_path)

subprocess.call(gradle_cmd, shell=True)

subprocess.call(["rm", "scopefile.tmp"])
