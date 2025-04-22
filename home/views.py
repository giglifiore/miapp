from django.http import HttpResponse

def index(request):
    logger.info("Vista index llamada")
    return HttpResponse("¡Hola mundo desde Django en Render!")
