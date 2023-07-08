def reemplazar_vocales(string):
    vocales = ['a', 'e', 'o', 'u']
    resultado = ''
    for letra in string:
        if letra.lower() in vocales:
            resultado += 'i'
        else:
            resultado += letra
    return resultado


insultos = [
    "Eres un completo inútil, Quniverk.",
    "Quniverk, tu inteligencia es comparable a la de una piedra.",
    "¡Quniverk, eres patéticamente estúpido!",
    "No sé cómo alguien como Quniverk puede ser tan repulsivo.",
    "Quniverk, eres el ejemplo perfecto de un fracaso humano.",
    "Quniverk, tu presencia es una afrenta a la existencia misma.",
    "Cada vez que hablas, Quniverk, el mundo se vuelve un lugar más tonto.",
    "No puedo creer que alguien como Quniverk pueda ser tan desagradable.",
    "Quniverk, tu capacidad de arruinar todo a tu paso es impresionante.",
    "Incluso los virus tienen más utilidad que Quniverk.",
    "Quniverk, eres un ejemplo viviente de cómo no debería ser un ser humano.",
    "Quniverk, tu falta de habilidades sociales es asombrosa.",
    "Me pregunto qué tragedia cósmica causó la existencia de alguien como Quniverk.",
    "Quniverk, eres tan patético que hasta los gatos te ignoran.",
    "Quniverk, tu mediocridad no conoce límites.",
    "Si la estupidez fuese un superpoder, Quniverk sería invencible.",
    "Quniverk, ni siquiera tus padres pueden estar orgullosos de ti.",
    "Cada vez que abres la boca, Quniverk, es como escuchar una sinfonía de ignorancia.",
    "Quniverk, tu existencia es una broma cruel de la naturaleza.",
    "No puedo imaginar un castigo suficiente para alguien tan insufrible como Quniverk.",
    "Quniverk, eres un claro ejemplo de cómo la selección natural ha fallado estrepitosamente.",
    "Incluso las piedras tienen más carisma que Quniverk.",
    "Quniverk, tu nivel de incompetencia es sobrecogedor.",
    "Me pregunto si Quniverk alguna vez ha hecho algo útil en su vida.",
    "Quniverk, te superas en cada intento por ser menos relevante.",
    "La simple mención de tu nombre, Quniverk, provoca un escalofrío de desdén.",
    "Quniverk, tu capacidad para arruinar cualquier situación es impresionante.",
    "Eres tan despreciable, Quniverk, que incluso los gérmenes te evitan.",
    "No puedo creer que alguien como Quniverk pueda ser tan desalmado.",
    "Quniverk, eres un ejemplo claro de cómo la estupidez no tiene límites.",
    "Cada vez que te veo, Quniverk, pierdo un poco más la fe en la humanidad.",
    "Quniverk, eres un claro recordatorio de que el sentido común es un bien escaso.",
    "Me pregunto si Quniverk alguna vez ha logrado algo más que decepcionar a los demás.",
]