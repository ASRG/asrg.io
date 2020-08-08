# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


class Chapter(models.Model):
    # TODO: Should we store the CHAPTERS in settings? I think this will be used in multiple components so it might be a better idea? (discuss with the team)
    CHAPTERS = (
        ("ASRG-S", "ASRG-S"),
        ("ASRG-D", "ASRG-D"),
        ("ASRG-TLV", "ASRG-TLV"),
        ("ASRG-C", "ASRG-C"),
        ("ASRG-SIN", "ASRG-SIN"),
        ("ASRG-MUC", "ASRG-MUC"),
        ("ASRG-CAI", "ASRG-CAI"),
        ("ASRG-SHA", "ASRG-SHA"),
        ("ASRG-BER", "ASRG-BER"),
        ("ASRG-PIT", "ASRG-PIT"),
        ("ASRG-SFO", "ASRG-SFO"),
        ("ASRG-FRA", "ASRG-FRA"),
        ("ASRG-JPN", "ASRG-JPN"),
        ("ASRG-OXF", "ASRG-OXF"),
        ("ASRG-SYD", "ASRG-SYD"),
        ("ASRG-IASI", "ASRG-IASI"),
        ("ASRG-DNCR", "ASRG-DNCR"),
        ("ASRG-DAY", "ASRG-DAY"),
        ("ASRG-REC", "ASRG-REC"),
        ("ASRG-BLR", "ASRG-BLR"),
        ("ASRG-LAX", "ASRG-LAX"),
        ("ASRG-BUC", "ASRG-BUC"),
        ("ASRG-QRO", "ASRG-QRO"),
        ("ASRG-CGN", "ASRG-CGN"),
        ("ASRG-TOR", "ASRG-TOR"),
        ("ASRG-WIN", "ASRG-WIN"),
        ("ASRG-KER", "ASRG-KER"),
        ("ASRG-VIE", "ASRG-VIE"),
        ("ASRG-HYD", "ASRG-HYD"),
    )

    # TODO: should we allow users with no chapters?
    chapter = models.CharField(max_length=24, null=False, blank=False, choices=CHAPTERS, default=CHAPTERS[0])
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.chapter

    class Meta:
        verbose_name = 'Chapter'
        verbose_name_plural = 'Chapters'
