"""" The force users struggle to remember which side is the different force users from because they switch them too often.
So you are tasked to create a web application to manage their profiles.
You should store information for every unique force user registered in the application.
You will receive several input lines in one of the following formats:
"{force_side} | {force_user}"
"{force_user} -> {force_side}"
The "force_user" and "force_side" are strings, containing any character.
If you receive "force_side | force_user":
•	If there is no such force user and no such force side -> create a new force side and add the force user to the corresponding side.
•	Only if there is no such force user in any force side -> add the force user to the corresponding side.
•	If there is such force user already -> skip the command and continue to the next operation.
If you receive a "force_user -> force_side":
•	If there is such force user already -> change their side.
•	If there is no such force user in any force side -> add the force user to the corresponding force side.
•	If there is no such force user and no such force side -> create new force side and add the force user to the corresponding side.
•	Then you should print on the console: "{force_user} joins the {force_side} side!".
You should end your program when you receive the command "Lumpawaroo". At that point, you should print each force side. For each side, print the force users.
In case there are no force users on a side, you shouldn't print the side information.
Input / Constraints
•	The input comes in the form of commands in one of the formats specified above.
•	The input ends when you receive the command "Lumpawaroo".
Output
•	As output for each force side, you must print all the force users.
•	The output format is:
"Side: {force_side}, Members: {force_users_count}
! {force_user1}
! {force_user2}
…
! {force_userN}"
•	In case there are NO force users on a side, don't print this side.
"""


force_side_dict = {}
command = input()

while not command == "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        user_is_part_of_the_force = False
        for value in force_side_dict.values():
            if force_user in value:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_side_dict:
                force_side_dict[force_side] = [force_user]
            else:
                force_side_dict[force_side].append(force_user)

    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for key, value in force_side_dict.items():
            if force_user in value:
                force_side_dict[key].pop(value.index(force_user))
        if force_side not in force_side_dict.keys():
            force_side_dict[force_side] = force_user
        else:
            force_side_dict[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

    command = input()

for force_side, force_user in force_side_dict.items():
    if len(force_user) > 0:
        print(f"Side: {force_side}, Members: {len(force_user)}")
        for user in force_user:
            print(f"! {user}")
