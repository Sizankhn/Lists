"""""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7
types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example:
N = 4
append 1
append 2
insert 3 1
print
    - append 1: Append 1 to the list. arr = [1]
    - append 2: Append 2 to the list, arr = [1,2]
    - append 3 1: Insert 3 at index 1, arr = [1,3,2]
    - print: Print the array
        Output:
        [1, 3, 2]

Input Format:
The first line contains an integer,n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints:
- The elements added to the list must be integers

Output Format:
For each command of type print, print the list on a new line.

Sample Input 1:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 1:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
if __name__ == '__main__':
    N = int(input())
    result = []
    for n in range(N):
        x = input().split(" ")
        command = x[0]
        if command == 'append':
            result.append(int(x[1]))
        if command == 'print':
            print(result)
        if command == 'insert':
            result.insert(int(x[1]), int(x[2]))
        if command == 'reverse':
            result = result[::-1]
        if command == 'pop':
            result.pop()
        if command == 'sort':
            result = sorted(result)
        if command == 'remove':
            result.remove(int(x[1]))
