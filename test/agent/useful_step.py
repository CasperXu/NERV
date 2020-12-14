from base_agent import*


class useful_step():

    def __init__(self, width=600, height=600):
        self.rows = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.side_length = min(width, height)
        self.top_left = (0, 0)
        self.actions = self._init_action_set()
        self.status = {i: 0 for i in range(64)}
        self.cur_player = -1
        self.enum = {r+c: i+j*8 for j,
                     c in enumerate(self.cols) for i, r in enumerate(self.rows)}

    def _init_action_set(self):
        actions = {}
        for i, row in enumerate(self.rows):
            for j, col in enumerate(self.cols):
                x = 0.1 * self.side_length + 0.8 * \
                    (j+0.5) / 8 * self.side_length
                y = 0.1 * self.side_length + 0.8 * \
                    (i+0.5) / 8 * self.side_length
                actions[row+col] = tuple([sum(i)
                                          for i in zip(self.top_left, (x, y))])
        return actions

    def _is_available(self, label, flip=False):
        status = self.get_game_state()

        if status[self.enum[label]] == 2 and flip == False:
            return True

        if status[self.enum[label]] == 0 or status[self.enum[label]] == 2:
            return self._check_around(label, flip=flip)

        return False

    def _check_around(self, label, flip):
        is_avail = False
        status = self.get_game_state()
        row = int(self.enum[label] // 8)
        col = int(self.enum[label] % 8)
        for i in range(-1, 2):
            if row+i < 0 or row+i >= 8:
                continue
            for j in range(-1, 2):
                if col+j < 0 or col+j >= 8:
                    continue
                label = self.rows[row+i] + self.cols[col+j]
                if status[self.enum[label]] == -1 * self.cur_player:  # ??��?????�??????��??
                    if self._check_direction(row, col, i, j, flip=flip):
                        is_avail = True
        return is_avail

    def _check_direction(self, row, col, dx, dy, flip):
        '''
        沿�???????��???????��??????????�端???�????�?�?
        ???話就??��?�status
        '''
        is_avail = False
        status = self.get_game_state()
        x, y = [dx], [dy]
        while 0 <= row+x[-1] < 8 and 0 <= col+y[-1] < 8:
            label = self.rows[row+x[-1]] + self.cols[col+y[-1]]
            if status[self.enum[label]] == 0:
                break
            if status[self.enum[label]] == self.cur_player:
                if flip:
                    for r, c in zip(x, y):
                        self.status.update(
                            self.rows[row+r]+self.cols[col+c], self.cur_player)
                    is_avail = True
                    break
                else:
                    return True
            x.append(x[-1] + dx)
            y.append(y[-1] + dy)
        return is_avail

    def _get_available_actions(self):
        avail = []
        for row in self.rows:
            for col in self.cols:
                if self._is_available(row+col):
                    avail.append(row+col)
        return avail

    def get_game_state(self):
        return self.status

    def get_actions(self):
        return self.actions

    def update(self, label, cur_player):
        '''
        update  status
        '''
        self.status[self.enum[label]] == -1*cur_player
