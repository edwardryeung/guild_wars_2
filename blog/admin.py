"""
blog admin config
"""
from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    admin comment display categories, filter, and search criteria
    """
    list_display = (
        '__str__',
        'post',
        'name',
        'email',
        'created',
        'updated',
        'likes',
        'dislikes',
    )
    list_filter = (
        'approved',
    )
    search_fields = (
        'post__title',
        'name',
        'email',
        'text',
    )


class CommentInline(admin.StackedInline):
    """
    admin-side comment formatting under posts
    """
    model = models.Comment
    extra = 0
    readonly_fields = (
        'name',
        'email',
        'text',
    )


class PostAdmin(admin.ModelAdmin):
    """
    admin post display categories, filters, and search criteria
    """
    list_display = (
        'title',
        'author',
        # 'status',
        'created',
        'updated',
    )

    list_filter = (
        'status',
        'topics',
        'popular',
    )

    prepopulated_fields = {'slug': ('title',)}

    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    inlines = [
        CommentInline,
    ]


admin.site.register(models.Post, PostAdmin)


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    admin topic display categories
    """
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'last_name',
        'first_name',
        'submitted',
    )

    readonly_fields = (
        'first_name',
        'last_name',
        'email',
        'message',
        'submitted',
    )


@admin.register(models.PhotoContestSubmission)
class PhotoContestSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'last_name',
        'first_name',
        'submitted',
        'photo',
    )

    readonly_fields = (
        'first_name',
        'last_name',
        'email',
        'submitted',
        'photo',
    )

    list_filter = (
        'first_name',
        'last_name',
        'email',
        'submitted',
    )

    search_fields = (
        'first_name',
        'last_name',
        'email',
        'submitted',
    )
