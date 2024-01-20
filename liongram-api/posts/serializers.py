from rest_framework.serializers import ModelSerializer

from .models import Post, Comment

class PostBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' 
        # 특정 필드만 넣고 싶다면
        # fields = ['id', 'title', 'contents']

class PostListModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'image',
            'created_at',
            'view_count',
            'writer',
        ]
        # exclude = ['content']
        depth = 1

class PostRetrieveModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        depth = 1


class PostCreateModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'image',
            'content',
        ]
        # exclude = ['content']

class PostDeleteModelSerializer(PostBaseModelSerializer):
    pass

class CommentListModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'