import boto3
from botocore.exceptions import ClientError


class LambdaManager:
    def __init__(self, lambda_name: str, payload: dict = None,
                 region: str = 'eu-west-1', profile: str = 'default'):
        """
        Initialize the LambdaManager instance.

        Args:
            lambda_name (str): The name of the AWS Lambda function.
            payload (dict, optional): The payload to be sent to the Lambda function. Default is None.
            region (str, optional): AWS region. Defaults to 'eu-west-1'.
            profile (str, optional): AWS profile name. Defaults to 'default'.
        """
        self.lambda_name = lambda_name
        self.payload = payload
        self.region = region
        self.profile = profile

        session = boto3.Session(profile_name=self.profile, region_name=self.region)
        self.lambda_client = session.client('lambda')

    def invoke_lambda(self) -> dict:
        """
        Invoke the AWS Lambda function synchronously and return the status of the invocation.

        Returns:
            dict: A dictionary containing the status code and status message.
                  - 'statusCode' (int): HTTP status code indicating the result of the invocation.
                  - 'statusMessage' (str): Status message describing the outcome of the invocation.
        """
        try:
            # Convert payload to JSON string if it's a dictionary
            payload = self.payload if isinstance(self.payload, (bytes, bytearray)) else str(self.payload)

            # Invoke the Lambda function with 'RequestResponse' invocation type
            response = self.lambda_client.invoke(
                FunctionName=self.lambda_name,
                InvocationType='RequestResponse',
                Payload=payload
            )
            status_code = response['StatusCode']

            if status_code == 200:
                return {
                    'statusCode': 200,
                    'statusMessage': f"Lambda function '{self.lambda_name}' ran successfully."
                }
            else:
                # Handle function errors, if any
                return {
                    'statusCode': 400,
                    'statusMessage': f"Lambda function error: {response.get('FunctionError', 'Unknown')}"
                }

        except ClientError as e:
            # Handle specific AWS Lambda client errors
            return {
                'statusCode': 400,
                'statusMessage': f"AWS Lambda ClientError: {e}"
            }

        except Exception as e:
            # Handle any unexpected errors
            return {
                'statusCode': 400,
                'statusMessage': f"An unexpected error occurred: {e}"
            }
