# PS398 Homework 7
# Matthias Orlowski
# 03/20/2012
    
"""Twetwork: A python script to search twitter user's network with a maximum path length of 2 and store the results in a sql database """

#!/opt/local/bin/python2.7

import tweepy
import datetime
import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

from time import sleep

# create data base
dbase = sqlalchemy.create_engine('sqlite:////twetwork.db', echo=True)

Base = declarative_base()

# create user data base class
class TWUser(Base):
    __tablename__ = 'twuser'

    id = Column(Integer,primary_key=T)
    tw_id = Column(Integer,unique = T)
    name = Column(String)
    activities = Column(Float)
    following = Column(Integer)
    follower = Column(Integer)
    crawled = Column(Integer, default = 0)

    # create relation to schemes for nodes
    node = Column(Integer, ForeignKey("tworknode.id"))

    def __init__(self,node,tw_id,name,activities,following,follower):
        self.node = node
        self.tw_id = tw_id
        self.name = name
        self.activities= activities
        self.following = following
        self.follower = follower


class TWorkNode(Base):
    __tablename__ = 'tworknode'

    id = Column(Inteher,primary_key=T, unique=T)
    users = relationship("TWUser", backref="tworknode")


#
class Twetwork(object):
    
    def __init__(self,target,api = None,n = 2):

        if api == None:
            self.api = self.getAuthorization()
        else:
            self.api = api

        self.session = None
        self.nodes = n
        
        # execute functions to built up network
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

    def pauseCrawling(self,session):
        """Function that writes memory to disc and pauses crawling for one hour."""
        lastNode = session.query(TWUser)
        sleep(7200)
        self.networkExpand(lastNode)


    def startSession(self):
        """Function to start data base session."""
        Session = sessionmaker(bind=dbase) # data base is hardcoded
        self.session = Session()


    def endSession(self):
        """Function to end data base session."""
        self.session.commit()

        
    def getRoot(self):
        """Function to create parent user"""
        root = self.api.get_user(self.target)
        tw_id = root.id
        name = str(root.screen_name)
        activities = self.getActivity(root)
        following = root.followers_count
        follower = root.friends_count
        self.startSession()
        parent = TWUser(1,tw_id,name,activities,following,follower)
        self.endSession()


    def networkExpand(self,n):
        """Expands the network by n nodes"""
        
        limit = self.api.rate_limit_status()['remaining_hits']
        toCheck = True
        n = n
        while not toCheck == False and limit > 10 and node <= n:
            toCheck = session.query(User).filter(User.crawled == 0)
            self.startSession()
            lastPlayer = toCheck.first()
            node = lastPlayer.first().node + 1
            followers = self.api.followers(id=lastPlayer.tw_id)
            limit = self.api.rate_limit_status()['remaining_hits']
            for i in followers:
                try: 
                    name = i.screen_name
                    activities = self.getActivity(i)
                    following = i.friends_count
                    follower = i.followers_count
                    session.add(User(node,name,activities,following,follower))
                    pass
           
                except:
                    continue
            lastPlayer.crawled = 1
            self.endSession()
        if limit <= 10 & not toCheck == False and node <= n:
            self.pauseCrawling()

        
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
