
# import pytest
# from django.urls import reverse
# from django.test import RequestFactory
# from blog.views import PostList, post_detail, search, post_comment


# @pytest.mark.django_db
# def factory():
#     return RequestFactory()

# # @pytest.mark.django_db
# # def test_post_list_view(factory):
# #     PostList.cycle(5).blend('blog.Post', status=1)
# #     path = reverse(path ='post_list')
# #     request = factory.get(path)
# #     response = PostList.as_view()(request)

# # assert response.status_code == 200


# @pytest.mark.django_db
# def test_search_view(factory):
#     search.blend('blog.Post', title='Test Post', content='Test Content')  
#     path = reverse('search')
#     request = factory.get(path,'/search/', {'q': 'Test'})
#     response = search(request)
#     assert response.status_code == 200
#     assert 'Test Post' in str(response.content)