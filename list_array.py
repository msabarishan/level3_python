# Create a list with duplicates
lst=list(set(lst))

# List Comprehension.
new_list-=[[i,j,k] for in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

#Creating array list from array input
lst=list([a,b])

# Finding second largest score from nested array
if __name__ == '__main__':
    list2=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list2.append([name,score])
        
sort_list2=sorted(list2,key=lambda x: x[1])

sr=None
for i in range(1,len(sort_list2)):
    if sort_list2[i][1]>sort_list2[0][1]:
        sr=sort_list2[i][1]
        break
    
val=[x[0] for x in sort_list2 if x[1]==sr]
val=sorted(val)

for v in val:
    print(v)
    
# Round and Format
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    v=student_marks[query_name]
    avg= sum(v)/len(v)
    avg=round(avg,2)
    # Round does not bring 5.9 to 5.90. So use format
    f_avg="{:.2f}".format(avg)
    print(f_avg)
