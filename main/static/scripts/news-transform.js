$(document).ready(function () {
  $('.news-link').click(function(){
    $("#news"+$(this).attr("id")).toggleClass("single-news");
    $("#news"+$(this).attr("id")).toggleClass("single-news-full");
  });
});
