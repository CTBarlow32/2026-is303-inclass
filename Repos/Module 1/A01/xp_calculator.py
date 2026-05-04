'''
Carter Barlow - IS 303 A01

XP Calculator
I am making a XP calculator that caculates how many more sessions
you need to play based on current XP, target XP, and XP earned per session.

Inputs:
-Player name (string)
-Current XP (integer)
-Target XP (integer)
-XP earned per session (integer)

Processes:
-(target XP - current XP) / XP per session

Outputs:
-Number of sessions needed to reach certain XP

'''

#Input:
player_name = input("Enter player name: ")
current_xp = int(input("Enter current XP: "))
target_xp = int(input("Enter Target XP: "))
xp_per_session = int(input("Enter XP earned per session: "))

#Process:
sessions_needed = (target_xp - current_xp) / xp_per_session

#Output:
print(f"{player_name} needs {sessions_needed:.2f} sessions to reach target XP.")