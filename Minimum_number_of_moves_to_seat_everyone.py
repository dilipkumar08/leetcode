class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res=0
        for i in range(len(seats)):
            res+=abs(seats[i]-students[i])
        return res

----------------------------------------------------------

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        mx=max(max(seats),max(students))+1
        seat_count=[0]*mx
        student_count=[0]*mx

        for i in seats:
            seat_count[i]+=1
        for j in students:
            student_count[j]+=1
        
        se,st=0,0
        res=0
        temp=len(seats)
        while temp:
            if seat_count[se]==0:
                se+=1
            if student_count[st]==0:
                st+=1
            if seat_count[se] and student_count[st]:
                res+=abs(se-st)
                seat_count[se]-=1
                student_count[st]-=1
                temp-=1
        return res
        
