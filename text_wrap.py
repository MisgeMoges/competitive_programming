import textwrap

def wrap(string, max_width):
    wrapped_lines = []
    for i in range(0, len(string), max_width):
        
        wrapped_lines.append(string[i:i+max_width])
        
    return '\n'.join(wrapped_lines)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
