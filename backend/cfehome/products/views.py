from rest_framework import authentication, generics, mixins, permissions
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# from ..api.permissions import IsStaffEditorPermission
# from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin

# 1234@jr10

class ProductDetailAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser , IsStaffEditorPermission]
    # permission_classes = [permissions.DjangoModelPermissions]
    # lookup_field = 'pk'
    # is equal to Product.objects.get(pk='abc')
# product_detail_view = ProductDetailAPIview.as_view()


class ProductListCreateAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser , IsStaffEditorPermission] #if all users have same permission this is not required

    #authentication class not required as we mentioned on settings.py
    # authentication_classes = [authentication.SessionAuthentication,TokenAuthentication]
    # permission_classes = [permissions.DjangoModelPermissions]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        # email = serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content) #form.save() model.save()
        # send a django signals

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     # print(request.user)
    #     return qs.filter(user=request.user)

class ProductUpdateAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser , IsStaffEditorPermission]
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDestroyAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser , IsStaffEditorPermission]
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

# class ProductListAPIView(generics.ListAPIView):
#     '''not gonna use this method '''
#     queryset = Product.objects.all() 
#     serializer_class = ProductSerializer

# class CreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
#     pass
    
class ProductMixinView(UserQuerySetMixin, mixins.CreateModelMixin,mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 
    # verbose_name = "rohit"

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "this is a single veiw doing"
        serializer.save(content=content)

@api_view(['GET', 'POST']) #all of crud in one view
def product_alt_view(request,pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # detail view
            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exist():
            #     raise Http404
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # url_args?? 
        # get request -> detail view
      
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
        # data = serializer.save()
            # print(serializer.data)
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid":"not good data"}, status=400)