import pytz
from datetime import datetime

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from authentication.models import Chapter, User
from events.models import Event
from sponsors.models import Sponsor
from cms_app.models import SponsorConfig, CounterConfig
from announcements.models import Announcement


@plugin_pool.register_plugin
class CounterPlugin(CMSPluginBase):
    model = CounterConfig
    name = _("Counter Plugin")
    render_template = "cms_app/plugins/counter.html"
    cache = False

    def render(self, context, instance, placeholder):
        age = round(
            (timezone.now() - datetime(2017, 7, 18, 0, 0, 0, 0, pytz.UTC)).days
            / 365.25,
            1,
        )
        context.update(
            {
                "members": instance.member_offset
                + User.objects.exclude(chapter=None).count()
            }
        )
        context.update(
            {"locations": instance.locations_offset + Chapter.objects.all().count()}
        )
        context.update({"age": age})
        context.update(
            {"meetings": instance.meetings_offset + Event.objects.all().count()}
        )
        return context


@plugin_pool.register_plugin
class LocationsPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Locations Plugin")
    render_template = "cms_app/plugins/locations.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({"locations": Chapter.objects.all()})
        return context


@plugin_pool.register_plugin
class SponsorPlugin(CMSPluginBase):
    model = SponsorConfig
    name = _("Sponsor")
    render_template = "cms_app/plugins/sponsor.html"
    cache = False

    def render(self, context, instance, placeholder):
        sponsor = Sponsor.objects.get(name=instance.name)
        context.update({"sponsor": sponsor})
        return context

@plugin_pool.register_plugin
class IndexPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Index Plugin")
    render_template = "cms_app/plugins/index_plugin.html"
    cache = False
      
    def render(self, context, instance, placeholder):
        context.update({"chapters": Chapter.objects.all(),
        "announcements": Announcement.objects.all(),"main_dashboard": True,})
        return context

      
    