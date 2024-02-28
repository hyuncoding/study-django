from django.test import TestCase

from member.models import Member
from post.models import Post
from reply.models import Reply
from django.db.models import Count


import random

class ReplyTest(TestCase):
    # replies = []
    # # 총 98개 댓글 작성하기
    # # 랜덤한 회원을 작성자로 설정하기
    # member_queryset = Member.objects.all()
    # # 랜덤한 게시물을 대상글로 설정하기
    # post_queryset = Post.objects.all()
    #
    # for i in range(98):
    #     reply = {
    #         'reply_content': f"테스트 댓글{i + 1}",
    #         'member': member_queryset[random.randint(0, len(member_queryset)-1)],
    #         'post': post_queryset[random.randint(0, len(post_queryset)-1)]
    #     }
    #     replies.append(Reply(**reply))
    # Reply.objects.bulk_create(replies)


    # 커스텀 문제
    # 나이가 30 이상인 회원이 작성한 댓글의 게시물 제목 및 회원의 이름 조회
    # reply_queryset = Reply.objects.filter(member__member_status=True, member__member_age__gte=30).values('post__post_title', 'member__member_name')
    # for reply in reply_queryset:
    #     print(reply)

    # 관익스 문제
    # 댓글을 작성한 회원들 중 댓글을 2개 이상 작성한 회원 이름 조회
    # reply_queryset = Reply.objects.values('member_id').annotate(count=Count('id')).filter(count__gte=2).values('member__member_name')
    # for member_name in reply_queryset:
    #     print(member_name)

    # 게시글과 댓글을 모두 작성한 회원을 찾으세요
    # reply_queryset = Reply.objects.filter(member_id__in=Post.objects.values('member_id')).values('member_id', 'member__member_name').distinct()
    # for member in reply_queryset:
    #     print(member)

    # 대댓글 3개 등록하기
    # member_id = 6
    # reply_id = 11
    # member = Member.objects.get(id=member_id)
    # post = Post.objects.get(reply__id=reply_id)
    #
    # data = {
    #             'reply_content': '테스트 대댓글1',
    #             'depth': 2,
    #             'member': member,
    #             'post': post,
    #         }
    #
    # reply = Reply.objects.create(**data)
    # reply.group_number = reply_id
    # reply.save()

    # 게시글 상세보기
    # 게시글 정보, 회원 정보, 댓글 목록, 댓글의 대댓글 목록
    # post_id = 351
    # post = Post.objects.get(id=post_id)
    # data = {}
    # data['post'] = post.__dict__
    # data['member'] = post.member.__dict__
    # data['reply'] = []
    # reply_queryset = post.reply_set.filter(depth=1)
    # for reply in reply_queryset:
    #     re_replies = []
    #     re_reply_queryset = post.reply_set.filter(group_number=reply.id, depth__gte=2).values()
    #     for re_reply in re_reply_queryset:
    #         re_replies.append(re_reply)
    #     data['reply'].append({'reply': reply.__dict__, 're_replies': re_replies})
    # print(data)

    # 대댓글을 작성한 적이 없는 회원 목록 출력
    # member_queryset = Member.objects.exclude(id__in=Reply.objects.filter(depth=2).values('member__id')).values()
    # for member in member_queryset:
    #     print(member)

    pass


