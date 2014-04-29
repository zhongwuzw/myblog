
def static_url_processor(request):
    return {'REQUESTTEMP':request.META}
#     return {'STATIC_URL_ROOT':'static/'}