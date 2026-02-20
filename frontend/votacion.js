$(document).ready(function () {

    $("#submit").click(function () {
        //var email = $("#campoCorreo").val()
        //var pass = $("#campoContrasenya").val()

        var voto = ""
        voto = $('input[name="voto"]:checked').val();

        //console.log("email: " + email)
        //console.log("voto: " + voto)

        if (voto == null) {
            $("#avisoFormulario").text("Seleccionar una opcion.")
        }
        else {
            enviarVoto(voto)
            /*
            if ($validarCorreo(email) && $validarPass(pass)) {
                $enviarVoto(email, pass, voto)
            }
            else {
                $("#avisoFormulario").text("email o contrasenya invalida.")
            }
            */
        }

    })

    $validarPass = function (pass) {
        if (pass.length < 3 || pass.length > 15) {
            return false
        }
        return true
    }

    $enviarVoto = function (voto) {
        var GETurl = "/vote/" + voto
        $.ajax({
            type: "GET",
            url: GETurl,
            success: function (data) {
                $("#avisoFormulario").text("voto enviado.");
            }
        });


    }

    /*
        $validarCorreo = function (email) {
            var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
            return regex.test(email);
    
        }
    
        $enviarVoto = function (email, pass, voto) {
            $("#avisoFormulario").text("")
            console.log("comprobar email")
            console.log("votado por " + voto)
    
        }
    */
});