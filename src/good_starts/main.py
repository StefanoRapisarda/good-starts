from pathlib import Path
from typing import Union

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

def extract_paths(lines: list[str],root_dir: Union[str,Path]=Path.cwd()):
    """
    Extracts a list of paths from a list of directory and file names with indentation indicating hierarchy.

    Parameters
    ----------
    lines : list of str
        A list of strings representing directory and file names, where indentation indicates hierarchy.
    root_dir : Union[str, Path], optional
        The root directory to which the paths are relative. Defaults to the current working directory.

    Returns
    -------
    list of Path
        A list of Path objects representing the full paths.
    """

    if isinstance(root_dir, str):
        root_dir = Path(root_dir)

    paths = []
    
    for i,line in enumerate(lines):

        name = Path(line.strip())

        indent = indent_counter(line)

        if indent == 0:
            paths += [root_dir/name]
        else:
            # At this point paths dimention is i-1
            for j in range(i-1,-1,-1):
                previous_line = lines[j]
                previous_indent = indent_counter(previous_line)
                if not '.' in previous_line and previous_indent == indent-1:
                    paths += [paths[j]/name]
                    break #Find the first one

    return paths

def indent_counter(line: str, char_list: list[str] = [' ']) -> int:
    """
    Counts the number of leading characters in a string that match any character in the given list.

    Parameters
    ----------
    line : str
        The input string in which leading characters are to be counted.
    char_list : list of str, optional
        A list of characters to be counted as indentation characters. Defaults to a list containing a single space character [' '].

    Returns
    -------
    int
        The count of leading characters in the input string that match any character in `char_list`.

    Examples
    --------
    >>> indent_counter("    Hello, world!")
    4

    >>> indent_counter("\t\tHello, world!", char_list=['\t'])
    2

    >>> indent_counter("  \t Hello, world!", char_list=[' ', '\t'])
    3

    >>> indent_counter("Hello, world!")
    0
    """
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

