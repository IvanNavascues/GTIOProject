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


    function enviarVoto(voto) {
        var GETurl = "vote/" + voto
        $.ajax({
            type: "GET",
            url: GETurl,
            success: function (data) {
                $("#avisoFormulario").text("voto enviado.");
            }
        });


    }


});
