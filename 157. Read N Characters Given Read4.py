"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

'''
https://leetcode.com/problems/read-n-characters-given-read4/discuss/705183/Python-Simple-solution-with-explanation
'''

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        
        # our final buf will have min( n, all the characters that are in file)
        
        # initialize storage with 4 chars limit
        # 2. At any point buf4, will maximum of 4 characters or count returned from the read4.
        buf4 = [''] * 4
        
        # counter for total character read
        read = 0
        
        # We need to read a total of n, character
        # we add the number of character read into 'read'
        while read < n:
            # read file into buf4 and count
            ## 3. As I can read utmost 4 chars at a time, 
            # I create an array of size 4 and pass it to the function read4(buf4). 
            # That read4 function will fill my buf4 and returns the 
            # count how many characters it filled.
        
            count = read4(buf4)
            # end of file reached, break
            if not count:
                break
                
            # if n = 5 and file size is 8, in second read you have to take only n-read i.e 5-4 = 1
            count = min(count, n - read) 
            
            # Copy from buf4 to buf.
            ## 4. I take those buf4 chars filled and append it to my final buf.
            buf[read:] = buf4[:count]
            read += count
        
        # we have return total num of characters read
        return read
    
            
            
                
