from requests import session

#e_id means event_id
e_id = '20799626242'

url_prefix = 'https://www.eventbriteapi.com/v3/'

with session() as s:
 r = s.get(url_prefix+'events/'+e_id+'/attendees/?token='+'YWTHY73ZVEJOL6EVMZUF')
 f = open('attendees.csv','w')
 f.write('Email,Checkin_Status\n')
 for i in r.json()['attendees']:
 	f.write( i['profile']['email'] + "," + str(i['barcodes'][0]['checkin_type']) + "\n")
