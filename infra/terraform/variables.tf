variable "aws_region" {
  type        = string
  description = "AWS region"
}

variable "aws_access_key" {
  type        = string
  description = "AWS Access Key for authentication"
}

variable "aws_secret_key" {
  type        = string
  description = "AWS Secret Key for authentication"
}

variable "s3_bucket_name" {
  type        = string
  description = "S3 bucket name for Lambda deployment package"
}

variable "lambda_name" {
  type        = string
  description = "Lambda function name"
}
