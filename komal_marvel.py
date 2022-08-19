import requests
import json
import pandas as pd
#URL from documentation
URL="http://gateway.marvel.com/v1/public/characters?limit=100"
#parameters
#time stamp taken from a site online
ts='1660755914'
private_key="f80b11e9580b61fa559c9054618717098b72065a"
public_key="eda4aaaba34072fd65190a13e76b2323"

#md5_hash is the md5 digest of timestamo+pricate_key+public_key
#calculated using online md5 generator
md5_hash="341c7bad6d8ac729660619e14efdcfad"
start=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z','1','2','3','4','5','6','7','8','9']
marvel=pd.DataFrame(columns=['Character name','event appearances/availability','series appearances/availability','stories appearances/availability','comics appearances/availability','Character id'])
for i in start:
    #print(i) - added for debugging
    params={'nameStartsWith':i,'ts':ts,'apikey':public_key, 'hash': md5_hash}

    #for the response
    response=requests.get(url=URL,params=params)   
    r=response.text
    data=json.loads(r)
    #print(len(data['data']['results']))
    ch_name=[]
    ch_id=[]
    comics=[]
    events=[]
    series=[]
    stories=[]
    col=[ch_name,events,series,stories,comics,ch_id,]
    for i in range(0,len(data['data']['results'])):
        ch_name.append(data['data']['results'][i]['name'])
        ch_id.append(data['data']['results'][i]['id'])
        comics.append(data['data']['results'][i]['comics']['available'])
        events.append(data['data']['results'][i]['events']['available'])
        series.append(data['data']['results'][i]['series']['available'])
        stories.append(data['data']['results'][i]['stories']['available'])


    m=pd.DataFrame(columns=['Character name','event appearances/availability','series appearances/availability','stories appearances/availability','comics appearances/availability','Character id'])
    '''marvel['Character']=ch_name
    marvel['Character id']=ch_id'''
    m['Character name']=ch_name
    m['Character id']=ch_id
    m['event appearances/availability']=events
    m['series appearances/availability']=series
    m['stories appearances/availability']=stories
    m['comics appearances/availability']=comics

    marvel=pd.concat([marvel,m])

    #print(m.head())

print(marvel.shape)
#data=response.text #Convert response to json file
#convert json to pandas
# marvel_df = pd.read_json(data, orient='records')

#print(data)

############### Activity 3 ################

def marvel_uni(ts,apk,hash):
    import requests
    import json
    import pandas as pd
    #URL from documentation, with limit=100 as given in documentation max limit can be 100
    URL="http://gateway.marvel.com/v1/public/characters?limit=100"

    start=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z','1','2','3','4','5','6','7','8','9']
    marvel=pd.DataFrame(columns=['Character name','event appearances/availability','series appearances/availability','stories appearances/availability','comics appearances/availability','Character id'])
    for i in start:
        #print(i)
        params={'nameStartsWith':i,'ts':ts,'apikey':apk, 'hash': hash}

        #for the response wwew use get, this was in documentation
        response=requests.get(url=URL,params=params)   
        r=response.text
        data=json.loads(r)
        #print(len(data['data']['results']))
        # creating list for different columns
        ch_name=[]
        ch_id=[]
        comics=[]
        events=[]
        series=[]
        stories=[]
        col=[ch_name,events,series,stories,comics,ch_id,]

        # fetch data from json file by traversing and appending in the courrect list
        # checked the interactive documentation to know where my reqd attribute is
        for i in range(0,len(data['data']['results'])):
            ch_name.append(data['data']['results'][i]['name'])
            ch_id.append(data['data']['results'][i]['id'])
            comics.append(data['data']['results'][i]['comics']['available'])
            events.append(data['data']['results'][i]['events']['available'])
            series.append(data['data']['results'][i]['series']['available'])
            stories.append(data['data']['results'][i]['stories']['available'])

        #create a dataframe for the following letter and then concat it into the main dataframe
        m=pd.DataFrame(columns=['Character name','event appearances/availability','series appearances/availability','stories appearances/availability','comics appearances/availability','Character id'])
        '''marvel['Character']=ch_name
        marvel['Character id']=ch_id'''
        m['Character name']=ch_name
        m['Character id']=ch_id
        m['event appearances/availability']=events
        m['series appearances/availability']=series
        m['stories appearances/availability']=stories
        m['comics appearances/availability']=comics

        marvel=pd.concat([marvel,m])
    return(marvel)

################ ACTIVITY 4 ################
def marvel_filter(df, col,op,i):
    '''if(condn[0]=='='):
        a='''
    if(op=='='):
        return(df[df[col]==i]['Character name'])
    elif(op=='>='):
        return(df[df[col]>=i]['Character name'])
    elif(op=='<='):
        return(df[df[col]<=i]['Character name'])
    elif(op=='>'):
        return(df[df[col]>i]['Character name'])
    elif(op=='<'):
        return(df[df[col]<i]['Character name'])    

