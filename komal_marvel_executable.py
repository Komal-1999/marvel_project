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
    # i will be passed as a list 
    if(op=='='or op=='equal to'):
        return(df[df[col]==i[0]]['Character name'])
    elif(op=='>=' or op=='greater than equal to'):
        return(df[df[col]>=i[0]]['Character name'])
    elif(op=='<=' or op=='less than equal to'):
        return(df[df[col]<=i[0]]['Character name'])
    elif(op=='>' or op=='greater than'):
        return(df[df[col]>i[0]]['Character name'])
    elif(op=='<' or op=='les than'):
        return(df[df[col]<i[0]]['Character name'])   
    elif(op=='between'or'<,>'):
        return(df[(df[col]>i[0]) & (df[col]<i[1]) ]['Character name']) 

if  __name__ == "__main__":
    import requests
    import json
    import pandas as pd

    apk=input("enter yout apikey")
    hash=input("enter your hashkey")
    ts='1660755914'
    # calling function to create dataframe
    marvel_df=marvel_uni(ts,apk,hash)
    print(marvel_df.head())

    #calling function to filter the charachter based on condn
    col=input("give the column on which you want to filter")
    op=input("operation you want to perform")

    #splitting the input and converting each individual part int integer and then finally making a list
    i=[int(x) for x in (input("give the integer you want")).split(',')]

    charachter=marvel_filter(marvel_df,col,op,i)
    print("your charachter is ", charachter)






