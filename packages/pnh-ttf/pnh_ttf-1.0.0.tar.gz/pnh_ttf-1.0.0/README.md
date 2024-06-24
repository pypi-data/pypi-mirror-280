# Table of Contents

* [aws](#aws)
* [aws.glue](#aws.glue)
  * [GlueManager](#aws.glue.GlueManager)
    * [\_\_init\_\_](#aws.glue.GlueManager.__init__)
    * [check\_crawler\_status](#aws.glue.GlueManager.check_crawler_status)
* [aws.lambda](#aws.lambda)
  * [LambdaManager](#aws.lambda.LambdaManager)
    * [\_\_init\_\_](#aws.lambda.LambdaManager.__init__)
    * [invoke\_lambda](#aws.lambda.LambdaManager.invoke_lambda)
* [aws.cloudwatch](#aws.cloudwatch)
  * [CWManager](#aws.cloudwatch.CWManager)
    * [\_\_init\_\_](#aws.cloudwatch.CWManager.__init__)
    * [check\_cloudwatch\_alarm\_state](#aws.cloudwatch.CWManager.check_cloudwatch_alarm_state)
* [aws.s3](#aws.s3)
  * [S3Manager](#aws.s3.S3Manager)
    * [\_\_init\_\_](#aws.s3.S3Manager.__init__)
    * [upload\_file](#aws.s3.S3Manager.upload_file)
    * [check\_file\_exists](#aws.s3.S3Manager.check_file_exists)

<a id="aws"></a>

# aws

<a id="aws.glue"></a>

# aws.glue

<a id="aws.glue.GlueManager"></a>

## GlueManager Objects

```python
class GlueManager()
```

<a id="aws.glue.GlueManager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(crawler_name: str,
             max_attempts: int = 10,
             delay: int = 30,
             region: str = 'eu-west-1',
             profile: str = 'default')
```

Initialize a GlueManager instance to manage AWS Glue crawlers.

**Arguments**:

- `crawler_name` _str_ - The name of the AWS Glue crawler.
- `max_attempts` _int, optional_ - Maximum number of attempts to check the crawler status. Default is 10.
- `delay` _int, optional_ - Delay in seconds between status checks. Default is 30 seconds.
- `region` _str, optional_ - AWS region. Defaults to 'eu-west-1'.
- `profile` _str, optional_ - AWS profile name. Defaults to 'default'.

<a id="aws.glue.GlueManager.check_crawler_status"></a>

#### check\_crawler\_status

```python
def check_crawler_status() -> dict
```

Checks the status of an AWS Glue crawler.

**Returns**:

- `dict` - A dictionary containing the status code and status message.

<a id="aws.lambda"></a>

# aws.lambda

<a id="aws.lambda.LambdaManager"></a>

## LambdaManager Objects

```python
class LambdaManager()
```

<a id="aws.lambda.LambdaManager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(lambda_name: str,
             payload: dict = None,
             region: str = 'eu-west-1',
             profile: str = 'default')
```

Initialize the LambdaManager instance.

**Arguments**:

- `lambda_name` _str_ - The name of the AWS Lambda function.
- `payload` _dict, optional_ - The payload to be sent to the Lambda function. Default is None.
- `region` _str, optional_ - AWS region. Defaults to 'eu-west-1'.
- `profile` _str, optional_ - AWS profile name. Defaults to 'default'.

<a id="aws.lambda.LambdaManager.invoke_lambda"></a>

#### invoke\_lambda

```python
def invoke_lambda() -> dict
```

Invoke the AWS Lambda function synchronously and return the status of the invocation.

**Returns**:

- `dict` - A dictionary containing the status code and status message.
  - 'statusCode' (int): HTTP status code indicating the result of the invocation.
  - 'statusMessage' (str): Status message describing the outcome of the invocation.

<a id="aws.cloudwatch"></a>

# aws.cloudwatch

<a id="aws.cloudwatch.CWManager"></a>

## CWManager Objects

```python
class CWManager()
```

<a id="aws.cloudwatch.CWManager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(alarm_name: str,
             start_date: datetime,
             end_date: datetime,
             region: str = 'eu-west-1',
             profile: str = 'default')
```

Initializes the CWManager with the specified alarm name and date range.

**Arguments**:

- `alarm_name` _str_ - The name of the CloudWatch alarm.
- `start_date` _datetime_ - The start date for the alarm history query.
- `end_date` _datetime_ - The end date for the alarm history query.
- `region` _str, optional_ - AWS region. Defaults to 'eu-west-1'.
- `profile` _str, optional_ - AWS profile name. Defaults to 'default'.

<a id="aws.cloudwatch.CWManager.check_cloudwatch_alarm_state"></a>

#### check\_cloudwatch\_alarm\_state

```python
def check_cloudwatch_alarm_state() -> dict
```

Checks the state history of the specified CloudWatch alarm within the given date range.

**Returns**:

- `dict` - A dictionary containing the status code and message indicating whether the alarm state changed to ALARM.

<a id="aws.s3"></a>

# aws.s3

<a id="aws.s3.S3Manager"></a>

## S3Manager Objects

```python
class S3Manager()
```

<a id="aws.s3.S3Manager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(file_name: str,
             bucket: str,
             object_name: str,
             region: str = 'eu-west-1',
             profile: str = 'default')
```

Initialize an S3Manager instance.

**Arguments**:

- `file_name` _str_ - Local path to the file to be uploaded.
- `bucket` _str_ - The name of the S3 bucket.
- `object_name` _str_ - The name of the object to be created in the
  S3 bucket.
- `region` _str, optional_ - AWS region. Defaults to 'eu-west-1'.
- `profile` _str, optional_ - AWS profile name. Defaults to 'default'.

<a id="aws.s3.S3Manager.upload_file"></a>

#### upload\_file

```python
def upload_file() -> dict
```

Upload a file to an S3 bucket.

**Returns**:

- `dict` - A dictionary containing the status code and status message.

<a id="aws.s3.S3Manager.check_file_exists"></a>

#### check\_file\_exists

```python
def check_file_exists() -> dict
```

Check if the specified file exists in the S3 bucket and if it was
modified in the last one minute of UTC time.

**Returns**:

- `dict` - A dictionary containing the status code and status message.

