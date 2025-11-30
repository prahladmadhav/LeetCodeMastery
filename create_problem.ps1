param (
    [Parameter(Mandatory = $true)]
    [int]$Number,

    [Parameter(Mandatory = $true)]
    [string]$Name,

    [Parameter(Mandatory = $true)]
    [string]$Topic,

    [Parameter(Mandatory = $true)]
    [string]$Difficulty
)

# Format number to 4 digits
$NumberPadded = "{0:D4}" -f $Number

# Sanitize name to folder-name (lowercase, hyphens)
$FolderName = $Name.ToLower() -replace ' ', '-'

# Full path
$Path = Join-Path $Topic "$NumberPadded-$FolderName"

# Create directory
if (-not (Test-Path $Path)) {
    New-Item -ItemType Directory -Path $Path | Out-Null
}

# README.md content
$ReadmeContent = @"
# $Name

**LeetCode Problem #$NumberPadded**  
**Topic:** $Topic  
**Difficulty:** $Difficulty  
**Date:** $(Get-Date -Format "yyyy-MM-dd")

---

## Problem Link  
https://leetcode.com/problems/$FolderName/

---

## Approach

(Explain your reasoning, algorithms, and edge cases here.)

---

## Complexity
- **Time:**  
- **Space:**  

"@

Set-Content -Path (Join-Path $Path "README.md") -Value $ReadmeContent -Encoding UTF8

# Solution.java content
$JavaContent = @"
public class Solution {
    public void solve() {
        // TODO: Implement solution for: $Name
    }
}
"@

Set-Content -Path (Join-Path $Path "Solution.java") -Value $JavaContent -Encoding UTF8

Write-Host "Created problem folder at: $Path"
