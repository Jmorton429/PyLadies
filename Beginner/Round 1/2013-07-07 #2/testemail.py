#!/usr/bin/python

import glob
from collections import defaultdict
import sys

# sets up initial empty dict of users
users = {}
# initializes dict of results from loops
results = defaultdict(list)
#list of mtas to loop through
mta_list = ["mta1/", "mta2/", "mta3/", "mta4/", "mta5/", "mta6/", "mta7/", "mta8/", "mta9/"]

#txt file should be list of uids and signup date/time in this format:
#uid,signupdate signuptime
uid_file = open('/tmp/rand200uid.txt')

#first loop through every userid and add to dict
for line in uid_file:
    uid, join_timestamp = line.split(',')
    users[uid] = join_timestamp[:-1]
 
#second loop through mta. logs are split up by mta. path looks
#like this: /storage_array/pmta-acct/archives/$mta/acct-2012-08-22-0000.log
for mta in mta_list:
    # loops through each line in the file to try to find the uid and "test_000"
    logpath = '/logs/archive/{0}/log-2012-08-*'.format(mta)
    # sorts all the log into dated order
    logs = sorted(glob.glob(logpath))
    #loops through logs
    for log in logs:
    	#outputs current log file to screen
        sys.stderr.write("{0}\n".format(log))
        #opens the log with only read capability
        f = open(log, 'r')
        #assigns record to each line of the log
        records = f.readlines()
        # loop through each line in records
        for record in records:
            #is that line a test?
            if "test_000" in record:
            	# loop through each uid in the list
                for uid in users.keys():
                    #if there's already a result for that uid/mta combo, continue to next uid
                    if mta in results[uid]: continue
                    # if the userid is in the record, add it to the dict
                    if str(uid) in record:
                    	# grabs just b or d and the send_time
                        success, send_time = record.split(',')[:2]
                        results[uid].append({'log':log, 'success':success, 'send_time':send_time})
                        sys.stderr.write("  Found mail from {0} at {1}\n".format(uid, send_time))

#prints out to uid
for uid in users.keys():
    if uid not in results:
        print "{0},None,0,0".format(uid)
    else:
        for message in results[uid]:
            print "{0},{1},{2},{3}".format(uid, users[uid], message['success'], message['send_time'])