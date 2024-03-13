from django.contrib.syndication.views import Feed
from django.urls import reverse
from Blog.models import Post


class LatestEntriesFeed(Feed):
    title = "new blog posts"
    link = "/sitenews/"
    description = "best blog contents"

    def items(self):
        return Post.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]