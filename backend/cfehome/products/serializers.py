from rest_framework import serializers 
from api.serializers import UserPublicSerializer
from .models import Product
from rest_framework.reverse import reverse
from .validators import validate_title_no_hello, unique_product_title
from . import validators

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True,
    )
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    # user = UserPublicSerializer(read_only=True)
    owner = UserPublicSerializer(source="user", read_only=True)
    # related_products = ProductInlineSerializer(source='user.product_set.all()', read_only=True, many=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    # edit_url = serializers.SerializerMethodField(read_only=True)
    # url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field = 'pk' )
    # email = serializers.EmailField(write_only=True) 
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    # name = serializers.CharField(source='title', read_only=True)
    # email = serializers.CharField(source='user.email', read_only=True)
    body = serializers.CharField(source='content')
    class Meta:
        model = Product
        fields = [
            # 'email',
            'owner',
            # 'user', #user_id
            # 'url',
            # 'edit_url',
            'pk',
            # 'name',
            'title',
            # 'content',
            'body',
            'price', 
            'sale_price',
            'public',
            'path',
            'endpoint',
            # 'my_discount',
            # 'my_user_data',
            # 'related_products'
            

        ]
    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        } 

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     # qs = Product.objects.filter(title__exact=value) #querys title from now not older ones
    #     qs = Product.objects.filter(user=user, title__iexact=value) #querys from older title also / user=user in foreignkey relations
    #     qs = Product.objects.filter( title__iexact=value) #querys from older title also 
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value


    # def create(Self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email,"hello", obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     # instance.title = validated_data.get('title')
    #     # return instance
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk":obj.pk}, request=request)

    # obj is the instance that's being called 
    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
        # print(obj.id)
        # obj.user -> user.username
        # obj.category -> foriegnkey 
        # try:
        #     return obj.get_discount()
        # except:
        #     return None