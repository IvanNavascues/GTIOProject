$(document).ready(function () {

    $("#submit").click(function () {

        var voto = ""
        voto = $('input[name="voto"]:checked').val();

        if (voto == null) {
            $("#avisoFormulario").text("Seleccionar una opcion.")
        }
        else {
            enviarVoto(voto)
        }

    })


    $enviarVoto = function (voto) {
        var GETurl = "api/votes/" + voto
        $.ajax({
            type: "GET",
            url: GETurl,
            success: function (data) {
                $("#avisoFormulario").text("voto enviado.");
            }
        });


    }

});