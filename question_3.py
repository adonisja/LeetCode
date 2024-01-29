''' Longest Substring Without Repeating Characters:
Given a string s, find the length of the longest 
substring without repeating characters.'''

''' Personal Note:
A substring is categorized as slices of a string, therefore,
if s = {wkjwkwwhjeuw}, the longest substring is: {whjeu} which is 5 characters long
'''
def lengthOfLongestSubstring(s):
    seen = {}       #create a dictionary
    max = 0         #set the max to 0
    count = 0       #initialize an accumulator
    for i in range(len(s)):
        if s[i] not in seen:    #inputs new characters into the dictionary with their index
            seen[s[i]] = i
            count += 1          #increase the accumulator
            if count > max:     #checks if max is less than the accumulator, if it is then perform a swap
                max = count
        else:
            seen = {}           #resets the dictionary
            seen[s[i]] = i      #enters the new character into the dictionary with its index
            count = 1           #resets the accumulator to 1 to represent the new character added
    return max

    


def main():
    s = input("Enter a string: ")
    max = lengthOfLongestSubstring(s)
    if max == len(s):
        print('No repeat characters in the string')
    else:
        print(f'The longest substring is {max} characters long')


        
main()