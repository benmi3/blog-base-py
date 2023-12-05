from django.contrib import admin

from .models import Post, Comment, Category


# Register your models here.
class CommentInline(admin.StackedInline):  # can change to TabularInline for more compact
    model = Comment
    extra = 3


class CategoryInline(admin.StackedInline):
    model = Category
    extra = 3


class PostAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "post_text"]
    fieldsets = [
        (None, {"fields": ["post_title",
                           "post_text",
                           "post_author",
                           "category",
                           "pub_date",
                           "upd_date"]}),]
    inlines = [CommentInline]
    list_display = [
        "post_text",
        "pub_date",
        "was_published_recently",
    ]
    list_filter = ["pub_date"]
    search_fields = ["post_text"]


class CommentAdmin(admin.ModelAdmin):
    fields = ["pub_date",
              "comment_text",
              "comment_author",
              "approved_comment"]


class CategoryAdmin(admin.ModelAdmin):
    fields = ["category_name", "category_description"]


admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
