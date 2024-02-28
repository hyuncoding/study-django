from django.db.models import Count
from django.test import TestCase
import random

from member.models import Member
from post.models import Post
from reply.models import Reply


class PostTest(TestCase):

    # posts = []
    # # 총 98개 게시글 작성하기
    # # 랜덤한 회원을 작성자로 설정하기
    # member_queryset = Member.objects.all()
    # for i in range(98):
    #     post = {
    #         'post_title': f"테스트 제목{i + 1}",
    #         'post_content': f"테스트 내용{i + 1}",
    #         'member': member_queryset[random.randint(0, len(member_queryset)-1)]
    #     }
    #     posts.append(Post(**post))
    # Post.objects.bulk_create(posts)
    # post_queryset = Post.objects.all()
    # for post in post_queryset:
    #     print(post.__dict__)

    # 로그인된 회원의 마이페이지에서 내가 작성한 게시글 조회하기
    # member = Member.objects.get(member_status=True, id=3)
    # for post in member.post_set.all():
    #     print(post.__dict__)

    # 나이가 30 미만인 회원이 작성한 게시글 목록 조회
    # 단, 회원의 이름과 회원의 나이까지 같이 조회하기

    # 1. 정방향으로 직접 참조
    # post_queryset = Post.objects.filter(member__member_age__lt=30)
    # for post in post_queryset:
    #     print(post.id, post.post_title, post.post_content,
    #           post.created_date, post.updated_date, post.member.member_name,
    #           post.member.member_age, sep=", ")

    # 2. 한번에 참조(member__member_name, member__member_age)
    # post_queryset = Post.objects.filter(member__member_status=True, member__member_age__lt=30).values(
    #     'id',
    #     'post_title',
    #     'post_content',
    #     'created_date',
    #     'updated_date',
    #     'member_id',
    #     'member__member_name',
    #     'member__member_age'
    # )
    # for post in post_queryset:
    #     print(post)

    # 회원의 나이가 20이상 30이하인 회원이 작성한 게시글 중 post_title에 "테"가 들어가고 내용에 "7"로 끝나는 게시글 정보 조회
    # Member는 사용하지 않고 Post만 사용해서 하기
    # 나이 범위는 __range를 사용해서 진행
    # post_queryset = Post.objects.filter(member__member_age__range=(20, 30), post_title__contains='테', post_content__endswith='7')
    # for post in post_queryset:
    #     print(post.__dict__)


    # A필드에 b가 있다고 가정한다.
    # a.b: 정방향 -> a로 b필드에 접근하면 정방향 참조이고, b의 null 상태에 따라 내부 또는 외부조인이 실행된다.(모델 선언 시 null=False || null=True)
    # b.a: 역방향 -> b로 a필드에 접근하면 역방향 참조이고, b의 모든 정보가 나와야 하기 때문에 항상 외부조인이 실행된다.

    # EAGER(즉시)
    # 실행하는 순간 쿼리가 실행된 뒤 이후 쿼리가 발생하지 않는다.
    # 하나의 서비스에서 여러 번 JOIN해야 할 경우 사용한다.
    # posts = Post.objects.select_related('member', 'reply').values('id', 'post_title', 'member__member_name')

    # LAZY(지연)
    # 실행할 때 쿼리가 만들어지고 필드에 접근할 때마다 쿼리가 발생한다.
    # print(Post.objects.values('member__member_name').query)
    # print(Member.objects.values('post__post_title').query)

    # 게시물을 2개 이상 작성한 회원의 id와 이름을 조회하세요
    # post_queryset = Post.objects.values('member_id').annotate(count=Count('id')).filter(count__gte=2).values('member__id', 'member__member_name').order_by('member__id')
    # for post in post_queryset:
    #     print(post)

    pass

