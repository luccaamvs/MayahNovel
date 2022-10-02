define a = Character("Albert")
image Albert normal = "images/albert-normal.png"

image pesadelo = "images/pesadelo.png"
image tenebre = "images/tenebre.png"

label start:

    scene pesadelo

    "Agonia. A ansiedade de sentir-se só em meio a imensidão do mundo." 
    with fade

    "Infinitas sombras negras, monstros sem forma definida que devoravam alguma cidade que para você é irreconhecível. Infinitos gritos se proliferavam ao seu redor."
    
    "Baixos monumentos e altas torres eram igualmente demolidos pelos colossos uivantes que se debatiam por todo lugar. Eles eram imateriais, negros como núvens de intensas tempestades, e, ao mesmo tempo, sólidos e afiados como navalhas gigantes. Tais criaturas eram numerosas e cobriam grande parte da cidade."

    "Você sente que vai morrer. Sabe que vai morrer. Encarando os enormes olhos vazios dos seres noturnos, sem opção, você busca por alguma arma. Sua espada. Ela não se encontra em mãos. Sua próxima tentativa é a fuga mas, antes mesmo de iniciar o movimento desesperado, sabe que não terá tempo ou sorte de escapar dos devoradores de nações."

    "Você sente que vai morrer. Sabe que vai morrer. Entre a entropia e o caos onipresente, tudo o que resta fazer é apenas aguardar o clemente fim inevitável. Seu corpo sente uma breve tranquilidade surgir como uma eutanasia aliviante."

    "Arregalando os olhos, deitado em sua cama, você encara o teto após o pesadelo inusitado."

    scene tenebre

    show Albert normal at center:
        zoom 0.8 ##isso vai ser mudado depois
    with dissolve

    a "You've created a new Ren'Py game."

    a "Once you add a story, pictures, and music, you can release it to the world!"

    return
