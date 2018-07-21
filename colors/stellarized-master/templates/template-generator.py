from colormath.color_conversions import convert_color
from colormath.color_objects import LCHabColor,sRGBColor
import sys

if len(sys.argv) < 2:
  print 'specify theme name'
  sys.exit()
else:
  theme_name = sys.argv[1]

def tohex(l,c,h):
  rgb = convert_color(LCHabColor(l,c,h),sRGBColor)
  clamp = sRGBColor(rgb.clamped_rgb_r, rgb.clamped_rgb_g, rgb.clamped_rgb_b)
  return clamp.get_rgb_hex()

def gold(e):
  return 0.61803398875**e*100

def print_airline(name,bg):
  print 'auxfile autoload/airline/themes/%s_%s.vim' % (name, bg)
  print 'let g:airline#themes#%s_%s#palette = {}' % (name, bg)
  print ''
  print 'let s:gry0 = [ "@guigry0", @termgry0 ]'
  print 'let s:gry1 = [ "@guigry1", @termgry1 ]'
  print 'let s:gry2 = [ "@guigry2", @termgry2 ]'
  print 'let s:gry3 = [ "@guigry3", @termgry3 ]'
  print 'let s:red_ = [ "@guired_", @termred_ ]'
  print 'let s:gren = [ "@guigren", @termgren ]'
  print 'let s:blue = [ "@guiblue", @termblue ]'
  print ''
  print 'let s:nrm1 = [ s:gry0[0] , s:gry3[0] , s:gry0[1] , s:gry3[1] ]'
  print 'let s:nrm2 = [ s:gry3[0] , s:gry1[0] , s:gry3[1] , s:gry1[1] ]'
  print 'let s:insr = [ s:gry0[0] , s:gren[0] , s:gry0[1] , s:gren[1] ]'
  print 'let s:visl = [ s:gry0[0] , s:blue[0] , s:gry0[1] , s:blue[1] ]'
  print 'let s:rplc = [ s:gry0[0] , s:red_[0] , s:gry0[1] , s:red_[1] ]'
  print 'let s:inac = [ s:gry2[0] , s:gry1[0] , s:gry2[1] , s:gry1[1] ]'
  print ''
  print 'let g:airline#themes#%s_%s#palette.normal =' % (name, bg)
  print '  \ airline#themes#generate_color_map( s:nrm1 , s:nrm2 , s:nrm2 )'
  print ''
  print 'let g:airline#themes#%s_%s#palette.insert =' % (name, bg)
  print '  \ airline#themes#generate_color_map( s:insr , s:nrm2 , s:nrm2 )'
  print ''
  print 'let g:airline#themes#%s_%s#palette.visual =' % (name, bg)
  print '  \ airline#themes#generate_color_map( s:visl , s:nrm2 , s:nrm2 )'
  print ''
  print 'let g:airline#themes#%s_%s#palette.replace =' % (name, bg)
  print '  \ airline#themes#generate_color_map( s:rplc , s:nrm2 , s:nrm2 )'
  print ''
  print 'let g:airline#themes#%s_%s#palette.inactive =' % (name, bg)
  print '  \ airline#themes#generate_color_map( s:inac , s:inac , s:inac )'
  print ''
  print 'let g:airline#themes#%s_%s#palette.ctrlp =' % (name, bg)
  print '  \ airline#extensions#ctrlp#generate_color_map( s:nrm2 , s:nrm1 , s:nrm2 )'
  print 'endauxfile'

def print_lightline(name,bg):
  print 'auxfile autoload/lightline/colorscheme/%s_%s.vim' % (name, bg)
  print 'let s:gry0 = "@guigry0"'
  print 'let s:gry1 = "@guigry1"'
  print 'let s:gry2 = "@guigry2"'
  print 'let s:gry3 = "@guigry3"'
  print 'let s:gryy = "@guigryy"'
  print 'let s:red_ = "@guired_"'
  print 'let s:yllw = "@guiyllw"'
  print 'let s:gren = "@guigren"'
  print 'let s:blue = "@guiblue"'
  print ''
  print 'let s:p = { "normal" : {} , "inactive": {} , "insert"  : {} ,'
  print '          \ "replace": {} , "visual"  : {} , "tabline" : {} }'
  print ''
  print 'let s:p.normal.left     = [[ s:gry0, s:gry3 ], [ s:gry3, s:gry1 ]]'
  print 'let s:p.normal.middle   = [[ s:gry3, s:gry1 ]]'
  print 'let s:p.normal.right    = [[ s:gry0, s:gry3 ], [ s:gry0, s:gry3 ]]'
  print ''
  print 'let s:p.inactive.left   = copy(s:p.normal.middle)'
  print 'let s:p.inactive.middle = copy(s:p.normal.middle)'
  print 'let s:p.inactive.right  = copy(s:p.normal.middle)'
  print ''
  print 'let s:p.insert.left     = [[ s:gry0, s:gren ]]'
  print 'let s:p.insert.right    = [[ s:gry0, s:gren ], [ s:gry0, s:gren ]]'
  print ''
  print 'let s:p.visual.left     = [[ s:gry0, s:blue ]]'
  print 'let s:p.visual.right    = [[ s:gry0, s:blue ], [ s:gry0, s:blue ]]'
  print ''
  print 'let s:p.replace.left    = [[ s:gry0, s:red_ ]]'
  print 'let s:p.replace.right   = [[ s:gry0, s:red_ ], [ s:gry0, s:red_ ]]'
  print ''
  print 'let s:p.tabline.left    = [[ s:gry0, s:gry3 ]]'
  print 'let s:p.tabline.tabsel  = copy(s:p.normal.middle)'
  print 'let s:p.tabline.right   = [[ s:gry0, s:gry3 ]]'
  print ''
  print 'let s:p.normal.error    = [[ s:red_, s:gry0 ]]'
  print 'let s:p.normal.warning  = [[ s:yllw, s:gryy ]]'
  print ''
  print 'let g:lightline#colorscheme#%s_%s#palette =' % (name, bg)
  print '  \ lightline#colorscheme#fill(s:p)'
  print 'endauxfile'

