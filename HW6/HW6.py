# PS398 Homework 6
# Matthias Orlowski
# 02/28/2012
    
"""Twetwork: A python script to search twitter user's network with a maximum path length of 2 """

#!/opt/local/bin/python2.7

import tweepy
import datetime

class Twetwork(object):
    
    def __init__(self,target,api = None):

        if api == None:
            self.api = self.getAuthorization()
        else:
            self.api = api

        self.root = self.api.get_user(target)
        self.name = str(self.root.screen_name)
        self.users =[[self.root.screen_name]]
        self.activities=[[self.getActivity(self.root)]]
        self.following = [[self.root.followers_count]]
        self.follower = [[self.root.friends_count]]

        self.networkExpand1()
        self.networkExpand2() # This works now for gruendinger's account. But for universal usage, I should add a check for rating limits. Maybe some day...

    def __str__(self):
        self.networkPrinter()

    
    def getAuthorization(self):
        """User prompt for authorization keys."""
        consumerKey = raw_input('Please enter your consumer key: ')
        consumerSecret = raw_input('Please enter your consumer secret: ')
        accessToken = raw_input('Please enter a valid access token: ')
        accessTokenSecret = raw_input('Please enter a corresponding secret: ')
        auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
        auth.set_access_token(accessToken,accessTokenSecret)
        api = tweepy.API(auth)
        return api


    def networkExpand1(self):
        """Expands the network by one path length of followers starting from given level."""
        followers = self.api.followers(id=self.root.screen_name)
        addUser = []
        addActivities = []
        addNumFollowing = []
        addNumFollowers = []

        for i in followers:
           try: 
               addUser.append(i.screen_name)
               addActivities.append(self.getActivity(i))
               addNumFollowing.append(i.friends_count)
               addNumFollowers.append(i.followers_count)
               pass
           
           except:
               continue

        self.users.append(addUser)
        self.activities.append(addActivities)
        self.following.append(addNumFollowing)
        self.follower.append(addNumFollowers)


    def networkExpand2(self):
        addUser = []
        addActivities = []
        addNumFollowing = []
        addNumFollowers = []
        for i in self.users[1]:
            try:
                followers = self.api.followers(id=i)
                for j in followers:
                    try:
                        addUser.append(j.screen_name)
                        addActivities.append(self.getActivity(j))
                        addNumFollowing.append(j.friends_count)
                        addNumFollowers.append(j.followers_count)
                        print j.screen_name
                        pass
                    except:
                        continue
            except:
                continue
                
        self.users.append(addUser)
        self.activities.append(addActivities)
        self.following.append(addNumFollowing)
        self.follower.append(addNumFollowers)

        
    def getActivity(self, id):
        """Function to be called on twitter user objects
        to retrieve their activity measured as tweets per day"""
        tweets = id.statuses_count
        subscription = id.created_at
        now = datetime.datetime.now()
        delta = now - subscription
        deltaSec = delta.total_seconds()
        deltaDays = round(deltaSec/86400)
        activity = tweets/(deltaDays + 1)
        return activity


    def mostFollowedFollower(self):
        """Returns most followed user among a the root's followers"""
        who = self.follower[1].index(max(self.follower[1]))
        return self.users[1][who]


    def mostFollowedFollower2(self):
        """Returns most followed user among a the root's followers
        of at most two degrees of separation.
        Activity is measured as tweets per day."""
        who1 = self.follower[1].index(max(self.follower[1]))
        who2 = self.follower[2].index(max(self.follower[2]))
        if self.follower[1][who1] > self.follower[2][who2]:
            return self.users[1][who1]
        elif self.follower[1][who1] < self.follower[2][who2]:
            return self.users[2][who2]
        else:
            return [self.users[2][who2],self.users[1][who1]]

        
    def mostActiveFollower(self):
        """Returns most active user among a the root's followers
        of at most two degrees of separation.
        Activity is measured as tweets per day."""
        who1 = self.activities[1].index(max(self.activities[1]))
        who2 = self.activities[2].index(max(self.activities[2]))
        if self.activities[1][who1] > self.activities[2][who2]:
            return self.users[1][who1]
        elif self.activities[1][who1] < self.activities[2][who2]:
            return self.users[2][who2]
        else:
            return [self.users[2][who2],self.users[1][who1]]


    def mostFollowedFollowing(self):
        """Returns most followed user among those the root follows."""
        friends = self.api.friends(id=self.root.screen_name)
        names = []
        follows = []
        for i in friends:
            names.append(i.screen_name)
            follows.append(i.followers_count)
        who = follows.index(max(follows))
        return names[who]

        
    def networkPrinter(self):
        out1 = str(self.mostFollowedFollower())
        out2 = str(self.mostFollowedFollower2())
        out3 = str(self.mostActiveFollower())
        out4 = str(self.mostFollowedFollowing())

        print """

        %s's twitter network.

        Path length: %i

        The most followed user that follows %s: %s

        The most followed user that has
        at most 2 degrees of separation from %s: %s

        The most active user that has
        at most 2 degrees of separation from %s: %s

        The most active user that %s target follows: %s
        
        """ %(self.name,len(self.users)-1,self.name,out1,self.name,out2, self.name, out3,self.name,out4)
