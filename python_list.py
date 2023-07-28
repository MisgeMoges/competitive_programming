if __name__ == '__main__':
    
    def execute_commands(commands):
        arr = []  # Initialize an empty list to store the elements
    
        for command in commands:
            parts = command.split()
            cmd = parts[0]
    
            if cmd == 'insert':
                i = int(parts[1])
                e = int(parts[2])
                arr.insert(i, e)
            elif cmd == 'print':
                print(arr)
            elif cmd == 'remove':
                e = int(parts[1])
                arr.remove(e)
            elif cmd == 'append':
                e = int(parts[1])
                arr.append(e)
            elif cmd == 'sort':
                arr.sort()
            elif cmd == 'pop':
                arr.pop()
            elif cmd == 'reverse':
                arr.reverse()
    
    if __name__ == "__main__":
        N = int(input())
        commands = []
        for _ in range(N):
            command = input().strip()
            commands.append(command)
    
        execute_commands(commands)
    
