set s stellarized
set t $s'.colortemplate'
python template-generator.py $s > $t
vim -c 'Colortemplate! ~/Documents/code/vim/stellarized' $t -c 'qa!'
sed -i '/Last Updated/d' ../colors/$s.vim
