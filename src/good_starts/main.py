from pathlib import Path
import os

test_struct = '''
dir1
file1.py
dir2
 sub_dir21
 sub_file21.py
 sub_dir22
  sub_dir221
   sub_file2211.py
  sub_file221.py
  sub_dir222
dir3
 sub_file31.py
 sub_file32.txt
dir4
 sub_dir41
  sub_file411.py
 sub_dir42
  sub_file421.py
    sub_file422.py
file2.qmd
'''

def extract_paths(lines,root_dir=Path.cwd()):

    paths = []
    
    for i,line in enumerate(lines):

        name = Path(line.strip())

        indent = char_counter(line)

        if indent == 0:
            paths += [root_dir/name]
        else:
            # At this point paths dimention is i-1
            for j in range(i-1,-1,-1):
                previous_line = lines[j]
                previous_indent = char_counter(previous_line)
                if not '.' in previous_line and previous_indent == indent-1:
                    paths += [paths[j]/name]
                    break #Find the first one

    return paths


def find_blocks(lines):
    basic_indent = char_counter(lines[0])
    
    block_indices = []

    in_block = False

    for i in range(1,len(lines)):

        indent = indent_counter(lines[i])

        if indent-basic_indent != 0:
            if not in_block:
                start_index = i
                in_block = True
        else:
            if in_block:
                in_block = False
                block_indices += [[start_index,i]]

    # Block open at the last line
    if in_block: block_indices += [[start_index,len(lines)]]        

    return block_indices

def indent_counter(line,char_list=[' ']):
    count = 0
    for char in line:
        if char in char_list: 
            count += 1
        else: break
    return count

if __name__ == '__main__':
    lines = test_struct.strip().split('\n')

    test = extract_paths(lines,'')

    for item in test:
        print(item)

