import PySimpleGUI as sg

"""
    Demo showing how to add your own theme.
    
    There are functions to make the job quick and easy.
    
    Copyright 2021 PySimpleGUI.org
"""

# First make a dictionary with the required keys.
# Use only colors in the format of #RRGGBB
DarkGrey20 = {'BACKGROUND': '#19232D',
             'TEXT': '#ffffff',
             'INPUT': '#32414B',
             'TEXT_INPUT': '#ffffff',
             'SCROLL': '#505F69',
             'BUTTON': ('#ffffff', '#32414B'),
             'PROGRESS': ('#505F69', '#32414B'),
             'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
             }

# Add your dictionary to the PySimpleGUI themes
sg.theme_add_new('DarkGrey20', DarkGrey20)

# Switch your theme to use the newly added one
sg.theme('Dark Grey 20')

def main():
    # Test it out!
    try:
        sg.popup_get_text('Dark Grey 20 looks like this.', image=sg.EMOJI_BASE64_HAPPY_THUMBS_UP)
    except:
        sg.popup_get_text('Dark Grey 20 looks like this.\n' + \
                          'Upgrading to 4.35.0+ will give you a nice emoji like the one above',
                          image=EMOJI_BASE64_HAPPY_THUMBS_UP)

if __name__ == '__main__':
    EMOJI_BASE64_HAPPY_THUMBS_UP = b'iVBORw0KGgoAAAANSUhEUgAAADgAAAA4CAYAAACohjseAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyJpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoV2luZG93cykiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6N0M3M0ExQkM3OTk2MTFFQkFDREU4QkE2OUQ2Njk5ODUiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6N0M3M0ExQkQ3OTk2MTFFQkFDREU4QkE2OUQ2Njk5ODUiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDo3QzczQTFCQTc5OTYxMUVCQUNERThCQTY5RDY2OTk4NSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDo3QzczQTFCQjc5OTYxMUVCQUNERThCQTY5RDY2OTk4NSIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PrSTufUAABP3SURBVHja3Fp5cF31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'
    main()