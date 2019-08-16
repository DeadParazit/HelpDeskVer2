var headers = ["Номер","","Дата","Время заявки","Заявитель","Причина","Приоритет","Исполнитель"];
var content=[["1","*","dd.mm.yyyy","hh.mm.ss","Name S.P.","reason","1","Name S.P."],
             ["2","#","dd.mm.yyyy","hh.mm.ss","Name S.P.","reason","2","Name S.P."],
             ["3","#","dd.mm.yyyy","hh.mm.ss","Name S.P.","reason","3","Name S.P."],
             ["4","*","dd.mm.yyyy","hh.mm.ss","Name S.P.","reason","1","Name S.P."],
             ["5","*","dd.mm.yyyy","hh.mm.ss","Name S.P.","reason","2","Name S.P."],
             ["6","#","dd.mm.yyyy","hh.mm.ss","Name S.P.","reason","3","Name S.P."],
             ["7","#","dd.mm.yyyy","hh.mm.ss","Name S.P.","reason","1","Name S.P."],
             ["8","*","dd.mm.yyyy","hh.mm.ss","Name S.P.","reason","2","Name S.P."]];
var htmlContent="";
function basic_form(){
  $(document).ready(function(){
    var htmlContent="<tr class=\"row row1 odd\">";
    for(var i=0;i<8;i++){
      htmlContent+="<th class=\"col col"+(i+1)+" theader\" title=\"-\">"+headers[i]+"</th>";
    }
    htmlContent+="</tr>";
    $('#table_header').html(htmlContent);
    htmlContent="";
    for(var i=0;i<8;i++){
      htmlContent+="<tr class=\"row row"+(i+2)+" ";
      if(i%2==0){
        htmlContent+="even\">";
      }
      else{
        htmlContent+="odd\">";
      }
      for(var j=0;j<8;j++){
          if(j==0){
            htmlContent+="<td class=\"col col"+(j+1)+"\"><a href=\"doc.html?"+content[i][j]+"\"><div>"+content[i][j]+"</div></a></td>";
          }
          else{
            htmlContent+="<td class=\"col col"+(j+1)+"\">"+content[i][j]+"</td>";
          }
      }
      htmlContent+="</tr>";
    }
    $('#table_body').html(htmlContent);
    applyHoverActions();
    applyClickActions();
  });
}
function update_with_filters(){
  htmlContent="";
  var headers=[$('.theader:nth-child(1)').attr('title'),$('.theader:nth-child(2)').attr('title'),$('.theader:nth-child(3)').attr('title'),$('.theader:nth-child(4)').attr('title'),$('.theader:nth-child(5)').attr('title'),$('.theader:nth-child(6)').attr('title'),$('.theader:nth-child(7)').attr('title'),$('.theader:nth-child(8)').attr('title')];
  for(var i=0;i<8;i++){
    if(headers[0] === content[i][0] || headers[0] === "-"){
      if(headers[1] === content[i][1] || headers[1] === "-"){
        if(headers[2] === content[i][2] || headers[2] === "-"){
          if(headers[3] === content[i][3] || headers[3] === "-"){
            if(headers[4] === content[i][4] || headers[4] === "-"){
              if(headers[5] === content[i][5] || headers[5] === "-"){
                if(headers[6] === content[i][6] || headers[6] === "-"){
                  if(headers[7] === content[i][7] || headers[7] === "-"){
                    htmlContent+="<tr class=\"row row"+(i+2)+" ";
                    if(i%2==0){
                      htmlContent+="even\">";
                    }
                    else{
                      htmlContent+="odd\">";
                    }
                    for(var j=0;j<8;j++){
                      if(j==0){
                        htmlContent+="<td class=\"col col"+(j+1)+"\"><a href=\"doc.html?"+content[i][j]+"\"><div>"+content[i][j]+"</div></a></td>";
                      }
                      else{
                        htmlContent+="<td class=\"col col"+(j+1)+"\">"+content[i][j]+"</td>";
                      }
                    }
                    htmlContent+="</tr>";
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  $('#table_body').html(htmlContent);
  applyHoverActions();
  applyClickActions();
}
