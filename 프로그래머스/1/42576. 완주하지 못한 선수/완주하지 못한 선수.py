def solution(participant, completion):
    person={}
    
    for name in participant:
        person[name]=person.get(name,0)+1
    
    for name in completion:
        person[name]-=1
    
    for k, v in person.items():
        if v>0:
            return k