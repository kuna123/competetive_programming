# competetive_programming
There are N particls present on the x axis, eachi particle has two 
properties associated with it, i.e, the Position of the particle and
its Attraction-Value

The Attraction-Force between two particls i and j defined as:

Attraction-Force(i,j)= Distance(i,j) * MAX (Attraction-Value[i], Attraction-Value[j])

Since all of them are in a straight line, distance between any 2 particles is equal to the 
absolute difference between their positions.


Can you do it?
Input Format:

The first line contains a single integer N, which denotes the number of particles. 
Each of the next lines contain 2 integer separated by space, where the 1st of them denotes the
Attraction-Value of the particle , and the 2nd one representes its positions.

Output Format:
print the required answer in a single line
