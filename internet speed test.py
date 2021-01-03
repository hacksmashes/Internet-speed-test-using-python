import speedtest

ist=speedtest.Speedtest()
print("Download speed : ",ist.download())
print("Upload speed : ",ist.upload())
