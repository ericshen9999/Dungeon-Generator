@if (@X)==(@Y) @end /* JScript comment 
        @echo off 
       
        rem :: the first argument is the script name as it will be used for proper help message 
        cscript //E:JScript //nologo "%~f0" "%~nx0" %* 
        exit /b %errorlevel% 
@if (@X)==(@Y) @end JScript comment */ 

var sh=new ActiveXObject("WScript.Shell"); 
var title="MinecraftServer";
var keys="/setblock 0 5 0 stone replace{Enter}";

sh.AppActivate(title);
WScript.Sleep(1000);

var ForReading = 1;
var fso = new ActiveXObject("Scripting.FileSystemObject");
var fileObj = fso.GetFile("D:\\Github\\Dungeon-Generator\\src\\commands.txt");
var ts = fileObj.OpenAsTextStream(ForReading, 0 );

while(!ts.AtEndOfSream) {
    var textLine = ts.ReadLine();
    sh.SendKeys(textLine + "{Enter}");
}
ts.Close();
 
WScript.Quit(0);