$(document).ready(function () {
  $('.tel-num').focus(function() {
    $(this).attr('placeholder', '+X (XXX) XXX-XX-XX')
  }).blur(function() {
    $(this).attr('placeholder', 'Номер')
  })
  $(".tel-num").on('input',function(){
      var value = $(this).val();
      var numbers="1234567890";
      var check=true;
      value=value.replace(/[( )-]/g,'');
      value=value.replace("+7",'');
      StrLen=value.length;
      if(StrLen>10){
        value=value.substring(0,10);
      }
      var i;
      for(i=0;i<10;i++){
          if(value[value.length-1]==numbers[i]){
            check=false;
            break;
        }
      }
      if(check){
        value=value.substring(0,value.length-1);
      }
      StrLen=value.length;
      if(StrLen>0){
        value="+7 ("+value;
      }
      if(StrLen>3){
        var substring1=value.substring(0,7);

        var substring2=value.substring(7,value.length);

        value=substring1+") "+substring2;
      }
      if(StrLen>6){
        var substring1=value.substring(0,12);
        var substring2=value.substring(12,value.length);
        value=substring1+"-"+substring2;
      }
      if(StrLen>8){
        var substring1=value.substring(0,15);
        var substring2=value.substring(15,value.length);
        value=substring1+"-"+substring2;
      }
      $(this).val(value);
  });
});
