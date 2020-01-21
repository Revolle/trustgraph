# trustgraph
Estimate an evaluation of trust, for any member in a non centralized network/graph.
## constraints
* a member knows only his list of contacts. 
* The member evaluates the trust for each of his contacts. 
* The evaluation given to his contacts is wieghted by his own evaluation :
  * if the member has a low evaluation in the network, his evaluation of his contacts does not matter so much
## objective
* a member must be able to estimate the evaluation of all members (contacts of contacts, recursively).
## methodology
* members receive/send tokens "permanently". These tokens capture information of the network/graph.
* When a member receives a token, the member :
  * adds a triplet to the token : member_id , evaluation , contact_id. Then he sends this token updated to the contact.
  * estimates evaluation of members, using the tokens already received
  * detects potential frauds, using the tokens already received
  * limits useless  "circular" movements of tokens in the network
## test
* evaluate_graph.py : Contribution from Vincent Yernaux. This python-script creates/display a complete graph (nodes, notes, edges oriented/valued between nodes). It makes a calculation of the trust for each node. It shows that the calculation can be stable after few iterations. This scripts needs to know the whole graph. To be done : for each node C - which knows only his contacts Ld(c) - , C should be able to discover by himself the whole graph (sending a token ?), calculate it like proposed in the script, and verify its result against Ld(C) (sending a token ?)
