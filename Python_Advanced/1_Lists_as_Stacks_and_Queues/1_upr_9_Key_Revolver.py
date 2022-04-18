from collections import deque
# Each bullet can unlock a lock with a size equal to or larger than the size of the bullet.
price_of_bullet=int(input())
size_gun_barrel=int(input())
bullets=[int(x) for x in input().split()] # quele
locks=deque([int(x) for x in input().split()])
value_of_intelligence=int(input())

used_bulets=0
"""If Sam runs out of bullets in his barrel, print "Reloading!" on the console, then continue shooting. 
If there aren't any bullets left, don't print it."""
counter_barrel=0
while bullets and locks:

    used_bulets += 1
    counter_barrel+=1
    current_shot=bullets.pop()
    current_lock=locks.popleft()

    if current_shot<=current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)
    if counter_barrel==size_gun_barrel and bullets:
        print("Reloading!")
        counter_barrel=0


costs=used_bulets*price_of_bullet
winn=value_of_intelligence-costs



if len(locks)==0:
    print(f"{len(bullets)} bullets left. Earned ${winn}")

else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

