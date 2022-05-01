# simpleJava
Python script that helps compile a plain java package (Unix environment only), Developed for personal use.

## Installation
	curl https://raw.githubusercontent.com/tmin002/simpleJava/main/sj.py > sj ; chmod a+x sj

## How to use
- sj reads Java source files in the 'src' folder, then reads 'manifest.mf', then creates 'output.jar'.
- sj will create a directory 'out', which contains a compiled class files waiting to be put into the jar file.
- The default main class is 'Runner.java'. You can change it on 'manifest.mf'.
- '?' option for help, '-r' option for output execution after compile.