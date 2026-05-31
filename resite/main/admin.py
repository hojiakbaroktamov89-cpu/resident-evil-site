from django.contrib import admin
from django.utils.html import format_html
from .models import Game, Character, Movie, History

admin.site.site_header = "🎮 Resident Evil — Boshqaruv Paneli"
admin.site.site_title = "RE Admin"
admin.site.index_title = "Xush kelibsiz, Umbrella Agent"


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('preview_img', 'title', 'release_year', 'steam_link')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('release_year',)
    list_per_page = 15

    def preview_img(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="55" height="55" style="object-fit:cover;border-radius:4px;">', obj.image.url)
        return "—"
    preview_img.short_description = ""

    def steam_link(self, obj):
        if obj.steam_url:
            return format_html('<a href="{}" target="_blank" style="color:#45d4e8;">Steam ↗</a>', obj.steam_url)
        return "—"
    steam_link.short_description = "Steam"


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('preview_img', 'name', 'games_short')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 15

    def preview_img(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="45" height="55" style="object-fit:cover;object-position:top;border-radius:4px;">', obj.image.url)
        return "—"
    preview_img.short_description = ""

    def games_short(self, obj):
        games = obj.games_list()
        if games:
            return ", ".join(games[:4]) + ("..." if len(games) > 4 else "")
        return "—"
    games_short.short_description = "O'yinlar"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('preview_img', 'title', 'release_year', 'yt_link')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_per_page = 15

    def preview_img(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="40" height="55" style="object-fit:cover;border-radius:4px;">', obj.image.url)
        return "—"
    preview_img.short_description = ""

    def yt_link(self, obj):
        return format_html('<a href="{}" target="_blank" style="color:#ff4444;">▶ YouTube</a>', obj.youtube_url)
    yt_link.short_description = "Treyler"


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'has_image')
    list_display_links = ('title',)
    search_fields = ('title', 'year')
    ordering = ['year']
    list_per_page = 20

    def has_image(self, obj):
        return "✅" if obj.image else "—"
    has_image.short_description = "Rasm"
