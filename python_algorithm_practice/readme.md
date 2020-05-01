- Add two numbers (arithmetics, overflow)
- Longest substring without repeating characters (hash that stores when last used with two pointers start and end)
- Longest polyndromic substring (dynamic programmin j in range(n) and i in range(j), the memorization is over longest sequence that ends on j)
- Number of islands (connected component in a tree, mark places that you already has visited and anlayze each component using a tree)
- 3sum, 3 elements that sum up to a given number (sort and then ofr each element check with two indices if we have a match, alternativly if you have has for sum of two
then you can check using this hash and making sure you do not overcount)
- Product of array except self, you compute product from the left and product from the right
- Merge intervals (Given a collection of intervals, merge all overlapping intervals, sort by ending, scan from largest ending backwards, if another ending is between the start and the end of the interval merge.)
- k-closest point to origin, not clear what the challange is? (I can compute the distance then sort, this is not efficient 
alternativly you can heapify and then select the top k elements, heap is O(n) and k elements would be klog(n)) I do think there is 
an alternative algorithm that can do it without heap. So there are some variations of this. 
- Find median of an array without sorting you can do quicksort, at each point you know the proper location of the element, so all element to left of it are smaller and all elements to the right of it are larger. So if element is at location i you can know at which part is the median. 
- How to implement quick sort, you can do it in place select a pivot put it at the end of array, then scan from top and bottom swap number if they do not maintain the rule and decide on a stop codition if left> right, then swap right with the pivot. Continue to work on the subarrays. 
- Search in rotated sorted array the breaking point, similar to binary search 
- Meeting room given meeting intervals decide how many rooms you need. (Sort start and end time separatly but keep distinction, use stack to count maximum number of open intervals)
- Generate parentheses, for given number all possible combinations. (Use self.array to store all results, maintain the number of avaliable open and closed brackets run recursivly on all options, no need to optimize because you need to produce every combination. You can optimize if you append the results and return arrays, write "res_str + '('")
- Container with most water (I remember there are to pointers, you need to move the one that is smaller, because of the blocking nature the smaller is blocking the hight so changing the largers does not make sense)
- Group anagrams (anagrams are words that are built from the same letters)  (order letters lexicographically and store in a hash, return the hash, you can also keep count of letters an array of length 26 each element is a letter and store relative to count)
- Subarray sum equals to k (Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.) This suggest to use running integral (record running sum and look at difference 
that is expected to be equal to k, sum of two elements equals to k)
- insert delete rand O(1), (I remmember that there is and array when I remove an element I chop the last element and put it in its place, I have a hash with indices, and for random I just randomly pick a number the length of my array)
- Spiral matrix, return elements in spiral order (hard indexing, the nice trick that I ddin't remember is that when matrix is empty I return [] otherwise I append what the recurtion call returns).
- !! Decode string: like so "3[a]2[bc]", return "aaabcbc". This can be done with stack, number can be
- !! Letter combination of phone numbers, return all possible letter combinations. Recursion for each letter split according to number of options. result can be stored in self.results, actually implemented using a loop where
 you use previous results to trump combinations, for every element in results you append all possible continuations, then the results are this new array)
- Decode ways (memorization and recursion)
- !!! Permutations od distinct integers, return all possible permutations. (I can mark which elements I have alredy used and move down the recursion
the down side is that the length is fixed, but it is not very large, the problem is that the number of combinations is extremely large, I can store is self.results, I can also have a loop as before )
- Word search, search words in 2D array.    (Start where there are A in the outer layers and go done the recursion, mark the locations where you have been when you move down the recursion, use indices to keep locations)
- Reconstruct itinerary.  
(Sort according to lexicographical order so you always try to start with lower next interval, run recursion if you exhaust all combination return the result, you can remove element from the list, and in the recursion you can use index i 
to try the element I, also you need to pass the current target airport, one you get the solution terminate all recursions, 
return True and use the solution to construct the chain)
- Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. 
The replacement must be in place (Implemented it the second time around, just logic)
- Deep copy, the idea worked after many small corrections. 
- !!! Coin change the fewest amount of money. (This is a classical DP DP[amount] mininum number of coins for amount, the amount hsould be 
defined up to the size of the coin, and then you take minimum between all the options, you can initialize the DP with value of the coins
and then there is trick how you prosee upwards, I have to write this code and compute complexity)  I tried recursion solution, which for me is easiest to think of, 
the I tried loop solution looping over amount, this gave somewhat better results, and finally I tried to analyze the best code
that I looked up (this seems to be about how you cycle through the data they start with coins. ) This line "return dp[-1] if dp[-1] != float('inf') else -1"
 the idea is that cycling for each i in the amount over all coins is the same as cycling for each coin through all amounts.  
the difference is whether I'm using top down approach or bottom up approach. 
- Word ladder. I realized I don't know dijkstar, but I don't really need it. 
What I need is breadth first search which is to appendleft in a queue. I compare with my previous result. 
- !!! Word break. Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words. 
This seems to be DP problem. Use string starts with and chop the begining. Continue down the stream if you reach the
result terminate. This is top down.  The idea for bottom up is similar to coins. 
- Find dublicate files in system. This is using two hashes file names and dublicates, there is also a trick to keep the previous name, so when you encounter it another time 
you add the previous name and the current name as well.
- Time based key-value store.    Store key time values and return the one that is latest below timestamp. There is no delete 
so you can maintain sorted array and get timestamp that is the lates below given value. All timeset are strictly increasing. 
so I don't even need to sort the array will be already sorted so log(n) to find. Than in another array you need to store the keys. 
so two arrays, one sorted and anotherr with keys. So is the question asking for binary search? Get also has a key!
then hash and we append to each key the timestemps. 
- Largest product, numbering that covers all options before i in range(n) j in range to i. Covering that goes by width and 
does not store all smaller results. I did the expanding search  for j in range(1, n): # width for i in range(j, n): # end dp[i] = dp[i] * nums[i-j] if dp[i] > res: res = dp[i] but this didn;t help 
I'm getting time limit, not memory limit. There is a trick, since numbers are integers and the sequence can only growso I can keep the negative and positive numbers runming or start a new one.
- Task scheduler. This is annoying weird question Seems like I need to start with one that is most common, and try to insert them one by one. 
- Reverse linked list from position n to m in one pass. I can do it with que pushing nodes to a que and then taking them in the reverse order 
but this is looking at each node twice. Recursion, start and end. I did manage to come up with a recursive solution. I did recursive solution 
but one can also do step by step solution with 3 pointers. 
                    
                     


 
 
