class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_one=0
        students_zero=0
        sandwiches_one=0
        sanwiches_zero=0
        sl=len(sandwiches)
        stl=len(students)
        if sl!=0 and stl!=0:

            while sandwiches[0] in students:
                if sandwiches[0]==students[0]:
                    sandwiches.pop(0)
                    students.pop(0)
                    stl-=1
                    sl-=1
                else:
                    students.append(students[0])
                    students.pop(0)
                if sl==0:
                    break  
        return stl
        