###

hue_bas0 = 075.0
hue_bas1 = 285.0
hue_yllw = 082.5

hexgry0_lt = tohex( gold(0.00) , gold(4.50) , hue_bas0 )
hexgry1_lt = tohex( gold(0.12) , gold(4.50) , hue_bas0 )
hexgry2_lt = tohex( gold(1.04) , gold(4.00) , hue_bas1 )
hexgry3_lt = tohex( gold(1.61) , gold(4.00) , hue_bas1 )
hexgryc_lt = tohex( gold(1.96) , gold(4.00) , hue_bas1 )
hexyllw_lt = tohex( gold(0.25) , gold(0.00) , hue_yllw )

hexgry0_dk = tohex( gold(4.11) , gold(4.75) , hue_bas1 )
hexgry1_dk = tohex( gold(3.58) , gold(4.50) , hue_bas1 )
hexgry2_dk = tohex( gold(1.61) , gold(4.00) , hue_bas0 )
hexgry3_dk = tohex( gold(1.04) , gold(4.00) , hue_bas0 )
hexgryc_dk = tohex( gold(0.78) , gold(4.00) , hue_bas0 )
hexyllw_dk = tohex( gold(0.50) , gold(1.50) , hue_yllw )

cro_lt = gold(1.0)
cro_dk = gold(3.0)
lum_dk = gold(1.0)

if theme_name == 'stellarized':
  hexred__lt = tohex( gold(1.45) , cro_lt , 037.5 )
  hexgren_lt = tohex( gold(1.48) , cro_lt , 135.0 )
  hexblue_lt = tohex( gold(1.64) , cro_lt , 255.0 )
  hexred__dk = tohex( gold(1.15) , cro_dk , 037.5 )
  hexgren_dk = tohex( gold(1.15) , cro_dk , 135.0 )
  hexblue_dk = tohex( gold(1.17) , cro_dk , 255.0 )
else:
  print 'invalid theme name'
  sys.exit()

###

print '# general'
print 'Author:          nightsense'
print 'Maintainer:      nightsense'
print 'License:         MIT'

print 'Full name:       %s' % theme_name
print 'Short name:      %s' % theme_name

print 'Terminal Colors: 256'
print ''
print '# light'
print 'Background: light'
print 'Color:      gry0 %s ~' % hexgry0_lt
print 'Color:      gry1 %s ~' % hexgry1_lt
print 'Color:      gry2 %s ~' % hexgry2_lt
print 'Color:      gry3 %s ~' % hexgry3_lt
print 'Color:      gryc %s ~' % hexgryc_lt
print 'Color:      gryy %s ~' % hexgry0_dk
print 'Color:      yllw %s ~' % hexyllw_lt
print 'Color:      red_ %s ~' % hexred__lt
print 'Color:      gren %s ~' % hexgren_lt
print 'Color:      blue %s ~' % hexblue_lt
print 'Include:    _common.colortemplate'
print 'DiffChanged yllw gryy reverse'
print 'DiffText    yllw gryy reverse'
print 'MatchParen  yllw gryy reverse'
print 'Search      yllw gryy reverse'
print ''
print_airline(theme_name,'light')
print_lightline(theme_name,'light')

###

print ''
print '# dark'
print 'Background: dark'
print 'Color:      gry0 %s ~' % hexgry0_dk
print 'Color:      gry1 %s ~' % hexgry1_dk
print 'Color:      gry2 %s ~' % hexgry2_dk
print 'Color:      gry3 %s ~' % hexgry3_dk
print 'Color:      gryc %s ~' % hexgryc_dk
print 'Color:      gryy %s ~' % hexgry0_dk
print 'Color:      yllw %s ~' % hexyllw_dk
print 'Color:      red_ %s ~' % hexred__dk
print 'Color:      gren %s ~' % hexgren_dk
print 'Color:      blue %s ~' % hexblue_dk
print 'Include:    _common.colortemplate'
print 'DiffChanged yllw gry0 reverse'
print 'DiffText    yllw gry0 reverse'
print 'MatchParen  yllw gry0 reverse'
print 'Search      yllw gry0 reverse'
print ''
print_airline(theme_name,'dark')
print_lightline(theme_name,'dark')
