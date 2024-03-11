##[PCCP 기출문제] 1번 / 붕대 감기
def solution(bandage, health, attacks):
    maxHealth = health
    bandageTimer = 0
    attackCount = 0
    i = 1
    lastAttackTime = attacks[-1][0]
    
    while i < lastAttackTime + 1:            
        if attacks[attackCount][0] == i :
            health -= attacks[attackCount][1] 
            attackCount += 1
            bandageTimer = 0
        else :
            if maxHealth > health :
                health += bandage[1]
                bandageTimer += 1
            if bandageTimer == bandage[0] :
                health += bandage[2]
                bandageTimer = 0
            if maxHealth < health :
                health = maxHealth
            
        if health <= 0 :
            health = -1
            break
            
        i += 1    
    
    return health