from django.shortcuts import render
from django.conf import settings


def team_view(request):
    return render(request, "organizational/team.html")


def strategy_view(request):
    return render(request, "organizational/strategy.html")


def history_view(request):
    return render(request, "organizational/history.html")


def press_view(request):
    return render(request, "organizational/press.html")


def benefits_view(request):
    return render(request, "organizational/benefits.html")


def supporters_view(request):
    return render(request, "organizational/supporters.html")


def sponsors_view(request):
    return render(request, "organizational/sponsors.html")


def privacy_view(request):
    return render(request, "organizational/privacy.html")


def termsofuse_view(request):
    return render(request, "organizational/termsofuse.html")


def meetings_view(request):
    return render(request, "events/meetings.html")


def conferences_view(request):
    return render(request, "events/conferences.html")


def ctfs_view(request):
    return render(request, "events/ctfs.html")


def workshop_view(request):
    return render(request, "events/workshop.html")


def awareness_view(request):
    return render(request, "knowledge/awareness.html")


def knowledge_asip_view(request):
    return render(
        request,
        "knowledge/asip.html",
        context={"link": settings.ASIP_DASHBOARD_LINK},
    )


def blog_view(request):
    return render(request, "knowledge/blog.html")


def podcast_view(request):
    return render(request, "knowledge/podcast.html")


def library_view(request):
    return render(request, "knowledge/library.html")


def resources_view(request):
    return render(request, "knowledge/resources.html")


def supplier_directory_view(request):
    return render(request, "knowledge/supplier_directory.html")


def threat_catalog_view(request):
    return render(request, "knowledge/threat_catalog.html")


def solutions_catalog_view(request):
    return render(request, "knowledge/solutions_catalog.html")


def tools_view(request):
    return render(request, "knowledge/tools.html")


def links_view(request):
    return render(request, "knowledge/links.html")


def channels_view(request):
    return render(request, "networking/channels.html")


def social_media_view(request):
    return render(request, "networking/social_media.html")


def forums_view(request):
    return render(request, "networking/forums.html")


def newsletter_view(request):
    return render(request, "networking/newsletter.html")


def collaboration_overview_view(request):
    return render(request, "collaboration/overview.html")


def collaboration_asip_view(request):
    return render(request, "collaboration/asip.html")


def asvm_view(request):
    return render(request, "collaboration/asvm.html")


def member_portal_view(request):
    return render(request, "collaboration/member_portal.html")


def academia_overview_view(request):
    return render(request, "academia/overview.html")


def learning_view(request):
    return render(request, "academia/learning.html")


def technical_committees_view(request):
    return render(request, "academia/technical_committees.html")


def student_organizations_view(request):
    return render(request, "academia/student_organizations.html")


def research_view(request):
    return render(request, "academia/research.html")


def career_dev_view(request):
    return render(request, "industry/career_dev.html")


def competency_mgmt_view(request):
    return render(request, "industry/competency_mgmt.html")
