$(document).ready(function () {

    var leyenda = {
        "0": "Carlos Fustel",
        "1": "Claudia Arenas",
        "2": "Cristina Lora",
        "3": "Elena Matateyou",
        "4": "Guille Toledano",
        "5": "Guillo Rist",
        "6": "Ivan Rojo",
        "7": "JaviCrespo",
        "8": "JuditGaruz",
        "9": "Laura Munyoz",
        "10": "Lucia Casani",
        "11": "Maria Cruz",
        "12": "Martin Yanyez",
        "13": "Olivia Bay",
        "14": "Salma De Diego"
    }

    
    $.ajax({
        type: "GET",
        url: "http://localhost:5000/votes",
        success: function (data) {
            update(data)
        }
    });
/*
    data={
        "1":"555",
        "7":"8979",
		"8":"4",
		"12":"44444",
		"4":"0"
	}
    update(data)
*/
    function update(data) {
        for (let i = 0; i < Object.keys(data).length; i++) {
            
            var id = Object.keys(data)[i]
            var img_source = "imagenes/" + id + ".webp"
            var nombre = leyenda[id]

            var col = document.createElement("div")
            col.className = "col-md "
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