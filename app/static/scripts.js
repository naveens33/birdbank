$(function() {
    var path = "/";

    $("#signin_button").click(function(event) {
        event.preventDefault();
        window.location.href = path + "login";
    });
});
