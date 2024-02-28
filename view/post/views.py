import math

from django.db import transaction
from django.db.models import F
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from post.models import Post



class PostWriteView(View):
    def get(self, request):
        return render(request, 'post/write.html')

    @transaction.atomic
    def post(self, request):
        data = request.POST

        member = Member(**request.session['member'])

        data = {
            'post_title': data['post-title'],
            'post_content': data['post-content'],
            'member': member
        }

        post = Post.objects.create(**data)

        return redirect(post.get_absolute_url())


class PostDetailView(View):
    def get(self, request):
        post = Post.objects.get(id=request.GET['id'])

        post.post_view_count += 1
        post.save(update_fields=['post_view_count'])

        context = {
            'post': post
        }
        return render(request, 'post/detail.html', context)


class PostUpdateView(View):
    def get(self, request):
        post = Post.objects.get(id=request.GET['id'])
        return render(request, 'post/update.html', {'post': post})

    @transaction.atomic
    def post(self, request):
        data = request.POST

        post = Post.objects.get(id=data['id'])
        post.post_title = data['post-title']
        post.post_content = data['post-content']
        post.save(update_fields=['post_title', 'post_content'])

        return redirect(post.get_absolute_url())


class PostDeleteView(View):
    def get(self, request):
        Post.objects.filter(id=request.GET['id']).update(post_status=False)
        return redirect('/post/list')


class PostListView(View):
    def get(self, request):
        return render(request, 'post/list.html')


class PostListAPI(APIView):
    def get(self, request, page):
        row_count = 5

        offset = (page - 1) * row_count
        limit = page * row_count

        # total = Post.enabled_objects.count()
        # page_count = 5
        # end_page = math.ceil(page / page_count) * page_count
        # start_page = end_page - page_count + 1
        # real_end = math.ceil(total / row_count)
        # end_page = real_end if end_page > real_end else end_page

        columns = [
            'id',
            'post_title',
            'post_content',
            'post_view_count',
            'member_name'
        ]
        posts = Post.enabled_objects\
                    .annotate(member_name=F('member__member_name'))\
                    .values(*columns)[offset:limit]

        has_next = Post.enabled_objects.filter()[limit:limit + 1].exists()

        post_info = {
            'posts': posts,
            'hasNext': has_next
        }
        return Response(post_info)
