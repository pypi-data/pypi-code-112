import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-solutions-constructs.aws-wafwebacl-cloudfront",
    "version": "1.140.0",
    "description": "CDK constructs for defining an AWS web WAF connected to Amazon CloudFront.",
    "license": "Apache-2.0",
    "url": "https://github.com/awslabs/aws-solutions-constructs.git",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/awslabs/aws-solutions-constructs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_solutions_constructs.aws_wafwebacl_cloudfront",
        "aws_solutions_constructs.aws_wafwebacl_cloudfront._jsii"
    ],
    "package_data": {
        "aws_solutions_constructs.aws_wafwebacl_cloudfront._jsii": [
            "aws-wafwebacl-cloudfront@1.140.0.jsii.tgz"
        ],
        "aws_solutions_constructs.aws_wafwebacl_cloudfront": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-cloudfront-origins==1.140.0",
        "aws-cdk.aws-cloudfront==1.140.0",
        "aws-cdk.aws-lambda==1.140.0",
        "aws-cdk.aws-s3==1.140.0",
        "aws-cdk.aws-wafv2==1.140.0",
        "aws-cdk.core==1.140.0",
        "aws-solutions-constructs.aws-cloudfront-apigateway-lambda==1.140.0",
        "aws-solutions-constructs.aws-cloudfront-mediastore==1.140.0",
        "aws-solutions-constructs.aws-cloudfront-s3==1.140.0",
        "aws-solutions-constructs.core==1.140.0",
        "constructs>=3.2.0, <4.0.0",
        "jsii>=1.54.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
