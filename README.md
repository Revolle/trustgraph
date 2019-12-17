# trustgraph
## summary
Calculate a trust between members of a graph
## constraints
* nobody owns (know) the whole content of the graph
* a member of a graph knows only his list of contacts part of the graph
## Description of the graph G
* A contact C has a list of contacts Ld(C) .
* All Contacts Ci which have C in their Ld(Ci) is part of a list Lh(C).
* In other terms, the contacts in Ld(C) and Lh(C) are the adjacent neighbors of the contact C.
* C gives - for each Ci of his list Ld(C) - a "qualification" Q(Ci) .
* The complete graph G contains all contacts Ci with all their oriented-valued relations Ld(Ci)
* C is only aware of his list Ld(C) and the qualifications Q(Ci) associated to Ld(C). C does not have the description of the whole graph G.
## objective
* any contact C must be able to know the list of all Ci part of G, with an estimation of their note N(Ci)
## Assumption about a function ftr: 
* for each contact C of graph  G : note N(C) = ftr(logs read in the tokens which cross C)
## methodology
* Each contact C of graph G can :
  * create a token T , with a log L, sent to one of the contacts Ci part of Ld(C)
  * receive a token Th (sent by Lh(C) ), anotates it with a log L, and  sent to one of the contacts Ci part of Ld(C)
## test
* evaluate_graph.py : Contribution from Vincent Yernaux. This python-script creates/display a complete graph (nodes, notes, edges oriented/valued between nodes). It makes a calculation of the trust for each node. It shows that the calculation can be stable after few iterations (with a correct function ftr) . This scripts needs to know the whole graph. To be done : for each node C - which knows only his contacts Ld(c) - , C should be able to discover by himself the whole graph (sending a token ?), calculate it like proposed in the script, and verify its result against Ld(C) (sending a token ?)
