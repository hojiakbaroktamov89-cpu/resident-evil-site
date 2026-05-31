from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name="O'yin nomi")
    release_year = models.CharField(max_length=4, verbose_name="Yil", blank=True)
    description = models.TextField(verbose_name="Tavsif", blank=True)
    steam_url = models.URLField(verbose_name="Steam havolasi", blank=True)
    image = models.ImageField(upload_to='games/', verbose_name="Muqova", blank=True, null=True)

    class Meta:
        verbose_name = "O'yin"
        verbose_name_plural = "O'yinlar"
        ordering = ['release_year']

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Character(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    bio = models.TextField(verbose_name="Biografiya")
    games = models.CharField(max_length=500, verbose_name="Qatnashgan o'yinlar", blank=True,
                             help_text="Vergul bilan ajrating: RE2, RE4, RE6")
    image = models.ImageField(upload_to='characters/', verbose_name="Rasm", blank=True, null=True)

    class Meta:
        verbose_name = "Personaj"
        verbose_name_plural = "Personajlar"
        ordering = ['name']

    def __str__(self):
        return self.name

    def games_list(self):
        if self.games:
            return [g.strip() for g in self.games.split(',') if g.strip()]
        return []


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Kino nomi")
    release_year = models.CharField(max_length=4, verbose_name="Yil")
    youtube_url = models.URLField(verbose_name="YouTube havolasi")
    image = models.ImageField(upload_to='movies/', verbose_name="Afisha", blank=True, null=True)

    class Meta:
        verbose_name = "Kino"
        verbose_name_plural = "Kinolar"
        ordering = ['release_year']

    def __str__(self):
        return f"{self.title} ({self.release_year})"

    def youtube_embed(self):
        url = self.youtube_url
        if 'watch?v=' in url:
            vid_id = url.split('watch?v=')[1].split('&')[0]
            return f"https://www.youtube.com/embed/{vid_id}"
        elif 'youtu.be/' in url:
            vid_id = url.split('youtu.be/')[1].split('?')[0]
            return f"https://www.youtube.com/embed/{vid_id}"
        return url


class History(models.Model):
    """RE tarixi — xronologik voqealar"""
    year = models.CharField(max_length=10, verbose_name="Yil/Sana",
                            help_text="Masalan: 1967, 1998, 2004")
    title = models.CharField(max_length=200, verbose_name="Voqea nomi")
    description = models.TextField(verbose_name="Tavsif")
    image = models.ImageField(upload_to='history/', verbose_name="Rasm", blank=True, null=True)

    class Meta:
        verbose_name = "Tarix voqeasi"
        verbose_name_plural = "RE Tarixi"
        ordering = ['year']

    def __str__(self):
        return f"{self.year} — {self.title}"
