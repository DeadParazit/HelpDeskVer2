$(document).ready(function () {
  $('.course-add-button').click(function(){
    $('.course-add').css("display","block");
    $('.course-add-select').val($(this).attr("id"));
  });
  $('.close-form').click(function(){
    $('.course-add').css("display","none");
    $('.add-input').val("");
  });
});
