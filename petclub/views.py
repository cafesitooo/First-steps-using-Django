# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Estoy en el get", status=200) # respuesta del servicio

    def patch(self, request):
        return Response(data="Estoy en el patch", status=200) # respuesta del servicio

    def delete(self, request):
        return Response(data="Estoy en el delete", status=200) # respuesta del servicio

    def post(self, request):
        return Response(data="Estoy en el post", status=200) # respuesta del servicio

#class PetListAPIView(ListAPIView):
 #   def get(self,request):
  #      return Response(data="Estoy en el get", status=200) #implementar como traer una lista de APIViews

class PersonAPIView(APIView):
    def get(self, request):
        return Response(data="estoy en el get del PersonApiView", status=200)

    def patch(self, request):
        return Response(PetAPIView.get(APIView)) # respuesta del servicio

    def delete(self, request):
        return Response(data="Estoy en el delete del PersonApiView", status=200) # respuesta del servicio

    def post(self, request):
        return Response(data="Estoy en el post del PersonApiView", status=200) # respuesta del servicio


class PetAPIView(APIView):
    def get(self, request):
        return Response(data="estoy en el get del PetApiView", status=200)

    def patch(self, request):
        return Response(data="Estoy en el patch del PetApiView", status=200) # respuesta del servicio

    def delete(self, request):
        return Response(data="Estoy en el delete del PetApiView", status=200) # respuesta del servicio

    def post(self, request):
        return Response(data="Estoy en el post del PetApiView", status=200) # respuesta del servicio