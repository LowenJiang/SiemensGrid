import pandas as pd
import sqlite3

#read pandas

def telecomToPopu(filename):
    df = pd.read_csv(filename, sep='\t',header=None)
    df.columns=["id","time",'country','sms-in','sms-out','call-in','call-out','internet']
    df['time']=(df['time'] - df['time'].min())/1000
    df['date'] = filename[-9:-4]
    df['population'] = df['sms-in']+df['sms-out']+df['call-in']+df['call-out']+df['internet']
    df = df.drop(columns=['sms-in','sms-out','call-in','call-out','internet','country'])
    print(df)
    # export sql
    conn = sqlite3.connect('/Volumes/TOSHIBA EXT/Siemens project/Dataset/population.db')
    df.to_sql('December', conn, if_exists='append', index=False)
    #df.to_sql('population',conn, if_exists='append',index=False)
    conn.close()

telecomToPopu('/Volumes/TOSHIBA EXT/Siemens project/Dataset/Milan/sms-call-internet-mi-2014-01-01.txt')




