import os

BEDROCK_GW_API_KEY = "bedrock"
API_ROUTE_PREFIX = "/api/v1"

TITLE = "AWS Bedrock Gateway"
SUMMARY = "OpenAI-Compatible APIs for Bedrock"
VERSION = "1.0.0"
DESCRIPTION = """
Use OpenAI-Compatible APIs for AWS Bedrock models.

Currently supported models:
- Anthropic Claude 2 / 3 /3.5 (Haiku/Sonnet/Opus)
- Meta Llama 2 / 3
- Mistral / Mixtral
- Cohere Command R / R+
- Cohere Embedding
"""

DEBUG = os.environ.get("DEBUG", "false").lower() != "false"
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
DEFAULT_MODEL = os.environ.get(
    "DEFAULT_MODEL", "anthropic.claude-3-5-sonnet-20240620-v1:0"
)
DEFAULT_EMBEDDING_MODEL = os.environ.get(
    "DEFAULT_EMBEDDING_MODEL", "cohere.embed-multilingual-v3"
)
