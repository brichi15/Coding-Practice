def permute(string):
    
    if len(string) == 1:
        return string

    perms = []
    
    for i in range(len(string)):
        for perm in permute(string[:i] + string[i+1:]):
            perms.append(string[i] + perm)
        
    return perms