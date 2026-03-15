from graph import Graph

'''An instance of NodeCover has the syntax: I = G;N

where 
G is an undirected, unweighted graph defind as a sequence of edges (for
example: 'a,b a,c c,d' )
 
N is the size of a subset S of the nodes in the graph.

I is a positive instance of NodeCover is there is a subset S of the
nodes of G, |S| <= N, such that every edge in G has a an endpoint in
a node in S. For example, 'a,b a,c c,d;2' is a positive instance of NodeCover,
because every edgepoint in the graph has an endpoint in {a,c}, and
|{a,c}| = 2; 'a,b a,c c,d;1' is a negative instance of NodeCover because
there is no node of the graph that is an endpoint of all the edges.
 '''

DEV = False    # DEV ==  diagnostics for testing and debugging
VERBOSE = True # VERBOSE == output that explains what program does

vncV = "VERBOSE: VfyNodeCover() - " #tag for verbose output
vncD = "DEV: VfyNodeCove() - " #tag for dev output

def printV(text):
    if VERBOSE: print(f'{vncV}{text}')
    return

def printD(text):
    if DEV: print(f'{vncD}{text}')
    return
    
def vfyNodeCover(I,S,H):

    S_len = len(S)
    H_len = len(H)
    ### L0311 -- replace "False" with a reasonable length test
    if H_len > len(I) or S_len > len(I):
        s = f'Solution length {S_len} or hint length {H_len} '
        printV(f'{s} is unreasonable')
        return 'unsure'
    
    ### L0311 -- replace "False" with a test to ensure that the caller
    ### is attempting to verify a positive instance.
    if S == 'no':
        printV(f'The solution "{S}" is not verifying a positive instance')
        return 'unsure'

    (G,N) = I.split(';')
    N = int(N)
    node_cover = H.split() # H is a white-spaced delimited list of nodes
    #
    ### L0311 -- replace False to verify that the size of the proposed
    ### node cover subset is less than or equal to the maximum.
    ### If not, return 'unsure' after generating this verbose output:
    ###     f'{n} nodes in Hint but {N} is the maximum allowed'
    ### where "n" is the number of nodes in the hint

    if False:
        printV(f'{len(node_cover)} nodes in Hint but {N} is the maximum allowed')
        return 'unsure'
        
    g = Graph(G, directed=False, weighted=False)
    nodes = list(g.nodes.keys()) # create list of graph's node names
    #
    ### L0311 -- add code to verify that every node in the hint is also
    ### in the graph
    ### If not, return 'unsure' after generating this verbose output:
    ###     (f'{node} in hint but not in graph'
    ###  where "node" is in the hint but not the graph.
    ###
    
    pass #replace this with required code
    
    edges = G.split()
    
    ### L0311 -- add code to  verify that one or both of the endpoints
    ### of every edge is in node_cover (initialized above). 
    ### If not, return 'unsure' after generating this verbose output:
    ###     f'Edge "{ends[0]}——{ends[1]}" not covered'
    ### where "ends" is a list or tuple of an edges's end points
    ###
    
    pass #replace this with required code
    
    printV(f'"{I}" is a positive instance, all verifications succeeded')
    return 'correct' 

if __name__ == '__main__':

    def test_case(func,I,S,H,expected,num,comment=''):
        err = '** '
        result = func(I,S,H)
        func_name = str(func).split()[1]
        func_call = f'''{func_name}("{I}","{S}","{H}")'''
        if result == expected: err = ''
        e = expected
        print (f'{err}test #{num} {func_call}: expected "{e}", received "{result}"')
        print (f'test #{num} Explanation: {comment}\n')
        return num+1
    
    F = vfyNodeCover

    I = 'a,b  a,c b,c;2'
    num = 1
    exp = 'Solution length unreasonable'
    num = test_case(F,I,'maybe','a b','unsure',num,exp)
        
    I = 'a,b  a,c b,c;2'
    exp = 'Not attempting to verify a positive instance'
    num = test_case(F,I,'no','a b','unsure',num,exp)

    I = 'a,b  a,c b,c;2'
    exp = '|{a,b,c}| = 3 > target size'
    num = test_case(F,I,'yes','a b c','unsure',num,exp)

    I = 'a,b  a,c b,c c,d;2'
    exp = 'Nodes {a,b} does not cover edge c,d'
    num = test_case(F,I,'yes','a b','unsure',num,exp)

    I = 'a,b  a,c b,c;2'
    exp = 'd not in graph'
    num = test_case(F,I,'yes','a d','unsure',num,exp)
    
    I = 'a,b  a,c b,c;2'
    exp = '{a,b} covers graph'
    num = test_case(F,I,'yes','a b','correct',num,exp)

    
