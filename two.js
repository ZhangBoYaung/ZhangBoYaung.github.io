window.alert("你好！\n这里是张博洋的网站！");
function butiaozhuan()
{
    document.getElementById("div").style='display:none';
}
function tiaozhuan()
{
    window.open("door.html")
}
function code()
{
    document.getElementById("div").style.display='block';
}
function hello()
{
    var txt = prompt("输入0至100的任意一个整数或小数")
   var a = document.getElementById("hello");
   a.style='font-size:25px;animation-name:welcome2;animation-duration:'+txt+'s;animation-iteration-count:infinite; position:fixed;';
}