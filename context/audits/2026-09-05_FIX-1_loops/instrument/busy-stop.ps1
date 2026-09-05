# busy-stop.ps1 <pidfile>
if (Test-Path $args[0]) { (Get-Content $args[0]) -split ',' | ForEach-Object { if ($_ -ne '') { Stop-Process -Id ([int]$_) -Force -ErrorAction SilentlyContinue } }; Remove-Item $args[0] }
Write-Output "busy loops stopped"
