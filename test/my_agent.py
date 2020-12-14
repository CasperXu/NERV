from base_agent import *
from reversi import *


class MyAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def step(self, obs, reward):
        '''
        def eat_amount(pos):
            cnt = 0
            d = 1
            tmp_cnt = 0
            while (obs[pos+d]==-obs[pos]) 
                tmp_cnt += 1
                d += 1
            if obs[pos+d] == obs[pos]:
                cnt += tmp_cnt 
            <<< and do the same thing when d = -1,8,-8,7,-7,9,-9 >>>
            return cnt
        def ��sboard  when place i and check if it will be eaten of not (i):
            return bool
        bad_move = {}bn 
        side = {}
        max_eats = []
        for pos in available:
            if i will be eat once place on it:
                bad_move.add(pos)
            if position of pos == {0,1,2,3,4,5,6,7,8,16,24,32,40,48,56,15,22,30,38,46,54,57,58,59,60,61,62,63}:<<<side>>>
                side.add(pos)
            max_eats.append({i:eat_amount(i)})
        place = side - bad_move
        �p�Gplace���O�Ŷ��X
        <<< �A�ӧ�Xplace�̭�max_eats�̦h���U >>>
        �p�Gplace�O�Ŷ��X�A��Xmax_eats�̭������bbad_move�̭���key��value�̰����U
        '''
    def same_row(i, j):
        return (i//8 == j//8)

    def same_col(i, j):
        return (i-j) % 8 == 0

    def same_dia(i, j):
        return i % 9 == j % 9 or i % 7 == j % 7:


if __name__ == '__main__':
    game = MyAgent()
    print