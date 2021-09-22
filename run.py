#!/usr/bin/env python

# Generate an application-only callgraph for a Java program using WALA.
# run as: run.py <java_main_class> <jarfile> <output>
# in order to:
#  (1) analyze <jarfile> with WALA from an entrypoint in <java_main_class>
#  (2) write to <output> a text file containing those callgraph edges originating in application code

import subprocess
import sys

java_main_class = sys.argv[1]
jarfile = sys.argv[2]
output_path = sys.argv[3]

with open("scopefile.tmp", "w") as scopefile:
    scopefile.write("Primordial,Java,stdlib,none\n\Primordial,Java,jarFile,primordial.jar.model\nApplication,java,jarFile,%s" % jarfile)

gradle_cmd = 'gradle run --args="-mainClass %s -scopeFile scopefile.tmp -out %s"' % (java_main_class, output_path)

subprocess.call(gradle_cmd, shell=True)

subprocess.call(["rm", "scopefile.tmp"])
