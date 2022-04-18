days_of_plunder=int(input())
daily_plunder=int(input())
expected_plunder_of_end=float(input())
gained_plunder=0

for day in range(1,days_of_plunder+1):
    gained_plunder+=daily_plunder
    if day%3==0:
        gained_plunder+=0.5*daily_plunder
    if day%5==0:
        gained_plunder-=gained_plunder*0.3

if gained_plunder>= expected_plunder_of_end:
    print(f"Ahoy! {gained_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {gained_plunder/(expected_plunder_of_end/100):.2f}% of the plunder.")
