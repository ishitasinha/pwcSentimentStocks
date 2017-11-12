#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "897302319548702720-zavIOoB84vuWUKEpeuTGr6LpqZHoM59"
access_token_secret = "qEaZWgEpxM2GD4uAr8WZLjFkEQNVf13aP77bVJeNjnoxu"
consumer_key = "1T0XlEUt8mZyoNMRzkI2hf9rF"
consumer_secret = "WRZECG8iPhhPTthbbRtrpZHLCv5sOL8TOQ4Qu7sQH26ddN76rU"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
  
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Mercedes'])
