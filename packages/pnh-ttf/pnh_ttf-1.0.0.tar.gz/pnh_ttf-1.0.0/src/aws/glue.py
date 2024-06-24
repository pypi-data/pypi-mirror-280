import time
import boto3
from botocore.exceptions import ClientError


class GlueManager:
    def __init__(self, crawler_name: str, max_attempts: int = 10, delay: int = 30,
                 region: str = 'eu-west-1', profile: str = 'default'):
        """
        Initialize a GlueManager instance to manage AWS Glue crawlers.

        Args:
            crawler_name (str): The name of the AWS Glue crawler.
            max_attempts (int, optional): Maximum number of attempts to check the crawler status. Default is 10.
            delay (int, optional): Delay in seconds between status checks. Default is 30 seconds.
            region (str, optional): AWS region. Defaults to 'eu-west-1'.
            profile (str, optional): AWS profile name. Defaults to 'default'.
        """
        self.crawler_name = crawler_name
        self.max_attempts = max_attempts
        self.delay = delay
        self.region = region
        self.profile = profile

        session = boto3.Session(profile_name=self.profile, region_name=self.region)
        self.glue_client = session.client('glue')

    def check_crawler_status(self) -> dict:
        """
        Checks the status of an AWS Glue crawler.

        Returns:
            dict: A dictionary containing the status code and status message.
        """
        attempts = 0
        while attempts < self.max_attempts:
            time.sleep(self.delay)

            try:
                # Get the current status of the AWS Glue crawler
                response = self.glue_client.get_crawler(
                    Name=self.crawler_name
                )

                crawler_state = response['Crawler']['State']

                if crawler_state == 'READY':
                    last_crawl_status = response['Crawler'].get('LastCrawl', {}).get('Status')
                    if last_crawl_status == 'SUCCEEDED':
                        return {
                            'statusCode': 200,
                            'statusMessage': f"Crawler {self.crawler_name} completed successfully."
                        }
                    elif last_crawl_status in ['CANCELLED', 'FAILED']:
                        return {
                            'statusCode': 400,
                            'statusMessage': f"Crawler {self.crawler_name} failed with status: {last_crawl_status}."
                        }

                attempts += 1
            except ClientError as e:
                # Handle ClientError exceptions from boto3
                return {
                    'statusCode': 400,
                    'statusMessage': f"ClientError: {e}"
                }
            except Exception as e:
                # Handle any other exceptions that occurred during the process
                return {
                    'statusCode': 400,
                    'statusMessage': f"An unexpected error occurred: {e}"
                }

        # Return a message if max attempts were reached without successful completion
        return {
            'statusCode': 400,
            'statusMessage': f"Max attempts '{self.max_attempts}' reached for checking crawler {self.crawler_name} status."
        }
