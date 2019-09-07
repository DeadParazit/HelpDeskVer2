function applyHoverActions(){
    // $('.option').unbind('hover');
    // $('.option').hover(function() {
    //   $('.'+$(this).attr("id")).css({'background-color': '#888','color':'#eee'});
    //   $('.'+$(this).attr("id")).first().css('box-shadow','0 0 10px #fff inset');
    // }, function() {
    //   $('.'+$(this).attr("id")).css({'background-color': '','color':''});
    //   $('.'+$(this).attr("id")).first().css('box-shadow','');
    // });
    // $('.multiple_options_name').unbind('hover');
    // $('.multiple_options_name').hover(function() {
    //   $('.'+$(this).attr("id")).css({'background-color': '#888','color':'#eee'});
    //   $('.'+$(this).attr("id")).first().css('box-shadow','0 0 10px #fff inset');
    // }, function() {
    //   $('.'+$(this).attr("id")).css({'background-color': '','color':''});
    //   $('.'+$(this).attr("id")).first().css('box-shadow','');
    // });
    $('.col').unbind('hover');
    $('.col').hover(function() {
      $(this).css('box-shadow','0 0 10px #fff inset');
      $('.'+$(this).attr("class").split(/\s+/)[1]).css({'background-color': '#888','color':'#eee'});
    }, function() {
      if($(this).attr('title')){
        if($(this).attr('title') != "-"){
          $(this).css('box-shadow','0 0 10px #000 inset');
        }
        else{
          $(this).css('box-shadow','');
        }
      }
      else{
        $(this).css('box-shadow','');
      }
      $('.'+$(this).attr("class").split(/\s+/)[1]).css({'background-color': '','color':''});
    });
    $('.row').unbind('hover');
    $('.row').hover(function() {
      $('.'+$(this).attr("class").split(/\s+/)[1]).css({'background-color': '#888','color':'#eee'});
    }, function() {

      $('.odd').css({'background-color': '#ccc','color':'#444'})
      $('.even').css({'background-color': '#ddd','color':'#444'})
    });
};
function applyClickActions(){
  $('.col:not(.theader)').unbind('click');
  $('.col:not(.theader)').on('click',function(){
    if(!($(this).attr("class").split(/\s+/)[1] === "col1")){
      if($('.'+$(this).attr("class").split(/\s+/)[1]).first().attr('title') != $(this).html()){
        $('.'+$(this).attr("class").split(/\s+/)[1]).first().attr('title',$(this).html());
        $('.'+$(this).attr("class").split(/\s+/)[1]).first().css('box-shadow','0 0 10px #000 inset');
        update_with_filters();
      }
    }
  });
  $('.theader').unbind('click');
  $('.theader').on('click',function(){
    $(this).attr('title','-');
    $(this).css('box-shadow','');
    update_with_filters();
  });
}
