from .base import *

SECRET_KEY = config("SECRET_KEY", default="S#perS3crEt_1122")
SITE_ID = config("MEMBERS_SITE_ID", default=2)

CMS_TEMPLATES = (
    ("cms_app/landing_template.html", "Landing page template"),
    ("cms_app/article.html", "Article template"),
    ("cms_app/menu.html", "Menu Template"),
    ("cms_app/base.html", "Base Template"),
)
MIDDLEWARE.append("cms_app.login_required.LoginRequired")
