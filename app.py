import json

# READ FILE followers_1.json and following.json
with open('followers_1.json', 'r') as file:
    follower_data = json.load(file)

with open('following.json', 'r') as file:
    following_data = json.load(file)
if "relationships_following" in following_data:
    following_data = following_data["relationships_following"]

# VARIABLE FOR FOLLOWER AND FOLLOWING
who_follower = set()
who_following = set()

# FOR TAKE AND ADD LINK HREF FROM JSON DATA TO VARIABLE
for follower in follower_data:
    for string_data_follower in follower["string_list_data"]:
        who_follower.add(string_data_follower["href"])

for following in following_data:
    if isinstance(following, dict) and "string_list_data" in following:
        for string_data_following in following["string_list_data"]:
            if "href" in string_data_following:
                who_following.add(string_data_following["href"])

# CHECK PEOPLE WHO PEOPLE NOT FOLLOW BACK
who_not_follback = who_following.difference(who_follower)

print(f"Amount People Follow:", len(who_follower))
print(f"Amount People Following:", len(who_following))
print(f"Who not follback:")
for this_the_people in who_not_follback:
    print(this_the_people)
print(f"Amount People Not Follback:", len(who_not_follback))
