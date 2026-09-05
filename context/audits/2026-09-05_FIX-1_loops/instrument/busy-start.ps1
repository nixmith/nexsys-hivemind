# busy-start.ps1 <pidfile> — two CPU-bound loops pinned to cores 0,1 (mask 3), the recipe's two `taskset -c 0,1` busy loops
$pids = @()
1..2 | ForEach-Object {
  $p = Start-Process -FilePath powershell.exe -ArgumentList '-NoProfile','-WindowStyle','Hidden','-Command','while($true){}' -PassThru -WindowStyle Hidden
  $p.ProcessorAffinity = [IntPtr]3
  $pids += $p.Id
}
($pids -join ',') | Set-Content -Path $args[0]
Write-Output ("busy pids: " + ($pids -join ','))
