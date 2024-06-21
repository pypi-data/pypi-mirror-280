from . import assign_form
from . import converter
from . import display
import os
from PIL import *

import sys
import time
from io import BytesIO

      
        
class GifObj:
    def __init__(self, filename, char='X' , quality_mp=4, brightness = 50, auto_adjust=False, additional_text="", repeat_times=-1,  respect_framerate=False):
        self.filename = filename
        self.framerate = respect_framerate
        self.text=additional_text
        self.repeat=repeat_times
        self.char = char 
        self.quality = quality_mp
        self.br = brightness
        self.adjust = auto_adjust 
        self.frame_draw_time = 0.0
        self.start_draw = False
    def _sleep(self, duration):
        start = time.perf_counter()
        while True:
            elapsed_time = time.perf_counter() - start
            remaining_time = duration - elapsed_time
            if remaining_time <= 0:
                break
            if remaining_time > 0.02:
                time.sleep(max(remaining_time/2, 0.0001)) 
            else:
                pass
    
            
    def render(self):
        if self.br < 0 or self.br > 100:
            return -1
        try:
            gif_img = Image.open(self.filename)
        except:
            return -1
        if self.framerate:
            fr = (gif_img.info['duration'])/1000
        else:
            fr = 0
        gif_img_frames = gif_img.n_frames
        quality_multiplier = self.quality
        char = self.char
        clear = lambda: sys.stdout.write("\033c")
        if self.text == "":
            if self.repeat == -1:
                while True:
                    for i in range(gif_img_frames):                       
                        o_t = time.perf_counter()
                        gif_img.seek(gif_img_frames // gif_img_frames * i)
                        n_img = converter.convert(gif_img , quality_multiplier)
                        pixel_arr = assign_form.assign_form(n_img)
                        display.display(pixel_arr, char, brightness=self.br, auto_adjust=self.adjust)   
                        self.frame_draw_time = time.perf_counter()-o_t;                                    
                        if self.framerate:                        
                            self._sleep(fr-self.frame_draw_time)
                        clear()
            elif self.repeat > 0:
                for i in range(self.repeat):
                    for i in range(gif_img_frames):
                        o_t = time.perf_counter()
                        gif_img.seek(gif_img_frames // gif_img_frames * i)
                        n_img = converter.convert(gif_img , quality_multiplier)
                        pixel_arr = assign_form.assign_form(n_img)
                        display.display(pixel_arr, char, brightness=self.br, auto_adjust=self.adjust)   
                        self.frame_draw_time = time.perf_counter()-o_t;              
                        if self.framerate:                        
                            self._sleep(fr-self.frame_draw_time)
                        clear()
            else:
                return None
        else:
            if self.repeat == -1:
                while True:
                    for i in range(gif_img_frames):
                        o_t = time.perf_counter()
                        gif_img.seek(gif_img_frames // gif_img_frames * i)
                        n_img = converter.convert(gif_img , quality_multiplier)
                        pixel_arr = assign_form.assign_form(n_img)
                        display.display(pixel_arr, char, brightness=self.br, auto_adjust=self.adjust, text=self.text)   
                        self.frame_draw_time = time.perf_counter()-o_t;                  
                        if self.framerate:                        
                            self._sleep(fr-self.frame_draw_time)
                        clear()
                        
            elif self.repeat > 0:
                for i in range(self.repeat):
                    for i in range(gif_img_frames):
                        o_t = time.perf_counter()
                        gif_img.seek(gif_img_frames // gif_img_frames * i)
                        n_img = converter.convert(gif_img , quality_multiplier)
                        pixel_arr = assign_form.assign_form(n_img)
                        display.display(pixel_arr, char, brightness=self.br, auto_adjust=self.adjust, text=self.text)   
                        self.frame_draw_time = time.perf_counter()-o_t;              
                        if self.framerate:                        
                            self._sleep(fr-self.frame_draw_time)
                        clear()
            else:
                return None

class ImageObj:
    def __init__(self, filename, char='X', quality_mp=4, brightness=50, auto_adjust= False):
        self.filename = filename
        self.char = char
        self.quality = quality_mp
        self.brightness = brightness
        self.adjust = auto_adjust
    
    def render(self):
        try:
            img = Image.open(self.filename)  
            _img_arr = converter.convert(img, self.quality)

        except:
            return -1
        _ = assign_form.assign_form(_img_arr) 
        display.display(_, char=self.char, brightness=self.brightness, auto_adjust=self.adjust)
        




