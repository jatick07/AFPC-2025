# AFPC 2025 Simple Problem Sets

A collection of problem sets for the Arab Future Programmers Competiton second team.


## Deployment
To deploy either run:
```bash
  git clone https://github.com/jatick07/AFPC-2025
  python SECTION/FILE_NAME.py
```
or download source code as zip file.


## Code Tester instructions

To use the code tester, navigate to `code-tester/test-files`, and enter the folder corresponding to the type of problem, lastly put the files you want to test in there.

To use the tester, run:

```bash
  python CodeTester.py
```

It will ask you to choose what type of problem you want to test the code at, enter either `1` or `2`

```
  Problem types:
      1 - Count letters in a string
      2 - Print even numbers from a range of integers
  Enter the problem type: 
```

Lastly, it will test every file in that folder and output results in the command line as well as in a text file.

#### Example

```
  Testing file 'aybaksamiz-cl.py':

  Test case 1: Pass
  Test case 2: Pass
  Test case 3: Pass
  Test case 4: Pass
  Test case 5: Pass
  Test case 6: Pass
  Test case 7: Pass
  Test case 8: Pass
  Test case 9: Pass
  
  Testing file 'nartabaza-cl.py':
  
  Test case 1: Pass
  Test case 2: Fail
  Test case 3: Pass
  Test case 4: Pass
  Test case 5: Pass
  Test case 6: Fail
  Test case 7: Pass
  Test case 8: Pass
  Test case 9: Fail
```