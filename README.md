# zeno-paradoxes

## Achille et la tortue
### Contexte:
Dans ses réflexions, Zenon imagine
Achille, le héros au pied léger,
engagé dans une course à pied avec
une humble tortue. Mais à
l'étonnement de Zénon, la course se
déroule de la manière la plus
singulière qui soit. Alors qu'Achille
donne à la tortue une longueur
d'avance, il découvre bientôt que,
quelle que soit la rapidité de son
sprint, il ne parvient jamais à
dépasser la créature pataude. En
effet, à chaque fois qu'Achille atteint
le point où se trouvait la Tortue, la créature a progressé davantage, lui échappant
éternellement.

Donc:
- Si la postion initiale d'Achille est 0 (achille = 0)
- et qu'il a un sprint de 10 (vitesse_achille = 10)
- Si la position initiale de la tortue est 100 (tortue = 100)
- avec un sprint de 2 (vitesse_tortue = 2)
<br>
Quand Achille atteindra la position de la tortue, celle ci aura déjà effectué une nouvelle distance de: <br>
- distance = vitesse de la tortue * temps mis par Achille pour rejoindre la position précédente de la tortue (temps = distance (position de la tortue - position d'Achille) / vitesse d'Achille) <br>
- La nouvelle position de la tortue sera donc de: postion initiale + vitesse de la tortue * temps
<br>
Autrement dit, à chaque fois qu'Achille arrivera à la hauteur de la tortue; celle-ci aura constamment un légère avance sur lui, aussi infime soit elle.

## Paradoxe de la dichotomie
### Contexte:
Imaginez que Zénon se trouve face à un arbre imposant, tenant fermement une
pierre dans sa main. Sa tentative de toucher l'arbre en lançant la pierre se heurte
à un paradoxe intrigant. Selon sa réflexion, la pierre doit franchir la moitié de la
distance totale de 8 mètres pour atteindre l'arbre, soit 4 mètres. Ensuite, celle-ci
doit parcourir des distances réduites successives : deux mètres, un mètre, et
ainsi de suite, chaque étape prenant un temps fini. Cette progression
ininterrompue amène Zénon à une conclusion : la pierre ne peut jamais atteindre
l'arbre. Il semblerait que pour ce faire, la pierre doive accomplir une infinité
d'étapes, ce qui, aux yeux de Zénon, défie toute logique.

Donc:
- Si la pierre est lancée depuis la distance 0 (pierre = 0)
- Et que sa cible, l'arbre, se situe à une distance de 100 (arbre = 100)
<br>
A chacune des étapes, la position de la pierre sera de: <br>
pierre += distance séparant l'arbre de la pierre / 2
<br>
Ainsi l'on constate que quelque soit la distance séparant l'arbre de la pierre, celle-ci ne se vera jamais réduite à 0.

## Flèche en vol
### Contexte:
Dans le paradoxe de la flèche, Zénon imagine une flèche en vol. À chaque instant,
la flèche occupe une position précise dans l'espace. Si l'instant est trop court,
alors la flèche n'a pas le temps de se déplacer et reste au repos pendant cet
instant. Maintenant, pendant les instants suivants, elle va rester immobile pour la
même raison. Si le temps est une succession d'instants et que chaque instant
est un moment où le temps est arrêté, le temps n'existe donc pas. La flèche est
donc toujours immobile à chaque instant et ne peut pas se déplacer : le
mouvement est donc impossible.

Donc:
#### Pour une flèche:
- position = 0
- vitesse = 50
#### Pour une cible:
- distance = 500
#### La position de la flèche sera de: temps écoulé depuis le tir de la flèche * vitesse de la flèche
#### Autrement dit, à l'instant t : la position de la flèche sera de:
- t * vitesse de la flèche 
