from django.contrib import admin
from .models import Student, Product, Course, Lesson, Book


admin.site.register(Student)
admin.site.register(Product)


class LessonInLine(admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ('title', 'order', 'duration_minutes', 'is_free')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_published', 'created_at', 'display_lessons_count')
    list_filter = ('is_published', 'category', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('price', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [LessonInLine]

    fieldsets = (
        ('Basic information', {
            'fields': ('title', 'slug', 'description', 'price', 'is_published'),
        }),
    )

    @admin.display(description='Number of lessons')
    def display_lessons_count(self, obj):
        return obj.lessons.count()


admin.site.register(Book)