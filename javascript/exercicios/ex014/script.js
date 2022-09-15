function carregar() {
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 0 && hora < 12) {
        //BOM DIA!
        img.src = 'fotomanha.png'
        msg.innerHTML += ' Boa Dia!'
        document.body.style.background = '#ccebff'
    } else if (hora >= 12 && hora <= 18) { 
        //BOA TARDE
        img.src = 'fototarde.png'
        msg.innerHTML += ' Boa Tarde!'
        document.body.style.background = '#fa6203'
    } else {
        //BOA NOITE
        img.src = 'fotonoite.png'
        msg.innerHTML += ' Boa Noite!'
        document.body.style.background = '#2a213f'
    }
}