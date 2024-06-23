import boto3
import datetime
import logging
import os
from aiobotocore.session import get_session

from io import BytesIO
from PIL import Image
from tools_commons.decorator import retry

# Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.put_object
# Ref. for content types : https://s3browser.com/features-content-mime-types-editor.aspx
# aws s3api get-bucket-policy --bucket prod.cdata.app.sprinklr.com
# aws s3api head-object --bucket prod.cdata.app.sprinklr.com --key narad-muni-tagging-export/product-insights_english_pgshavecare_2019-02-25.xlsx

logger = logging.getLogger(__name__)


class AwsUploadTool:
    def __init__(self, settings):
        tagging_aws_upload_config = settings.AWS_UPLOAD_CONFIG
        missing_conf_msg = "Missing aws upload config!"
        if not tagging_aws_upload_config:
            logger.error(missing_conf_msg)
            raise Exception(missing_conf_msg)

        aws_bucket_config = tagging_aws_upload_config["bucket_config"]
        if not aws_bucket_config:
            logger.error(missing_conf_msg)
            raise Exception(missing_conf_msg)

        self.bucket_name = aws_bucket_config["bucket"]
        self.expiry_in_days = aws_bucket_config["expiry_in_days"]
        self.public_key = os.environ.get("AWS_ACCESS_KEY_ID")
        self.secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
        self.role_arn = os.environ.get("AWS_ROLE_ARN")
        self.jwt_token_path = os.environ.get("AWS_WEB_IDENTITY_TOKEN_FILE")

    @staticmethod
    def validate_file_type(file_type):
        if file_type.lower() in ["xlsx", "png", "jpg", "jpeg", "wav", "txt"]:
            return True

    @retry(exception_to_check=(Exception,), tries=3, delay=1, back_off=2, logger=logging)
    def upload_file_to_s3(self, folder_name, file_path, filename=None):
        """
        Upload xlsx/png/jpeg file to aws
        :param folder_name:
        :param file_path: local file pat
        :return:
        """
        file_type = "xlsx"
        file_name = os.path.basename(file_path) if not filename else filename
        if file_name:
            temp_file_type = file_name.split(".")[-1]
            # filename without extension is by default considered a spreadsheet
            if self.validate_file_type(temp_file_type):
                file_type = temp_file_type

        # Based on the received file type, prepare data and content type to upload file to
        if file_type.lower() == "xlsx":
            data = open(file_path, "rb")
            content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        elif file_type.lower() == "wav":
            data = open(file_path, "rb")
            content_type = "audio/wav"
        elif file_type.lower() == "txt":
            data = open(file_path, "r")
            content_type = "text/plain"
        else:
            image = Image.open(file_path)
            imgByteArr = BytesIO()
            image.convert("RGB").save(imgByteArr, format="JPEG", quality=95, optimize=True)
            data = imgByteArr.getvalue()
            content_type = "image/jpeg"

            # Image files are uploaded in jpeg format
            filename_split = file_name.split(".")
            filename_split[-1] = "jpeg"
            file_name = ".".join(filename_split)

        key = folder_name + '_' + file_name
        expiry_date = datetime.datetime.utcnow() + datetime.timedelta(
            days=self.expiry_in_days
        )

        if self.role_arn:
            # create an STS service client
            sts_client = boto3.client('sts')

            # Load the web identity token from jwt token file path
            with open(self.jwt_token_path, mode="r") as f:
                web_identity_token = f.read()

            # Request for temporary credentials through STS using the role ARN
            assumed_role_object = sts_client.assume_role_with_web_identity(
                RoleArn=self.role_arn,
                WebIdentityToken=web_identity_token,
                RoleSessionName="aws_uploader_session"
            )

            # From the response that contains the assumed role, get the temporary
            # credentials that can be used to make subsequent API calls
            credentials = assumed_role_object['Credentials']

            # Use the temporary credentials that AssumeRole returns to make a connection to Amazon S3
            s3 = boto3.resource(
                's3',
                aws_access_key_id=credentials['AccessKeyId'],
                aws_secret_access_key=credentials['SecretAccessKey'],
                aws_session_token=credentials['SessionToken'],
            )
            s3.Bucket(self.bucket_name).put_object(
                Key=key,
                Body=data,
                ACL="public-read",
                Expires=expiry_date,
                ContentType=content_type,
            )

        elif self.public_key:
            s3 = boto3.resource('s3',
                                aws_access_key_id=self.public_key,
                                aws_secret_access_key=self.secret_key
                                )
            s3.Bucket(self.bucket_name).put_object(
                Key=key,
                Body=data,
                ACL="public-read",
                Expires=expiry_date,
                ContentType=content_type,
            )
        url = "https://" + self.bucket_name + "/" + key
        return url

    @retry(exception_to_check=(Exception,), tries=3, delay=1, back_off=2, logger=logging)
    async def async_upload_file_to_s3(self, data, s3_folder, filename, content_type):
        """
        Asynchronously upload files to aws
        :param data: binary content of the file to be uploaded
        :param s3_folder: target folder in s3 bucket
        :param filename: filename you want your data to be saved in s3 eg, sample.txt, speech.wav, etc.
        :param content_type: HTTP content-type field for eg, image/jpeg, audio/wav, etc.
        :return: s3 url of the uploaded file
        """
        sess = get_session()
        expiry_date = datetime.datetime.utcnow() + datetime.timedelta(
            days=self.expiry_in_days
        )
        key = s3_folder + "/" + filename
        async with sess.create_client('s3',
                                      aws_secret_access_key=self.secret_key,
                                      aws_access_key_id=self.public_key) as client:
            await client.put_object(
                Bucket=self.bucket_name,
                Key=key,
                Body=data,
                ACL="public-read",
                Expires=expiry_date,
                ContentType=content_type
            )
            return "https://"+self.bucket_name+"/"+key

