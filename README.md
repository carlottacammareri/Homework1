# Homework 1 Basic data Types-python


LIST COMPREHENSIONS

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print ([[a,b,c] for a in range (0, x+1)for b in range (0, y+1)for c in range(0,z+1)if a + b + c != n])
    
    
    
FIND THE RUNNER-UP SCORE

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print (sorted(set(arr))[-2])
    
    
    
FINDING THE PERCENTAGES

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
    
    
    
LISTS

if __name__ == '__main__':
    N = int(input())
    empty = []
    conv = []
    for i in range (N):
        x= input().split()
        empty.append(x)
    for i in range(len(empty)):
        if empty[i][0]== 'insert': 
            x = int(empty[i][1])
            y = int(empty[i][2])
            conv.insert(x,y)
        elif empty[i][0]== 'print':
            print(conv)
        elif empty[i][0] == 'remove':
            conv.remove(int(empty[i][1]))
        elif empty[i][0] == 'append':
            conv.append(int(empty[i][1]))
        elif empty[i][0] == 'sort':
            conv.sort()
        elif empty[i][0]== 'pop':
            conv.pop()
        elif empty[i][0]== 'reverse':
            conv.reverse()
            
            
NESTED LISTS

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    students = sorted(students, key = lambda x: x[1])
    second_lowest_score = sorted(list(set([x[1] for x in students])))[1]
    desidered_students = []
    for stu in students:
        if stu[1] == second_lowest_score:
            desidered_students.append(stu[0])
    print("\n".join(sorted(desidered_students)))



