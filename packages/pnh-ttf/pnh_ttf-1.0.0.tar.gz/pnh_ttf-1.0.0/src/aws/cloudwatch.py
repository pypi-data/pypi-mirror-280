import boto3
from botocore.exceptions import ClientError
from datetime import datetime


class CWManager:
    def __init__(self, alarm_name: str, start_date: datetime, end_date: datetime,
                 region: str = 'eu-west-1', profile: str = 'default'):
        """
        Initializes the CWManager with the specified alarm name and date range.

        Args:
            alarm_name (str): The name of the CloudWatch alarm.
            start_date (datetime): The start date for the alarm history query.
            end_date (datetime): The end date for the alarm history query.
            region (str, optional): AWS region. Defaults to 'eu-west-1'.
            profile (str, optional): AWS profile name. Defaults to 'default'.
        """
        self.alarm_name = alarm_name
        self.start_date = start_date
        self.end_date = end_date
        self.region = region
        self.profile = profile

        session = boto3.Session(profile_name=self.profile, region_name=self.region)
        self.cw_client = session.client('cloudwatch')

    def check_cloudwatch_alarm_state(self) -> dict:
        """
        Checks the state history of the specified CloudWatch alarm within the given date range.

        Returns:
            dict: A dictionary containing the status code and message indicating whether the alarm state changed to ALARM.
        """
        try:
            # Request the alarm history from CloudWatch
            response = self.cw_client.describe_alarm_history(
                AlarmName=self.alarm_name,
                HistoryItemType='StateUpdate',
                StartDate=self.start_date,
                EndDate=self.end_date,
                ScanBy='TimestampDescending'
            )

            # Extract the history items from the response
            alarm_history_items = response.get('AlarmHistoryItems', [])

            # Extract the summaries of each history item
            history_summaries = [item['HistorySummary'] for item in alarm_history_items]

            # Check if any history summary indicates a state change from OK to ALARM
            if any('Alarm updated from OK to ALARM' in summary for summary in history_summaries):
                return {
                    'statusCode': 200,
                    'statusMessage': "Alarm state changed to ALARM."
                }

            # Return a message if no alarm state change to ALARM was detected
            return {
                'statusCode': 400,
                'statusMessage': "No alarm action detected."
            }
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
