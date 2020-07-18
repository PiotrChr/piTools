import settings
from library import tkinterUtils

templating = tkinterUtils.TkinterTemplating(
    switch_text_on=settings.LAYOUT_TEXT_ON,
    switch_text_off=settings.LAYOUT_TEXT_OFF,
    button_width=settings.LAYOUT_BUTTON_WIDTH,
    button_height=settings.LAYOUT_BUTTON_HEIGHT,
    font_size=settings.LAYOUT_FONT_SIZE,
    font_family=settings.LAYOUT_FONT_FAMILY,
    font_size_big=settings.LAYOUT_BIG_FONT_SIZE,
    font_size_small=settings.LAYOUT_SMALL_FONT_SIZE,
    frame_width=settings.LAYOUT_FRAME_WIDTH,
    frame_height=settings.LAYOUT_FRAME_HEIGHT,
    left_right_ratio=settings.LAYOUT_FRAME_LEFT_RIGHT_RATIO
)
