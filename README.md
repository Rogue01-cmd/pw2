# pw2
To run this program from Run dialog (windows, sorry I don't know how other OS works XD) you should:
_**first:**_ create a  **.bat** batch file for running the Python program with py.exe.
To do so, make a new text file containing this single line : **@py.exe C:\path\to\your\pythonScript.py %***
and save above file with **.bat** extension
_**Second:**_ Click the Start button and type **Edit environment variables for your account**.
From System variables,
select the Path variable and
click Edit.In the Value text
field, append a semicolon,
type the path to the folder the batch file located. then click ok. (now you can run your script by pressin Windows+R and typing scripts name and account as second argument in Run dialog)
_**Third:**_ Create a text file wich will contain passwords in a form of, **account:password** in a singl line.
