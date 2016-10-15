"""
  Example for posting data to Device Cloud for data graphing, storage and analysis.
  (digi.com/products/cloud/digi-device-cloud)
  by Rob Faludi, faludi.com
"""

import time
import httpclient
import ubinascii

version = '1.0.0'


username = 'your username here' #enter your username!
password = 'your password here' #enter your password!


# Device Cloud connection info
url = 'http://devicecloud.digi.com/ws/v1/streams/history'
headers= {'authorization': 'Basic ' + auth}
stream_id = 'myStream'
stream_type = 'DOUBLE'
auth = ubinascii.b2a_base64(username + ':' + password).decode().strip() #base64 encoding


# posts data to Digi Device Cloud
def dc_post(data):
    json={"stream_id": stream_id, "stream_type": stream_type, "value": str(data)}
    r = httpclient.post(url, headers=headers, json=json)
    r.close()
    return r.status_code


# example program: posts 0 to 499 to a Device Cloud data stream
if __name__ == "__main__":
    
    for data in range(500):
        try:
            status = dc_post(data) # post data to Device Cloud
        except Exception as e:
            status = type(e).__name__ + ': ' + str(e)
            print('exception:', e)
        print('post', data, 'status:', status)
        time.sleep(1)
