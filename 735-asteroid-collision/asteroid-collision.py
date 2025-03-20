class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = [asteroids[0]]
        for i in range(1,len(asteroids)):
            st.append(asteroids[i])
            while len(st) > 1 and ((st[-1] <0 and st[-2]>0)):
                if st[-1] == -st[-2]:
                    st.pop(-1)
                    st.pop(-1)
                elif abs(st[-1]) < abs(st[-2]):
                    st.pop(-1)
                else:
                    st.pop(-2)                
        return st
                
            