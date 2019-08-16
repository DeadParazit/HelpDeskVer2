$(document).ready(function(){
    $('.multiple_options_name_div').click(function(){
      $('#list'+$(this).attr('id')).toggleClass("hidden");
      $('#arrow'+$(this).attr('id')).toggleClass("right");
      $('#arrow'+$(this).attr('id')).toggleClass("down");
    });
});
