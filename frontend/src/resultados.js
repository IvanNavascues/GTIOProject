$(document).ready(function () {

    var leyenda = {
        "1": "Carlos Fustel",
        "2": "Claudia Arenas",
        "3": "Cristina Lora",
        "4": "Elena Matateyou",
        "5": "Guille Toledano",
        "6": "Guillo Rist",
        "7": "Ivan Rojo",
        "8": "JaviCrespo",
        "9": "JuditGaruz",
        "10": "Laura Munyoz",
        "11": "Lucia Casani",
        "12": "Maria Cruz",
        "13": "Martin Yanyez",
        "14": "Olivia Bay",
        "15": "Salma De Diego"
    }

/*
    $.ajax({
        type: "GET",
        url: "http://localhost:5000/votes",
        success: function (data) {
            update(data)
        }
    });
*/
    data={
        "1":"555",
        "7":"8979",
		"8":"40",
		"12":"5505",
		"4":"108"
	}
    mostrar(data)


    function mostrar(data) {
        let max = 0
        let keys = Object.keys(data)        
        for (let i = 0; i < keys.length; i++) {
            if (Number(data[keys[i]])>max){
                console.log("here")
                max = Number(data[keys[i]])
            }
        }

        let name = ""
        let votes = 0

        var row = document.createElement("div")
        row.className="row"
        var col2 = document.createElement("div")
        col2.className="col-2"
        var col8 = document.createElement("div")
        col8.className="col-8"
        var spacing = document.createElement("div")
        spacing.className="dontainer mt-4"
        for (let i = 0; i<keys.length; i++){
            name = leyenda[keys[i]]
            votes = Number(data[keys[i]])
            var spanName = document.createElement("span")
            spanName.textContent=name + " (" + String(votes) + ")"

            var progress = document.createElement("div")
            progress.className="progress"
            progress.role="progressbar"
            progress.ariaValueNow=votes
            progress.ariaValueMin=0
            progress.ariaValueMax=max

            var width = Math.floor(votes*100.0/max)

            var width_text = "width: "+ String(width) + "%"
            var bar = document.createElement("div")
            bar.className="progress-bar"
            bar.style=width_text

            progress.appendChild(bar)

            col8.appendChild(spanName)
            col8.appendChild(progress)

            row.appendChild(col2)
            row.appendChild(col8)
            
            document.getElementById("nominados").appendChild(row)
            document.getElementById("nominados").appendChild(spacing)
        
        }
/*
    <div class = "row">
        <div class="col-2"></div>
        <div class="col-8">
            <span>candidato</span>
            <div class="progress" role="progressbar" aria-label="Basic example" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
                <div class="progress-bar" style="width: 0%"></div>
            </div>           
        </div>
    </div>

    <div class="container mt-4"></div>
*/
        //NECESITAMOS: nombre, votos maximos, votos individuales
        //valuemax TODAS = valor maximo en el array
        //valuenw = valor individual

    }


})