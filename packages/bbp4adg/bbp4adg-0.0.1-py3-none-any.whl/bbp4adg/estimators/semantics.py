from ..estimators import ArgumentationDecisionGraph

'''
verified function, 
2 parameters, 
parameter adg is of class ArgumentationDecisionGraph, 
parameter t is a tuple of (v1,v2,v3,..vi) where v is a tuple of (fi,vi), i is the feature index and vi is the value of the feature
return a verified adg
'''
def verified(adg, t):
    verified_ar = set()
    verified_r = set()

    for i in adg.arguments:
        if i[0] in t:
            verified_ar.add(i)
    for j in adg.relations:
        #  j[0]: ((fj,vj),yj) 
        if (j[0][0] in t) and (j[1][0] in t):
            verified_r.add(j)

    return ArgumentationDecisionGraph(verified_ar, verified_r)


'''
label argumentaion framework according to grounded semantics, 
parameter adg is of class ArgumentationDecisionGraph, 
adg.arguments is a set of tuples of (x, y), ((fi,vi), y)
adg.relations is a set of tuples of ((x1, y2), (x2, y2), etc.), ( ((fi,vi),yi), ((fj,vj),yj) )
'''
def grounded(adg):
    # adg_snapshot = copy.deepcopy(adg) # DEBUG ONLY
    #initialize set
    in_set = set()
    #initialize set
    out_set = set()
    #initialize set
    und_set = set()
    '''
    find roots of the graph 
    by iterate through the egdes 
    and put nodes don't have any incoming edges to in_set
    '''
    del_set = set()
    # i: ((fi,vi), yi)
    for i in adg.arguments:
        #  i:((fi,vi), yi)     x[1]:((fi,vi), yi)
        if i not in [x[1] for x in adg.relations]:
            #add new tuple to in_set
            in_set.add(i)
            #remove i from arguments
            # adg.arguments.remove(i)
            del_set.add(i)
    # print("del_set:", del_set)
    # print("adg.arguments before del:", adg.arguments)
    for i in del_set:
        adg.arguments.remove(i)
    #     print("deleting:", i)
    # print("adg.arguments after del:", adg.arguments)
    '''
    if in_set is empty, 
    put all nodes in und_set, 
    and return {'in': in_set, 'out': out_set, 'und': und_set}
    '''
    if len(in_set) == 0:
        for i in adg.arguments:
            und_set.add(i)
        return {'in': in_set, 'out': out_set, 'und': und_set}
    
    # reapeat 4 steps until no new arguments are added to in_set
    Flag = True
    cnt = 0

    while Flag:
        cnt += 1
        if(len(adg.arguments) == 0):
            # print('no more arguments')
            break
        # print('After break statement')
        '''
        step 1:
        reject argumetns attacked by accepted arguments:
        iterate through the nodes in in_set,
        and find the nodes that have incoming edges from the nodes in in_set, 
        and put them in out_set
        '''
        for i in in_set:
            for j in adg.relations:
                #  i:((fi,vi), yi)     j[0]:((fj,vj), yj)
                if i == j[0]:
                    del_set = set()
                    for k in adg.arguments:
                        #  k:((fk,vk), yk) 
                        if j[1] == k:
                            out_set.add(k)
                            #remove k from arguments
                            # adg.arguments.remove(k)
                            # print("step1 to be deleted", k)
                            del_set.add(k)
                    # print("step1 arguments before delete", adg.arguments)
                    for k in del_set:
                        adg.arguments.remove(k)
                    #     print("step1 deleting:", k)
                    # print("step1 arguments after delete", adg.arguments)
        # step2: find and remove attack relations outcoming from out_set
        for i in out_set:
            del_set = set()
            for j in adg.relations:
                if i == j[0]:
                    # adg.relations.remove(j)
                    del_set.add(j)
            # print("step2 relations before delete:",  adg.relations)
            for j in del_set:
                adg.relations.remove(j)
        # step3: find arguments still attacked and store in set atkd
        atkd = set()
        for i in adg.arguments:
            for j in adg.relations:
                if i == j[1]:
                    atkd.add(i)
        # step4: accept arguments attacked only by rejected arguments
        del_set = set()
        acptd = 0
        for i in adg.arguments:
            if i not in atkd:
                in_set.add(i)
                #remove i from arguments
                # adg.arguments.remove(i)
                del_set.add(i)
                acptd += 1
        if acptd == 0:
            # no accepted arguments then stop while loop
            Flag = False
        for i in del_set:
            adg.arguments.remove(i)

    for i in adg.arguments:
        und_set.add(i)
    return {'in': in_set, 'out': out_set, 'und': und_set}