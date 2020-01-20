# trustgraph
Estimate an evaluation of trust, for any contacts in a non centralized network.
## constraints
* a member knows only his list of contacts. 
* The member evaluates the trust for each of his contacts. 
## objective
* a member must be able to estimate the evaluation of all members (contacts of contacts, recursively).
## methodology
* When a member receives a token, he :
  * adds a triplet to the token : member_id , evaluation , contact_id
  * sends the token updated to the contact
  * estimates evaluation of members, using the tokens already received
  * detects potential frauds, using the tokens already received
## test
* evaluate_graph.py : Contribution from Vincent Yernaux. This python-script creates/display a complete graph (nodes, notes, edges oriented/valued between nodes). It makes a calculation of the trust for each node. It shows that the calculation can be stable after few iterations (with a correct function ftr) . This scripts needs to know the whole graph. To be done : for each node C - which knows only his contacts Ld(c) - , C should be able to discover by himself the whole graph (sending a token ?), calculate it like proposed in the script, and verify its result against Ld(C) (sending a token ?)
