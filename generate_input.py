def get_table():
    '''
        A->C C
        C->c C
        C->d
    '''
    
    l = [{"c":"s3","d":"s4","A":"1","C":"2","$":""},{"c":"","d":"","$":"accept","A":"","C":""},\
         {"c":"s3","d":"s4","$":"","A":"","C":"5"},{"c":"s3","d":"s4","$":"","A":"","C":"6"},\
         {"c":"r3","d":"r3","$":"","A":"","C":""},{"c":"","d":"","$":"r1","A":"","C":""},\
         {"c":"r2","d":"r2","$":"","A":"","C":""}]
    return l
    
    '''
        E->E + T
        E->T
        T->T * F
        T->F
        F->( E )
        F->id
    '''
    '''
    l = [{"id":"s5","(":"s4","E":"1","T":"2","F":"3"},\
         {"+":"s6","$":"accept"},\
         {"+":"r2","*":"s7",")":"r2","$":"r2"},\
         {"+":"r4","*":"r4",")":"r4","$":"r4"},\
         {"id":"s5","(":"s4","E":"8","T":"2","F":"3"},\
         {"+":"r6","*":"r6",")":"r6","$":"r6"},\
         {"id":"s5","(":"s4","T":"9","F":"3"},\
         {"id":"s5","(":"s4","F":"10"},\
         {"+":"s6",")":"s11"},\
         {"+":"r1","*":"s7",")":"r1","$":"r1"},\
         {"+":"r3","*":"r3",")":"r3","$":"r3"},\
         {"+":"r5","*":"r5",")":"r5","$":"r5"}]
    return l
    '''
    '''
        E->E * B
        E->E + B
        E->B
        B->0
        B->1
    '''
    '''l = [{"*":"","+":"","0":"s1","1":"s2","$":"","E":"3","B":"4"},\
         {"*":"r4","+":"r4","0":"r4","1":"r4","$":"r4","E":"","B":""},\
         {"*":"r5","+":"r5","0":"r5","1":"r5","$":"r5","E":"","B":""},\
         {"*":"s5","+":"s6","0":"","1":"","$":"accept","E":"","B":""},\
         {"*":"r3","+":"r3","0":"r3","1":"r3","$":"r3","E":"","B":""},\
         {"*":"","+":"","0":"s1","1":"s2","$":"","E":"","B":"7"},\
         {"*":"","+":"","0":"s1","1":"s2","$":"","E":"","B":"8"},\
         {"*":"r1","+":"r1","0":"r1","1":"r1","$":"r1","E":"","B":""},\
         {"*":"r2","+":"r2","0":"r2","1":"r2","$":"r2","E":"","B":""}]
    return l'''
def get_grammar():
    l = []
    fin = open("input.txt","r")
    for line in fin.readlines():
        l.append(line.strip())
    return l
if __name__ == "__main__":
    get_grammar()
    
