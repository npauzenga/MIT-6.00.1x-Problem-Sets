substring = ""
temp = ""
    
for letter in range(0, len(s)):
        temp += s[letter]
        if s[letter] < s[letter - 1]:
            temp = s[letter]
        if len(temp) > len(substring):
            substring = temp
                
     
print("Longest substring in alphabetical order is: %s" % str(substring)) 