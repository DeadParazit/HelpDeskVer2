function applyInputLimits(){
  $('.inputTextField').on('input',function(){
    var value = $(this).val();
    if(value.lenght>255){
      value=value.substring(0,255);
    }
    $(this).val(value);
  });
}
function applyInputRequerments(){
  $('.requered').focusout(function(){
    var value = $(this).val();
    if(value == ""){
      $('#'+$(this).attr('class').split(' ')[1]+'2').addClass('red');
      $('.'+$(this).attr('class').split(' ')[1]+'1').addClass('red');
      $('#'+$(this).attr('class').split(' ')[2]).addClass('red');
      $('#'+$(this).attr('class').split(' ')[2]+'_title').addClass('red');
      $('#'+$(this).attr('class').split(' ')[2]+'_title').addClass('red');
      $('#'+$("."+$(this).attr('class').split(' ')[1]+'1').attr('class').split(' ')[1]+"_title").addClass('red');
      $('#'+$('#'+$("."+$(this).attr('class').split(' ')[1]+'1').attr('class').split(' ')[1]+"_title").attr('class').split(' ')[0]+"_title").addClass('red');
    }
  });
  $('.requered').on('input',function(){
    var value = $(this).val();
    if(value != ""){
      $('#'+$(this).attr('class').split(' ')[1]+'2').removeClass('red');
      $('.'+$(this).attr('class').split(' ')[1]+'1').removeClass('red');
      if($('#'+$(this).attr('class').split(' ')[2]).find('.red').length==0){
        $('#'+$(this).attr('class').split(' ')[2]).removeClass('red');
        $('#'+$(this).attr('class').split(' ')[2]+'_title').removeClass('red');
        $('#'+$(this).attr('class').split(' ')[2]+'_title').removeClass('red');
      }
      if($('.'+$("."+$(this).attr('class').split(' ')[1]+'1').attr('class').split(' ')[1]+"_content").find('.red').length==0){
        $('#'+$("."+$(this).attr('class').split(' ')[1]+'1').attr('class').split(' ')[1]+"_title").removeClass('red');
      }
      if($('.'+$('#'+$("."+$(this).attr('class').split(' ')[1]+'1').attr('class').split(' ')[1]+"_title").attr('class').split(' ')[0]+"_content").find('.red').length==0){
        $('#'+$('#'+$("."+$(this).attr('class').split(' ')[1]+'1').attr('class').split(' ')[1]+"_title").attr('class').split(' ')[0]+"_title").removeClass('red');
      }
    }
  });
  $('.requered').on('change',function(){
    var value = $(this).val();
    if(value != ""){
      $('#'+$(this).attr('class').split(' ')[1]+'2').removeClass('red');
      $('.'+$(this).attr('class').split(' ')[1]+'1').removeClass('red');
      if($('#'+$(this).attr('class').split(' ')[2]).find('.red').length==0){
        $('#'+$(this).attr('class').split(' ')[2]).removeClass('red');
        $('#'+$(this).attr('class').split(' ')[2]+'_title').removeClass('red');
        $('#'+$(this).attr('class').split(' ')[2]+'_title').removeClass('red');
      }
      if($('.'+$("."+$(this).attr('class').split(' ')[1]+'1').attr('class').split(' ')[1]+"_content").find('.red').length==0){
        $('#'+$("."+$(this).attr('class').split(' ')[1]+'1').attr('class').split(' ')[1]+"_title").removeClass('red');
      }
      if($('.'+$('#'+$("."+$(this).attr('class').split(' ')[1]+'1').attr('class').split(' ')[1]+"_title").attr('class').split(' ')[0]+"_content").find('.red').length==0){
        $('#'+$('#'+$("."+$(this).attr('class').split(' ')[1]+'1').attr('class').split(' ')[1]+"_title").attr('class').split(' ')[0]+"_title").removeClass('red');
      }
    }
  });
}
function applyClickSelection(){
  $('.option').on('click',function(){
    $('.'+$(this).attr('class').split(' ')[0].slice(0,-1)).not('select').focus();
    $('.'+$(this).attr('class').split(' ')[0].slice(0,-1)).filter('select').select2('open');
  });
}
