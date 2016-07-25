$(document).ready(function(){
    $(".question-button").click(function(){
        showPopup();
    });
    
function showPopup() {
    $(".popup").fadeIn();
    $(".wrapper").css({"display":"block"});
}
$(".add_review").click(function(){
    $(".popup_review").fadeIn();
    $(".wrapper").css({"display":"block"});
});
$(".fa-times").click(function(){
   $(".popup").fadeOut();
    $(".popup_review").fadeOut();
   $(".wrapper").fadeOut();
})

})