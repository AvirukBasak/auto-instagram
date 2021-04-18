# Login credentials
username = open ("user.txt", "r").readline ();

# open following file, make a followings list
Ffollowing = NULL
try:
    Ffollowing = open (username + "/following.list", "r")
except:
    print ("Could not locate file: " + username + "/following.list")
    exit ()
# Read data from file into a list
followings = Ffollowing.readlines ()
Ffollowing.close()

# open follower file, make a followers list
FFollowers = NULL
try:
    Ffollowers = open (username + "/followers.list", "r")
except:
    print ("Could not locate file: " + username + "/followers.list")
    exit ()
# Read data from file into a list
followers = Ffollowers.readlines ()
Ffollowers.close()

# unfollow list
unfollows = []

# get a following from followings list
for following in followings:
    unfollow = True
    # get a follower from followers list
    for follower in followers:
        # if the following is a follower
        if following == follower:
            # don't unfollow, ie unfollow flag false
            unfollow = False
            break
    # if unfollow flag isn't false, continue to next following
    if not unfollow:
        continue
    # else print that peep's ID, and add that peep to unfollows list
    else:
        print (following[:-1])
        unfollows.append (following)

# create unfollow file
Funfollow = NULL
try:
    Funfollow = open (username + "/unfollow.list", "w")
except:
    print ("Could not locate file: " + username + "/unfollow.list")
    exit ()

# write unfollows list to unfollow file
for unfollow in unfollows:
    Funfollow.write (unfollow)
    
Funfollow.close ()
