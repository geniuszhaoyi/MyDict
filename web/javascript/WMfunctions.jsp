$.extend({XMLgetOne:function(xml){
  var mark = 0;
  var ans = '';
  xml.each(function(index, ele){
    if(mark==1) return 
    mark=1
    ans=$(ele).text()
  });
  return ans
}});
$.extend({WMRP:function(string){
  if(string==null) return '';
  string=string.replace(eval("/"+"<it>"+"/gi"),'<span style="font-style: italic; ">');
  string=string.replace(eval("/"+"<[\/]it>"+"/gi"),"</span>");
  string=string.replace(eval("/"+"<un>"+"/gi")," --");
  string=string.replace(eval("/"+"<[\/]un>"+"/gi")," ");
  string=string.replace(eval("/"+"<vi>"+"/gi"),"&lt;");
  string=string.replace(eval("/"+"<[\/]vi>"+"/gi"),"&gt");
  string=string.replace(eval("/"+"<ma>"+"/gi"),"[");
  string=string.replace(eval("/"+"<[\/]ma>"+"/gi"),"]");
  return string;
}});

