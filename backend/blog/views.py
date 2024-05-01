from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer, EmailSerializer
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class ListView(ListAPIView):   
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("title",)


class BlogDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        try:
            blog = Blog.objects.get(slug=slug)
            serializer = BlogSerializer(blog)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error":"Data is not availalbe"}, status=status.HTTP_204_NO_CONTENT)
            
class SendEmailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        from_email = serializer.validated_data['from_email']
        to_email = serializer.validated_data['to_email']
        name = serializer.validated_data['name']
        comment = serializer.validated_data['comments']


        subject = 'Blog Sharing from Bolg_'
        message = f"Hi everyone, it's {name} here. I'm excited to introduce new blog post, '{slug}'.\n\nIn this post, {comment}...\n\nIf you'd like to read the full post, check it out here: ."

        send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [to_email], fail_silently=False)
        
        return Response("sended verification message")