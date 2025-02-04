$header=@"
"<a href="../">Enrere</a>
"@

Get-ChildItem -Recurse -Filter *.md | Foreach-Object { 
    $header`n" + (Get-Content $_.FullName | Out-String) | Set-Content -Path $_.FullName
}