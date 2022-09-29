from cgi import test
from typing import ClassVar
import boto3
import boto.s3.connection
from io import StringIO
import pandas as pd

"""s3 BUCKET CONNECTION"""

access_key =  'AKIAR4UTGZ7GXC7YYA5X'
secret_key =  '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'

conn = boto.connect_s3(

       aws_access_key_id= 'AKIAR4UTGZ7GXC7YYA5X' ,
       aws_secret_access_key= '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'
)

"""CREATING A BUCKET"""

bucket1 = conn.create_bucket('maddy21')

"""GETTING  THE BUCKET OBJECT"""

bucket2 = conn.get_bucket('maddy21')


"""LOADING CSV FILE IN S3"""

hc = pd.read_csv('C:/Users/91800/Desktop/data engineer/output1.csv')


s3 = boto3.client('s3', aws_access_key_id='AKIAR4UTGZ7GXC7YYA5X',
    aws_secret_access_key= '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'
)

csv_buf = StringIO()

hc.to_csv(csv_buf, header = True, index = False )

csv_buf.seek(0)
s3.put_object(Bucket='maddy21', Body = csv_buf.getvalue(), Key = 'test.csv')

