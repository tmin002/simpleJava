# simpleJava
Python script that helps compile a plain java package (Unix environment only), Developed for personal use.

## Installation
	curl https://raw.githubusercontent.com/tmin002/simpleJava/main/sj.py > sj ; curl https://raw.githubusercontent.com/tmin002/simpleJava/main/manifest.mf > manifest.mf; chmod a+x sj

## How to use
- sj reads Java source files in the 'src' folder, then reads 'manifest.mf', then creates 'output.jar'.
- sj will create a directory 'out', which contains a compiled class files waiting to be put into the jar file.
- The default main class is 'Runner.java'. You can change it on 'manifest.mf'.
- '?' option for help, '-r' option for output execution after compile, '-c' option for deleting 'out' folder.

## Examples
<p>Run at shell:</p>
<span><img src="https://raw.githubusercontent.com/tmin002/simpleJava/main/examples/shell.png" width="150" height="100"></span>
<p>Vim integration:</p>
<span><img src="https://raw.githubusercontent.com/tmin002/simpleJava/main/examples/vim_code.png" width="150" height="100"></span>
<span><img src="https://raw.githubusercontent.com/tmin002/simpleJava/main/examples/vim_run.png" width="150" height="100"></span>
