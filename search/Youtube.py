# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import sys
from django.conf import settings
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main(name):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "result.json"
    
    # me ja rha sone ab ye company ma chudaye uski 
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    temp = " official trailer"
    query = name + temp

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q=query
    )
    response = request.execute()

    print(response)
    return response

if __name__ == "__main__":
    main(sys.argv[0])