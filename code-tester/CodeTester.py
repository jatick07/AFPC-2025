import subprocess
import os

# Test cases
CountLetters_cases = [
    ("hello", "{'h': 1, 'e': 1, 'l': 2, 'o': 1}"),
    ("HELLO", "{'h': 1, 'e': 1, 'l': 2, 'o': 1}"),
    ("hello world", "{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}"),
    ("hello123", "{'h': 1, 'e': 1, 'l': 2, 'o': 1, '1': 1, '2': 1, '3': 1}"),
    ("café", "{'c': 1, 'a': 1, 'f': 1, 'é': 1}"),
    ("aaaAAA", "{'a': 6}"),
    ("!!!???", "{'!': 3, '?': 3}"),
    ("ab@#cd@#", "{'a': 1, 'b': 1, '@': 2, '#': 2, 'c': 1, 'd': 1}"),
    ("The quick Brown fox Jumps over the lazy dog",
     "{'t': 2, 'h': 2, 'e': 3, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}")  # Pangram test
]
PrintEvenNums_cases = [
    ("4", "4", "[4]"),
    ("3", "5", "[4]"),
    ("10", "5", "[]"),
    ("0", "5", "[0, 2, 4]"),
    ("2", "10", "[2, 4, 6, 8, 10]"),
    ("-3", "2", "[-2, 0, 2]"),
    ("1000000", "1000004", "[1000000, 1000002, 1000004]")
]

# Run the file and test every case in the test cases
def test_file(folder, file, cases):
    checklist = []
    full_file = folder + file
    
    if file[-3:] == 'cpp':
        os.mkdir(f"test-results/{file[:-4]}")
    
    for i, edge_case in enumerate(cases, 1):
        expected_output = edge_case[-1]
        
        if len(edge_case) == 2:
            case = edge_case[0]
        elif len(edge_case) == 3:
            case = f"{edge_case[0]}\n{edge_case[1]}"
        
        if file[-2:] == 'py':
            process = subprocess.run(["python", full_file], input=case, text=True, capture_output=True)
            output = process.stdout.strip()
        
            if output == expected_output:
                checklist.append("Pass")
            else:
                checklist.append("Fail")
        elif file[-3:] == 'cpp':
            subprocess.run(["g++", "-o", full_file[:-4], full_file])
            process = subprocess.run([full_file[:-4] + ".exe"], input=case, text=True, capture_output=True)
            
            stdout = open(f"test-results/{file[:-4]}/stdout-{i}.txt", "w")
            stdout.write(process.stdout.strip())
            stdout.close()
    
    if file[-2:] == 'py':
        return checklist
    elif file[-3:] == 'cpp':
        return "C++, I ain't remaking ALL of it, check the txt"
    
def folder_iter(folder):
    file_list = [file for file in os.listdir(folder) if file[-2:] == 'py' or file[-3:] == 'cpp']
    problem_type = folder.split("/")[-2]
    case_list = []
    
    if problem_type == 'CountLetters':
        case_list = CountLetters_cases
    elif problem_type == 'PrintEvenNums':
        case_list = PrintEvenNums_cases
    
    for file in file_list:
        print(f"\nTesting file '{file}': \n")
        output = test_file(folder, file, case_list)
        if type(output) is str:
            print(output)
        else:
            output_file = open(f"test-results/{file}.txt", "w")
        
            for index, result in enumerate(output):
                fresult = f"Test case {index + 1}: {result}"
                print(fresult)
                output_file.write(fresult + "\n")
            output_file.close()
        
        
    
# Input sequence
problem_type = int(input("Problem types:\n    1 - Count letters in a string\n    2 - Print even numbers from a range of integers\nEnter the problem type: "))

# Choose problem type and test files based on the type
if problem_type == 1:
    folder = "test-files/CountLetters/"
    folder_iter(folder)
elif problem_type == 2:
    folder = "test-files/PrintEvenNums/"
    folder_iter(folder)