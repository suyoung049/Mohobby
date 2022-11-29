from django.db import models
from django.conf import settings

# 커뮤니티 글 부분
class Community(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=""
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_community"
    )
    hits = models.PositiveBigIntegerField(default=1, verbose_name="조회수")


# 댓글 부분
class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    posting = models.ForeignKey(Community, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="recomment", null=True
    )
