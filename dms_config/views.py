from django.http import HttpResponse

""" 
====================================
First view: Example view

Shows a message.
====================================
"""

def index(request):
    document =  '''<!DOCTYPE html>
                    <html lang="es">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Index</title>
                    </head>
                    <body>
                        <h1> First View </h1>
                    </body>
                    </html>'''

    return HttpResponse(document)