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
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"],
                              "classes": ["collapse"]}),
    ]
    inlines = [CommentInline, CategoryInline]
    list_display = [
        "question_text",
        "pub_date",
        "was_published_recently",
    ]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


class CommentAdmin(admin.ModelAdmin):
    fields = ["pub_date", "likes"]


class CategoryAdmin(admin.ModelAdmin):
    fields = ["category_name", "category_description"]


admin.site.register(Post, PostAdmin)
# admin.site.register(Choice)
