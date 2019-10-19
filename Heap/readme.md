
# Heap 

Is a partially ordered dataset, 
where data is stored in a blanced binary tree in which (maxheap) the parent is larger than
its children. 



<img align="center" src="maxheap.png"/>


The most basic ingridient in heap datatype is adding a new element to an already existing heap. 
When we add an element we are traversing a single branch of the tree, at each step moving 
down the height of the tree, so we can do at most log(n) steps. 

At each step we will do a fixed number of operations (this is a binary tree so each node has at most two children)

How we add an element? We do a bubble sort on a shorter branch. We check if 
the our pivot is larger than the current node, if it is, then plug it in place of the
the node. And the element in the node becomes our pivot, and we proceed to examine it childeren. 
We again pick the largest element among the children and the pivot and plug it in, the replaced 
node is our new pivot.

If it happens that the pivot we begin with is smaller than the node, we just move down 
the generation and repeat our attempt to plug in the pivot. If we move all the way untill we hit 
the end of the tree we just plug in the pivot as a new leaf. 

Question: how do we insure the heap is balanced?     