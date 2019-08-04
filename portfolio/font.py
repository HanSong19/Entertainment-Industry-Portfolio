import matplotlib
import matplotlib.font_manager as fm

fm.get_fontconfig_fonts()
font_location = 'C:/Windows/Fonts/NanumBarunGothic.ttf'
font_name= fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)

