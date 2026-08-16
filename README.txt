ABRÉVIATION
c : computer mode
p : phone mode
fr : french
en : english

STRUCTURE
text.txt : contenu des pages, build.py est run quand il est modifié et que les changements sont push
update.yml : permet d'automatiquement run buil.py après une modification de text.txt et un push
build.py : code pour générer les pages web, il doit être run à chaque modification du site web
script.js : code qui interagit avec les pages, il gère aussi les langues et les modes
style.css : style des pages, il est répartit entre 2 fichiers, un pour chaque mode
