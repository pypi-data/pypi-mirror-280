import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timedelta, timezone


class S3Manager:
    def __init__(self, file_name: str, bucket: str, object_name: str,
                 region: str = 'eu-west-1', profile: str = 'default'):
        """
        Initialize an S3Manager instance.

        Args:
            file_name (str): Local path to the file to be uploaded.
            bucket (str): The name of the S3 bucket.
            object_name (str): The name of the object to be created in the 
                S3 bucket.
            region (str, optional): AWS region. Defaults to 'eu-west-1'.
            profile (str, optional): AWS profile name. Defaults to 'default'.
        """
        self.file_name = file_name
        self.bucket = bucket
        self.object_name = object_name
        self.region = region
        self.profile = profile

        session = boto3.Session(profile_name=self.profile, region_name=self.region)
        self.s3_client = session.client('s3')

    def upload_file(self) -> dict:
        """
        Upload a file to an S3 bucket.

        Returns:
            dict: A dictionary containing the status code and status message.
        """
        try:
            # Attempt to upload the file to the specified S3 bucket and object name
            self.s3_client.upload_file(
                Filename=self.file_name,
                Bucket=self.bucket,
                Key=self.object_name
            )

            # Return a success message if the file was uploaded successfully
            return {
                'statusCode': 200,
                'statusMessage': (f"Successfully uploaded local file "
                                  f"'{self.file_name}' to S3 bucket "
                                  f"'{self.bucket}' as '{self.object_name}'.")
            }

        except (FileNotFoundError, OSError):
            # Handle the case where the local file was not found
            return {
                'statusCode': 400,
                'statusMessage': f"The local file '{self.file_name}' was not found."
            }
        except boto3.exceptions.S3UploadFailedError as e:
            # Handle specific S3 upload failure errors
            return {
                'statusCode': 400,
                'statusMessage': f"S3UploadFailedError: {e}"
            }
        except Exception as e:
            # Handle any other exceptions that occurred during the file upload
            return {
                'statusCode': 400,
                'statusMessage': f"An unexpected error occurred: {e}"
            }

    def check_file_exists(self) -> dict:
        """
        Check if the specified file exists in the S3 bucket and if it was 
        modified in the last one minute of UTC time.

        Returns:
            dict: A dictionary containing the status code and status message.
        """
        try:
            # Calculate the timestamp for one minute ago in UTC
            one_minute_ago = datetime.now(timezone.utc) - timedelta(minutes=1)

            # Get the object's metadata from S3 with IfModifiedSince parameter
            self.s3_client.head_object(
                Bucket=self.bucket,
                Key=self.object_name,
                IfModifiedSince=one_minute_ago
            )
            
            # If we reach here, the file exists and was modified since one minute ago
            return {
                'statusCode': 200,
                'statusMessage': f"File '{self.object_name}' exists."
            }

        except ClientError as e:
            error_code = e.response['Error']['Code'] if e.response else None
            
            if error_code == '304':
                # File exists but was not modified since one minute ago
                return {
                    'statusCode': 400,
                    'statusMessage': (f"File '{self.object_name}' exists but was not "
                                      f"modified within the last one minute of UTC time.")
                }
            elif error_code == '404':
                # File does not exist
                return {
                    'statusCode': 404,
                    'statusMessage': (f"File '{self.object_name}' not found in bucket "
                                      f"'{self.bucket}'.")
                }
            else:
                # Other client errors
                return {
                    'statusCode': 400,
                    'statusMessage': f"ClientError: {e}"
                }

        except Exception as e:
            # Handle any unexpected errors
            return {
                'statusCode': 400,
                'statusMessage': f"An unexpected error occurred: {e}"
            }
