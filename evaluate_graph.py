# -*- coding: utf8 -*-
import matplotlib.pyplot as plt
from math import *
import networkx as nx
from networkx.algorithms import bipartite
import random
import sys,copy


class tygone(object):
    "polygone à face triangulaire"
    def __init__(self,nnodes=6,nedges=20):
        secure_random=random.SystemRandom()
        self.G=nx.DiGraph()
        for i in range(nnodes):
            self.G.add_node(i,valeur=0,target=0)
        for i in range(nedges):
            lnodes=self.G.nodes()
            n1=secure_random.choice(lnodes)
            lnodes.remove(n1)
            n2=secure_random.choice(lnodes)
            valeur=secure_random.randrange(-10,10)
            if (not self.G.has_edge(n1,n2)): 
                self.G.add_edge(n1,n2,valeur=valeur)
        return
   
   
    def displaygraph(self,GR,pos=0,block=True,annotation=""): 
        if (len(GR.nodes())==0): return
        if (pos==0): pos=nx.spring_layout(GR)
        proprietegraph="taille: " + str(len(GR.nodes())) + " nodes \nconnectivity: " + str(nx.node_connectivity(GR)) + "\n" + "edge connectivity: " + str(nx.edge_connectivity(GR))
        if (annotation==""): plt.figure('Graphe',figsize=(8,8)).text(0,0,proprietegraph, fontsize=12)
        else: plt.figure(annotation,figsize=(8,8)).text(0,0,proprietegraph, fontsize=12)
        valeurs={}
        for n in self.G.nodes():
            if (self.G.node[n]["valeur"]>0):
                color='red'
            elif (self.G.node[n]["valeur"]<0):
                color='blue'
            else: color='green'
            nx.draw_networkx_nodes(GR,pos, nodelist=[n], node_color=color, node_size=500, alpha=0.8)
            valeurs[n]=int(ceil(self.G.node[n]["valeur"]))
        nx.draw_networkx_labels(GR,pos,labels=valeurs)
        for e in self.G.edges(data=True):
            if (e[2]["valeur"]<0):
                nx.draw_networkx_edges(GR, pos, edgelist=[e], edge_color="blue")
            elif (e[2]["valeur"]>0):
                nx.draw_networkx_edges(GR, pos, edgelist=[e], edge_color="red")
            else:
                nx.draw_networkx_edges(GR, pos, edgelist=[e], edge_color="green")
        edge_valeur=nx.get_edge_attributes(self.G,'valeur')
        nx.draw_networkx_edge_labels(GR, pos, edge_labels =edge_valeur)
        plt.axis('off')
        plt.show(block=block)
        return

        
    def compute_target(self):
        for n in self.G.nodes():
            if (len(self.G.predecessors(n))==0): continue
            target=0.0
            for p in self.G.predecessors(n):
                target_that_predecessor_wants=10*self.G.edge[p][n]["valeur"]
                fiability_predecessor=(self.G.node[p]["valeur"]+101)/(201) 
                target+=target_that_predecessor_wants*fiability_predecessor
            nco=len(self.G.predecessors(n))
            #self.G.node[n]["target"]=(target/nco)*((nco-0.9)/nco)
            self.G.node[n]["target"]=(target/nco)
        return
        
    def converge_target(self,method):
        delta2=0
        sign = lambda x: (x > 0) - (x < 0)
        for n in self.G.nodes():
            gaps=self.G.node[n]["target"]-self.G.node[n]["valeur"]
            if (method=='linear'):
                self.G.node[n]["valeur"]+=gaps  #valeur = target
            if (method=='sqrt'):
                self.G.node[n]["valeur"]+=sign(gaps)*sqrt(sign(gaps)*gaps)
            #if (self.G.node[n]["valeur"]<1): self.G.node[n]["valeur"]=1
            #if (self.G.node[n]["valeur"]>100): self.G.node[n]["valeur"]=100
            delta2+=gaps*gaps
        return delta2
        
    
 
        
if (len(sys.argv)>1): 
    nbnode=int(sys.argv[1]) 
    nbedge=int(sys.argv[2])  
else:
    nbnode=8
    nbedge=20
t1=tygone(nnodes=nbnode,nedges=nbedge)
#print (t1.G.edges(data=True))
pos=nx.spring_layout(t1.G)
t1.displaygraph(pos=pos,GR=t1.G,block=True,annotation='starting graph')
i=0
while(True):
    i+=1
    t1.compute_target()
    delta2=t1.converge_target('linear')
    if (delta2 < 1): break
    #print(t1.G.nodes(data=True))
    if (i%100==0): t1.displaygraph(pos=pos,GR=t1.G,block=True,annotation='setp '+str(i)+',delta='+str(delta2))

t1.displaygraph(pos=pos,GR=t1.G,block=True,annotation='graph at the end')

