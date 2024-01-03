# coding=utf-8
# @Time     : 16th December, 2023  21:30
# @Author   : Nick Z
# @Email    : nick_zz@qq.com
# @File     : 841.Keys and Rooms.py
# @Software : PyCharm 
# =======================================================
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True
        res = [False for _ in range(len(rooms))]
        res[0] = True

        def dfs(room, vis):
            nonlocal res, rooms
            if False not in res:
                return
            if room:
                for i in room:
                    if i not in vis:
                        res[i] = True
                        vis.append(i)
                        dfs(rooms[i], vis)

        dfs(rooms[0], vis=[0])
        return False not in res


if __name__ == "__main__":
    t = Solution()
    print(t.canVisitAllRooms([[1,3],[1,4],[2,3,4,1],[],[4,3,2]]))
