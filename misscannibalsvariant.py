from search import *


class MissCannibalsVariant(Problem):


    def __init__(self, N1=4, N2=4, goal=None):
        
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        if goal is None:
            goal = (0, 0, False)
        super().__init__(initial, goal)


    def actions(self, state):
        m, c, left = state
        valid_actions = []
        
        possible_actions = ['M', 'C', 'MM', 'MC', 'CC', 'MMM', 'MMC', 'MCC', 'CCC']
        
        if left:  
            for action in possible_actions:
                m_count = action.count('M')
                c_count = action.count('C')
                
                
                if m_count <= m and c_count <= c:
                    
                    newleft_m = m - m_count
                    newleft_c = c - c_count
                    newright_m = self.N1 - newleft_m
                    newright_c = self.N2 - newleft_c
                    
                    
                    if ((newleft_m == 0 or newleft_m >= newleft_c) and 
                        (newright_m == 0 or newright_m >= newright_c)):
                        valid_actions.append(action)
        
        else:  
            right_m = self.N1 - m
            right_c = self.N2 - c
            
            for action in possible_actions:
                m_count = action.count('M')
                c_count = action.count('C')
                
                
                if m_count <= right_m and c_count <= right_c:
                    
                    newleft_m = m + m_count
                    newleft_c = c + c_count
                    newright_m = self.N1 - newleft_m
                    newright_c = self.N2 - newleft_c
                    
                    
                    if ((newleft_m == 0 or newleft_m >= newleft_c) and 
                        (newright_m == 0 or newright_m >= newright_c)):
                        valid_actions.append(action)
        
        return valid_actions

    def result(self, state, action):
   
        m, c, left = state
        m_count = action.count('M')
        c_count = action.count('C')
        
        if left:  
            return (m - m_count, c - c_count, False)
        else:  
            return (m + m_count, c + c_count, True)


if __name__ == '__main__':
    mc = MissCannibalsVariant(4,4)
    print(mc.actions((3, 3, True)))  
    

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)