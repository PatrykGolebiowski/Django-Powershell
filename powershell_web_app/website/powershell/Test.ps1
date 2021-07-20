Param(
    [Parameter(Mandatory)][int]$a,
    [Parameter(Mandatory = $false)][int]$b = 15
)

$array = [PSCustomObject]@{
    Value1 = $a
    Value2 = $b
    Addition = $a+$b
}

return $array | ConvertTo-Json