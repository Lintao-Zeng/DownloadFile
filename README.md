# DownloadFile
下载文件并发送到邮箱

```
name: Download File

on: [push]

jobs:
  build:

    runs-on: windows-latest

    steps:
    - name: Install download tool
      run: dotnet tool install -g dotnetCampus.FileDownloader.Tool
    - name: Install send mail tool
      run: dotnet tool install -g dotnetCampus.SendEmailTask

    - name: Download File
      run: DownloadFile -u https://github.com/git-for-windows/git/releases/download/v2.37.1.windows.1/Git-2.37.1-64-bit.exe -o file.zip
    - name: Send file
      run: SendEmail -t 2534324260@qq.com -s "SendFile" -b "File" --Files file.zip --SmtpServer smtp.qq.com --SmtpServerPort 465 --UserName 2070047236@qq.com --Password mwzcpfwrixjecfbj

```
