from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)
    # Для видео
    video = models.FileField(
        upload_to='project_videos/',
        blank=True,
        null=True,
        verbose_name='Видео демонстрация'
    )
    video_url = models.URLField(
        blank=True,
        verbose_name='Ссылка на видео (альтернатива)'
    )

    def __str__(self):
        return self.title

    @property
    def has_video(self):
        return bool(self.video) or bool(self.video_url)