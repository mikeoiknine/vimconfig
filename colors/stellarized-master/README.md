<table><tbody><tr><td align="center"><h1>stellarized</h1>
<img src="https://github.com/nightsense/stellarized/raw/master/images/header.jpg" />
<h4>paint vim with the stars</h4>
</td></tr></tbody></table>

## palette

<table><tbody>
<tr>
<td align="center"><h6><img alt="screenshot of the stellarized vim theme, light version" src="https://github.com/nightsense/stellarized/raw/master/images/screenshot-light.png" height="325" /><br><br>
sunny day</h6>
</td>
<td align="center"><h6><img alt="screenshot of the stellarized vim theme, dark version" src="https://github.com/nightsense/stellarized/raw/master/images/screenshot-dark.png" height="325" /><br><br>
starry night</h6>
</td>
</tr>

<tr></tr>

<tr><td align='center' colspan='2'>

<h6>The <a href='http://ethanschoonover.com/solarized'>solarized theme</a>, inspired by reading a book under<br>a shady tree on a sunny day, features a base palette<br>of dark green-blue and bright orange-yellow.</h6>

<h6>The stellarized theme takes this basic idea and shifts<br>the base hues to reflect the <a href='http://www.vendian.org/mncharity/dir3/starcolor/details.html'>colours of the stars</a>.

<h6>Specifically, dark base colors are shifted bluewise (to<br>the approximate "hot star hue"), while light base colors<br>are shifted orangewise (to the "cold star hue").</h6>

<h6>stellarized is a special adaptation of <a href='https://github.com/nightsense/snow'>snow</a>.</h6>

</h6>
</td></tr>

</tbody></table>


## installation

If you don’t have a preferred plugin helper, consider trying [vim-plug](https://github.com/junegunn/vim-plug), which can be installed with:

```
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

With vim-plug, stellarized can be installed by adding the following to the top of your vimrc...

```
call plug#begin('~/.vim/plugged')
Plug 'nightsense/stellarized'
call plug#end()
```

...then reloading vimrc (by running `:so %` at the vim command line, or by restarting vim), followed by `:PlugUpdate`.

## activation

For a sunny day, add the following to vimrc:

```
colorscheme stellarized
set background=light
```

For a starry night:

```
colorscheme stellarized
set background=dark
```

If you'd like the background to switch automatically at sunrise/set (or any other time), consider trying [night-and-day](https://github.com/nightsense/night-and-day).

## terminal vim

### colors

stellarized should work in 256-color and true-color terminals. You may need the following in vimrc:

```
set termguicolors
```

### cursor shape

To set mode-specific cursor shapes in terminal vim, see the [Vim Tips Wiki](http://vim.wikia.com/wiki/Change_cursor_shape_in_different_modes).

For instance, to set cursor shapes in vte-compatible terminals (like urxvt), you could add to vimrc:

```
let &t_SI = "\<Esc>[6 q"
let &t_SR = "\<Esc>[4 q"
let &t_EI = "\<Esc>[2 q"
```

...which sets the cursor to a vertical line for insert mode, underline for replace mode, and block for normal mode.

## status line themes

stellarized comes with themes for airline and lightline. A separate theme is provided for each variant+background.

For instance, to activate the dark airline theme:

```
let g:airline_theme='stellarized_dark'
```

For lightline:

```
let g:lightline = { 'colorscheme': 'stellarized_dark' }
```

`dark` can be replaced with `light`.

---

###### ▸&nbsp;&nbsp;the stellarized colorscheme is generated with [Colortemplate](https://github.com/lifepillar/vim-colortemplate) and provided under the [MIT license](https://opensource.org/licenses/MIT)
###### ▸&nbsp;&nbsp;text contrast meets the 4.5:1 [W3C standard](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html), except for peripheral text (e.g. comments) which meets the 3:1 ISO standard
###### ▸&nbsp;&nbsp;image credit: night sky photo by [ESO/S. Brunier (CC BY 4.0)](https://commons.wikimedia.org/wiki/File:ESO_-_Milky_Way.jpg)
