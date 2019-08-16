$(document).ready(function() {
  if($(location).attr("href").indexOf('#')==-1){
    $(".flash-movie").css("display","block");
    $("header").css("display","none");
    $("main").css("display","none");
    $("footer").css("display","none");
  }
});
$(".skip").click(function(){
  $(".flash-movie").css("display","none");
  $("header").css("display","block");
  $("main").css("display","block");
  $("footer").css("display","block");
});
