$codeqlPath = "C:\Users\Asus\Downloads\codeql-bundle-win64\codeql" # replace with your CodeQL CLI path
$userPath = [Environment]::GetEnvironmentVariable("Path","User")

if ($userPath -notlike "*$codeqlPath*") {
  [Environment]::SetEnvironmentVariable(
    "Path",
    "$userPath;$codeqlPath",
    "User"
  )
}
