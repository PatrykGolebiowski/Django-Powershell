Param(
    [Parameter(Mandatory)][string]$FIRSTNAME,
    [Parameter(Mandatory)][string]$LASTNAME
)

$result = [PSCustomObject]@{
    FirstName = $FIRSTNAME
    LastName = $LASTNAME
    FullName = $FIRSTNAME + " " + $LASTNAME
}

return $result | ConvertTo-Json