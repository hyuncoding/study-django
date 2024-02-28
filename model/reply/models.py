from django.db import models

from member.models import Member
from model.models import Period
from post.models import Post


class Reply(Period):
    PRIVATE_CHOICES = [
        (0, '일반댓글'),
        (1, '비밀댓글')
    ]

    reply_content = models.CharField(null=False, blank=False, max_length=100)
    member = models.ForeignKey(Member, null=False, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, null=False, on_delete=models.PROTECT)
    group_number = models.IntegerField(null=False, blank=False, default=1)
    depth = models.IntegerField(null=False, blank=False, default=1)
    is_private = models.BooleanField(null=False, blank=False, default=False, choices=PRIVATE_CHOICES)

    class Meta:
        db_table = 'tbl_reply'

    def __str__(self):
        return self.reply_content

