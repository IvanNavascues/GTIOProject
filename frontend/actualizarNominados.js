$(document).ready(function () {

    var leyenda = {
        "01": "Carlos Fustel",
        "02": "Claudia Arenas",
        "03": "Cristina Lora",
        "04": "Elena Matateyou",
        "05": "Guille Toledano",
        "06": "Guillo Rist",
        "07": "Ivan Rojo",
        "08": "JaviCrespo",
        "09": "JuditGaruz",
        "10": "Laura Munyoz",
        "11": "Lucia Casani",
        "12": "Maria Cruz",
        "13": "Martin Yanyez",
        "14": "Olivia Bay",
        "15": "Salma De Diego"
    }

    
    $.ajax({
        type: "GET",
        url: "/votes",
        success: function (data) {
            update(data)
        }
    });

    function update(data) {
        for (let i = 0; i < Object.keys(data).length; i++) {

            var id = Object.keys(data)[i]
            var img_source = "imagenes/" + id + ".webp"
            var nombre = leyenda[id]

            var col = document.createElement("div")
            col.className = "col"
            var row1 = document.createElement("div")
            row1.className = "row"
            var row2 = document.createElement("div")
            row2.className = "row"
            var row3 = document.createElement("div")
            row3.className = "row"

            var img = document.createElement("img")
            img.src = img_source

            var label = document.createElement("label")
            label.id = "nominado_" + id
            label.textContent = nombre

            var input = document.createElement("input")
            input.type = "radio"
            input.name = "voto"
            input.value = id

            row1.appendChild(img)
            row2.appendChild(label)
            row3.appendChild(input)

            col.appendChild(row1)
            col.appendChild(row2)
            col.appendChild(row3)

            document.getElementById("nominados").appendChild(col)
        }
    }



})