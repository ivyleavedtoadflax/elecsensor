import dropbox,access_token

# For security the access token is included in a seprate file,
# to avoid accidentally posting it to github!

#access_token_file = open("/home/pi/Sensor/access_token","r")
#access_token = access_token_file.read()
#access_token_file.close()

access_token = access_token.token

# Check that we have access:

client = dropbox.client.DropboxClient(access_token)

def uploadLog(lpath,spath):
	f = open(lpath,'rb')
	response = client.put_file(spath, f, overwrite=True)

uploadLog("/home/pi/elec/Log_adu.csv","Log_adu.csv")
