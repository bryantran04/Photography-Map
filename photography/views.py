from django.shortcuts import render

# Create your views here.
def index(request):
    """
    View for the about_page.html
    :param request:
    :return renders the request parameter, html template, and the context list:
    """
    context = {}
    template = 'photography/index.html'
    return render(request, template, context)



import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="auth.json"

from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six


def sample_analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()

    #content = 'GOOD'

    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment
    return('Score: {}'.format(sentiment.score))
