records = {}

while True:
    command = input().split(": ")
    if "Log out" in command:
        break

    elif "New follower" in command:
        username = command[1]
        if username not in records:
            records[username] = {}
            records[username]["likes"] = 0
            records[username]["text"] = 0
        else:
            continue

    elif "Like" in command:
        username = command[1]
        likes_number = int(command[2])
        if username not in records:
            records[username] = {}
            records[username]["likes"] = likes_number
            records[username]["text"] = 0
        else:
            records[username]["likes"] += likes_number

    elif "Comment" in command:
        username = command[1]
        if username not in records:
            records[username] = {}
            records[username]["likes"] = 0
            records[username]["text"] = 1
        else:
            records[username]["text"] += 1

    elif "Blocked" in command:
        username = command[1]
        if username not in records:
            print(f"{username} doesn't exist.")
        else:
            del records[username]

print(f"{len(records)} followers")
for username, value in records.items():
    likes = records[username]["likes"]
    text = records[username]["text"]
    print(f"{username}: {likes + text}")

