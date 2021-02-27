# pw2
To run this program from Run dialog (windows, sorry I don't know how other OS works XD) you should:
create a** .bat** batch
file for running the Python program with py.exe.
To do so, make a new text file containing a single line containing: **@py.exe C:\path\to\your\pythonScript.py %***
and save above file with .bat extension
Next: Click the Start button and type **Edit environment variables for your account**.
From System variables,
select the Path variable and
click Edit.In the Value text
field, append a semicolon,
type the path to the folder the batch file located. then clock ok. (now you can run your script by pressin Windows+R and typing scripts name and account as second argument in Run dialog)
Next: Create a text file wich will contain passwords in a form of, **account:password** in a singl line.
