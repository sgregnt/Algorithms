

# Heap 

Is a partially ordered dataset, 
where data is stored in a binary tree in which (maxheap) the parent is larger than
its children. 

<img align="center" src="maxheap.png"/>

<style TYPE="text/css">code.has-jax {font: inherit; font-size: 100%; background: inherit; border: inherit;} </style>
The main ingridient is how to add a new element into an existing heap (say, maxheap)
While we try to add an element we travese the depth of the tree, so we do at most $log(n)$


