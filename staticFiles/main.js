$(document).ready(function () {
    $("#submitBtn").click(function (e) {
        e.preventDefault();

        var language1 = $("#language1").val();
        var language2 = $("#language2").val();
        var inputText = $("#inputText").val();

        var data = {
            language1: language1,
            language2: language2,
            input_text: inputText
        };

        $.ajax({
            type: "POST",
            url: "/",
            data: data,
            success: function (response) {
                console.log(response);
                $("#outputText").val(response);
                $("#inputText").val("");
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    $("#swapDropdownsBtn").click(function () {
        var language1 = $("#language1").val();
        var language2 = $("#language2").val();


        $("#language1").val(language2);
        $("#language2").val(language1);
    });

    $("#swapInputBtn").click(function () {
        var inputText = $("#inputText").val();
        var outputText = $("#outputText").val();

        $("#inputText").val(outputText);
        $("#outputText").val(inputText);
    });
});