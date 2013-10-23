[October 14 Meetup](http://www.meetup.com/PyLadies-Boston/events/122655442/)
================

Subjects covered:
* APIs: Echonest & Twitter - [Jennifer Konikowski](https://github.com/jmkoni)

Questions from this meetup:
-----------------
Got some questions from an attendee and wanted to answer both directly and to the group in case more people were confused:
1.  How much of the syntax is determined by the entity (Twitter/echonest), and how much of it is determined by knowing python? I didn't understand the syntax of your requests - is that because I didn't read the documentation?

  The syntax is different for pretty much any API. On a base level, APIs have nothing to do with Python. The Python clients (python-twitter and pyechonest) are sorta like wrappers for the API (http://en.wikipedia.o...­, not the API itself. Part of understanding the syntax is based on reading the documentation.

  As far as API documentation and wrappers: you are likely not going to be able to follow documentation very easily, if at all right now. Most of them don't bother to be easy to understand, because documentation is a reference, not a guide. The best way is to google what you want and check out the stack overflow answers. However, that's still not going to make any sense until you learn the basics of programming. Gotta take it one step at a time :) Here's a quick explanation of wrappers: an API request tends to be bulky and ugly. Think of a wrapper as the pretty package that covers up the ugliness and presents it in a beautiful, pythonic way.

2.  What are the different parts of an API and what order do they go in? (authentication?, request/call?, output?)
  Order, like syntax, depends on the API. Generally authentication is first, followed by the request. The output is the response… so it's at the end :) Here's a breakdown:
    request = 'http://developer.echonest.com/api/v4/so­ng/search?api_key=12345&format=json&­results=1&min_danceability=0.4&s­ong_min_hotttnesss=0.4'

  http://developer.echo...­ - the url. this is the basis of any api call. For this one, you can see that you are looking at songs and in particular the search method.

  ?api_key=12345 - authentication. This tells the site owner who you are so they can track your use of their api

  format=json&results=1&min_danc­eability=0.4&song_min_hotttnesss=0.4­ - the request parameters. These are all the different things you are looking for. In this case a hot, danceable song… just one, in json format.

3.  How do we know an API "allows" python (you said Twitter doesn't usually use it)?
  APIs don't necessarily allow or disallow Python. The question about Twitter was asking if Twitter was developed in Python (it's not). They also didn't create a separate client like Echo Nest did, so this other guy (@bear on github) created one. The standard Twitter API call is similar to the Echo Nest one above, but it also requires that headers be sent, which gets a bit more complicated.

4.  How do we know if we generated our keys properly? How did keys work in Echonest? I only had two out of 4 keys from Twitter. I did something wrong. There wasn't really an opportunity to check this with anyone.
  To generate keys from twitter, go to dev.twitter.com, login with a twitter account, then go to https://dev.twitter.c...­. Create a new app. Call it whatever you want, give it whatever site you want (someone used ebay.com), click the "Details" tab, scroll to the bottom, then click "create my access token". Now if you go to the "Oauth Tools" tab, you will see your access keys.