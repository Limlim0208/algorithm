def solution(participant, completion):
    person={}
    
    for name in participant:
        person[name]=person.get(name,0)+1
    
    for name in completion:
        person[name]-=1
    
    for name in person:
        if person[name]>0:
            return name