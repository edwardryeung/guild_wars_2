from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'post',
        'name',
        'email',
        'created',
        'updated',
        # 'approved',
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
    model = models.Comment
    extra = 0
    readonly_fields = (
        'name',
        'email',
        'text',
    )


class PostAdmin(admin.ModelAdmin):
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
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}
